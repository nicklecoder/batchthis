# Generated by Django 3.0.3 on 2020-02-29 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('batchthis', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='batchnote',
            old_name='note',
            new_name='notetype',
        ),
        migrations.AddField(
            model_name='batchnote',
            name='batch',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='batchthis.Batch'),
            preserve_default=False,
        ),
    ]
