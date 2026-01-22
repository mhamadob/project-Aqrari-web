from django.urls import path 
from . import views


urlpatterns = [
    path('login',views.login_form,name='login'),  
    path('logout',views.logout_form,name='logout'),  
    path('register',views.register_form,name='register'),  
 
    
    path('edit_profile',views.edit_profile,name='edit_profile'),  
    
    
    path('service_provider_page',views.service_provider_page,name='service_provider_page'),  
    path('service_provider_profile',views.service_provider_profile,name='service_provider_profile'),  
    
]
