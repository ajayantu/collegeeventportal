# Generated by Django 4.0.5 on 2022-07-18 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventportal', '0003_fest_delete_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='fest',
            name='fest_desc',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='fest',
            name='fest_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='fest',
            name='fest_venue',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=255)),
                ('event_img', models.ImageField(blank=True, null=True, upload_to='images/eventimg')),
                ('event_tags', models.CharField(max_length=255)),
                ('event_desc', models.TextField(default='')),
                ('event_fest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventportal.fest')),
            ],
        ),
    ]