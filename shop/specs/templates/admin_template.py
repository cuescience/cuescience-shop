""" GENERATED FILE. ALL CHANGES WILL BE OVERWRITTEN! """
from django.contrib import admin
from .models import {% for admin in admins %}{{admin.model.name}}{%if not loop.last %},{%endif%}{%endfor%}
{% for admin in admins %}
class {{ admin.name }}(admin.ModelAdmin):
    {%if not admin.properties%}pass{%else%}{% for property in admin.properties %}{{property.name}} = {{property.definition}}({%for arg in property.args%}{{arg}}, {%endfor%}{% for name, value in property.kwargs.items() %}{{name}}={{value}}, {%endfor%})
    {% endfor %}{%endif%}

admin.site.register({{admin.model.name}}, {{admin.name}})
{%endfor%}