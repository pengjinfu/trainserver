from rest_framework.renderers import JSONRenderer
from collections import OrderedDict


class EmberJSONRenderer(JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        if renderer_context and data:
            response = renderer_context["response"]
            if response.status_code >= 200 and response.status_code < 300:
                if isinstance(data, dict):
                    if not data.pop('NOCHANGE', False):
                        data = {'status': 'ok', 'data': data}
                else:
                    data = {'status': 'ok', 'data': data}
            else:
                data = {'status': 'error', "resonse": data}

        return super(EmberJSONRenderer, self).render(data, accepted_media_type, renderer_context)
