
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.context_processors import request
from django.views import View
from django.views.generic import ListView, CreateView, RedirectView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .models import Event, Feedback, Category, Organizer, Attendee
from .forms import EventForm, CustomUserCreationForm, CustomAuthenticationForm

class Home(TemplateView):
    template_name = 'events/home.html'


class UserLoginView(LoginView):
    template_name = 'events/login.html'
    form_class = CustomAuthenticationForm

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect('event_list')
        else:
            messages.error(self.request, 'Invalid username or password.')
            return super().form_invalid(form)
class EventListView(LoginRequiredMixin, ListView):
    model = Event
    queryset = Event.objects.all()
    template_name = 'events/event_list.html'
    context_object_name = 'events'

class EventFeedbackView(LoginRequiredMixin, ListView):
    model = Feedback
    template_name = 'events/feedback.html'
    context_object_name = 'feedback_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        event_id = self.kwargs.get('event_id')
        if event_id:
            queryset = queryset.filter(event_id=event_id)
        return queryset

class EventCategoryView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'events/category.html'
    context_object_name = 'category_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        event_id = self.kwargs.get('event_id')
        if event_id:
            queryset = queryset.filter(event_id=event_id)
        return queryset




class EventAttendeeView(LoginRequiredMixin, ListView):
    model = Attendee
    template_name = 'events/attendee.html'
    context_object_name = 'attendee_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        event_id = self.kwargs.get('event_id')
        if event_id:
            queryset = queryset.filter(event_id=event_id)
        return queryset


class Create_event(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'
    context_object_name = 'createEvents'


    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('event_list')

class UpdateEvent(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'
    context_object_name = 'event'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('event_list')


class EventDeleteView(DeleteView):
    model = Event
    success_url = reverse_lazy('event_list')
    template_name = 'events/event_confirm_delete.html'
    context_object_name = 'event'


    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('event_list')

class UserLogoutView(LoginRequiredMixin, RedirectView):
    url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


class EventOrganizerView:
    pass

