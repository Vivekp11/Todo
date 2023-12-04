from django.shortcuts import render,redirect
from django.urls import reverse_lazy

from . models import Task
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import DetailView
# Create your views here.
def home(request):
    obj = Task.objects.all()
    return render(request,'home.html', {'result': obj})
def add(request):

    if request.method=='POST':
        name = request.POST.get('name', '')
        priority = request.POST.get('priority','')
        date = request.POST.get('date','')
        task = Task(name=name, priority=priority, date=date)
        task.save()
        return redirect('/')
    return render(request, 'add.html')

def delete(request, t_id):
    if request.method == 'POST':
        task = Task.objects.get(id=t_id)
        task.delete()
        return redirect('/')

    return render(request, 'delete.html')

class detail(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'

class update(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('todoapp:home')

