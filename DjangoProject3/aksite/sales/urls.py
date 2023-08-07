from django.urls import path
from .import views


urlpatterns =[
    path('',views.base,name="sales"),
    path('add-customers',views.add_cust,name="add-customers")

]