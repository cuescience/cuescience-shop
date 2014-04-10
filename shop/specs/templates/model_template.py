""" GENERATED FILE. ALL CHANGES WILL BE OVERWRITTEN! """
from django.db import models
from django.utils.translation import ugettext as _

{% for model in models %}
class {{ model.name }}Base(models.Model):
    """
    {% for property in model.properties %}:param {{property.name}}{% if property.comment %}: {{property.comment}}{% endif %}
    {% endfor %}"""
    class Meta:
        abstract = True
        verbose_name = _("{{model.verbose_name}}")
        verbose_name_plural = _("{{model.verbose_name_plural}}")
    {% for property in model.properties %}{{property.name}} = {{property.definition}}({%for arg in property.args%}{{arg}}, {%endfor%}{% for name, value in property.kwargs.items() %}{{name}}={{value}}, {%endfor%})
    {% endfor %} 
	
    def __unicode__(self):
        return u"%s"%self.{{model.properties.0.name}}
{% endfor %}