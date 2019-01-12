from django.views.generic import TemplateView
from django.conf import settings


class HomeView(TemplateView):
    template_name = "common/index.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['app_name'] = settings.APP_NAME
        return ctx
