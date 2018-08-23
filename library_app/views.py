from datetime import datetime
from django.views.generic import TemplateView, ListView, DetailView
from django.core.mail import send_mail
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import Book, SOP

# Create your views here.
class LibraryTemplateView(TemplateView):
    template_name = 'library_app/library.html'

    def get_context_data(self, **kwargs):
        ctx = super(LibraryTemplateView, self).get_context_data(**kwargs)
        ctx['recent'] = Book.objects.order_by('-uploaddate')[:3]
        return ctx

class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'library_app/book_list.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = Book.objects.all()
        if self.request.GET.get('book'):
            search = self.request.GET.get('book')
            queryset = queryset.filter(Q(title__icontains=search)|
                                        Q(year__contains=search)|
                                        Q(author__icontains=search))
        return queryset


class BookDetailView(DetailView):
    model = Book
    template_name = 'library_app/book_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        ctx = super(BookDetailView, self).get_context_data(**kwargs)
        book = Book.objects.get(id=self.kwargs['pk'])
        ctx['related'] = Book.objects.filter(title__icontains=book.title)

        if self.request.GET.get('submit'):
            book.status = 'Unavailable'
            book.save()
            user = self.request.user
            subject = 'Request for ' + str(book.title)
            message = 'There was a request for ' + str(book.title) + "\n" + \
                        'From ' + user.first_name + " " + user.last_name + "\n" + \
                        'Email: ' + user.email
            send_mail(subject, message, 'libraryRequest@waterresourcestt.com', ['librarian@waterresourcestt.com'], fail_silently=False,)
        return ctx

class SOPTemplateView(TemplateView):
    template_name = 'library_app/sop_list.html'

    def get_context_data(self, **kwargs):
        ctx = super(SOPTemplateView, self).get_context_data(**kwargs)
        ctx['general'] = SOP.objects.filter(category='general').order_by('title')
        ctx['rainfall'] = SOP.objects.filter(category='rainfall').order_by('title')
        ctx['streamflow'] = SOP.objects.filter(category='streamflow').order_by('title')
        ctx['groundwater'] = SOP.objects.filter(category='groundwater').order_by('title')
        ctx['quality'] = SOP.objects.filter(category='quality').order_by('title')
        ctx['gis'] = SOP.objects.filter(category='gis').order_by('title')

        return ctx

class SOPDetailView(DetailView):
    model = SOP
    template_name = 'library_app/sop_detail.html'
    context_object_name = 'sop'
