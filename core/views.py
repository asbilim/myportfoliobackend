from .serializer import ContactSerializer
from rest_framework.viewsets import ModelViewSet
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser

class ContactViewSet(ModelViewSet):

    serializer_class = ContactSerializer
    permission_classes = []

    def create(self,request):

        interest = request.GET.get('interest')
        name = request.GET.get('name')
        email = request.GET.get('email')
        message = request.GET.get('message')

        # Forming the more detailed, informative message
        email_subject = f"New Enquiry - {interest} from {name}"

        email_body = f"""
                Dear Admin,

                A new visitor, {name}, has just expressed interest in your services. The specifics of their query are as follows:

                Name: {name}
                Email: {email}
                Area of Interest: {interest}

                They have left the following message:

                {message}

                It would be prudent to address their enquiry at the earliest to provide a responsive service experience. 

                Please do not reply directly to this automated email. Instead, use the contact details provided above to reach out to {name} directly.

                Thank you for your attention to this matter. Keep up the excellent work!

                Best Regards,
                Your Website Automation System
        """

        try:

            # Sending the email
            send_mail(
                email_subject,  # Subject
                email_body,     # Message
                'from@example.com',  # From
                ['to@example.com'],  # To
                fail_silently=False,
            )
        
        except Exception as e:

            return Response({"status":"error","content":e.message},status=status.HTTP_400_BAD_REQUEST)
        
        return Response({"status":"success","content":"message sent successfully"},status=status.HTTP_200_OK)

        # Continue with your saving or other tasks...



    def get_permissions(self):

        permissions = []
        
        if self.action != "create" :

            permissions = [IsAdminUser]

        return [permission() for permission in permissions]
