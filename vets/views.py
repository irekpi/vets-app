from django.views.generic import TemplateView

from utils.utils import BaseContextMixinView


class HomePageView(BaseContextMixinView, TemplateView):
    template_name = 'vets/home.html'
