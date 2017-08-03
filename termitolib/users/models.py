from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


User = settings.AUTH_USER_MODEL
