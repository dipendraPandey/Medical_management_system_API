from rest_framework import serializers
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


#  ********************** Medicine Company related serializers **********************************##################
class CompanyAccountSerializers(serializers.ModelSerializer):
    class Meta:
        model = CompanyAccount
        fields = '__all__'

    def to_representation(self, instance):
        response = super(CompanyAccountSerializers, self).to_representation(instance)
        response['medicinecompany'] = MedicineCompanySerializers(instance.company_id).data
        return response


class MedicineCompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = MedicineCompany
        fields = '__all__'


class CompanyBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyBank
        fields = '__all__'

    # def to_representation(self, instance):
    #     response = super(CompanyBankSerializer, self).to_representation(instance)
    #     response['medicinecompany'] = MedicineCompanySerializers(instance.company_id).data
    #     return response


#  ***** Medicine Related serializers ********************************##########################################

class MedicineSerializers(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'

    def to_representation(self, instance):
        response = super(MedicineSerializers, self).to_representation(instance)
        response['medicinecompany'] = MedicineCompanySerializers(instance.company_id).data
        return response


class MedicalDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = MedicalDetails
        fields = '__all__'

    def to_representation(self, instance):
        response = super(MedicalDetailsSerializers, self).to_representation(instance)
        response['medicine'] = MedicineSerializers(instance.medicine_id).data
        return response


class SimpleMedicalDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = MedicalDetails
        fields = '__all__'


# ************************** Employee Related serializers *********************************#######################


class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeSalarySerializers(serializers.ModelSerializer):
    class Meta:
        model = EmployeeSalary
        fields = '__all__'

    def to_representation(self, instance):
        response = super(EmployeeSalarySerializers, self).to_representation(instance)
        response['employee'] = EmployeeSerializers(instance.employee_id).data
        return response


class EmployeeBankSerializers(serializers.ModelSerializer):
    class Meta:
        model = EmployeeBank
        fields = '__all__'

    def to_representation(self, instance):
        response = super(EmployeeBankSerializers, self).to_representation(instance)
        response['employee'] = EmployeeSerializers(instance.employee_id).data
        return response


#  ************************* Bill Related Serializers *****************************##########################


class BillDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = BillDetails
        fields = '__all__'

    # def to_representation(self, instance):
    #     response = super(BillDetailsSerializers, self).to_representation(instance)
    #     response['bill'] = BillSerializers(instance.bill_id).data
    #     response['medicine'] = MedicineSerializers(instance.medicine_id).data
    #     return response


class BillSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'

    # def to_representation(self, instance):
    #     response = super(BillSerializers, self).to_representation(instance)
    #     response['customer'] = CustomerSerializers(instance.customer_id).data
    #     return response


# ***********Customer related serializer **************************************########################

class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class CustomerRequestSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomerRequest
        fields = '__all__'
