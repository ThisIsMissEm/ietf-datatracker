# Copyright The IETF Trust 2018-2020, All Rights Reserved
# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-02 10:20


from django.db import migrations

def forward(apps, schema_editor):
    ReviewTeamSettings = apps.get_model('review','ReviewTeamSettings')
    ReviewTeamSettings.objects.get(group__acronym='secdir').notify_ad_when.set(['serious-issues', 'issues', 'not-ready'])

def reverse(apps, schema_editor):
    ReviewTeamSettings = apps.get_model('review','ReviewTeamSettings')
    ReviewTeamSettings.objects.get(group__acronym='secdir').notify_ad_when.set([])

class Migration(migrations.Migration):

    dependencies = [
        ('review', '0004_reviewteamsettings_secr_mail_alias'),
    ]

    operations = [
        migrations.RunPython(forward, reverse)
    ]
