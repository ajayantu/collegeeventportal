from django.shortcuts import redirect, render
from .models import Fest
# Create your views here.

def welcome(request):
    return render(request,'welcome/index.html')
    
def fests(request):
    desc = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque sapien finibus sapien nec ornare. Sed venenatis pulvinar enim at porttitor. Proin lectus justo, condimentum id ipsum ac, elementum laoreet elit. Nam odio dui, euismod ut lacinia ac, luctus vel dolor. Nulla facilisi. Nunc feugiat congue nisl, sed ultricies nibh varius non. Integer dapibus ultrices interdum.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque sapien finibus sapien nec ornare. Sed venenatis."

    context = {'fests':Fest.objects.all(),'festdesc':desc}
    return render(request,'homepage/fests.html',context);

def addfest(request):
    if request.method=='POST':
        fest_name = request.POST.get('fest_name')
        fest_img = request.FILES.get('myfile')
        venue = request.POST.get('venue')
        if(fest_name and fest_img and venue):
            Fest.objects.create(fest_name=fest_name,fest_venue=venue,fest_img=fest_img)
        return redirect('/fests')
    return render(request,'AddFest/addfests.html');
    
def login(request):
    return render(request,'Login/login.html');