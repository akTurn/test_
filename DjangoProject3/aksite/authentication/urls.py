from .views import RegistrationView
from django.urls import path

urlpatterns = [

    path('Register', RegistrationView.as_view(), name="Register")

]