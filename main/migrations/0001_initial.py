# Generated by Django 5.0.6 on 2024-06-10 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='APFCS11Reading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('sub_device_id', models.CharField(max_length=50)),
                ('phase_1_current', models.FloatField(blank=True, null=True)),
                ('phase_2_current', models.FloatField(blank=True, null=True)),
                ('phase_3_current', models.FloatField(blank=True, null=True)),
                ('average_current', models.FloatField(blank=True, null=True)),
                ('v1_voltage', models.FloatField(blank=True, null=True)),
                ('v2_voltage', models.FloatField(blank=True, null=True)),
                ('v3_voltage', models.FloatField(blank=True, null=True)),
                ('ln_voltage', models.FloatField(blank=True, null=True)),
                ('kwh', models.FloatField(blank=True, null=True)),
                ('kvah', models.FloatField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DG1S12Reading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('sub_device_id', models.CharField(max_length=50)),
                ('phase_1_current', models.FloatField(blank=True, null=True)),
                ('phase_2_current', models.FloatField(blank=True, null=True)),
                ('phase_3_current', models.FloatField(blank=True, null=True)),
                ('average_current', models.FloatField(blank=True, null=True)),
                ('v1_voltage', models.FloatField(blank=True, null=True)),
                ('v2_voltage', models.FloatField(blank=True, null=True)),
                ('v3_voltage', models.FloatField(blank=True, null=True)),
                ('ln_voltage', models.FloatField(blank=True, null=True)),
                ('kwh', models.FloatField(blank=True, null=True)),
                ('kvah', models.FloatField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DG2S3Reading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('sub_device_id', models.CharField(max_length=50)),
                ('phase_1_current', models.FloatField(blank=True, null=True)),
                ('phase_2_current', models.FloatField(blank=True, null=True)),
                ('phase_3_current', models.FloatField(blank=True, null=True)),
                ('average_current', models.FloatField(blank=True, null=True)),
                ('v1_voltage', models.FloatField(blank=True, null=True)),
                ('v2_voltage', models.FloatField(blank=True, null=True)),
                ('v3_voltage', models.FloatField(blank=True, null=True)),
                ('ln_voltage', models.FloatField(blank=True, null=True)),
                ('kwh', models.FloatField(blank=True, null=True)),
                ('kvah', models.FloatField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EBS10Reading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('sub_device_id', models.CharField(max_length=50)),
                ('phase_1_current', models.FloatField(blank=True, null=True)),
                ('phase_2_current', models.FloatField(blank=True, null=True)),
                ('phase_3_current', models.FloatField(blank=True, null=True)),
                ('average_current', models.FloatField(blank=True, null=True)),
                ('v1_voltage', models.FloatField(blank=True, null=True)),
                ('v2_voltage', models.FloatField(blank=True, null=True)),
                ('v3_voltage', models.FloatField(blank=True, null=True)),
                ('ln_voltage', models.FloatField(blank=True, null=True)),
                ('kwh', models.FloatField(blank=True, null=True)),
                ('kvah', models.FloatField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SixthFloorS5Reading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('sub_device_id', models.CharField(max_length=50)),
                ('ln_avg_voltage', models.FloatField(blank=True, null=True)),
                ('rn_voltage', models.FloatField(blank=True, null=True)),
                ('yn_voltage', models.FloatField(blank=True, null=True)),
                ('bn_voltage', models.FloatField(blank=True, null=True)),
                ('avg_current', models.FloatField(blank=True, null=True)),
                ('r_current', models.FloatField(blank=True, null=True)),
                ('y_current', models.FloatField(blank=True, null=True)),
                ('b_current', models.FloatField(blank=True, null=True)),
                ('hz', models.FloatField(blank=True, null=True)),
                ('kwh_eb', models.FloatField(blank=True, null=True)),
                ('kvah_eb', models.FloatField(blank=True, null=True)),
                ('kwh_dg', models.FloatField(blank=True, null=True)),
                ('kvah_dg', models.FloatField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Skyd1Reading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('sub_device_id', models.CharField(max_length=50)),
                ('ln_avg_voltage', models.FloatField(blank=True, null=True)),
                ('rn_voltage', models.FloatField(blank=True, null=True)),
                ('yn_voltage', models.FloatField(blank=True, null=True)),
                ('bn_voltage', models.FloatField(blank=True, null=True)),
                ('avg_current', models.FloatField(blank=True, null=True)),
                ('r_current', models.FloatField(blank=True, null=True)),
                ('y_current', models.FloatField(blank=True, null=True)),
                ('b_current', models.FloatField(blank=True, null=True)),
                ('hz', models.FloatField(blank=True, null=True)),
                ('kwh_eb', models.FloatField(blank=True, null=True)),
                ('kvah_eb', models.FloatField(blank=True, null=True)),
                ('kwh_dg', models.FloatField(blank=True, null=True)),
                ('kvah_dg', models.FloatField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SolarS13Reading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('sub_device_id', models.CharField(max_length=50)),
                ('phase_1_current', models.FloatField(blank=True, null=True)),
                ('phase_2_current', models.FloatField(blank=True, null=True)),
                ('phase_3_current', models.FloatField(blank=True, null=True)),
                ('average_current', models.FloatField(blank=True, null=True)),
                ('v1_voltage', models.FloatField(blank=True, null=True)),
                ('v2_voltage', models.FloatField(blank=True, null=True)),
                ('v3_voltage', models.FloatField(blank=True, null=True)),
                ('ln_voltage', models.FloatField(blank=True, null=True)),
                ('kwh', models.FloatField(blank=True, null=True)),
                ('kvah', models.FloatField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SpareS6Reading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('sub_device_id', models.CharField(max_length=50)),
                ('ln_avg_voltage', models.FloatField(blank=True, null=True)),
                ('rn_voltage', models.FloatField(blank=True, null=True)),
                ('yn_voltage', models.FloatField(blank=True, null=True)),
                ('bn_voltage', models.FloatField(blank=True, null=True)),
                ('avg_current', models.FloatField(blank=True, null=True)),
                ('r_current', models.FloatField(blank=True, null=True)),
                ('y_current', models.FloatField(blank=True, null=True)),
                ('b_current', models.FloatField(blank=True, null=True)),
                ('hz', models.FloatField(blank=True, null=True)),
                ('kwh_eb', models.FloatField(blank=True, null=True)),
                ('kvah_eb', models.FloatField(blank=True, null=True)),
                ('kwh_dg', models.FloatField(blank=True, null=True)),
                ('kvah_dg', models.FloatField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SpareS7Reading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('sub_device_id', models.CharField(max_length=50)),
                ('ln_avg_voltage', models.FloatField(blank=True, null=True)),
                ('rn_voltage', models.FloatField(blank=True, null=True)),
                ('yn_voltage', models.FloatField(blank=True, null=True)),
                ('bn_voltage', models.FloatField(blank=True, null=True)),
                ('avg_current', models.FloatField(blank=True, null=True)),
                ('r_current', models.FloatField(blank=True, null=True)),
                ('y_current', models.FloatField(blank=True, null=True)),
                ('b_current', models.FloatField(blank=True, null=True)),
                ('hz', models.FloatField(blank=True, null=True)),
                ('kwh_eb', models.FloatField(blank=True, null=True)),
                ('kvah_eb', models.FloatField(blank=True, null=True)),
                ('kwh_dg', models.FloatField(blank=True, null=True)),
                ('kvah_dg', models.FloatField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SpareStation3Reading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('sub_device_id', models.CharField(max_length=50)),
                ('ln_avg_voltage', models.FloatField(blank=True, null=True)),
                ('rn_voltage', models.FloatField(blank=True, null=True)),
                ('yn_voltage', models.FloatField(blank=True, null=True)),
                ('bn_voltage', models.FloatField(blank=True, null=True)),
                ('avg_current', models.FloatField(blank=True, null=True)),
                ('r_current', models.FloatField(blank=True, null=True)),
                ('y_current', models.FloatField(blank=True, null=True)),
                ('b_current', models.FloatField(blank=True, null=True)),
                ('hz', models.FloatField(blank=True, null=True)),
                ('kwh_eb', models.FloatField(blank=True, null=True)),
                ('kvah_eb', models.FloatField(blank=True, null=True)),
                ('kwh_dg', models.FloatField(blank=True, null=True)),
                ('kvah_dg', models.FloatField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ThirdFifthFloorKotakReading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('sub_device_id', models.CharField(max_length=50)),
                ('ln_avg_voltage', models.FloatField(blank=True, null=True)),
                ('rn_voltage', models.FloatField(blank=True, null=True)),
                ('yn_voltage', models.FloatField(blank=True, null=True)),
                ('bn_voltage', models.FloatField(blank=True, null=True)),
                ('avg_current', models.FloatField(blank=True, null=True)),
                ('r_current', models.FloatField(blank=True, null=True)),
                ('y_current', models.FloatField(blank=True, null=True)),
                ('b_current', models.FloatField(blank=True, null=True)),
                ('hz', models.FloatField(blank=True, null=True)),
                ('kwh_eb', models.FloatField(blank=True, null=True)),
                ('kvah_eb', models.FloatField(blank=True, null=True)),
                ('kwh_dg', models.FloatField(blank=True, null=True)),
                ('kvah_dg', models.FloatField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ThirdFloorZohoS4Reading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('sub_device_id', models.CharField(max_length=50)),
                ('ln_avg_voltage', models.FloatField(blank=True, null=True)),
                ('rn_voltage', models.FloatField(blank=True, null=True)),
                ('yn_voltage', models.FloatField(blank=True, null=True)),
                ('bn_voltage', models.FloatField(blank=True, null=True)),
                ('avg_current', models.FloatField(blank=True, null=True)),
                ('r_current', models.FloatField(blank=True, null=True)),
                ('y_current', models.FloatField(blank=True, null=True)),
                ('b_current', models.FloatField(blank=True, null=True)),
                ('hz', models.FloatField(blank=True, null=True)),
                ('kwh_eb', models.FloatField(blank=True, null=True)),
                ('kvah_eb', models.FloatField(blank=True, null=True)),
                ('kwh_dg', models.FloatField(blank=True, null=True)),
                ('kvah_dg', models.FloatField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Utility1st2ndFS2Reading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('sub_device_id', models.CharField(max_length=50)),
                ('ln_avg_voltage', models.FloatField(blank=True, null=True)),
                ('rn_voltage', models.FloatField(blank=True, null=True)),
                ('yn_voltage', models.FloatField(blank=True, null=True)),
                ('bn_voltage', models.FloatField(blank=True, null=True)),
                ('avg_current', models.FloatField(blank=True, null=True)),
                ('r_current', models.FloatField(blank=True, null=True)),
                ('y_current', models.FloatField(blank=True, null=True)),
                ('b_current', models.FloatField(blank=True, null=True)),
                ('hz', models.FloatField(blank=True, null=True)),
                ('kwh_eb', models.FloatField(blank=True, null=True)),
                ('kvah_eb', models.FloatField(blank=True, null=True)),
                ('kwh_dg', models.FloatField(blank=True, null=True)),
                ('kvah_dg', models.FloatField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
