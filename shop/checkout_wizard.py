""" GENERATED FILE. ALL CHANGES WILL BE OVERWRITTEN! """
from django import forms
from django.contrib.formtools.wizard.views import SessionWizardView
from cuescience_shop.models import Client, Address, Address

class Step1Form(forms.ModelForm):
    
    class Meta:
        model = Client
        fields = ('first_name', 'last_name',) 
    
    def __init__(self, *args, **kwargs):
        super(Step1Form, self).__init__(*args, **kwargs)
        
        self.grouped_fields = [
            (self['first_name'],),
            (self['last_name'],),
            
        ]



class Step2Form(forms.ModelForm):
    different_billing_address = forms.BooleanField(required=False, label="Different billing address?",)
    
    class Meta:
        model = Address
        fields = ('street', 'number', 'postcode', 'city',) 
    
    def __init__(self, *args, **kwargs):
        super(Step2Form, self).__init__(*args, **kwargs)
        self.heading = "Shipping Address"
        self.grouped_fields = [
            (self['street'], self['number'],),
            (self['postcode'], self['city'],),
            (self['different_billing_address'],),
            
        ]



class Step3Form(forms.ModelForm):
    
    class Meta:
        model = Address
        fields = ('street', 'number', 'postcode', 'city',) 
    
    def __init__(self, *args, **kwargs):
        super(Step3Form, self).__init__(*args, **kwargs)
        self.heading = "Billing Address"
        self.grouped_fields = [
            (self['street'], self['number'],),
            (self['postcode'], self['city'],),
            
        ]


def condition_step_3(wizard):
    cleaned_data = wizard.get_cleaned_data_for_step("2") or {"different_billing_address": 'none'}
    return cleaned_data["different_billing_address"] == True


class Step4Form(forms.Form):
    paypent_options = forms.ChoiceField(required=False, label="Please choose one", choices=[(u'Prepayment', u'Prepayment'), (u'PayPal', u'PayPal')])
    
    
    
    def __init__(self, *args, **kwargs):
        super(Step4Form, self).__init__(*args, **kwargs)
        self.heading = "Payment options"
        self.grouped_fields = [
            (self['paypent_options'],),
            
        ]




class CheckoutWizardBase(SessionWizardView):
    form_list = [("1", Step1Form), ("2", Step2Form), ("3", Step3Form), ("4", Step4Form), ]
    condition_dict = { "3": condition_step_3, }
