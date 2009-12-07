from django import template

from djangohelpers.templatetags import TemplateTagNode
from staticblocks.models import StaticBlock

class GetStaticBlock(TemplateTagNode):

    noun_for = {"for":"name"}

    def __init__(self, varname, name):
        TemplateTagNode.__init__(self, varname, name=name)

    def execute_query(self, name):
        try:
            return StaticBlock.objects.get(name=name)
        except StaticBlock.DoesNotExist:
            return ''


def has_perm(user, codename):
    model, codename = codename.split('.')
    return user.has_perm('%ss.%s_%s' % (model, codename, model))

register = template.Library()
register.tag('get_static_block', GetStaticBlock.process_tag)

register.filter('has_perm', has_perm)
