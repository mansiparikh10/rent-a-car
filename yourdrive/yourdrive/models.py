from django.db import models

class YD_Class(models.Model):
    class_id = models.IntegerField(primary_key=True)
    daily_rental_rate = models.DecimalField(max_digits=8, decimal_places=2)
    weekly_rental_rate = models.DecimalField(max_digits=8, decimal_places=2)
    class_name = models.CharField(max_length=20)

class YD_Location(models.Model):
    location_id = models.IntegerField(primary_key=True)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    state = models.CharField(max_length=2)

class YD_Model(models.Model):
    model_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    year = models.IntegerField()
    class_id = models.ForeignKey(YD_Class, on_delete=models.CASCADE)

class YD_Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    license_no = models.CharField(max_length=20)
    state_issued = models.CharField(max_length=2)
    address = models.CharField(max_length=100)
    cc_type = models.CharField(max_length=20)
    cc_number = models.CharField(max_length=16)
    cc_exp_month = models.IntegerField()
    cc_exp_year = models.IntegerField()

class YD_Car(models.Model):
    vin = models.CharField(max_length=17, primary_key=True)
    class_id = models.ForeignKey(YD_Class, on_delete=models.CASCADE)
    model_id = models.ForeignKey(YD_Model, on_delete=models.CASCADE)
    location_id = models.ForeignKey(YD_Location, on_delete=models.CASCADE)

class YD_Employee(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    location_id = models.ForeignKey(YD_Location, on_delete=models.CASCADE)

class YD_Reservation(models.Model):
    reservation_id = models.IntegerField(primary_key=True)
    pick_up_date = models.DateField()
    pickup_time = models.DateTimeField()
    drop_off_date = models.DateField()
    dropoff_time = models.DateTimeField()
    location_id = models.ForeignKey(YD_Location, on_delete=models.CASCADE)
    class_id = models.ForeignKey(YD_Class, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(YD_Customer, on_delete=models.CASCADE)
    emp_id = models.ForeignKey(YD_Employee, on_delete=models.CASCADE)

class YD_RentalAgreement(models.Model):
    contract_no = models.IntegerField(primary_key=True)
    start_date = models.DateField()
    start_time = models.DateTimeField()
    end_date = models.DateField()
    end_time = models.DateTimeField()
    odo_read_start = models.IntegerField()
    odo_read_end = models.IntegerField()
    rental_cost = models.DecimalField(max_digits=10, decimal_places=2)
    customer_id = models.ForeignKey(YD_Customer, on_delete=models.CASCADE)
    reservation_id = models.ForeignKey(YD_Reservation, on_delete=models.CASCADE)

class YD_RentalAssignment(models.Model):
    contract_no = models.ForeignKey(YD_RentalAgreement, on_delete=models.CASCADE)
    vin = models.ForeignKey(YD_Car, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(YD_Customer, on_delete=models.CASCADE)

class PhoneNo(models.Model):
    customer_id = models.ForeignKey(YD_Customer, on_delete=models.CASCADE)
    telephone_no = models.CharField(max_length=15)
