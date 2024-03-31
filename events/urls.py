
from django.contrib.auth.views import LoginView
from django.urls import path
from .views import EventListView, Create_event, UserLoginView, UserLogoutView,  \
    EventFeedbackView, Home, UpdateEvent, EventDeleteView, EventCategoryView, EventAttendeeView



urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('', Home.as_view(), name='home'),
    path('event_list/', EventListView.as_view(), name='event_list'),
    path('event_feedback/', EventFeedbackView.as_view(), name='event_feedback'),
    path('event_category/', EventCategoryView.as_view(), name='event_category'),
    path('event_attendee/', EventAttendeeView.as_view(), name='event_attendee'),
    path('create_event/', Create_event.as_view(), name='create_event'),
    path('update_event/<int:pk>', UpdateEvent.as_view(), name='update_event'),
    path('delete_event/<int:pk>/', EventDeleteView.as_view(), name='delete_event'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]

