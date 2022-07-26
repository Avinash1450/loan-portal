from django.contrib import admin
from .models import * 

# Register your models 
admin.site.register(Homeloan)
admin.site.register(Businessloan)
admin.site.register(LoanAgainstProperty)
admin.site.register(PersonalLoan)
admin.site.register(Query)
admin.site.register(Homeloantransfer)