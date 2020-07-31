from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.FinRecords,name ='fr'),
    path("first",views.first,name='first'),
    path('display',views.disp,name="display"),
    path('edit',views.edit,name="edit"),
    path('cashAcc',views.CashAccountDisp,name="cs"),
]
