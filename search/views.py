from rest_framework import generics, filters, permissions

from .models import Opportunity
from .serializers import OpportunitySerializer

"""
DRF provides a filter called SearchFilter which can filter through the queryset
based on a query paramater called search.

To implement this, the two fields
    search_fields
        AND
    filter_backends
have been added.

To use the searchfilter, a url with the search query parameter has to be used
For example,

    GET api/search/Opportunity/?search=first
                           ^^^^^^^^

"""
class OpportunityAPIView(generics.ListCreateAPIView):
    search_fields=['title','url'] #these are the model fields which can be filtered by
    filter_backends=(filters.SearchFilter,) #this implements the filters, for now we're only using the SearchFilter 
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer
    lookup_field='slug'

class OpportunityDetailView(generics.RetrieveAPIView):
    queryset = Opportunity.objects.all()
    serializer_class=OpportunitySerializer
    permission_classes=(permissions.AllowAny,)
    lookup_field='slug'


