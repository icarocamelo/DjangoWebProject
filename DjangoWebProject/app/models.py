"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Person(object):
    def __init__(self):
        self.speech = 'Hey guys!'

    def speak(self):
        self.speech