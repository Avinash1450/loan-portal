from django import forms
from django.forms import Textarea
from .models import *

class QueryForm(forms.ModelForm):
	class Meta:
		model = Query
		widgets = {
			'query' : Textarea() 
		}
		fields = "__all__"

class Homeloansalariedform(forms.ModelForm):
	class Meta:
		model = Homeloan
		fields = ['name','mobile_no','salaried','net_monthly_income','address','pincode','property_market_value','loan_amount_needed']


class Homeloanselfform(forms.ModelForm):
	class Meta:
		model = Homeloan
		fields = ['name','mobile_no','self_employed','annual_turnover','number_of_ITR','address','pincode','property_market_value','loan_amount_needed']

class Businessloanform(forms.ModelForm):
	class Meta:
		model = Businessloan
		fields = ['name','mobile_no','current_address','pincode','loan_amount_needed','annual_turnover','number_of_ITR','business_registration']



class LAPsalariedform(forms.ModelForm):
	class Meta:
		model = LoanAgainstProperty
		fields = ['name','mobile_no','salaried','net_monthly_income','address','pincode','property_market_value','loan_amount_needed','property_type']


class LAPselfform(forms.ModelForm):
	class Meta:
		model = LoanAgainstProperty
		fields = ['name','mobile_no','self_employed','annual_turnover','number_of_ITR','address','pincode','property_market_value','loan_amount_needed','property_type']


class PL(forms.ModelForm):

	class Meta:
		model = PersonalLoan
		fields = '__all__'

class HLTsalariedform(forms.ModelForm):

	class Meta:
		model = Homeloantransfer
		fields = ['name','mobile_no','address','pincode','salaried','net_monthly_income','topup_required']


class HLTselfform(forms.ModelForm):

	class Meta:
		model = Homeloantransfer
		fields = ['name','mobile_no','address','pincode','self_employed','annual_profit','existing_loan','current_outstanding','topup_required']