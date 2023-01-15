from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Categories ,Jobsection 

# Create your views here.
def index(request):
    cat = Categories.objects.all()
    return render(request, 'index.html',{'cat':cat})
def about(request):
    return render(request, 'about.html')
def jobs(request,id=None):
    if id:
        cat = get_object_or_404(Categories,id=id)
        jobsections = Jobsection.objects.filter(Categories= cat)
        print(jobsections)
        return render(request, 'job.html',{'cat':jobsections})
    else:
        cat = Categories.objects.all()
        return render(request, 'job.html',{'cat':cat})

def benefits(request,id):
    sect = Jobsection.objects.get(id=id)
    print(sect)
    context = {
        'sect':sect
    }
    return render(request, 'benefits.html',context)



