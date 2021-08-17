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

    # def create(self, validated_data):
    #     # access the data held in the 'feature' attribute from the data passed in, and remove it from the validated_data object
    #     features_data = validated_data.pop('features')

    #     # create a new description card with the data
    #     description_card = OpportunityDescriptionCard.objects.create(**validated_data)

    #     # for each feature in the array of features
    #     for feature_data in features_data:

    #         # create a feature model and set the related description card to the one just created (removed **feature_data)
    #         OpportunityDescriptionCardFeature.objects.create(description_card=description_card, **feature_data)

    #     return description_card

class OpportunitySerializer(serializers.ModelSerializer):

    description_cards = OpportunityDescriptionCardSerializer(many=True)

    class Meta:
        model = Opportunity
        fields =[ 'slug', 'image', 'company', 'type', 'title', 'duration', 'location', 'url', 'description_cards']
        lookup_field = 'slug'
    
    def create(self, validated_data):
        description_cards_data = validated_data.pop('description_cards')
        opportunity = Opportunity.objects.create(**validated_data)

        for card_data in description_cards_data:

            features_data = card_data.pop('features')

            description_card = OpportunityDescriptionCard.objects.create(opportunity=opportunity, **card_data )

            for feature_data in features_data:
                OpportunityDescriptionCardFeature.objects.create(description_card=description_card,  **feature_data)

        return opportunity
