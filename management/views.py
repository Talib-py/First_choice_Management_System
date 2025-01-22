from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Company, Employee, Customer, PantMeasurement, ShirtMeasurement,KurtaMeasurement,BlazerMeasurement

# View for adding a Company
def add_company(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        manager_name = request.POST.get('manager_name')
        contact_no = request.POST.get('contact_no')
        address = request.POST.get('address')
        amount = request.POST.get('amount')
        payment_status = request.POST.get('payment_status')

        Company.objects.create(name=name, manager_name=manager_name, contact_no=contact_no, address=address,amount=amount,payment_status=payment_status)

    return render(request, 'add_company.html')

# View for adding an Employee
def add_employee(request):
    companies = Company.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        company_id = request.POST.get('company')
        mobile_no = request.POST.get('mobile_no')

        company = Company.objects.get(id=company_id)
        Employee.objects.create(name=name, company=company, mobile_no=mobile_no)
        

    return render(request, 'add_employee.html', {'companies': companies})

# View for adding a Customer
def add_customer(request):
    if request.method == 'POST':
        phone_no = request.POST.get('phone_no')
        name = request.POST.get('name')
        payment = request.POST.get('payment')

        Customer.objects.create(phone_no=phone_no, name=name, payment=payment)
        

    return render(request, 'add_customer.html')

# View for adding Pant Measurements
def add_pant_measurement(request):
    employees = Employee.objects.all()
    customers = Customer.objects.all()
    if request.method == 'POST':
        employee_id = request.POST.get('employee')
        customer_id = request.POST.get('customer')
        length = request.POST.get('length')
        waist = request.POST.get('waist')
        hip = request.POST.get('hip')
        bottom = request.POST.get('bottom')
        round_ = request.POST.get('round')
        fog = request.POST.get('fog')
        thighs = request.POST.get('thighs')
        knee = request.POST.get('knee')

        employee = Employee.objects.get(id=employee_id) if employee_id else None
        customer = Customer.objects.get(id=customer_id) if customer_id else None

        PantMeasurement.objects.create(
            employee=employee, customer=customer, length=length, waist=waist,
            hip=hip, bottom=bottom, round=round_, fog=fog, thighs=thighs, knee=knee
        )
    return render(request, 'add_pant_measurement.html', {'employees': employees, 'customers': customers})

# View for adding Shirt Measurements
def add_shirt_measurement(request):
    employees = Employee.objects.all()
    customers = Customer.objects.all()
    if request.method == 'POST':
        employee_id = request.POST.get('employee')
        customer_id = request.POST.get('customer')
        length = request.POST.get('length')
        sleeves = request.POST.get('sleeves')
        collar = request.POST.get('collar')
        chest = request.POST.get('chest')
        front = request.POST.get('front')
        hip = request.POST.get('hip')

        employee = Employee.objects.get(id=employee_id) if employee_id else None
        customer = Customer.objects.get(id=customer_id) if customer_id else None

        ShirtMeasurement.objects.create(
            employee=employee, customer=customer, length=length, sleeves=sleeves,
            collar=collar, chest=chest, front=front, hip=hip
        )   
    return render(request, 'add_shirt_measurement.html', {'employees': employees, 'customers': customers})


def add_kurta_measurement(request):
    employees = Employee.objects.all()
    customers = Customer.objects.all()
    if request.method == 'POST':
        employee_id = request.POST.get('employee')
        customer_id = request.POST.get('customer')
        length = request.POST.get('length')
        sleeves = request.POST.get('sleeves')
        collar = request.POST.get('collar')
        chest = request.POST.get('chest')
        daman = request.POST.get('daman')
        hip = request.POST.get('hip')
        shoulder = request.POST.get('shoulder')

        employee = Employee.objects.get(id=employee_id) if employee_id else None
        customer = Customer.objects.get(id=customer_id) if customer_id else None

        KurtaMeasurement.objects.create(
            employee=employee, customer=customer, length=length, sleeves=sleeves,
            collar=collar, chest=chest, daman=daman, hip=hip,shoulder=shoulder
        )   
    return render(request, 'add_kurta_measurement.html', {'employees': employees, 'customers': customers})

def add_blazer_measurement(request):
    employees = Employee.objects.all()
    customers = Customer.objects.all()
    if request.method == 'POST':
        employee_id = request.POST.get('employee')
        customer_id = request.POST.get('customer')
        length = request.POST.get('length')
        sleeves = request.POST.get('sleeves')
        waist = request.POST.get('waist')
        chest = request.POST.get('chest')
        shoulder = request.POST.get('shoulder')
        hip = request.POST.get('hip')

        employee = Employee.objects.get(id=employee_id) if employee_id else None
        customer = Customer.objects.get(id=customer_id) if customer_id else None

        KurtaMeasurement.objects.create(
            employee=employee, customer=customer, length=length, sleeves=sleeves,
            shoulder=shoulder, chest=chest, waist=waist, hip=hip
        )   
    return render(request, 'add_blazer_measurement.html', {'employees': employees, 'customers': customers})


from django.shortcuts import render
from django.contrib.auth.models import User  # To access user details
from .models import Company, Employee, Customer

def home(request):
    # Get user login details (logged-in user)
    user = request.user

    # Calculate totals
    total_companies = Company.objects.count()
    total_employees = Employee.objects.count()
    total_customers = Customer.objects.count()

    # Get all companies with their employee count
    companies = Company.objects.all()
    company_details = []
    for company in companies:
        company_details.append({
            'name': company.name,
            'manager_name': company.manager_name,
            'contact_no': company.contact_no,
            'address': company.address,
            'employee_count': Employee.objects.filter(company=company).count(),
        })

    # Render data to the template
    context = {
        'user': user,
        'total_companies': total_companies,
        'total_employees': total_employees,
        'total_customers': total_customers,
        'company_details': company_details,
    }
    return render(request, 'home.html', context)

# views.py
from django.shortcuts import render
from .models import Employee, KurtaMeasurement, BlazerMeasurement

def employee_list(request):
    query = request.GET.get('q', '')  # Get the search query from the request
    employees = Employee.objects.filter(name__icontains=query) if query else Employee.objects.all()

    # Create a context with employee details and related measurements
    context = {
        'employees': employees,
        'query': query,
    }
    return render(request, 'employee_list.html', context)

# views.py
from django.shortcuts import render
from .models import Customer, KurtaMeasurement, BlazerMeasurement, PantMeasurement, ShirtMeasurement

def customer_list(request):
    query = request.GET.get('q', '')  # Get the search query for customer name
    customers = Customer.objects.filter(name__icontains=query) if query else Customer.objects.all()

    customer_data = []
    
    for customer in customers:
        # Retrieve all measurements related to each customer
        kurta_measurements = KurtaMeasurement.objects.filter(customer=customer)
        blazer_measurements = BlazerMeasurement.objects.filter(customer=customer)
        pant_measurements = PantMeasurement.objects.filter(customer=customer)
        shirt_measurements = ShirtMeasurement.objects.filter(customer=customer)

        customer_data.append({
            'customer': customer,
            'kurta_measurements': kurta_measurements,
            'blazer_measurements': blazer_measurements,
            'pant_measurements': pant_measurements,
            'shirt_measurements': shirt_measurements,
        })

    contexts = {
        'customer_data': customer_data,
        'query': query,
    }
    return render(request, 'customer_list.html', contexts)


def delete_company(request,id):
    exp=Company.objects.get(id=id)
    exp.delete()
    return redirect('/company_list')


def edit_company(request,id):
    exp=Company.objects.get(id=id)

    if request.method=='POST':
        f=Company(request.POST,instance=exp)
        f.save()
        return redirect('/company_list')
    else:
        f=Company(instance=exp)
        context={'form1':f}
        return render(request,'company_list.html',context)
    
# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee, Customer, KurtaMeasurement, BlazerMeasurement, PantMeasurement, ShirtMeasurement
from .forms import EmployeeForm, CustomerForm, KurtaMeasurementForm, BlazerMeasurementForm, PantMeasurementForm, ShirtMeasurementForm

# Edit Employee View
def edit_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')  # Redirect to the employee/customer list
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'edit_employee.html', {'form': form, 'employee': employee})

# Edit Customer View
def edit_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')  # Redirect to the customer list
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'edit_customer.html', {'form': form, 'customer': customer})

# Edit Kurta Measurement View
def edit_kurta_measurement(request, kurta_id):
    kurta = get_object_or_404(KurtaMeasurement, id=kurta_id)
    if request.method == 'POST':
        form = KurtaMeasurementForm(request.POST, instance=kurta)
        if form.is_valid():
            form.save()
            return redirect('customer_measurements')  # Redirect to the customer list
    else:
        form = KurtaMeasurementForm(instance=kurta)
    return render(request, 'edit_kurta_measurement.html', {'form': form, 'kurta': kurta})

# Edit Blazer Measurement View
def edit_blazer_measurement(request, blazer_id):
    blazer = get_object_or_404(BlazerMeasurement, id=blazer_id)
    if request.method == 'POST':
        form = BlazerMeasurementForm(request.POST, instance=blazer)
        if form.is_valid():
            form.save()
            return redirect('customer_measurements')  # Redirect to the customer list
    else:
        form = BlazerMeasurementForm(instance=blazer)
    return render(request, 'edit_blazer_measurement.html', {'form': form, 'blazer': blazer})

# Edit Pant Measurement View
def edit_pant_measurement(request, pant_id):
    pant = get_object_or_404(PantMeasurement, id=pant_id)
    if request.method == 'POST':
        form = PantMeasurementForm(request.POST, instance=pant)
        if form.is_valid():
            form.save()
            return redirect('customer_measurements')  # Redirect to the customer list
    else:
        form = PantMeasurementForm(instance=pant)
    return render(request, 'edit_pant_measurement.html', {'form': form, 'pant': pant})

# Edit Shirt Measurement View
def edit_shirt_measurement(request, shirt_id):
    shirt = get_object_or_404(ShirtMeasurement, id=shirt_id)
    if request.method == 'POST':
        form = ShirtMeasurementForm(request.POST, instance=shirt)
        if form.is_valid():
            form.save()
            return redirect('customer_measurements')  # Redirect to the customer list
    else:
        form = ShirtMeasurementForm(instance=shirt)
    return render(request, 'edit_shirt_measurement.html', {'form': form, 'shirt': shirt})


# views.py
from django.shortcuts import get_object_or_404, redirect
from .models import Employee

# Delete Employee View
def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    employee.delete()
    return redirect('employee_list')  # Redirect to the employee/customer list


# views.py
from .models import Customer

# Delete Customer View
def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    customer.delete()
    return redirect('customer_list')  # Redirect to the customer list

# views.py
from .models import KurtaMeasurement

# Delete Kurta Measurement View
def delete_kurta_measurement(request, kurta_id):
    kurta = get_object_or_404(KurtaMeasurement, id=kurta_id)
    kurta.delete()
    return redirect('customer_list')  # Redirect to the customer list

# views.py
from .models import BlazerMeasurement

# Delete Blazer Measurement View
def delete_blazer_measurement(request, blazer_id):
    blazer = get_object_or_404(BlazerMeasurement, id=blazer_id)
    blazer.delete()
    return redirect('customer_list')  # Redirect to the customer list

# views.py
from .models import PantMeasurement

# Delete Pant Measurement View
def delete_pant_measurement(request, pant_id):
    pant = get_object_or_404(PantMeasurement, id=pant_id)
    pant.delete()
    return redirect('customer_list')  # Redirect to the customer list

# views.py
from .models import ShirtMeasurement

# Delete Shirt Measurement View
def delete_shirt_measurement(request, shirt_id):
    shirt = get_object_or_404(ShirtMeasurement, id=shirt_id)
    shirt.delete()
    return redirect('customer_list')  # Redirect to the customer list


# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Company
from .forms import CompanyForm
from django.contrib import messages

# View to list all companies
def company_list(request):
    companies = Company.objects.all()
    return render(request, 'company_list.html', {'companies': companies})

# View to edit a company
def edit_company(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            messages.success(request, f'Company {company.name} updated successfully!')
            return redirect('company_list')
    else:
        form = CompanyForm(instance=company)
    return render(request, 'edit_company.html', {'form': form, 'company': company})

# View to delete a company
def delete_company(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    company_name = company.name
    company.delete()
    messages.success(request, f'Company {company_name} has been deleted.')
    return redirect('company_list')
