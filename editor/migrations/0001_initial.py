# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sketch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('lastCompiled', models.DateTimeField(auto_now=True)),
                ('sourceURL', models.TextField(default=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='sketch',
            name='creator',
            field=models.ForeignKey(to='editor.User'),
            preserve_default=True,
        ),
    ]
