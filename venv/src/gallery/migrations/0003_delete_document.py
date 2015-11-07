# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20151107_0614'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Document',
        ),
    ]
