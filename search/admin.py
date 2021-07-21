from django.contrib import admin
from .models import Opportunity, OpportunityDescriptionCard, OpportunityDescriptionCardFeature
# Register your models here.

main_models = [Opportunity, OpportunityDescriptionCard, OpportunityDescriptionCardFeature]

admin.site.register( main_models)