from django.conf.urls import url, include
from rest_framework import serializers
from .models import Opportunity, OpportunityDescriptionCard,OpportunityDescriptionCardFeature

class OpportunityDescriptionCardFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpportunityDescriptionCardFeature
        fields = ['title','description',]
        # above used to include 'icon' but this attribute was removed

class OpportunityDescriptionCardSerializer(serializers.ModelSerializer):
    features = OpportunityDescriptionCardFeatureSerializer(many=True)

    class Meta:
        model = OpportunityDescriptionCard
        fields = ['title','subtitle','description', 'image', 'url', 'features' ]

class OpportunitySerializer(serializers.ModelSerializer):

    description_cards = OpportunityDescriptionCardSerializer(many=True)

    class Meta:
        model = Opportunity
        fields =[ 'slug', 'image', 'company', 'type', 'title', 'duration', 'location', 'url', 'description_cards']
        lookup_field = 'slug'
        
