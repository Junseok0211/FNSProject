# Generated by Django 2.1.8 on 2019-10-21 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0016_auto_20191021_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(choices=[('recruitingReply', 'recruitingReply'), ('teamComment', 'teamComment'), ('teamAccepted', 'teamAccepted'), ('leagueComment', 'leagueComment'), ('personalApply', 'personalApply'), ('recruitingApply', 'recruitingApply'), ('personalReply', 'personalReply'), ('joinTeam', 'joinTeam'), ('personalComment', 'personalComment'), ('suggestTeamMatching', 'suggestTeamMatching'), ('teamMatchingApply', 'teamMatchingApply'), ('recruitingAccepted', 'recruitingAccepted'), ('leaguePersonalApply', 'leaguePersonalApply'), ('leagueTeamApply', 'leagueTeamApply'), ('teamReply', 'teamReply'), ('leagueReply', 'leagueReply'), ('recruitingComment', 'recruitingComment')], max_length=20),
        ),
    ]