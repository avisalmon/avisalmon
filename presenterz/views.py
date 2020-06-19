from django.shortcuts import render
from django.views.generic.list import ListView
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
