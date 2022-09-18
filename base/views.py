
from urllib import request
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , UpdateView , DeleteView  , FormView
from base.models import Task, UploadImage
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.models import User






class CustomLoginView(LoginView):
    template_name="base/login.html"
    fields='__all__'
    redirect_authenticated_user= True

    def get_success_url(self):
        return reverse_lazy('tasks')

class RegisterPage(FormView):
    template_name="base/register.html"
    form_class=UserCreationForm

    success_url=reverse_lazy('tasks')
    def form_valid(self, form):
        user=form.save()
        if user is not None:
            login(self.request,user)
        return super(RegisterPage,self).form_valid(form)
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("tasks")
        return super(RegisterPage,self).get(self, *args, **kwargs)
    

class TaskList(LoginRequiredMixin,ListView):
    model=Task
    context_object_name="tasks" 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(completed=False).count()
        return context

class TaskDetail(DetailView):
    model=Task
    template_name='base/task.html'
    context_object_name="task" 

class CreateTask(LoginRequiredMixin,CreateView):
    model=Task
    fields=['title','description','completed']
    success_url=reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user=self.request.user 
        return super(CreateTask,self).form_valid(form)
    
class TaskUpdate(LoginRequiredMixin,UpdateView):
    model=Task
    fields='__all__'
    fields=['title','description','completed']
    success_url=reverse_lazy('tasks')

class TaskDelete(LoginRequiredMixin,DeleteView):
    model=Task
    context_object_name="task" 
    success_url=reverse_lazy('tasks')





from django.shortcuts import render  
from django.http import HttpResponse  
from .forms import UploadFileForm


from django.shortcuts import render  
from django.http import HttpResponse  
from base.functions import handle_uploaded_file  
from base.forms import UploadFileForm  , UploadForm


def index(request):  
        return render(request,"notes2.html")




# Create your views here.
def FileUploadView(request):

    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if request.user.is_authenticated:

            if form.is_valid():
                new_record = UploadImage.objects.create(
                    poster = User.objects.get(pk=request.user.id),
                    image = form.cleaned_data["image"],
                    keywords = form.cleaned_data["keywords"],
                )
                new_record.save()
                form.save()
                return HttpResponse("File uploaded successfuly")  
            else:
                print("ERROR : Form is invalid")
                print(form.errors)
    else:
        form = UploadForm()
        return render(request, 'notes.html', {'form' : form})
    
  
def success(request):
    return HttpResponse('successfully uploaded')  






def showimages(request):

    context = {
    "img" : UploadImage.objects.filter(poster = request.user), 


    }


    return render(request, 'preview.html', context)

