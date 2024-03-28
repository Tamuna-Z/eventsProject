from django.urls import path
from .views import EventListView, UpdateEvent, EventDeleteView, Create_event, UpdateEvent, EventDeleteView, \
    UserRegisterView, UserLogoutView, LoginView

UserRegisterView, UserLogoutView, LoginView

urlpatterns = [
    path('login/', LoginView.as_view(),name='login_page'),
    path('', EventListView.as_view(), name='event_list'),
    path('create_event/', Create_event.as_view(), name='create_event'),
    path('update_event/<int:pk>', UpdateEvent.as_view(), name='update_event'),
    path('delete_event/<int:pk>/', EventDeleteView.as_view(), name='delete_event'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]