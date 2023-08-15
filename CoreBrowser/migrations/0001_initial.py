# Generated by Django 4.2.4 on 2023-08-14 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Well',
            fields=[
                ('file_num', models.TextField(primary_key=True, serialize=False)),
                ('api', models.BigIntegerField(blank=True, null=True)),
                ('box_count', models.IntegerField(blank=True, null=True)),
                ('operator', models.TextField(blank=True, null=True)),
                ('lease', models.TextField(blank=True, null=True)),
                ('well_num', models.TextField(blank=True, null=True)),
                ('sec', models.IntegerField(blank=True, null=True)),
                ('twn', models.IntegerField(blank=True, null=True)),
                ('twn_d', models.TextField(blank=True, null=True)),
                ('rng', models.IntegerField(blank=True, null=True)),
                ('rng_d', models.TextField(blank=True, null=True)),
                ('qq', models.TextField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('county', models.TextField(blank=True, null=True)),
                ('state', models.TextField(blank=True, null=True)),
                ('field', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'wells',
                'ordering': ['file_num'],
            },
        ),
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('box_num', models.IntegerField(blank=True, null=True)),
                ('formation', models.TextField(blank=True, null=True)),
                ('top', models.TextField(blank=True, null=True)),
                ('bottom', models.TextField(blank=True, null=True)),
                ('diameter', models.TextField(blank=True, null=True)),
                ('box_type', models.TextField(blank=True, null=True)),
                ('sample_type', models.TextField(blank=True, null=True)),
                ('condition', models.TextField(blank=True, null=True)),
                ('restrictions', models.TextField(blank=True, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('file_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CoreBrowser.well')),
            ],
            options={
                'db_table': 'boxes',
            },
        ),
    ]