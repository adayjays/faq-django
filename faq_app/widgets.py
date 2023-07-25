from django.forms.widgets import Textarea
from django.utils.safestring import mark_safe
from django.conf import settings

class JoditWidget(Textarea):
    class Media:
        css = {
            'all': (settings.STATIC_URL + 'jodit.css', settings.STATIC_URL + 'css/jodit.css'),
            'print': (),
        }
        js = (settings.STATIC_URL + 'jodit.js',settings.STATIC_URL + 'joditinit.js',)

    def render(self, name, value, attrs=None, renderer=None):
        rendered = super().render(name, value, attrs=attrs, renderer=renderer)
        return rendered
