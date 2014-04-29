""" @Imports """

from jinja2.environment import Environment
from jinja2.loaders import PackageLoader

from django_lean_modelling import helper
from django_lean_modelling.models import support
from django_lean_modelling.admin.support import AdminSupport

class _NatSpecTemplate():

    def __init__(self):
        self.model_support = support.ModelSupport()
        self.admin_support = AdminSupport()
    
    def generate_models(self):
        """ @MethodBody """
        

if __name__ == '__main__':
    model = _NatSpecTemplate()
    model.generate_models()
    
    env = Environment(loader=PackageLoader('shop.specs', 'templates'), trim_blocks=False)
    template = env.get_template("model_template.py")
    
    content = template.render(models=model.model_support.models)
    
    template_admin = env.get_template("admin_template.py")
    content_admin = template_admin.render(admins=model.admin_support.admins)
    
    print model.admin_support.admins
    
    f = open("../../%s_abstract.py" % helper.convert(model.__class__.__name__), 'w')
    f.write(content)
    f.close()
    f1 = open("../../admin.py", 'w')
    f1.write(content_admin)
    f1.close()