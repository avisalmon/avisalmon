from django.shortcuts import render, reverse, redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import Lecture, Session, Participation
from .forms import SessionCreateForm
import datetime
from django.db import IntegrityError

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
        sessions = Session.objects.filter(lecture_id=self.kwargs.get('pk'), time__gte=datetime.datetime.now()).order_by('time')
        context['sessions'] = sessions
        print(f'User is: {self.request.user}')
        listed_to_session = []
        for session in sessions:
            print(session)
            for participant in session.participants.all():
                print(f'Session: {session} / participant: {participant}')
                if participant == self.request.user:
                    listed_to_session.append(session.pk)
                    print(f'The user is listed to session {listed_to_session}')
        print(f'writing to context {listed_to_session}')
        context['listed_to_session'] = listed_to_session

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
#    form_class = SessionCreateForm
    # don't apply lecture in the form - will be in thr kwargs
    # don;t show the time, it will be manualy handled in HTML
    #  and form_valid since I want to add datetime picker
    fields = ['location', 'length', 'link']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lecture'] = Lecture.objects.get(pk=self.kwargs.get('lecture_pk'))
        return context

    def form_valid(self, form):
        lecture = Lecture.objects.get(pk=self.kwargs.get('lecture_pk'))
        if lecture.user != self.request.user:
            return redirect('presenterz:lecture_details', pk=lecture.pk)
        form.instance.time = self.request.POST.get('time')
        form.instance.lecture = lecture
        return super().form_valid(form)


class SessionDetailView(DetailView):
    model=Session


class SessionUpdateView(LoginRequiredMixin, UpdateView):
    model = Session
    template_name = 'presenterz/session_update.html'
    fields = ['lecture', 'location', 'length', 'link']

    def form_valid(self, form):
        lecture = Lecture.objects.get(pk=self.request.POST.get('lecture'))
        if lecture.user != self.request.user:
            return redirect('presenterz:lecture_details', pk=lecture.pk)
        form.instance.time = self.request.POST.get('time')
        return super().form_valid(form)

class SessionDeleteView(LoginRequiredMixin, DeleteView):
    model=Session
    success_url = reverse_lazy('presenterz:all_lectures')

    def form_valid(self, form):
        lecture = Lecture.objects.get(pk=self.request.POST.get('lecture'))
        if lecture.user != self.request.user:
            return redirect('presenterz:lecture_details', pk=lecture.pk)
        form.instance.time = self.request.POST.get('time')
        return super().form_valid(form)

def partcipationCreate(request, session_pk):
    session = Session.objects.get(pk=session_pk)
    try:
        participation = Participation.objects.create(user=request.user, session=session)
    except IntegrityError:
        print('Validation error')
    return redirect('presenterz:lecture_details', session.lecture.pk)

def paticipationDelete(request, session_pk):
    session = Session.objects.get(pk=session_pk)
    print('Hi')
    user = request.user
    try:
        print('Suucesful delete should happen here')
        participation = Participation.objects.get(user=user, session=session)
        participation.delete()
        print(participation)
        return redirect('presenterz:lecture_details', session.lecture.pk)
    except:
        return redirect('presenterz:lecture_details', session.lecture.pk)
