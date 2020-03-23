from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import LabPost
import os
from django.views.generic import DetailView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.conf import settings
from django.http import HttpResponseRedirect

# Create your views here.


class index(ListView):
    model = LabPost
    template_name = 'notes/index.html'
    context_object_name = 'posts'
    ordering = ["-date_posted"]
    paginate_by = 6


def about(request):
    return render(request, "notes/about.html")


class fullpost(DetailView):
    model = LabPost


class PostCreateView(CreateView):  # LoginRequiredMixin,
    model = LabPost
    fields = [

        "title",
        "description",
        "semester",
        "stream",
        "subject",
        
        "language",
        "file",
        "postbody",

    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
