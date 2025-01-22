from django.db import models

# Company model
class Company(models.Model):
    id = models.AutoField(primary_key=True)                  # Auto-incrementing ID
    name = models.CharField(max_length=255)     # Unique company name
    manager_name = models.CharField(max_length=255)          # Manager's name
    contact_no = models.CharField(max_length=15)             # Contact number
    address = models.TextField()                             # Address
    amount=models.IntegerField()
    payment_status = models.CharField(max_length=150)

    def __str__(self):
        return self.name


# Employee model
class Employee(models.Model):
    id = models.AutoField(primary_key=True)                  # Auto-incrementing ID
    name = models.CharField(max_length=255)                  # Employee's name
    company = models.ForeignKey(                             # Foreign key to the Company model
        Company,
        on_delete=models.CASCADE,                            # Cascade delete when company is deleted
        related_name="employees"                             # Related name for reverse lookup
    )
    mobile_no = models.CharField(max_length=15)              # Mobile number

    def __str__(self):
        return f"{self.name} ({self.company.name})"


# Customer model
class Customer(models.Model):
    id = models.AutoField(primary_key=True)                  # Auto-incrementing ID
    phone_no = models.CharField(max_length=15, unique=True)  # Unique phone number
    name = models.CharField(max_length=255)                  # Customer's name
    payment = models.DecimalField(max_digits=10, decimal_places=2)  # Payment field for monetary values

    def __str__(self):
        return f"{self.name} ({self.phone_no})"


# PantMeasurement model
class PantMeasurement(models.Model):
    id = models.AutoField(primary_key=True)                  # Auto-incrementing ID
    employee = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="pant_measurements"
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="pant_measurements"
    )
    length = models.DecimalField(max_digits=5, decimal_places=2)  # Length (lambai)
    waist = models.DecimalField(max_digits=5, decimal_places=2)   # Waist (kamar)
    hip = models.DecimalField(max_digits=5, decimal_places=2)     # Hip
    bottom = models.DecimalField(max_digits=5, decimal_places=2)  # Bottom
    round = models.DecimalField(max_digits=5, decimal_places=2)   # Round
    fog = models.DecimalField(max_digits=5, decimal_places=2)     # Fog
    thighs = models.DecimalField(max_digits=5, decimal_places=2)  # Thighs (mandi)
    knee = models.DecimalField(max_digits=5, decimal_places=2)    # Knee (ghutna)

    def __str__(self):
        related_name = self.employee.name if self.employee else self.customer.name
        return f"PantMeasurement for {related_name}"


# ShirtMeasurement model
class ShirtMeasurement(models.Model):
    id = models.AutoField(primary_key=True)                  # Auto-incrementing ID
    employee = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="shirt_measurements"
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="shirt_measurements"
    )
    length = models.DecimalField(max_digits=5, decimal_places=2)  # Length (lambai)
    sleeves = models.DecimalField(max_digits=5, decimal_places=2) # Sleeves (aastin)
    collar = models.DecimalField(max_digits=5, decimal_places=2)  # Collar
    chest = models.DecimalField(max_digits=5, decimal_places=2)   # Chest
    front = models.DecimalField(max_digits=5, decimal_places=2)   # Front
    hip = models.DecimalField(max_digits=5, decimal_places=2)     # Hip

    def __str__(self):
        related_name = self.employee.name if self.employee else self.customer.name
        return f"ShirtMeasurement for {related_name}"
# KurtaMeasurement model
class KurtaMeasurement(models.Model):
    id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="kurta_measurements"
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="kurta_measurements"
    )
    length = models.DecimalField(max_digits=5, decimal_places=2)  # Length (lambai)
    sleeves = models.DecimalField(max_digits=5, decimal_places=2) # Sleeves (aastin)
    collar = models.DecimalField(max_digits=5, decimal_places=2)  # Collar
    chest = models.DecimalField(max_digits=5, decimal_places=2)   # Chest
    hip = models.DecimalField(max_digits=5, decimal_places=2)     # Hip
    daman = models.DecimalField(max_digits=5, decimal_places=2)   # Bottom hem (daman)
    shoulder = models.DecimalField(max_digits=5, decimal_places=2) # Shoulder width

    def __str__(self):
        related_name = self.employee.name if self.employee else self.customer.name
        return f"KurtaMeasurement for {related_name}"


# BlazerMeasurement model
class BlazerMeasurement(models.Model):
    id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="blazer_measurements"
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="blazer_measurements"
    )
    length = models.DecimalField(max_digits=5, decimal_places=2)  # Length (lambai)
    sleeves = models.DecimalField(max_digits=5, decimal_places=2) # Sleeves (aastin)
    chest = models.DecimalField(max_digits=5, decimal_places=2)   # Chest
    waist = models.DecimalField(max_digits=5, decimal_places=2)   # Waist
    shoulder = models.DecimalField(max_digits=5, decimal_places=2) # Shoulder width
    hip = models.DecimalField(max_digits=5, decimal_places=2)     # Hip

    def __str__(self):
        related_name = self.employee.name if self.employee else self.customer.name
        return f"BlazerMeasurement for {related_name}"