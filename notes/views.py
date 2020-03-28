from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import LabPost, FilePost
import os
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

# Create your views here.


class Posts(ListView):
    model = LabPost
    template_name = 'notes/index.html'
    # template_name = 'notes/index.html'
    context_object_name = 'labpost'
    ordering = ["-date_posted"]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['filepost'] = FilePost.objects.all().order_by('-date_posted')
        # context['labpost']=LabPost.objects.all()
        return context





def about(request):
    return render(request, "notes/about.html")




#Post detail views
class fullpost(DetailView):
    model = LabPost


class filefullpost(DetailView):
    model = FilePost




#New Post views

class PostCreateView(LoginRequiredMixin, CreateView):  # LoginRequiredMixin,
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





class FilePostCreateView(LoginRequiredMixin, CreateView):  # LoginRequiredMixin,
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




#List Views
class labpostlistview(ListView):
    model = LabPost
    template_name = 'notes/labpost_all.html'
    context_object_name = 'posts'
    ordering = ["-date_posted"]
    paginate_by = 6


class materiallistview(ListView):
    model = FilePost
    template_name = 'notes/filepost_all.html'
    context_object_name = 'filepost'
    ordering = ["-date_posted"]
    paginate_by = 6


class UserPostListView(ListView):
    model = LabPost
    template_name = "notes/user_posts.html"  # app/model_viewtype.html
    context_object_name = "posts"
    # ordering = ["-date_posted"]

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return LabPost.objects.filter(author=user).order_by('-date_posted')







#Post update Views
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
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

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# LoginRequiredMixin,
class FilePostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
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

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



# Post Delete Views

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = LabPost
    success_url = "/notes"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class FilePostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = FilePost
    success_url = "/notes"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False





# category Filters

class SemesterLabListView(ListView):
    model = LabPost
    template_name = "notes/filter.html"  # app/model_viewtype.html
    context_object_name = "posts"
    # ordering = ["-date_posted"]

    def get_queryset(self):

        return LabPost.objects.filter(semester=self.kwargs.get('semester')).order_by('-date_posted')


class BranchLabListView(ListView):
    model = LabPost
    template_name = "notes/filter.html"  # app/model_viewtype.html
    context_object_name = "posts"
    # ordering = ["-date_posted"]

    def get_queryset(self):

        return LabPost.objects.filter(stream=self.kwargs.get('branch').upper()).order_by('-date_posted')


class SemesterMaterialListView(ListView):
    model = FilePost
    template_name = "notes/filter.html"  # app/model_viewtype.html
    context_object_name = "posts"
    # ordering = ["-date_posted"]

    def get_queryset(self):

        return FilePost.objects.filter(semester=self.kwargs.get('semester')).order_by('-date_posted')


class BranchMaterialListView(ListView):
    model = FilePost
    template_name = "notes/filter.html"  # app/model_viewtype.html
    context_object_name = "posts"
    # ordering = ["-date_posted"]

    def get_queryset(self):

        return FilePost.objects.filter(stream=self.kwargs.get('branch').upper()).order_by('-date_posted')
