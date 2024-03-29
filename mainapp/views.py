from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from authapp.models import User
from mainapp.forms import CatsForm, CreationCatsForm
from mainapp.models import Cats

cats_list = Cats.objects.all()


class MainListView(ListView):
    template_name = 'mainapp/index.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context


class CatsListView(ListView):
    template_name = 'mainapp/cats.html'
    model = Cats
    form_class = CatsForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Кошечки'
        context['cats_list'] = cats_list
        return context

    def get_queryset(self):
        return Cats.objects.filter(user=self.request.user)


class CatsCreateView(CreateView):
    template_name = 'mainapp/create_cats.html'
    model = Cats
    form_class = CreationCatsForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создать кошечку'
        context['cats_list'] = cats_list
        return context


class CatsUpdateView(UpdateView):
    template_name = 'mainapp/update_cats.html'
    model = Cats
    form_class = CreationCatsForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактировать кошечку'
        context['cats_list'] = cats_list
        return context


class CatDeleteView(DeleteView):
    template_name = 'mainapp/delete_cats.html'
    model = Cats
    success_url = reverse_lazy('mainapp:cats')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удалить кошечку'
        context['cats_list'] = cats_list
        return context


class AboutUsListView(ListView):
    template_name = 'mainapp/about_us.html'
    title = 'О нас'
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'О нас'
        return context
