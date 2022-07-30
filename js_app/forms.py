from django import forms


class IndexForm(forms.Form):
    a_field = forms.FloatField(label='')
    b_field = forms.FloatField(label='')
    c_field = forms.FloatField(label='')
