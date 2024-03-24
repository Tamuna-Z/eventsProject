from django.urls import path
from .views import EventListView, Create_event, EventRSVPView, UserRegisterView, UserLoginView, UserLogoutView, \
    UpdateEvent, EventDeleteView

urlpatterns = [
    path('', EventListView.as_view(), name='event_list'),
    path('create_event/', Create_event.as_view(), name='create_event'),
    path('update_event/<int:pk>', UpdateEvent.as_view(), name='update_event'),
    path('delete_event/<int:pk>/', EventDeleteView.as_view(), name='delete_event'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),

    path('events/<int:event_id>/rsvp/', EventRSVPView.as_view(), name='event_rsvp'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]
