
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django_medical_app import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register('company-bank', views.CompanyBankViewSets, basename='company-bank')
router.register('medicine-company', views.MedicineCompanyViewSet, basename='medicine-company')
router.register('company-account', views.CompanyAccountViewSets, basename='company-account')
router.register('medicine', views.MedicineViewSets, basename='medicine')
router.register('medical-details', views.MedicalDetailsViewSets, basename='medical-details')
router.register('customer', views.CustomerViewSets, basename='customer')
router.register('customer-request', views.CustomerRequestViewSets, basename='customer-request')
router.register('employee', views.EmployeeViewSets, basename='employee')
router.register('employee-salary', views.EmployeeSalaryViewSets, basename='employee-salary')
router.register('employee-bank', views.EmployeeBankViewSets, basename='employee-bank')
router.register('bill', views.BillViewSets, basename='bill')
router.register('bill-details', views.BillDetailsViewSets, basename='bill-details')
router.register('generate-bill', views.BillGenerateViewSets, basename='generate_bill')
router.register('home', views.HomePageViewSets, basename='home')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/gettoken/', TokenObtainPairView.as_view(), name='get_token'),
    path('api/refresh_token/', TokenRefreshView.as_view(), name='refresh_token'),
    path('api/companybyname/<str:name>/', views.CompanyNameViewSets.as_view(), name='company_by_name'),
    path('api/medicinebyname/<str:name>/', views.MedicineByNameViewSets.as_view(), name='medicine_by_name'),
    path('api/employeesalaryinfo/<int:id>/', views.EmployeeSalaryList.as_view(), name='company_by_name'),
    path('api/employeebankinfo/<int:id>/', views.EmployeeBankList.as_view(), name='company_by_name'),
]
