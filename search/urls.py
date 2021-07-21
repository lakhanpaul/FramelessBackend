from django.db.models import query
from django.urls import path, re_path
from .views import  OpportunityAPIView, OpportunityDetailView



urlpatterns = [
    #any path that hits Opportunity will display the Opportunity api
    path('opportunity/', OpportunityAPIView.as_view(),), 
    path('<slug>', OpportunityDetailView.as_view(),)
]
