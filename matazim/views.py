from django.shortcuts import render, reverse, redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import Program, Facilitator, Facility
from main.models import Profile


def matazim_main(request):
    return render(request, 'matazim/main_matazim.html')


class ProgramListView(ListView):
    model=Program


class ProgramDetailView(DetailView):
    model=Program


class ProgramCreateView(LoginRequiredMixin, CreateView):
    model=Program
    fields = ['name', 'description', 'link', 'image']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.owner = self.request.user
        obj.save()
        return super().form_valid(form)


class ProgramUpdateView(LoginRequiredMixin, UpdateView):
    model=Program
    fields = ['name', 'description', 'link', 'image']

    def dispatch(self, request, *args, **kwargs):
        """" Making sure that only owners can update """
        obj = self.get_object()
        print(f'obj: {obj}')
        if obj.owner != self.request.user:
            print('Hi')
            return redirect('matazim:program_list')
        return super(ProgramUpdateView, self).dispatch(request, *args, **kwargs)


class ProgramDeleteView(DeleteView):
    model=Program
    success_url = reverse_lazy('matazim:program_list')


def program_add_member(request, program_id, profile_id):
    try:
        program = Program.objects.get(pk=program_id)
        profile = Profile.objects.get(pk=profile_id)
    except:
        return redirect('matazim:program_list')

    program.members.add(profile)
    return redirect('matazim:program_detail', pk=program_id)

def program_remove_member(request, program_id, profile_id):
    print(f'got here with {program_id} and {profile_id}')
    try:
        program = Program.objects.get(pk=program_id)
        profile = Profile.objects.get(pk=profile_id)
    except:
        return redirect('matazim:program_list')

    program.members.remove(profile)
    return redirect('matazim:program_detail', pk=program_id)
