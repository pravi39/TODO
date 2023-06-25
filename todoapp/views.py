from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import Task
from . forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
# Create your views here.


class Tasklistview(ListView):
    model=Task
    template_name='home.html'
    context_object_name ='key'

class TaskDetailview(DetailView):
    model=Task
    template_name='detail.html'
    context_object_name='task'

class TaskUpdateView(UpdateView):
    model:Task
    template_name='update.html'
    context_object_name='task'

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk:self.objects.id'})

class TaskDeleteview(DeleteView):
    model=Task
    template_name='delete.html'
    success_url = reverse_lazy('cbvhome')




def add(request):
    task = Task.objects.all()
    if request.method=='POST':
        a=request.POST.get('task','')
        b=request.POST.get('priority','')
        c=request.POST.get('date','')
        x=Task(name=a,priority=b,date=c)
        x.save()

    return render(request,'home.html',{'key':task})

# def details(request):
#     task=Task.objects.all()
#     return render(request,'detail.html',{'key':task})

def delete(request,taskid):
    y=Task.objects.get(id=taskid)
    if request.method=='POST':
        y.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    z=Task.objects.get(id=id)
    w=TodoForm(request.POST or None, instance=z)
    if w.is_valid():
        w.save()
        return redirect('/')
    return render(request,'edit.html',{'key1':z,'key2':w})