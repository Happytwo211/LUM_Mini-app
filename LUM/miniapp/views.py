from django.shortcuts import render
from .models import User_benefits_data
from django.views.generic import DetailView


class UserBenefitsView(DetailView):
    model = User_benefits_data
    ordering = 'user'
    template_name = 'user_benefits_data.html'
    context_object_name = 'user_benefits_data'

