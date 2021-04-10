from django.urls import path
from . import views

urlpatterns = [
    path('', views.enquiry, name='enquiry'),
    path('enquiry', views.enquiry_details, name='get_all_details'),
    path('enquiry/<uuid:pk>', views.feedback, name='feedback'),
    path('customer-review', views.customer_review, name='customer_review_details'),
    path('customer-review/<uuid:pk>', views.customer_review, name='customer-review')
    
]