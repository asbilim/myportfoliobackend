from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.routers import SimpleRouter
from core.views import ContactViewSet

router = SimpleRouter()

router.register("contact",ContactViewSet,basename="contact")

urlpatterns = [
    path('api/', include(router.urls),name="contact-api"),
]

urlpatterns+=staticfiles_urlpatterns()
