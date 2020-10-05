from django.urls import reverse_lazy
from django.views.generic import CreateView, View, DetailView
from django_filters.views import FilterView

from users.forms import AddPetForm
from users.models import Pet
from utils.filters import PetsFilter
from utils.utils import BaseContextMixinView


class AddPetView(BaseContextMixinView, CreateView):
    template_name = 'users/add_pet_view.html'
    form_class = AddPetForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner_name = self.request.user
        return super().form_valid(form)


class DetailPetView(DetailView):
    template_name = 'users/detail_pet.html'
    model = Pet


class AllPetsView(FilterView):
    template_name = 'users/all_pets.html'
    paginate_by = 5
    login_url = reverse_lazy('account_login')
    filterset_class = PetsFilter

    def get_queryset(self):
        return PetsFilter(self.request.GET,
                          queryset=Pet.objects.filter(owner_name=self.request.user)).qs


class AddDoctorList(FilterView):
    template_name = 'users/add_doctor_list.html'
    paginate_by = 5
    login_url = reverse_lazy('account_login')
    filterset_class = PetsFilter

    def get_queryset(self):
        return PetsFilter(self.request.GET,
                          queryset=Pet.objects.filter(doctor=None)).qs


class AddDoctor(View):
    def dispatch(self, request, pk):
        pet = Pet.objects.get(id=pk)
        pet.doctor = self.request.user
        pet.save()
        view = AddDoctorList.as_view()
        return view(request)


class PatientsListView(FilterView):
    template_name = 'users/patients_list.html'
    paginate_by = 5
    login_url = reverse_lazy('account_login')
    filterset_class = PetsFilter

    def get_queryset(self):
        return PetsFilter(self.request.GET,
                          queryset=Pet.objects.filter(doctor=self.request.user)).qs
