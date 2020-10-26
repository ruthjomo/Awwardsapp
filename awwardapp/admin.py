from __future__ import unicode_literals
from django.contrib import admin
from .models import Project,Votes,Profile

# Register your models here.
admin.site.register(Project)
admin.site.register(Votes)
admin.site.register(Profile)
