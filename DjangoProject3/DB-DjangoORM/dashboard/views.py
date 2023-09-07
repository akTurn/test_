from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Customer, Employee, OrderDetail, Order, Products, Office, ProductLine

# myapp/views.py

def home_view(request):
    return render(request, 'home.html')

class CustomerListView(ListView):
    model = Customer
    template_name = 'customer_list.html'  # The template to display the list of customers

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer_detail.html'  # The template to display a single customer's details

class CustomerCreateView(CreateView):
    model = Customer
    fields = '__all__'  # Use all fields in the form
    success_url = '/customers/'
    template_name = 'customer_form.html'  # The template for the customer creation form

class CustomerUpdateView(UpdateView):
    model = Customer
    fields = '__all__'
    success_url = '/customers/'
    template_name = 'customer_form.html'

class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = '/customers/'  # Redirect to customer list after deletion
    template_name = 'customer_delete.html'  # The template for the delete confirmation page

##########################################################################
class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee_list.html'

"""
# listings/views.py

def band_list(request):# rename the view function
   bands = Band.objects.all()
   return render(request,
           'listings/band_list.html',# point to the new template name
           {'bands': bands})
           
"""

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee_detail.html'

class EmployeeCreateView(CreateView):
    model = Employee
    fields = '__all__'
    success_url = '/employees/'
    template_name = 'employee_form.html'

class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = '__all__'
    success_url = '/employees/'
    template_name = 'employee_form.html'
"""
 ALTERNATE METHOD
 
    def employee_update(request, id):
        employee = Employee.objects.get(id=id)
        form = EmployeeForm(instance=employee) # prepopulate the form with an existing band
        return render(request,
                      'employee_form.html',
                      {'form': form})
"""
class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = '/employees/'
    template_name = 'employee_delete.html'

# Create similar views for OrderDetail, Order, Product, and Office models

class OrderDetailListView(ListView):
    model = OrderDetail
    template_name = 'orderdetails_list.html'

class OrderDetailDetailView(DetailView):
    model = OrderDetail
    template_name = 'orderdetails_detail.html'

class OrderDetailCreateView(CreateView):
    model = OrderDetail
    fields = '__all__'
    success_url = '/orderdetails/'
    template_name = 'orderdetails_form.html'

class OrderDetailUpdateView(UpdateView):
    model = OrderDetail
    fields = '__all__'
    success_url = '/orderdetails/'
    template_name = 'orderdetails_form.html'

class OrderDetailDeleteView(DeleteView):
    model = OrderDetail
    success_url = '/orderdetails/'
    template_name = 'orderdetails_delete.html'

###################################################################################
class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'

class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'

class OrderCreateView(CreateView):
    model = Order
    fields = '__all__'
    success_url = '/orders/'
    template_name = 'order_form.html'

class OrderUpdateView(UpdateView):
    model = Order
    fields = '__all__'
    success_url = '/orders/'
    template_name = 'order_form.html'

class OrderDeleteView(DeleteView):
    model = Order
    success_url = '/orders/'
    template_name = 'order_delete.html'
##############################################################################################
class ProductListView(ListView):
    model = Products
    template_name = 'product_list.html'

class ProductDetailView(DetailView):
    model = Products
    template_name = 'product_detail.html'

class ProductCreateView(CreateView):
    model = Products
    fields = '__all__'
    success_url = '/products/'
    template_name = 'product_form.html'

class ProductUpdateView(UpdateView):
    model = Products
    fields = '__all__'
    success_url = '/products/'
    template_name = 'product_form.html'

class ProductDeleteView(DeleteView):
    model = Products
    success_url = '/products/'
    template_name = 'product_delete.html'
##########################################################################################3
class OfficeListView(ListView):
    model = Office
    template_name = 'office_list2.html'

class OfficeDetailView(DetailView):
    model = Office
    template_name = 'office_detail.html'

class OfficeCreateView(CreateView):
    model = Office
    fields = '__all__'
    success_url = '/offices'
    template_name = 'office_form.html'

class OfficeUpdateView(UpdateView):
    model = Office
    fields = '__all__'
   # success_url = '/offices'
    template_name = 'office_form.html'

    """

    def form_valid(self, form):
        response = super().form_valid(form)
        # Redirect to the detail page of the updated object
        return redirect(self.object.get_absolute_url())
    """




class OfficeDeleteView(DeleteView):
    model = Office
    success_url = '/offices/'
    template_name = 'office_delete.html'

def office_list(request):
    offices = Office.objects.all()
    return render(request, 'office_list2.html', {'offices': offices})
#########################################################################################
class ProductLineListView(ListView):
    model = ProductLine
    template_name = 'productlines_list.html'

class ProductLineDetailView(DetailView):
    model = ProductLine
    template_name = 'productlines_detail.html'

class ProductLineCreateView(CreateView):
    model = ProductLine
    fields = '__all__'
    success_url = '/productlines/'
    template_name = 'productlines_form.html'

class ProductLineUpdateView(UpdateView):
    model = ProductLine
    fields = '__all__'
    success_url = '/productlines/'
    template_name = 'productlines_form.html'

class ProductLineDeleteView(DeleteView):
    model = ProductLine
    success_url = '/productlines/'
    template_name = 'productlines_delete.html'



#def productline_list(request):
 #   productlines = ProductLine.objects.all()
  #  return render(request, 'productline_list.html', {'productlines': productlines})
