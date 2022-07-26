from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^admin/logout/$', views.logged_out),
    path('admin/', admin.site.urls),
    path('loans/', views.loans, name='loans'),
    path('properties/', views.properties, name='properties'),
    path('others/', views.others, name='others'),
    path('homeloan/', views.homeloan, name='homeloan'),
    path('homeloan/<str:loantype>', views.homeloantype, name='homeloantype'),
    path('homeloansalaried/', views.homeloansalaried, name='homeloansalaried'),
    path('homeloanselfemployed/', views.homeloanselfemployed, name='homeloanselfemployed'),
    path('businessloan/', views.businessloan, name='businessloan'),
    path('loanagainstproperty/<str:loantype>', views.laptype, name='laptype'),
    path('loanagainstpropertysalaried/', views.lapsalaried, name='lapsalaried'),
    path('loanagainstpropertyselfemployed/', views.lapselfemployed, name='lapselfemployed'),
    path('personalloan/', views.pl, name='pl'),
    path('homeloantransfertype/<str:loantype>', views.hlttype, name='hlttype'),
    path('homeloantransfersalaried/', views.hltsalaried, name='hltsalaried'),
    path('homeloantransferselfemployed/', views.hltself, name='hltself'),
    

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
