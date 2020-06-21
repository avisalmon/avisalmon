from django.shortcuts import render, reverse, redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import Lecture

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


class LectureDeleteView(DeleteView):
    model = Lecture
    success_url = reverse_lazy('presenterz:all_lectures')
