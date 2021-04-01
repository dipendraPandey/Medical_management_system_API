from rest_framework import viewsets
import datetime
from django.db import transaction
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from .serializers import (MedicineCompanySerializers,
                          CompanyBankSerializer,
                          CompanyAccountSerializers,
                          MedicineSerializers,
                          MedicalDetailsSerializers,
                          CustomerSerializers,
                          CustomerRequestSerializers,
                          EmployeeSerializers,
                          EmployeeSalarySerializers,
                          EmployeeBankSerializers,
                          BillSerializers,
                          BillDetailsSerializers,
                          SimpleMedicalDetailsSerializers,
                          )
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
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView


class MedicineCompanyViewSet(viewsets.ViewSet):
    queryset = MedicineCompany.objects.all()
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def list(self, request):
        serializer = MedicineCompanySerializers(self.queryset, many=True, context={"request": request})
        response_dict = {'error': False,
                         'message': 'All Medicine Company list Invoked',
                         'data': serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = MedicineCompanySerializers(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_dict = {'error': False,
                             'message': 'Medicine Company Created successfully ',
                             }
        except:
            response_dict = {'error': True,
                             'message': 'Error Creating Medicine Company ', }

        return Response(response_dict)

    def update(self, request, pk=None):
        try:
            company = get_object_or_404(self.queryset, pk=pk)
            serializer = MedicineCompanySerializers(company, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_dict = {'error': False,
                             'message': 'Medicine Company Updated successfully ',
                             }
        except:
            response_dict = {'error': True,
                             'message': 'Error Updating Medicine Company ', }

        return Response(response_dict)

    def retrieve(self, request, pk):
        try:

            company = get_object_or_404(self.queryset, pk=pk)
            serializer = MedicineCompanySerializers(company, context={"request": request})
            serializer_data = serializer.data
            company_bank_details = CompanyBank.objects.filter(company_id=serializer_data["id"])
            company_bank_details_serializer = CompanyBankSerializer(company_bank_details, many=True)
            serializer_data['company_bank'] = company_bank_details_serializer.data
            response_dict = {"error": False, "message": "Medicine Company Details invoked", 'data': serializer_data}

        except:
            response_dict = {"error": True, "message": " Error invoking Medicine Company", }
        return Response(response_dict)

    def destroy(self, request, pk):
        try:
            company_data = get_object_or_404(MedicineCompany, id=pk)
            company_data.delete()
            response_dict = {'error': False,
                             'message': 'Medicine Company Deleted successfully',
                             }
        except:
            response_dict = {'error': True,
                             'message': 'Error Deleting Medicine Company', }

        return Response(response_dict)


class CompanyAccountViewSets(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def create(self, request):
        try:
            serializer = CompanyAccountSerializers(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_dict = {'error': False,
                             'message': "Company Account Created successfully",
                             'data': serializer.data}
        except:
            response_dict = {'error': True,
                             'message': " Error During creating Company Account", }
        return Response(response_dict)

    def list(self, request):
        bank_list = CompanyAccount.objects.all()
        serializer = CompanyAccountSerializers(bank_list, many=True, context={"request": request})
        response_dict = {'error': False,
                         'message': 'All Company Account bank list Invoked',
                         'data': serializer.data}
        return Response(response_dict)

    def retrieve(self, request, pk):
        try:
            queryset = CompanyAccount.objects.all()
            companyaccount = get_object_or_404(queryset, pk=pk)
            serializer = CompanyAccountSerializers(companyaccount, context={"request": request})
            response_dict = {"error": False, "message": "Company Account invoked", 'data': serializer.data}
        except:
            response_dict = {"error": False, "message": " Error invoking Company Account", 'data': serializer.data}
        return Response(response_dict)

    def update(self, request, pk=None):
        try:
            queryset = CompanyAccount.objects.all()
            companyaccount = get_object_or_404(queryset, pk=pk)
            serializer = CompanyAccountSerializers(companyaccount, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_dict = {'error': False,
                             'message': 'Company Account Updated successfully',
                             }
        except:
            response_dict = {'error': True,
                             'message': 'Error Updating Company Account', }

        return Response(response_dict)


class CompanyBankViewSets(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def create(self, request):
        try:
            serializer = CompanyBankSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)

            serializer.save()

            response_dict = {'error': False,
                             'message': "CompanyBank Created successfully",
                             'data': serializer.data}
        except:
            response_dict = {'error': True,
                             'message': " Error During creating CompanyBank", }
        return Response(response_dict)

    def list(self, request):
        bank_list = CompanyBank.objects.all()
        serializer = CompanyBankSerializer(bank_list, many=True, context={"request": request})
        response_dict = {'error': False,
                         'message': 'All CompanyBank list Invoked',
                         'data': serializer.data}
        return Response(response_dict)

    def retrieve(self, request, pk):
        try:
            queryset = CompanyBank.objects.all()
            companybank = get_object_or_404(queryset, pk=pk)
            serializer = CompanyBankSerializer(companybank, context={"request": request})
            response_dict = {"error": False, "message": "Companybank invoked", 'data': serializer.data}
        except:
            response_dict = {"error": False, "message": "Companybank invoked", 'data': serializer.data}
        return Response(response_dict)

    def update(self, request, pk=None):
        try:
            queryset = CompanyBank.objects.all()
            companybank = get_object_or_404(queryset, pk=pk)
            serializer = CompanyBankSerializer(companybank, data=request.data, context={"request": request})

            serializer.is_valid(raise_exception=True)

            serializer.save()
            response_dict = {'error': False,
                             'message': 'CompanyBank Updated successfully',
                             }
        except:
            response_dict = {'error': True,
                             'message': 'Error Updating CompanyBank', }

        return Response(response_dict)


class MedicineViewSets(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def list(self, request):
        mdeicine_list = Medicine.objects.all()
        serializer = MedicineSerializers(mdeicine_list, many=True, context={"request": request})
        medicine_data = serializer.data
        new_medicine_list = []
        for medicine in medicine_data:
            medicine_detail = MedicalDetails.objects.filter(medicine_id=medicine['id'])
            medicine_detail_serializers = SimpleMedicalDetailsSerializers(medicine_detail, many=True)
            medicine['medicine_details'] = medicine_detail_serializers.data
            new_medicine_list.append(medicine)
        response_dict = {'error': False,
                         'message': 'All Medicine  list Invoked',
                         'data': new_medicine_list}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = MedicineSerializers(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            medicine_id = serializer.data['id']
            medicine_detail_list = []
            for medicine_detail in request.data['medicine_details']:
                # adding medicine id to the medicinedetails leist
                medicine_detail['medicine_id'] = medicine_id
                medicine_detail_list.append(medicine_detail)
            serializer2 = MedicalDetailsSerializers(data=medicine_detail_list, many=True, context={'request': request})
            serializer2.is_valid()
            serializer2.save()
            response_dict = {'error': False,
                             'message': "Medicinec data Created successfully",
                             'data': serializer.data}
        except:
            response_dict = {'error': True,
                             'message': " Error During creating Medicine", }
        return Response(response_dict)

    def retrieve(self, request, pk):
        try:
            queryset = Medicine.objects.all()
            medicine = get_object_or_404(queryset, pk=pk)
            serializer = CompanyBankSerializer(medicine, context={"request": request})
            medicine_detail = MedicalDetails.objects.filter(medicine_id=serializer['id'])
            new_medicine_data = serializer.data
            medicine_detail_serializers = SimpleMedicalDetailsSerializers(medicine_detail, many=True)
            new_medicine_data['medicine_details'] = medicine_detail_serializers.data
            response_dict = {"error": False, "message": "Medicine data invoked", 'data': new_medicine_data.data}
        except:
            response_dict = {"error": False, "message": "Error invoking Medicine data "}
        return Response(response_dict)

    def update(self, request, pk=None):
        try:
            queryset = Medicine.objects.all()
            medicine = get_object_or_404(queryset, pk=pk)
            serializer = MedicineSerializers(medicine, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            for details in request.data['medicine_details']:
                if details['id'] == 0:
                    del details['id']
                    details['medicine_id'] = pk
                    medicine_detail_serializers = MedicalDetailsSerializers(data=details,
                                                                            context={'request': request})
                    medicine_detail_serializers.is_valid(raise_exception=True)
                    medicine_detail_serializers.save()
                else:
                    id = details['id']
                    details_update = get_object_or_404(MedicalDetails, pk=id)
                    serializer = MedicalDetailsSerializers(details_update, data=details, context={request: request})
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
            response_dict = {'error': False,
                             'message': 'Medicine data Updated successfully',
                             }
        except:
            response_dict = {'error': True,
                             'message': 'Error Updating Medicine data', }

        return Response(response_dict)


class MedicalDetailsViewSets(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def create(self, request):
        try:
            serializer = MedicalDetailsSerializers(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_dict = {'error': False,
                             'message': "Medical Details Created successfully",
                             'data': serializer.data}
        except:
            response_dict = {'error': True,
                             'message': " Error During creating Medical Details", }
        return Response(response_dict)

    def list(self, request):
        bank_list = MedicalDetails.objects.all()
        serializer = MedicalDetailsSerializers(bank_list, many=True, context={"request": request})
        response_dict = {'error': False,
                         'message': 'All Medical Details list Invoked',
                         'data': serializer.data}
        return Response(response_dict)

    def retrieve(self, request, pk):
        try:
            queryset = MedicalDetails.objects.all()
            medicaldetails = get_object_or_404(queryset, pk=pk)
            serializer = MedicalDetailsSerializers(medicaldetails, context={"request": request})
            response_dict = {"error": False, "message": "Medical Details invoked", 'data': serializer.data}
        except:
            response_dict = {"error": False, "message": "Error invocking Medical Details ", 'data': serializer.data}
        return Response(response_dict)

    def update(self, request, pk=None):
        try:
            queryset = MedicalDetails.objects.all()
            medicaldetails = get_object_or_404(queryset, pk=pk)
            serializer = MedicalDetailsSerializers(medicaldetails, data=request.data, context={"request": request})

            serializer.is_valid(raise_exception=True)

            serializer.save()
            response_dict = {'error': False,
                             'message': 'Medical Details Updated successfully',
                             }
        except:
            response_dict = {'error': True,
                             'message': 'Error Updating Medical Details', }

        return Response(response_dict)


class CustomerViewSets(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def create(self, request):
        try:
            serializer = CustomerSerializers(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_dict = {'error': False,
                             'message': "Customer Created successfully",
                             'data': serializer.data}
        except:
            response_dict = {'error': True,
                             'message': " Error During creating Customer", }
        return Response(response_dict)

    def list(self, request):
        bank_list = Customer.objects.all()
        serializer = CustomerSerializers(bank_list, many=True, context={"request": request})
        response_dict = {'error': False,
                         'message': 'All Customer list Invoked',
                         'data': serializer.data}
        return Response(response_dict)

    def retrieve(self, request, pk):
        try:
            queryset = Customer.objects.all()
            customer = get_object_or_404(queryset, pk=pk)
            serializer = CustomerSerializers(customer, context={"request": request})
            response_dict = {"error": False, "message": "Customer invoked", 'data': serializer.data}
        except:
            response_dict = {"error": False, "message": " Error in Customer invoke", 'data': serializer.data}
        return Response(response_dict)

    def update(self, request, pk=None):
        try:
            queryset = Customer.objects.all()
            customer = get_object_or_404(queryset, pk=pk)
            serializer = CustomerSerializers(customer, data=request.data, context={"request": request})

            serializer.is_valid(raise_exception=True)

            serializer.save()
            response_dict = {'error': False,
                             'message': 'Customer Updated successfully',
                             }
        except:
            response_dict = {'error': True,
                             'message': 'Error Updating Customer', }

        return Response(response_dict)


class CustomerRequestViewSets(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def create(self, request):
        try:
            serializer = CustomerRequestSerializers(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_dict = {'error': False,
                             'message': "CustomerRequest Created successfully",
                             'data': serializer.data}
        except:
            response_dict = {'error': True,
                             'message': " Error During creating CustomerRequest", }
        return Response(response_dict)

    def list(self, request):
        bank_list = CustomerRequest.objects.all()
        serializer = CustomerRequestSerializers(bank_list, many=True, context={"request": request})
        response_dict = {'error': False,
                         'message': 'All Customer Request list Invoked',
                         'data': serializer.data}
        return Response(response_dict)

    def retrieve(self, request, pk):
        try:
            queryset = CustomerRequest.objects.all()
            customerrequest = get_object_or_404(queryset, pk=pk)
            serializer = CustomerRequestSerializers(customerrequest, context={"request": request})
            response_dict = {"error": False, "message": "Customer Request invoked", 'data': serializer.data}
        except:
            response_dict = {"error": False, "message": "Error in Customer Request invok", 'data': serializer.data}
        return Response(response_dict)

    def update(self, request, pk=None):
        try:
            queryset = CustomerRequest.objects.all()
            print('entering try block')
            customer_request = get_object_or_404(queryset, id=pk)
            print('customer invoked')
            serializer = CustomerRequestSerializers(customer_request, data=request.data, context={"request": request})
            print('hello validating')
            serializer.is_valid(raise_exception=True)
            print('data validated')
            serializer.save()
            response_dict = {'error': False,
                             'message': 'Customer Request Updated successfully',
                             }
        except:
            response_dict = {'error': True,
                             'message': 'Error Updating Customer Request', }

        return Response(response_dict)

    def destroy(self, request, pk=None):
        try:
            queryset = CustomerRequest.objects.all()
            customer_requst = get_object_or_404(queryset, pk=pk)
            customer_requst.delete()
            response_dict = {'error': False,
                             'message': 'Customer Request Delete successfully',
                             }
        except:
            response_dict = {'error': True,
                             'message': 'Error Deleting customer request', }

        return Response(response_dict)


class EmployeeViewSets(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def create(self, request):
        try:
            serializer = EmployeeSerializers(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_dict = {'error': False,
                             'message': "Employee Created successfully",
                             'data': serializer.data}
        except:
            response_dict = {'error': True,
                             'message': " Error During creating Employee", }
        return Response(response_dict)

    def list(self, request):
        bank_list = Employee.objects.all()
        serializer = EmployeeSerializers(bank_list, many=True, context={"request": request})
        response_dict = {'error': False,
                         'message': 'All Employee list Invoked',
                         'data': serializer.data}
        return Response(response_dict)

    def retrieve(self, request, pk):
        try:
            queryset = Employee.objects.all()
            employee = get_object_or_404(queryset, pk=pk)
            serializer = EmployeeSerializers(employee, context={"request": request})
            response_dict = {"error": False, "message": "Employee invoked", 'data': serializer.data}
        except:
            response_dict = {"error": False, "message": "Error in Employee invok", 'data': serializer.data}
        return Response(response_dict)

    def update(self, request, pk=None):
        try:
            queryset = Employee.objects.all()
            employee = get_object_or_404(queryset, pk=pk)
            serializer = EmployeeSerializers(employee, data=request.data, context={"request": request})

            serializer.is_valid(raise_exception=True)

            serializer.save()
            response_dict = {'error': False,
                             'message': 'Employee Updated successfully',
                             }
        except:
            response_dict = {'error': True,
                             'message': 'Error Updating Employee', }

        return Response(response_dict)


class EmployeeSalaryList(ListAPIView):
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get(self, request, id):
        try:
            salaryinfo = EmployeeSalary.objects.filter(employee_id=id)
            serializer = EmployeeSalarySerializers(salaryinfo, many=True, context={"request": request})
            response_dict = {'error': False,
                             'message': 'All Employee Salary list Invoked',
                             'data': serializer.data}
        except:
            response_dict = {'error': True,
                             'message': " Error During creating Employee Salary", }

        return Response(response_dict)


class EmployeeSalaryViewSets(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def create(self, request):
        try:
            serializer = EmployeeSalarySerializers(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_dict = {'error': False,
                             'message': "Employee Salary Created successfully",
                             'data': serializer.data}
        except:
            response_dict = {'error': True,
                             'message': " Error During creating Employee Salary", }
        return Response(response_dict)

    def list(self, request, id):
        bank_list = EmployeeSalary.objects.filter(employee_id=id)
        serializer = EmployeeSalarySerializers(bank_list, many=True, context={"request": request})
        response_dict = {'error': False,
                         'message': 'All Employee Salary list Invoked',
                         'data': serializer.data}
        return Response(response_dict)

    def retrieve(self, request, pk):
        try:
            queryset = EmployeeSalary.objects.all()
            employeesalary = get_object_or_404(queryset, pk=pk)
            serializer = EmployeeSalarySerializers(employeesalary, context={"request": request})
            response_dict = {"error": False, "message": "Employee Salary invoked", 'data': serializer.data}
        except:
            response_dict = {"error": True, "message": "Error in Employee Salary invok", }
        return Response(response_dict)

    def update(self, request, pk=None):
        try:
            queryset = EmployeeSalary.objects.all()
            employeesalary = get_object_or_404(queryset, pk=pk)
            serializer = EmployeeSalarySerializers(employeesalary, data=request.data, context={"request": request})

            serializer.is_valid(raise_exception=True)

            serializer.save()
            response_dict = {'error': False,
                             'message': 'Employee Salary Updated successfully',
                             }
        except:
            response_dict = {'error': True,
                             'message': 'Error Updating EmployeeS alary', }

        return Response(response_dict)

    def destroy(self, request, pk=None):
        try:
            queryset = EmployeeSalary.objects.all()
            employeesalary = get_object_or_404(queryset, pk=pk)
            employeesalary.delete()
            response_dict = {'error': False,
                             'message': 'Employee Salary Delete successfully',
                             }
        except:
            response_dict = {'error': True,
                             'message': 'Error Deleting EmployeeS alary', }

        return Response(response_dict)


class EmployeeBankViewSets(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def create(self, request):
        try:
            serializer = EmployeeBankSerializers(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_dict = {'error': False,
                             'message': "Employee Bank Created successfully",
                             'data': serializer.data}
        except:
            response_dict = {'error': True,
                             'message': " Error During creating Employee Bank", }
        return Response(response_dict)

    def list(self, request):
        bank_list = EmployeeBank.objects.all()
        serializer = EmployeeBankSerializers(bank_list, many=True, context={"request": request})
        response_dict = {'error': False,
                         'message': 'All Employee Bank list Invoked',
                         'data': serializer.data}
        return Response(response_dict)

    def retrieve(self, request, pk):
        try:
            queryset = EmployeeBank.objects.all()
            employeebank = get_object_or_404(queryset, pk=pk)
            serializer = EmployeeBankSerializers(employeebank, context={"request": request})
            response_dict = {"error": False, "message": "Employee Bank invoked", 'data': serializer.data}
        except:
            response_dict = {"error": False, "message": "Error in Employee Bank invok", 'data': serializer.data}
        return Response(response_dict)

    def update(self, request, pk=None):
        try:
            queryset = EmployeeBank.objects.all()
            employeebank = get_object_or_404(queryset, pk=pk)
            serializer = EmployeeBankSerializers(employeebank, data=request.data, context={"request": request})

            serializer.is_valid(raise_exception=True)

            serializer.save()
            response_dict = {'error': False,
                             'message': 'Employee Bank Updated successfully',
                             }
        except:
            response_dict = {'error': True,
                             'message': 'Error Updating Employee Bank', }

        return Response(response_dict)

    def destroy(self, request, pk):
        try:
            queryset = EmployeeBank.objects.all()
            employeebank = get_object_or_404(queryset, pk=pk)
            employeebank.delete()
            response_dict = {'error': False,
                             'message': 'Employee Bank Delete successfully',
                             }
        except:
            response_dict = {'error': True,
                             'message': 'Error Deleting Employee Bank', }
        return Response(response_dict)


class EmployeeBankList(ListAPIView):
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get(self, request, id):
        try:
            bankinfo = EmployeeBank.objects.filter(employee_id=id)
            serializer = EmployeeBankSerializers(bankinfo, many=True, context={"request": request})
            response_dict = {'error': False,
                             'message': 'Employee Bank list Invoked',
                             'data': serializer.data}
        except:
            response_dict = {'error': True,
                             'message': " Error in Invoking Employee Bank List", }
        return Response(response_dict)


class BillViewSets(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def create(self, request):
        try:
            serializer = BillSerializers(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_dict = {'error': False,
                             'message': "Bill Created successfully",
                             'data': serializer.data}
        except:
            response_dict = {'error': True,
                             'message': " Error During creating Bill", }
        return Response(response_dict)

    def list(self, request):
        bank_list = Bill.objects.all()
        serializer = BillSerializers(bank_list, many=True, context={"request": request})
        response_dict = {'error': False,
                         'message': 'All Bill list Invoked',
                         'data': serializer.data}
        return Response(response_dict)

    def retrieve(self, request, pk):
        try:
            queryset = Bill.objects.all()
            bill = get_object_or_404(queryset, pk=pk)
            serializer = BillSerializers(bill, context={"request": request})
            response_dict = {"error": False, "message": "Bill invoked", 'data': serializer.data}
        except:
            response_dict = {"error": True, "message": "Error in Bill invok", 'data': serializer.data}
        return Response(response_dict)

    def update(self, request, pk=None):
        try:
            queryset = Bill.objects.all()
            bill = get_object_or_404(queryset, pk=pk)
            serializer = BillSerializers(bill, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_dict = {'error': False,
                             'message': 'Bill Updated successfully',
                             }
        except:
            response_dict = {'error': True,
                             'message': 'Error Updating Bill', }

        return Response(response_dict)


class BillDetailsViewSets(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def create(self, request):
        try:
            serializer = BillDetailsSerializers(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_dict = {'error': False,
                             'message': "Bill Details Created successfully",
                             'data': serializer.data}
        except:
            response_dict = {'error': True,
                             'message': " Error During creating Bill Details", }
        return Response(response_dict)

    def list(self, request):
        bank_list = BillDetails.objects.all()
        serializer = BillDetailsSerializers(bank_list, many=True, context={"request": request})
        response_dict = {'error': False,
                         'message': 'All Bill Details list Invoked',
                         'data': serializer.data}
        return Response(response_dict)

    def retrieve(self, request, pk):
        try:
            queryset = BillDetails.objects.all()
            billdetails = get_object_or_404(queryset, pk=pk)
            serializer = BillDetailsSerializers(billdetails, context={"request": request})
            response_dict = {"error": False, "message": "BillDetails invoked", 'data': serializer.data}
        except:
            response_dict = {"error": True, "message": "Error in Bill Details invok", 'data': serializer.data}
        return Response(response_dict)

    def update(self, request, pk=None):
        try:
            queryset = BillDetails.objects.all()
            billdetails = get_object_or_404(queryset, pk=pk)
            serializer = BillDetailsSerializers(billdetails, data=request.data, context={"request": request})

            serializer.is_valid(raise_exception=True)

            serializer.save()
            response_dict = {'error': False,
                             'message': 'BillDetails Updated successfully',
                             }
        except:
            response_dict = {'error': True,
                             'message': 'Error Updating Bill Details', }

        return Response(response_dict)


class CompanyNameViewSets(ListAPIView):
    serializer_class = MedicineCompanySerializers

    def get_queryset(self):
        name = self.kwargs['name']
        return MedicineCompany.objects.filter(name__contains=name)


class MedicineByNameViewSets(ListAPIView):
    serializer_class = MedicineSerializers

    def get_queryset(self):
        name = self.kwargs['name']
        return Medicine.objects.filter(name__contains=name)


class BillGenerateViewSets(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def create(self, request):
        try:
            # first creating the Customer of the bill
            customer_serializer = CustomerSerializers(data=request.data, context={"request": request})
            customer_serializer.is_valid(raise_exception=True)
            customer_serializer.save()
            print('customer is valid')
            # adding the bill for the customer just added
            customer_id = customer_serializer.data['id']
            print('hello')
            if customer_id:
                print('id found')

            else:
                print('no id found')


            bill_data = {}
            bill_data['customer_id'] = customer_id
            bill_serializer = BillSerializers(data=bill_data, context={"request": request})
            bill_serializer.is_valid(raise_exception=True)
            bill_serializer.save()
            print('Bill is valid')

            # adding the dill details with the medicine
            bill_id = bill_serializer.data['id']

            bill_details_list = []

            for medicine in request.data["medicine_list"]:
                bill_details = {}
                bill_details['bill_id'] = bill_id
                bill_details['medicine_id'] = medicine['medicine_id']
                bill_details['qty'] = medicine['qty']
                bill_details_list.append(bill_details)

            bill_details_serializer = BillDetailsSerializers(data=bill_details_list, many=True,
                                                             context={"request": request})
            bill_details_serializer.is_valid(raise_exception=True)
            print('Bill details is valid')

            bill_details_serializer.save()

            response_dict = {'error': False,
                             'message': "Bill Generated successfully",
                             }
        except:
            response_dict = {'error': True,
                             'message': " Error During Generating Bill", }
        return Response(response_dict)

    def list(self, request):
        bank_list = BillDetails.objects.all()
        serializer = BillDetailsSerializers(bank_list, many=True, context={"request": request})
        response_dict = {'error': False,
                         'message': 'All Bill Details list Invoked',
                         'data': serializer.data}
        return Response(response_dict)

    def retrieve(self, request, pk):
        try:
            queryset = BillDetails.objects.all()
            billdetails = get_object_or_404(queryset, pk=pk)
            serializer = BillDetailsSerializers(billdetails, context={"request": request})
            response_dict = {"error": False, "message": "BillDetails invoked", 'data': serializer.data}
        except:
            response_dict = {"error": True, "message": "Error in Bill Details invok", 'data': serializer.data}
        return Response(response_dict)

    def update(self, request, pk=None):
        try:
            queryset = BillDetails.objects.all()
            billdetails = get_object_or_404(queryset, pk=pk)
            serializer = BillDetailsSerializers(billdetails, data=request.data, context={"request": request})

            serializer.is_valid(raise_exception=True)

            serializer.save()
            response_dict = {'error': False,
                             'message': 'BillDetails Updated successfully',
                             }
        except:
            response_dict = {'error': True,
                             'message': 'Error Updating Bill Details', }

        return Response(response_dict)


class HomePageViewSets(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def list(self, request):
        employee = Employee.objects.all()
        employee_serializer = EmployeeSerializers(employee, many=True, context={"request": request})
        employee_number = len(employee_serializer.data)
        customer_request = CustomerRequest.objects.all()
        customer_request_pending = customer_request.filter(statue=False)
        customer_request_serializer = CustomerRequestSerializers(customer_request, many=True,
                                                                 context={"request": request})
        customer_pending_request_serializer = CustomerRequestSerializers(customer_request_pending, many=True,
                                                                         context={"request": request})
        medicine = Medicine.objects.all()
        medicine_serializer = MedicineSerializers(medicine, many=True, context={'request': request})
        company = MedicineCompany.objects.all()
        company_serializer = MedicineCompanySerializers(company, many=True, context={'request': request})
        bill_details = BillDetails.objects.all()
        current_date = datetime.date.today().strftime('%Y-%m-%d')
        total_buy_amount = 0
        total_sell_amount = 0
        for item in bill_details:
            total_buy_amount = total_buy_amount + float(item.medicine_id.buy_price * item.qty)
            total_sell_amount = total_sell_amount + float(item.medicine_id.sell_price * item.qty) +(( float(item.medicine_id.sell_price * item.qty) * float(item.medicine_id.vat))/100)
        total_profit = total_sell_amount - total_buy_amount

        today_bill = bill_details.filter(added_on=current_date)
        today_total_buy_amount = 0
        today_total_sell_amount = 0
        for itemtoday in today_bill:
            today_total_buy_amount = today_total_buy_amount + float(itemtoday.medicine_id.buy_price * itemtoday.qty)
            today_total_sell_amount = today_total_sell_amount + float(itemtoday.medicine_id.sell_price * itemtoday.qty) +(( float(itemtoday.medicine_id.sell_price * itemtoday.qty) * float(item.medicine_id.vat))/100)
        today_total_profit = today_total_sell_amount - today_total_buy_amount
        total_company = len(company_serializer.data)
        total_medicine = len(medicine_serializer.data)
        total_request = len(customer_request_serializer.data)
        pending_request = len(customer_pending_request_serializer.data)
        completed_request = total_request - pending_request

        response_dict = {'error': False,
                         'message': 'All Bill Details list Invoked',
                         'employee_number': employee_number,
                         'total_company': total_company,
                         'total_medicine': total_medicine,
                         'total_request': total_request,
                         'pending_request': pending_request,
                         'completed_request': completed_request,
                         'total_buy_amount': total_buy_amount,
                         'total_sell_amount': total_sell_amount,
                         'total_profit': total_profit,
                         'today_total_profit': today_total_profit,
                         'today_total_sell': today_total_sell_amount,
                         }
        return Response(response_dict)


medicinecompany_list = MedicineCompanyViewSet.as_view({"get": "list"})
medicinecompany_create = MedicineCompanyViewSet.as_view({"post": "create"})
medicinecompany_update = MedicineCompanyViewSet.as_view({"put": "update"})
