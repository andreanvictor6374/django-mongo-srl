# Generated by Django 3.0.5 on 2021-01-18 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('decks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.TextField()),
                ('deck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='decks.Deck')),
            ],
        ),
    ]
