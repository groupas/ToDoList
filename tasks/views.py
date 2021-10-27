from django.shortcuts import render
from tasks.models import Task


# Create your views here.
def tasks(request):
    all_tasks = Task.objects.order_by('date_posted')
    context = {'tasks': all_tasks}
    return render(request, 'tasks/all.html', context)