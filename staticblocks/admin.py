from django.contrib import admin

from staticblocks.models import StaticBlock

class Admin(admin.ModelAdmin):
    list_display = ('name', 'content')

admin.site.register(StaticBlock, Admin)


# setup flatpages to use tiny_mce
from django import forms
from tinymce.widgets import TinyMCE
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld

class FlatPageForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    
    class Meta:
        model = FlatPage

class FlatPageAdmin(FlatPageAdminOld):
    form = FlatPageForm

# We have to unregister it, and then reregister
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
