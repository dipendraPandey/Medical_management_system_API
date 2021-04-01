from django.db import models


# ******************* Company Details **********************************####

class MedicineCompany(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    license_no = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    description = models.CharField(max_length=1000)
    added_on = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class CompanyAccount(models.Model):
    PAYMENT_CHOICE = [
        ('DEBIT', 'Debit'),
        ('CREDIT', 'Credit'),
    ]
    id = models.AutoField(primary_key=True)
    company_id = models.ForeignKey(MedicineCompany, on_delete=models.CASCADE)
    transaction_type = models.CharField(choices=PAYMENT_CHOICE, max_length=120)
    transaction_amount = models.CharField(max_length=255)
    transaction_date = models.DateField()
    payment_mode = models.CharField(max_length=255)
    objects = models.Manager()


class CompanyBank(models.Model):
    id = models.AutoField(primary_key=True)
    bank_account_no = models.CharField(max_length=255)
    company_id = models.ForeignKey(MedicineCompany, on_delete=models.CASCADE)
    added_on = models.DateField(auto_now_add=True)
    objects = models.Manager()


# ******************************Medicine models ******************************

class Medicine(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    medical_type = models.CharField(max_length=255)
    buy_price = models.DecimalField(max_digits=10, decimal_places=2)
    sell_price = models.DecimalField(max_digits=10, decimal_places=2)
    vat = models.DecimalField(max_digits=10, decimal_places=2)
    batch_no = models.CharField(max_length=255)
    shelf_no = models.CharField(max_length=255)
    expire_date = models.DateField()
    mfg_date = models.DateField()
    company_id = models.ForeignKey(MedicineCompany, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    in_stock = models.IntegerField()
    qty_in_strip = models.IntegerField()
    added_on = models.DateField(auto_now_add=True)
    objects = models.Manager()


class MedicalDetails(models.Model):
    id = models.AutoField(primary_key=True)
    medicine_id = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    salt_name = models.CharField(max_length=255)
    salt_qty = models.CharField(max_length=255)
    salt_qty_type = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    added_on = models.DateField(auto_now_add=True)
    objects = models.Manager()


#  *************************************Customer Related models ************************** ######
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    added_on = models.DateField(auto_now_add=True)
    objects = models.Manager()


class CustomerRequest(models.Model):
    id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    medicine_detail = models.CharField(max_length=255)
    statue = models.BooleanField(default=False)
    added_on = models.DateField(auto_now_add=True)
    objects = models.Manager()


# **************************Employee related models *********************************######

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    joining_date = models.DateField()
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    added_on = models.DateField(auto_now_add=True)
    objects = models.Manager()


class EmployeeSalary(models.Model):
    id = models.AutoField(primary_key=True)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary_date = models.DateField()
    salary_amount = models.CharField(max_length=255)
    salary = models.CharField(max_length=255)
    added_on = models.DateField(auto_now_add=True)
    objects = models.Manager()


class EmployeeBank(models.Model):
    id = models.AutoField(primary_key=True)
    bank_account_no = models.CharField(max_length=255)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    added_on = models.DateField(auto_now_add=True)
    objects = models.Manager()

# ************************* Bill related models *******************#########

class Bill(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    added_on = models.DateField(auto_now_add=True)
    objects = models.Manager()


class BillDetails(models.Model):
    id = models.AutoField(primary_key=True)
    bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE)
    medicine_id = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    qty = models.IntegerField()
    added_on = models.DateField(auto_now_add=True)
    objects = models.Manager()




# //
# //
# //
# //
# //
# //
# //
# // description
# // in_stock
# // qty_in_strip
# // added_on   company_id
