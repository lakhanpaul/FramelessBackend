# Generated by Django 3.1.7 on 2021-07-19 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0006_auto_20210715_2117'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpportunityDescriptionCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('image', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['?'],
            },
        ),
        migrations.RenameModel(
            old_name='Website',
            new_name='Opportunity',
        ),
        migrations.RenameModel(
            old_name='WebsiteDescriptionCardFeature',
            new_name='OpportunityDescriptionCardFeature',
        ),
        migrations.DeleteModel(
            name='WebsiteDescriptionCard',
        ),
        migrations.AddField(
            model_name='opportunitydescriptioncard',
            name='opportunity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='description_cards', to='search.opportunity'),
        ),
        migrations.AlterField(
            model_name='opportunitydescriptioncardfeature',
            name='description_card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='features', to='search.opportunitydescriptioncard'),
        ),
        migrations.AlterUniqueTogether(
            name='opportunitydescriptioncard',
            unique_together={('opportunity', 'title')},
        ),
    ]
