from django import forms

class InputForm(forms.Form):
    age_v = forms.DecimalField(min_value=0)
    sex_v = forms.DecimalField(min_value=0)

    cp_v = forms.DecimalField(min_value=0)
    thalach_v = forms.DecimalField(min_value=0)
    exang_v = forms.DecimalField(min_value=0)
    oldpeak_v = forms.DecimalField(min_value=0)
    slope_v = forms.DecimalField(min_value=0)

    ca_v = forms.DecimalField(min_value=0)