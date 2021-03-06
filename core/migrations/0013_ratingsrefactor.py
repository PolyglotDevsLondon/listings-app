# Generated by Django 2.2.1 on 2019-10-07 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20191007_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='atmosphere',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='venue',
            name='coffee',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='venue',
            name='food',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='venue',
            name='sockets',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='venue',
            name='wifi',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=5),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
