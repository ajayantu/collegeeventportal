from django.shortcuts import redirect, render
from .models import Fest
# Create your views here.


def fests(request):
    if request.method=='POST':
        fest_name = request.POST.get('fest_name')
        fest_img = request.FILES.get('myfile')
        venue = request.POST.get('venue')
        if(fest_name and fest_img and venue):
            Fest.objects.create(fest_name=fest_name,fest_venue=venue,fest_img=fest_img)
        return redirect('/')
    context = {'fests':Fest.objects.all()}
    return render(request,'homepage/home.html',context);