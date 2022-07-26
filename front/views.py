from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from django.contrib.auth import logout

# Create your views here.
def home(request):
	return render(request, 'front/home.html')

def loans(request):
	return render(request, 'front/loans.html')

def logged_out(request):
	logout(request)
	return redirect('home')

def properties(request):
	return render(request, 'front/properties.html')


def others(request):
	form = QueryForm()
	if request.method == 'POST':
		form = QueryForm(request.POST)
		form.save()
		print('form saved')
		return redirect('home')
	context = { 'form' : form }
	return render(request, 'front/others.html', context)


def homeloan(request):
	return render(request, 'front/homeloan.html')


def homeloantype(request,loantype):
	if(loantype == 'salaried'):
		return redirect('homeloansalaried')
	else:
		return redirect('homeloanselfemployed')


def homeloansalaried(request):
	form = Homeloansalariedform(initial={ 'salaried' : True})
	return render(request, 'front/forms.html',{ 'form' : form })


def homeloanselfemployed(request):
	form = Homeloanselfform(initial = { 'self_employed' : True})
	print('selfemployed')
	return render(request, 'front/forms.html',{ 'form' : form })



def businessloan(request):
	form = Businessloanform()
	return render(request, 'front/forms.html',{ 'form' : form })



def laptype(request,loantype):
	if(loantype == 'salaried'):
		return redirect('lapsalaried')
	else:
		return redirect('lapselfemployed')


def lapsalaried(request):
	form = LAPsalariedform(initial={ 'salaried' : True})
	return render(request, 'front/forms.html',{ 'form' : form })


def lapselfemployed(request):
	form = LAPselfform(initial = { 'self_employed' : True})
	return render(request, 'front/forms.html',{ 'form' : form })


def pl(request):
	form = PL()
	return render(request,'front/forms.html', { 'form' : form })

def hlttype(request,loantype):
	if(loantype == 'salaried'):
		return redirect('hltsalaried')
	else:
		return redirect('hltself')


def hltsalaried(request):
	form = HLTsalariedform(initial={ 'salaried' : True})
	return render(request, 'front/forms.html',{ 'form' : form })

def hltself(request):
	form = HLTselfform(initial = { 'self_employed' : True})
	return render(request, 'front/forms.html',{ 'form' : form })
