from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import LabPost, FilePost
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


class recentfileposts(ListView):
    model = FilePost
    template_name = 'notes/getrecentfilposts.html'
    context_object_name = 'posts'
    ordering = ["-date_posted"]


class labpostlistview(ListView):
    model = LabPost
    template_name = 'notes/labpost_all.html'
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


class filefullpost(DetailView):
    model = FilePost


class FilePostCreateView(CreateView):  # LoginRequiredMixin,
    model = FilePost
    fields = [

        "title",
        "description",
        "semester",
        "stream",
        "subject",
        "file0",
        "file1",
        "file2",
        "file3",
        "file4",
        "file5",
        "file6",


    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class materiallistview(ListView):
    model = FilePost
    template_name = 'notes/filepost_all.html'
    context_object_name = 'filepost'
    ordering = ["-date_posted"]
    paginate_by = 6
