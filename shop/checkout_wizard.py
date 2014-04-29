""" GENERATED FILE. ALL CHANGES WILL BE OVERWRITTEN! """
from django import forms
from django.contrib.formtools.wizard.views import SessionWizardView
from shop.models import Client, Address, Address
from django.utils.translation import ugettext_lazy as _

class Step1Form(forms.ModelForm):
    
    class Meta:
        model = Client
        fields = ('email','first_name','last_name',) 
    
    def __init__(self, *args, **kwargs):
        super(Step1Form, self).__init__(*args, **kwargs)
        self.heading = _("General Information")
        self.grouped_fields = [
            (self['first_name'],self['last_name'],),
            (self['email'],),
        ]



class Step2Form(forms.ModelForm):
    different_billing_address = forms.BooleanField(required=False, label=_("Different billing address?"), )
    
    class Meta:
        model = Address
        fields = ('street','number','postcode','city',) 
    
    def __init__(self, *args, **kwargs):
        super(Step2Form, self).__init__(*args, **kwargs)
        self.heading = "Shipping Address"
        self.grouped_fields = [
            (self['street'],self['number'],),
            (self['postcode'],self['city'],),
            (self['different_billing_address'],),
            
        ]



class Step3Form(forms.ModelForm):
    
    class Meta:
        model = Address
        fields = ('street','number','postcode','city',) 
    
    def __init__(self, *args, **kwargs):
        super(Step3Form, self).__init__(*args, **kwargs)
        self.heading = _("Billing Address")
        self.grouped_fields = [
            (self['street'],self['number'],),
            (self['postcode'],self['city'],),
            
        ]


def condition_step_3(wizard):
    cleaned_data = wizard.get_cleaned_data_for_step("2") or {"different_billing_address": 'none'}
    return cleaned_data["different_billing_address"] == True


class Step4Form(forms.Form):
    payment_options = forms.ChoiceField(required=False, label=_("Please choose one"), choices=[(u'Prepayment', _(u'Prepayment')), (u'PayPal', _(u'PayPal'))])
    
    
    
    def __init__(self, *args, **kwargs):
        super(Step4Form, self).__init__(*args, **kwargs)
        self.heading = _("Payment options")
        self.grouped_fields = [
            (self['payment_options'],),
            
        ]




class CheckoutWizardBase(SessionWizardView):
    form_list = [("1",Step1Form),("2",Step2Form),("3",Step3Form),("4",Step4Form),]
    condition_dict = { "3": condition_step_3, }