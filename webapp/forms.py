from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Layout, 
    Fieldset, 
    Submit, 
    Reset,
    Row,
    Field,
    Column,
)


from .models import WorkLoad



class WorkLoadForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method='POST'
        self.helper.layout = Layout(
            'province',
            'hospital_name',
            'opd','ipd', 'er', 'icu','labour',
            Submit('submit', 'Add')
        )
    # province = forms.TypedChoiceField(
    #     required=True,
    #     choices=province_choices)
    hospital_name = forms.CharField(
        required=False, label="โรงพยาบาล (ไม่เปิดเผยชื่อโรงพยาบาลต่อสาธารณะ)"
        )
    class Meta:
        model = WorkLoad
        fields = "__all__"

