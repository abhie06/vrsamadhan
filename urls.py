from django.urls import path
from .import views 

from django.urls import path

urlpatterns = [
   

    path("register",views.register, name ="register"),
    path("form",views.form,name="form"),
    path('permission/',views.permission,name='permission'),
    path('appr/<str:id>', views.appr,name ='appr'),
    path('disappr/<str:id>', views.disappr,name ="disappr"),
    path('approve/',views.approve,name = "approve"),
    path('reject/',views.reject,name= "reject"),
    path('show/<int:id>/',views.show,name = "show"), 
    path('choose/<int:id>/',views.choose,name = "choose"),
    path('user_registration',views.user_registration,name ="user_registration"),
    path('loginPage',views.loginPage,name = "loginPage"),
    path('logoutPage',views.logoutPage,name = "logoutPage"),
    path('welcomePage',views.welcomePage,name = "welcomePage"),
    path('simple_upload',views.simple_upload,name = 'simple_upload'),
]
