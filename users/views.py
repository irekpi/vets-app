from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django_filters.views import FilterView
from users.forms import AddPetForm
from utils.utils import BaseContextMixinView
from users.models import Pet
from utils.filters import PetsFilter


class AddPetView(BaseContextMixinView, CreateView):
    template_name = 'users/add_pet_view.html'
    form_class = AddPetForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner_name = self.request.user
        return super().form_valid(form)


class AllPetsView(FilterView):
    template_name = 'users/all_pets.html'
    paginate_by = 5
    login_url = reverse_lazy('account_login')
    filterset_class = PetsFilter

    def get_queryset(self):
        return PetsFilter(self.request.GET,
                          queryset=Pet.objects.filter(owner_name=self.request.user)).qs
