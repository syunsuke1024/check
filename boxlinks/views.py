from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView,ListView,DeleteView,UpdateView
from .models import User,Links
from .forms import LinksForm,UserForm
from django.urls import reverse_lazy

class LinksListView(ListView):
    model = Links
    template_name = "boxlinks_list.html"

    def queryset(self):
        return Links.objects.all()

class LinksCreateView(CreateView):
    model = Links
    forms_class = LinksForm
    template_name = "boxlinks_form.html"
    fields = ["priority","link","memo","user"]
    success_url = reverse_lazy('boxlinks:boxlinks_list')

class LinksUpdateView(UpdateView):
    model = Links
    form_class = LinksForm
    template_name = "boxlinks_form.html"

    success_url = reverse_lazy('boxlinks:boxlinks_list')

class LinksDeleteView(DeleteView):
    model = Links
    template_name = "boxlinks_confirm_delete.html"
    success_url = reverse_lazy('boxlinks:boxlinks_list')
