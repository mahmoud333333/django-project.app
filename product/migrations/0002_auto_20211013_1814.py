# Generated by Django 3.2.8 on 2021-10-13 15:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accepted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('REQ_NO', models.CharField(max_length=1000, null=True)),
                ('Descreption', models.CharField(max_length=1000, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Approve', 'Approve'), ('Reject', 'Reject')], max_length=200, null=True)),
                ('note', models.CharField(max_length=1000, null=True)),
                ('my_file', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Chiefs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Finaldesscion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('REQ_NO', models.CharField(max_length=1000, null=True)),
                ('Note', models.CharField(max_length=1000, null=True)),
                ('status', models.CharField(choices=[('Final Approve', 'Final Approve'), ('Final Reject', 'Final Reject')], max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('my_file', models.CharField(max_length=200)),
                ('Chiefs', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.chiefs')),
            ],
        ),
        migrations.CreateModel(
            name='GMANAGER',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descreption', models.CharField(max_length=1000, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Refused', 'Refused')], max_length=200, null=True)),
                ('REQ_NO', models.CharField(max_length=1000, null=True)),
                ('my_file', models.FileField(blank=True, upload_to='')),
                ('Chiefs', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.chiefs')),
                ('GMANAGER', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.gmanager')),
            ],
        ),
        migrations.CreateModel(
            name='Resent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('REQ_NO', models.CharField(max_length=1000, null=True)),
                ('Note', models.CharField(max_length=1000, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('my_file', models.FileField(blank=True, upload_to='')),
                ('Chiefs', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.chiefs')),
                ('GMANAGER', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.gmanager')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='product',
        ),
        migrations.AddField(
            model_name='finaldesscion',
            name='GMANAGER',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.gmanager'),
        ),
        migrations.AddField(
            model_name='chiefs',
            name='tags',
            field=models.ManyToManyField(to='product.Tag'),
        ),
        migrations.AddField(
            model_name='accepted',
            name='Chiefs',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.chiefs'),
        ),
        migrations.AddField(
            model_name='accepted',
            name='GMANAGER',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.gmanager'),
        ),
    ]
