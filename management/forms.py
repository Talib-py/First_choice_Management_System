# forms.py
from django import forms
from .models import Employee, Customer, KurtaMeasurement, BlazerMeasurement, PantMeasurement, ShirtMeasurement,Company

#Company Form
class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name','address', 'contact_no','manager_name','amount','payment_status']  # Add more fields as needed

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'mobile_no']  # Add more fields as needed

# Customer Form
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone_no']  # Add more fields as needed

# Kurta Measurement Form
class KurtaMeasurementForm(forms.ModelForm):
    class Meta:
        model = KurtaMeasurement
        fields = ['length', 'sleeves', 'collar', 'chest', 'hip', 'daman']

# Blazer Measurement Form
class BlazerMeasurementForm(forms.ModelForm):
    class Meta:
        model = BlazerMeasurement
        fields = ['length', 'sleeves', 'chest', 'waist', 'shoulder', 'hip']

# Pant Measurement Form
class PantMeasurementForm(forms.ModelForm):
    class Meta:
        model = PantMeasurement
        fields = ['waist', 'length', 'hip','bottom','round','fog','thighs','knee']

# Shirt Measurement Form
class ShirtMeasurementForm(forms.ModelForm):
    class Meta:
        model = ShirtMeasurement
        fields = ['length', 'sleeves', 'chest','collar','front','hip']
