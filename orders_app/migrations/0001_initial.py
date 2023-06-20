# Generated by Django 4.2.2 on 2023-06-20 10:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Краткое описание')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Подробное описание')),
                ('status', models.CharField(choices=[('new', 'новый'), ('assigned', 'назначен'), ('done', 'выполнен'), ('completed', 'завершен')], default='new', max_length=10, verbose_name='статус')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(default='Другое', on_delete=django.db.models.deletion.SET_DEFAULT, to='orders_app.category', verbose_name='Категория')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client', to=settings.AUTH_USER_MODEL, verbose_name='клиент')),
                ('master', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='master', to=settings.AUTH_USER_MODEL, verbose_name='мастер')),
            ],
        ),
    ]