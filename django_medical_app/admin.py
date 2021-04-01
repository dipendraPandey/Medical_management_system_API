from django.contrib import admin
from .models import (MedicineCompany,
                     Medicine,
                     CompanyBank,
                     CompanyAccount,
                     Customer,
                     CustomerRequest,
                     MedicalDetails,
                     Employee,
                     EmployeeSalary,
                     EmployeeBank,
                     BillDetails,
                     Bill)

admin.site.register(MedicineCompany)
admin.site.register(Medicine)
admin.site.register(CompanyAccount)
admin.site.register(CompanyBank)
admin.site.register(CustomerRequest)
admin.site.register(Customer)
admin.site.register(MedicalDetails)
admin.site.register(Employee)
admin.site.register(EmployeeSalary)
admin.site.register(EmployeeBank)
admin.site.register(Bill)
admin.site.register(BillDetails)
