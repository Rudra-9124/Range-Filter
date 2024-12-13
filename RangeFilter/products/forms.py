from django import forms

class RangeFilterForm(forms.Form):
    min_price = forms.FloatField(required=False, label="Min Price")
    max_price = forms.FloatField(required=False, label="Max Price")
    size = forms.ChoiceField(
        required=False,
        choices=[('', 'All Sizes'), ('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')],
        label="Size"
    )
    