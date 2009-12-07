=============
Static Blocks
=============

Static blocks provides you with tools that lets content managers easily include
flatpage content as a snippet in your templates.

The template designer will define page blocks in the templates. The content
managers will choose which flatpage to use as the snippet.

You must have 'django.contrib.flatpages' in your INSTALLED_APPS.

To install, add 'staticblocks' to your INSTALLED_APPS and re-run syncdb.

Using it
========

On the template level, define your static blocks with arbitrary string labels
by passing the label into the scope of the included template snippet:

{% with "firstpageblock" as blockname %}
 {% include 'staticblock/widgets/block.html' %}
{% endwith %}

On the site, users will now be able to associate that page block
with a flatpage, which will be pulled in as page content into that block.

Assign the following permisssions to your users and groups as desired:

 flatpages.add_flatpage
 flatpages.change_flatpage
 staticblocks.add_staticblock
 staticblocks.change_staticblock

You can customize the layout of the pulled-in block by editing or forking
the templates staticblock/templates/staticblock/widgets/block.html 
and/or staticblock/templates/staticblock/widgets/title.html

