from django.forms import ModelForm
from staticblocks.models import StaticBlock

class StaticBlockForm(ModelForm):
    class Meta:
        model = StaticBlock
