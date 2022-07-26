from django.db import models
from datetime import date
import datetime

# Create your models here.

class Query(models.Model):
	name = models.CharField(max_length=30)
	email = models.EmailField()
	mobile_no = models.CharField(max_length=10)
	address = models.CharField(max_length=50,help_text="(Your current address)")
	query = models.TextField(max_length=100,help_text="(Enter yoyr query")
	date = models.DateField(auto_now_add=True)
	status = models.CharField(max_length=50, default="pending",blank=True)

	def __str__(self):
		return self.name + "  status - " + self.status

class Homeloan(models.Model):
	cus_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=30)
	mobile_no = models.CharField(max_length=10)
	salaried = models.BooleanField(max_length=10)
	self_employed = models.BooleanField(default=False)
	net_monthly_income = models.CharField(max_length=10)
	annual_turnover = models.CharField(max_length=10)
	number_of_ITR = models.IntegerField(help_text="(Number of years ITR available for)")
	address = models.CharField(max_length=40,help_text="(Your current address)")
	pincode = models.CharField(max_length=6)
	property_market_value =  models.CharField(max_length=8)
	loan_amount_needed = models.CharField(max_length=8)
	date = models.DateField(auto_now_add=True)
	status = models.CharField(max_length=50, default="pending",blank=True)

	def __str__(self):
		return self.name + "  status - " + self.status


class Businessloan(models.Model):
	CHOICES = [
		('yes','YES'),
		('no','NO')]
	name = models.CharField(max_length=30,help_text="(As per PAN Card)")
	mobile_no = models.CharField(max_length=10)
	current_address = models.CharField(max_length=40)
	pincode = models.CharField(max_length=6)
	loan_amount_needed = models.CharField(max_length=8)
	annual_turnover = models.CharField(max_length=10)
	number_of_ITR = models.IntegerField(help_text="(Number of years ITR available for)")
	business_registration = models.CharField(max_length=3,choices=CHOICES,default="YES")
	date = models.DateField(auto_now_add=True)
	status = models.CharField(max_length=50, default="pending",blank=True)

	def __str__(self):
		return self.name + "  status - " + self.status


class LoanAgainstProperty(models.Model):

	CHOICES = [
		('residential','RESIDENTIAL'),
		('commercial','COMMERCIAL'),
		('industrial','INDUSTRIAL')]

	cus_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=30)
	mobile_no = models.CharField(max_length=10)
	salaried = models.BooleanField(max_length=10)
	self_employed = models.BooleanField(default=False)
	net_monthly_income = models.CharField(max_length=10)
	annual_turnover = models.CharField(max_length=10)
	number_of_ITR = models.IntegerField(help_text="(Number of years ITR available for)")
	address = models.CharField(max_length=40,help_text="(Your current address)")
	pincode = models.CharField(max_length=6)
	property_market_value =  models.CharField(max_length=8)
	loan_amount_needed = models.CharField(max_length=8)
	property_type = models.CharField(max_length=15,choices=CHOICES,default="commercial",help_text="(Choose any)")
	date = models.DateField(auto_now_add=True)
	status = models.CharField(max_length=50, default="pending",blank=True)

	def __str__(self):
		return self.name + "  status - " + self.status


class PersonalLoan(models.Model):

	CHOICES = [
		('private','PRIVATE'),
		('goverment','GOVERMENT')]
	name = models.CharField(max_length=30)
	mobile_no = models.CharField(max_length=10)
	net_monthly_income = models.CharField(max_length=8)
	job_type = models.CharField(max_length=10,choices=CHOICES,default="private")
	bank_name = models.CharField(max_length=30,help_text="(Salary account bank name)")
	emi = models.CharField(max_length=10,help_text="(EMI if any)")
	experience = models.IntegerField(help_text="(Total working experience)")
	loan_amount_needed = models.CharField(max_length=7)
	date = models.DateField(auto_now_add=True)
	status = models.CharField(max_length=50, default="pending",blank=True)

	def __str__(self):
		return self.name + "  status - " + self.status


class Homeloantransfer(models.Model):
	CHOICES = [
		('yes','YES'),
		('no','NO')]
	cus_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=30)
	mobile_no = models.CharField(max_length=10)
	address = models.CharField(max_length=40,help_text="(Your current address)")
	pincode = models.CharField(max_length=6)
	self_employed = models.BooleanField(default=False)
	annual_profit = models.CharField(max_length=10,help_text="(As per ITR)")
	existing_loan = models.CharField(max_length=30,help_text="(Existing loan if any)",blank=True)
	current_outstanding = models.CharField(max_length=10,help_text="(Current loan outstanding(bank deatils) if any)",blank=True)
	salaried = models.BooleanField(max_length=10)
	net_monthly_income = models.CharField(max_length=10)
	topup_required = models.CharField(max_length=3,choices=CHOICES,default="NO")
	status = models.CharField(max_length=50, default="pending",blank=True)

	def __str__(self):
		return self.name + "  status - " + self.status





