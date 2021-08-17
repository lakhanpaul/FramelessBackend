from django.db import models
from datetime import datetime
from django.core.validators import FileExtensionValidator
from django.template.defaultfilters import slugify
# Create your models here.


class Opportunity(models.Model):
    slug = models.SlugField(default='abc')
    image = models.TextField(max_length=300, blank=False, default='',null=True)

    company = models.CharField(max_length=200, blank=False, default='', null=True)
    type = models.CharField(max_length=200, blank=False, default='', null=True)
    title = models.CharField(max_length=200, blank=False, default='', null=True)

    duration = models.TextField(max_length=300, blank=False, default='',null=True)
    location = models.TextField(max_length=300, blank=False, default='',null=True)
    description = models.TextField(max_length=300, blank=False, default='',null=True)

    url = models.URLField(max_length=200)

    # this function is used to automatically update the slug
    # and featured field

    def save(self, *args, **kwargs):
        # slugifies the title
        original_slug = slugify(self.title)

        # checks for any other blog posts with same name
        queryset = Opportunity.objects.all().filter(slug__iexact=original_slug).count()

        # as long as there are blogposts with the same slug
        # the following for loop will run and append a number
        # to the end of the slug until it is different
        count = 1
        slug = original_slug
        while(queryset):
            slug = original_slug + '-' + str(count)
            count += 1
            queryset = Opportunity.objects.all().filter(slug__iexact=slug).count()
        
        self.slug = slug

        super(Opportunity, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class OpportunityDescriptionCard(models.Model):
    opportunity = models.ForeignKey(Opportunity, related_name='description_cards', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.CharField(max_length=200)
    url = models.CharField(max_length=200)

    class Meta:
        unique_together = ['opportunity', 'title']
        ordering = ['?']

    def __str__(self):
        return self.title 
    

class OpportunityDescriptionCardFeature(models.Model):
    description_card = models.ForeignKey(OpportunityDescriptionCard, related_name='features', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

# removed the icon attribute, used to be "icon = models.FileField(upload_to="media/icons/%Y/%m/", validators=[FileExtensionValidator(['pdf', 'doc', 'svg'])])"
    class Meta:
        unique_together = ['description_card', 'title']
        ordering = ['?']

    def __str__(self):
        return self.title 
