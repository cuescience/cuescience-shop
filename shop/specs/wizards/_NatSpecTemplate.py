""" @Imports """

from django_lean_modelling import helper
from django_lean_modelling.forms.wizard_suport import WizardSupport

from jinja2.environment import Environment
from jinja2.loaders import PackageLoader


class _NatSpecTemplate():
    
    wizard_support = WizardSupport()
    
    
    def generate_models(self):
        """ @MethodBody """
        

if __name__ == '__main__':
    model = _NatSpecTemplate()
    model.generate_models()

    env = Environment(loader=PackageLoader('cuescience_cart.specs', 'templates'), trim_blocks=False)
    template = env.get_template("wizard_template.py")
    content = template.render(wizard=model.wizard_support.wizard)

    
    f = open("../../%s.py" % helper.convert(model.__class__.__name__), 'w')
    f.write(content)
    f.close()