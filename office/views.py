from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView
from .models import operation,leave,snacks,booking
from django.contrib import messages
from django.shortcuts import redirect

class HomePageView(TemplateView):
    template_name = 'office/home.html'

class add_requestView(CreateView):
    template_name = 'office/operational.html'
    model = operation
    fields = ['firstname','lastname','department','operations']

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.manager = self.request.user
        instance.save()
        messages.success(self.request, 'Your Booking Has been done.')
        return redirect('home')

class leave_requestView(CreateView):
    template_name = 'office/leave.html'
    model = leave
    fields = ['firstname','lastname','department','leavetype','supervisoremail','teamleademail','numberofdays']

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.manager = self.request.user
        instance.save()
        messages.success(self.request, 'Your Leave Request Has been Submitted. Confirm after mail from department.')
        return redirect('home')


# snacks,booking
class SnacksView(CreateView):
    template_name = 'office/snacks.html'
    model =  snacks
    fields = ['firstname','lastname','department','drinks','sugar']

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.manager = self.request.user
        instance.save()
        messages.success(self.request, 'Request has been made for your snacks')
        return redirect('home')

class BookingView(CreateView):
    template_name = 'office/booking.html'
    model = booking
    fields = ['firstname', 'lastname', 'department', 'mettingroom']

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.manager = self.request.user
        instance.save()
        messages.success(self.request, 'Your Meeting room Booking Has been done.')
        return redirect('home')

