""" GENERATED FILE. ALL CHANGES WILL BE OVERWRITTEN! """
from django import forms
from django.contrib.formtools.wizard.views import SessionWizardView
from cuescience_shop.models import {% for step in wizard.steps %}{%if step.form.model%}{%if not loop.first %}, {%endif%}{{step.form.model}}{%endif%}{%endfor%}
{% for step in wizard.steps %}
class Step{{ step.number }}Form(forms.{%if step.form.model%}Model{%endif%}Form):
    {% for field in step.form.extra_fields %}{{field.name}} = forms.{{field.field_type}}(required=False, label="{{field.verbose_name}}", {% for k,v in field.kwargs.items() %}{{k}}={{v}}{% endfor %})
    {% endfor %}
    {%if step.form.model%}class Meta:
        model = {{step.form.model}}
        {% if step.form.fields %}fields = ({% for field in step.form.fields %}{{field}},{% endfor %}) {%endif%}{%endif%}
    
    def __init__(self, *args, **kwargs):
        super(Step{{ step.number }}Form, self).__init__(*args, **kwargs)
        {%if step.form.heading%}self.heading = "{{step.form.heading}}"{%endif%}
        {%if step.form.grouped_fields%}self.grouped_fields = [
            {%for group in step.form.grouped_fields%}({%for field in group%}self[{{field}}],{%endfor%}),
            {%endfor%}
        ]{%endif%}

{% if step.condition %}
def condition_step_{{step.number}}(wizard):
    cleaned_data = wizard.get_cleaned_data_for_step("{{step.condition.step}}") or {"{{step.condition.name}}": 'none'}
    return cleaned_data["{{step.condition.name}}"] == {{step.condition.value}}
{%endif%}
{%endfor%}

class {{wizard.name}}WizardBase(SessionWizardView):
    form_list = [{% for step in wizard.steps %}("{{step.number}}",Step{{step.number}}Form),{%endfor%}]
    {%if wizard.conditions%}condition_dict = { {% for step in wizard.steps %}{% if step.condition %}"{{step.number}}": condition_step_{{step.number}},{%endif%}{% endfor %} }{% endif %}