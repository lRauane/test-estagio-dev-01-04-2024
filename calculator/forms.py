from django import forms
from .models import Consumer, DiscountRule


class ConsumerForm(forms.ModelForm):
    class Meta:
        model = Consumer
        fields = ['name', 'document', 'zip_code', 'city', 'state', 'consumption', 'distributor_tax', 'discount_rule']

    def __init__(self, *args, **kwargs):
        super(ConsumerForm, self).__init__(*args, **kwargs)
        super().__init__()
        self.fields['discount_rule'].queryset = DiscountRule.objects.all()  #


class DiscountRulesForm(forms.ModelForm):
    class Meta:
        model = DiscountRule
        fields = ['consumer_type', 'consumption_range', 'cover_value', 'discount_value']
