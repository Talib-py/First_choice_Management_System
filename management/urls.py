"""
URL configuration for First_choice_Management_System project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.home, name='home'),  # This defines the 'home' URL pattern
    path('add_company/', v.add_company, name='add_company'),
    path('add_employee/', v.add_employee, name='add_employee'),
    path('add_customer/', v.add_customer, name='add_customer'),
    path('add_pant_measurement/', v.add_pant_measurement, name='add_pant_measurement'),
    path('add_shirt_measurement/', v.add_shirt_measurement, name='add_shirt_measurement'),
    path('add_blazer_measurement/', v.add_blazer_measurement, name='add_blazer_measurement'),
    path('add_kurta_measurement/', v.add_kurta_measurement, name='add_kurta_measurement'),
    path('employee_list/', v.employee_list, name='employee_list'),
    path('customer_list/', v.customer_list, name='customer_list'),
    path('edit_employee/<int:employee_id>/', v.edit_employee, name='edit_employee'),
    path('edit_customer/<int:customer_id>/', v.edit_customer, name='edit_customer'),
    path('edit_kurta_measurement/<int:kurta_id>/', v.edit_kurta_measurement, name='edit_kurta_measurement'),
    path('edit_blazer_measurement/<int:blazer_id>/', v.edit_blazer_measurement, name='edit_blazer_measurement'),
    path('edit_pant_measurement/<int:pant_id>/', v.edit_pant_measurement, name='edit_pant_measurement'),
    path('edit_shirt_measurement/<int:shirt_id>/', v.edit_shirt_measurement, name='edit_shirt_measurement'),
    path('delete_employee/<int:employee_id>/', v.delete_employee, name='delete_employee'),
    path('delete_customer/<int:customer_id>/', v.delete_customer, name='delete_customer'),
    path('delete_kurta_measurement/<int:kurta_id>/', v.delete_kurta_measurement, name='delete_kurta_measurement'),
    path('delete_blazer_measurement/<int:blazer_id>/', v.delete_blazer_measurement, name='delete_blazer_measurement'),
    path('delete_pant_measurement/<int:pant_id>/', v.delete_pant_measurement, name='delete_pant_measurement'),
    path('delete_shirt_measurement/<int:shirt_id>/', v.delete_shirt_measurement, name='delete_shirt_measurement'),
    path('company_list/', v.company_list, name='company_list'),
    path('edit_company/<int:company_id>/', v.edit_company, name='edit_company'),
    path('delete_company/<int:company_id>/', v.delete_company, name='delete_company'),
    path('add_company/', v.add_company, name='add_company'),  # Link to add company
    
]
