from __future__ import unicode_literals
from django.db import models


# Create your models here.

class MovieInfo(models.Model):
    mTitle = models.CharField(max_length=32)
    mReleaseDate = models.CharField(max_length=32)
    mDuration = models.CharField(max_length=32)
    mGenre = models.CharField(max_length=32)
    mSynopsis = models.CharField(max_length=200)


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
