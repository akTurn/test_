from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request,'sales/index.html')
def add_cust(request):
    return render(request,'sales/add_cust.html')
