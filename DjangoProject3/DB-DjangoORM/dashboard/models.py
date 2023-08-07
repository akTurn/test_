from django.db import models
from django.urls import reverse


class Customer(models.Model):
    customerNumber = models.IntegerField(primary_key=True)
    customerName = models.CharField(max_length=50)
    contactLastName = models.CharField(max_length=50)
    contactFirstName = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    addressLine1 = models.CharField(max_length=50)
    addressLine2 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50, blank=True, null=True)
    postalCode = models.CharField(max_length=15, blank=True, null=True)
    country = models.CharField(max_length=50)
    salesRepEmployeeNumber = models.IntegerField(blank=True, null=True)
    creditLimit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        db_table = 'customers'
class Employee(models.Model):
    employeeNumber = models.IntegerField(primary_key=True)
    lastName = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    extension = models.CharField(max_length=10)
    email = models.EmailField()
    officeCode = models.ForeignKey('Office', on_delete=models.CASCADE, db_column='officeCode')
    reportsTo = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, db_column='reportsTo')
    jobTitle = models.CharField(max_length=50)

    class Meta:
        db_table = 'employees'
class OrderDetail(models.Model):
    id = models.AutoField(primary_key=True)
    orderNumber = models.ForeignKey('Order', on_delete=models.CASCADE,  db_column='orderNumber')
    productCode = models.ForeignKey('Products', on_delete=models.CASCADE, db_column='productCode')
    quantityOrdered = models.IntegerField()
    priceEach = models.DecimalField(max_digits=10, decimal_places=2)
    orderLineNumber = models.SmallIntegerField()

    class Meta:
        db_table = 'orderdetails'
        constraints = [
            models.UniqueConstraint(fields=['orderNumber', 'productCode'], name='composite_pk'),
        ]

class Order(models.Model):
    orderNumber = models.IntegerField(primary_key=True)
    orderDate = models.DateField()
    requiredDate = models.DateField()
    shippedDate = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=15)
    comments = models.TextField(blank=True, null=True)
    customerNumber = models.ForeignKey('Customer', on_delete=models.CASCADE,db_column='customerNumber')

    class Meta:
        db_table = 'orders'
class Products(models.Model):
    productCode = models.CharField(max_length=15, primary_key=True)
    productName = models.CharField(max_length=70)
    productLine = models.ForeignKey('ProductLine', on_delete=models.CASCADE,db_column='productLine')
    productScale = models.CharField(max_length=10)
    productVendor = models.CharField(max_length=50)
    productDescription = models.TextField()
    quantityInStock = models.SmallIntegerField()
    buyPrice = models.DecimalField(max_digits=10, decimal_places=2)
    MSRP = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'products'

class Office(models.Model):
    officeCode = models.CharField(max_length=10, primary_key=True)
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    addressLine1 = models.CharField(max_length=50)
    addressLine2 = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50)
    postalCode = models.CharField(max_length=15)
    territory = models.CharField(max_length=10)

    class Meta:
        db_table = 'offices'

    def get_absolute_url(self):
        return reverse('office-detail', kwargs={'pk': self.pk})  #
    """
    The reverse function is used to generate URLs based on their view names or pattern names, 
    not the actual URLs themselves. In your get_absolute_url method, you should be using the view or pattern name,
     not the URL.
    
    'office-detail' is the view name
    'offices/<int:pk>/' is the url
    

    """


class ProductLine(models.Model):
    productLine = models.CharField(max_length=50, primary_key=True)
    textDescription = models.CharField(max_length=4000, blank=True, null=True)
    htmlDescription = models.TextField(blank=True, null=True)
    image = models.BinaryField(blank=True, null=True)

    class Meta:
        db_table = 'productlines'