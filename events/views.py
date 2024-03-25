from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.context_processors import request
from django.views.generic import View, ListView, CreateView, RedirectView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Event, RSVP
from .forms import EventForm, CustomUserCreationForm, CustomAuthenticationForm

class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'

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




class EventRSVPView(LoginRequiredMixin, CreateView):
    model = RSVP
    fields = '__all__'
    success_url = reverse_lazy('event_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.event = Event.objects.get(pk=self.kwargs['event_id'])
        return super().form_valid(form)



class UserRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('event_list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
#
def authenticate(username, password):
    pass


class LoginView(View):
    template_name = 'events/login_register.html'
    form_class = CustomAuthenticationForm  # Use your custom authentication form

    def get(self, request):
        form = self.form_class()  # Instantiate the form
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)  # Bind POST data to the form
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('event_list')
        # If authentication fails or form is invalid, render the login page again with error message
        return render(request, self.template_name, {'form': form, 'error_message': 'Invalid username or password'})
class UserLogoutView(LoginRequiredMixin, RedirectView):
    url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)