from django.db import models

class StaticBlock(models.Model):
    name = models.CharField(max_length=80, unique=True)
    content = models.ForeignKey('flatpages.FlatPage')

    description = models.TextField(blank=True)

