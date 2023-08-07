from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('customers/', views.CustomerListView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', views.CustomerDetailView.as_view(), name='customer-detail'),
    path('customers/create/', views.CustomerCreateView.as_view(), name='customer-create'),
    path('customers/<int:pk>/update/', views.CustomerUpdateView.as_view(), name='customer-update'),
    path('customers/<int:pk>/delete/', views.CustomerDeleteView.as_view(), name='customer-delete'),

    path('employees/', views.EmployeeListView.as_view(), name='employee-list'),
    path('employees/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee-detail'),
    path('employees/create/', views.EmployeeCreateView.as_view(), name='employee-create'),
    path('employees/<int:pk>/update/', views.EmployeeUpdateView.as_view(), name='employee-update'),
    path('employees/<int:pk>/delete/', views.EmployeeDeleteView.as_view(), name='employee-delete'),

    path('offices/', views.OfficeListView.as_view(), name='office-list'),
    path('offices/<int:pk>/', views.OfficeDetailView.as_view(), name='office-detail'),
    path('offices/create/', views.OfficeCreateView.as_view(), name='office-create'),
    path('offices/<int:pk>/update/', views.OfficeUpdateView.as_view(), name='office-update'),
    path('offices/<int:pk>/delete/', views.OfficeDeleteView.as_view(), name='office-delete'),

    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('products/<str:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('products/create/', views.ProductCreateView.as_view(), name='product-create'),
    path('products/<str:pk>/update/', views.ProductUpdateView.as_view(), name='product-update'),
    path('products/<str:pk>/delete/', views.ProductDeleteView.as_view(), name='product-delete'),

    path('orders/', views.OrderListView.as_view(), name='order-list'),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),
    path('orders/create/', views.OrderCreateView.as_view(), name='order-create'),
    path('orders/<int:pk>/update/', views.OrderUpdateView.as_view(), name='order-update'),
    path('orders/<int:pk>/delete/', views.OrderDeleteView.as_view(), name='order-delete'),

    path('orderdetails/', views.OrderDetailListView.as_view(), name='orderdetail-list'),
    path('orderdetails/<int:pk>/', views.OrderDetailDetailView.as_view(), name='orderdetail-detail'),
    path('orderdetails/create/', views.OrderDetailCreateView.as_view(), name='orderdetail-create'),
    path('orderdetails/<int:pk>/update/', views.OrderDetailUpdateView.as_view(), name='orderdetail-update'),
    path('orderdetails/<int:pk>/delete/', views.OrderDetailDeleteView.as_view(), name='orderdetail-delete'),

    path('productlines/', views.ProductLineListView.as_view(), name='productline-list'),
    path('productlines/<str:pk>/', views.ProductLineDetailView.as_view(), name='productline-detail'),
    path('productlines/create/', views.ProductLineCreateView.as_view(), name='productline-create'),
    path('productlines/<str:pk>/update/', views.ProductLineUpdateView.as_view(), name='productline-update'),
    path('productlines/<str:pk>/delete/', views.ProductLineDeleteView.as_view(), name='productline-delete'),

]
