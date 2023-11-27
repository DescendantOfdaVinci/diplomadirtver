from django.contrib import admin
from django.urls import path
from hub.views import *

urlpatterns = [
    path('', EventListView.as_view(), name='eventlist'),
    path('event/<slug:slug>/', EventDetailView.as_view(), name='eventdetail'),
    path('create/', CreateEventView.as_view(), name='createevent'),
    path('event/<int:pk>/delete/', DeleteEventView.as_view(), name='deleteevent'),
    path('update/<slug:slug>/', UpdateEventView.as_view(), name='updateevent')
]

