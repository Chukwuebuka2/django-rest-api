# Generated by Django 4.0.3 on 2022-03-21 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0005_alter_testmodel_options_testmodel_extra_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testmodel',
            options={'ordering': ['-created_at'], 'verbose_name_plural': 'Test Model'},
        ),
        migrations.CreateModel(
            name='ModelX',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mileage', models.FloatField()),
                ('test_content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_content', to='test_app.testmodel')),
            ],
            options={
                'verbose_name_plural': 'ModelX',
            },
        ),
    ]
