# -*- coding: utf-8 -*-
from locale import *
import sys,os

project_dir = '../skill/skill/'

sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django
django.setup()

from django.conf import settings
from users.models import User


User.objects.create(username="Serg",
                    phone="79042373637",
                    password="ulihos46",
                    email="ochkarik1983@mail.ru",
                    is_superuser=True)
