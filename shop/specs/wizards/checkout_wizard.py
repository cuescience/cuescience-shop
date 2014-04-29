""" @Imports """

from django_lean_modelling import helper
from django_lean_modelling.forms.wizard_suport import WizardSupport

from jinja2.environment import Environment
from jinja2.loaders import PackageLoader


class CheckoutWizard():
    
    wizard_support = WizardSupport()
    
    
    def generate_models(self):
        """
         The code in this method is generated from: /cuescience-shop/shop/specs/wizards/checkout_wizard.natspec
         Never change this method or any contents of this file, all local changes will we overwritten.
        """
        
        

if __name__ == '__main__':
    model = CheckoutWizard()
    model.generate_models()

    env = Environment(loader=PackageLoader('shop.specs', 'templates'), trim_blocks=False)
    template = env.get_template("wizard_template.py")
    content = template.render(wizard=model.wizard_support.wizard)

    
    f = open("../../%s.py" % helper.convert(model.__class__.__name__), 'w')
    f.write(content)
    f.close()