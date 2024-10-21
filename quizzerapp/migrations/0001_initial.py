# Generated by Django 5.1.1 on 2024-10-07 09:59

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(message='Postal code must be exactly 6 digits.', regex='^\\d{6}$')])),
                ('phone_number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Phone number must be exactly 10 digits.', regex='^\\d{10}$')])),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('choices', models.JSONField(blank=True, null=True)),
                ('correct_answer', models.CharField(blank=True, max_length=10, null=True)),
                ('match_the_following', models.JSONField(blank=True, null=True)),
                ('correct_answer_pairs', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('question_type_code', models.CharField(max_length=10, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('organization_name', models.CharField(max_length=255, unique=True)),
                ('organization_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('domain_name', models.CharField(max_length=255, unique=True)),
                ('admin_email', models.EmailField(max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('disable', models.BooleanField(default=False)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'png', 'jpeg'])])),
                ('address', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='organization', to='quizzerapp.address')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionBank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('questions', models.ManyToManyField(related_name='question_banks', to='quizzerapp.question')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzerapp.questiontype'),
        ),
    ]
