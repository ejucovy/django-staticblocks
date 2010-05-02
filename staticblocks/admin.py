from django.contrib import admin

from staticblocks.models import StaticBlock

class Admin(admin.ModelAdmin):
    list_display = ('name', 'content')

admin.site.register(StaticBlock, Admin)
