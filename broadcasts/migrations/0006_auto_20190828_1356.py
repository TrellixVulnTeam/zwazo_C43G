# Generated by Django 2.1.5 on 2019-08-28 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_site', '0001_initial'),
        ('broadcasts', '0005_auto_20190828_1353'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.CharField(max_length=255)),
                ('transcription', models.TextField(blank=True)),
                ('call_sid', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='broadcast_question_response', to='base_site.Contact')),
            ],
        ),
        migrations.RemoveField(
            model_name='messageresponse',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='messageresponse',
            name='message',
        ),
        migrations.RenameModel(
            old_name='Message',
            new_name='Question',
        ),
        migrations.DeleteModel(
            name='MessageResponse',
        ),
        migrations.AddField(
            model_name='questionresponse',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='broadcasts.Question'),
        ),
    ]