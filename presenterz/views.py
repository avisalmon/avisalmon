from django.shortcuts import render, reverse, redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import Lecture, Session
from .forms import SessionCreateForm


def presenterz(request):
    #todos = Todo.objects.filter(user=request.user, datecompleted__isnull=True)
    context = {}
    #context = {'todos':todos}
    return render(request, 'presenterz/presenterz.html', context)


class LectureListView(ListView):
    model = Lecture
    template_name = 'presenterz/all.html'
    context_object_name = 'all_lectures'

    def get_queryset(self):
        return Lecture.objects.order_by('-created')



class LectureDetailView(DetailView):
    model = Lecture

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sessions'] = Session.objects.filter(lecture_id=self.kwargs.get('pk'))
        return context


class LectureCreateView(LoginRequiredMixin, CreateView):
    model = Lecture
    fields = ['title', 'description', 'image', 'url']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('presenterz:all_lectures')


class LectureUpdateView(LoginRequiredMixin, UpdateView):
    model = Lecture
    fields = ['title', 'description', 'image', 'url']

    def dispatch(self, request, *args, **kwargs):
        """" Making sure that only owners can update Lectires """
        obj = self.get_object()
        if obj.user != self.request.user:
            return redirect('presenterz:all_lectures')
        return super(LectureUpdateView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('presenterz:all_lectures')


class LectureDeleteView(LoginRequiredMixin, DeleteView):
    model = Lecture
    success_url = reverse_lazy('presenterz:all_lectures')


class SessionCreateView(LoginRequiredMixin, CreateView):
    model = Session
    form_class = SessionCreateForm
#    fields = ['location', 'time', 'length', 'link']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lecture'] = Lecture.objects.get(pk=self.kwargs.get('lecture_pk'))
        return context

    def form_valid(self, form):
        lecture = Lecture.objects.get(pk=self.kwargs.get('lecture_pk'))
        if lecture.user != self.request.user:
            return redirect('presenterz:lecture_details', pk=lecture.pk)
        form.instance.lecture = lecture
        return super().form_valid(form)
