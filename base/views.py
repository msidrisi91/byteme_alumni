from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Notice

class NoticeListView(LoginRequiredMixin,ListView):
    model = Notice
    template_name = 'noticeboard.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'notices'
    ordering = ['-date']
    paginate_by = 5

class NoticeDetailView(LoginRequiredMixin,DetailView):
    template_name = 'base/detail_notice.html'
    model = Notice


class NoticeCreateView(LoginRequiredMixin, CreateView):
    template_name = 'base/create_notice.html'
    model = Notice
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class NoticeUpdateView(LoginRequiredMixin, UpdateView):
    model = Notice
    template_name = 'base/update_notice.html'
    fields = ['title', 'content']


class NoticeDeleteView(LoginRequiredMixin, DeleteView):
    model = Notice
    success_url = '/'
    template_name = 'base/delete_notice.html'


# def about(request):
#     return render(request, 'blog/about.html', {'title': 'About'})