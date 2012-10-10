staticblocks provides you with tools for content managers to easily
include flatpage content as a snippet in your templates while
retaining structured control over the templates themselves.

The template designers will define page blocks in the templates. 

The content managers will choose which flatpage to use as the snippet
embedded in each page block.

You must have 'django.contrib.flatpages' in your INSTALLED_APPS.

To install, add 'staticblocks' to your INSTALLED_APPS and re-run syncdb.

Using it
========

Code to write
-------------

On the template level, define your static blocks with arbitrary string labels
by passing the label into the scope of the included template snippet::

  {% with "index.html/firstpageblock" as blockname %}
    {% include 'staticblock/widgets/block.html' %}
  {% endwith %}
    
  {% with "index.html/secondpageblock" as blockname %}
    {% include 'staticblock/widgets/block.html' %}
  {% endwith %}

On the site, allowed users will now be able to associate that page block
with a flatpage, which will be pulled in as page content into that block.

Permissions to assign
---------------------

Assign the following permisssions to your users and groups as desired::

  flatpages.add_flatpage
  flatpages.change_flatpage
  staticblocks.add_staticblock
  staticblocks.change_staticblock

Templates to use
----------------

You can customize the layout of the pulled-in block by editing or forking
these templates::

  staticblock/templates/staticblock/widgets/block.html 
  staticblock/templates/staticblock/widgets/title.html

