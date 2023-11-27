from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from hub.models import *


class EventListView(ListView):
    template_name = 'hub/eventlist.html'
    model = Event
    context_object_name = 'eventlist'


class EventDetailView(DetailView):
    template_name = 'hub/eventdetail.html'
    model = Event

class CreateEventView(CreateView):
    template_name = 'hub/createevent.html'
    model = Event
    fields = {'title',
              'category',
              'description',
              'requirements',
              'event_date',
              'event_time',
              'slug',
              'age_range',
              'volunteers_quantity_needed',
              'event_place'}
    success_url = reverse_lazy('eventlist')


class DeleteEventView(DeleteView):
    template_name = 'hub/deleteevent.html'
    model = Event
    success_url = reverse_lazy('eventlist')


class UpdateEventView(UpdateView):
    template_name = 'hub/updateevent.html'
    model = Event
    success_url = reverse_lazy('eventlist')
    slug_field = 'slug'
    fields = {'title',
              'category',
              'description',
              'requirements',
              'event_date',
              'event_time',
              'slug',
              'age_range',
              'volunteers_quantity_needed',
              'event_place'}
    success_url = reverse_lazy('eventlist')


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
