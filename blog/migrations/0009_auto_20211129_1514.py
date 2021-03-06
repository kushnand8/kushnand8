# Generated by Django 3.2.9 on 2021-11-29 09:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0008_rename_uer_addcomment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcomment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='AddComment', to='blog.addpost'),
        ),
        migrations.AlterField(
            model_name='addcomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='AddComment', to=settings.AUTH_USER_MODEL),
        ),
    ]
