from django.urls import path
from . import  views
urlpatterns = [
    path('client_profile/',views.client_profile,name='client_profile'),
    path('client_edit_profile/',views.client_edit_profile,name='client_edit_profile'),
    path('register_client/',views.register_client,name='register_client'),
    path('reservation_propertys/<str:pk>',views.reservation_propertys,name='reservation_propertys'),
    path('delete_reservation_propertys/<str:pk>',views.delete_reservation_propertys,name='delete_reservation_propertys'),
]
