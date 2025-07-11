# Generated by Django 5.2 on 2025-06-11 01:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_photo_created_at_photo_title'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='context',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='location',
        ),
        migrations.AddField(
            model_name='collection',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collection',
            name='collected_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='collection',
            name='completed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='collection',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='collection',
            name='photo_url',
            field=models.ImageField(blank=True, null=True, upload_to='collections_photos/'),
        ),
        migrations.AddField(
            model_name='collection',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='status',
            field=models.CharField(default='active', max_length=50),
        ),
    ]
