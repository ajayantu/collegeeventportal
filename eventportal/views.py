from django.shortcuts import redirect, render
from .models import Events,Registered,Fests
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.


def welcome(request):
    return render(request,'welcome/index.html')

@login_required(login_url='/auth/login')
def fests(request):
    desc = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque sapien finibus sapien nec ornare. Sed venenatis pulvinar enim at porttitor. Proin lectus justo, condimentum id ipsum ac, elementum laoreet elit. Nam odio dui, euismod ut lacinia ac, luctus vel dolor. Nulla facilisi. Nunc feugiat congue nisl, sed ultricies nibh varius non. Integer dapibus ultrices interdum.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque sapien finibus sapien nec ornare. Sed venenatis."
    fests = Fests.objects.all()
    context = {'fests':fests,'festdesc':desc}
    return render(request,'homepage/fests.html',context);

@login_required(login_url='/auth/login')
def addfest(request):
    if request.user.profile.isCordinator:
        if request.method=='POST':
            fest_name = request.POST.get('festname')
            fest_img = request.FILES.get('festimg')
            venue = request.POST.get('festvenue')
            desc = request.POST.get('festdesc')
            if(fest_name and fest_img and venue):
                Fests.objects.create(fest_name=fest_name,fest_venue=venue,fest_img=fest_img,fest_desc=desc,fest_author=request.user)
            return redirect('/fests')
    else:
        return redirect('/fests');
    return render(request,'CreateFest/createfest.html');
    

def events(request,id):
    fest = Fests.objects.filter(pk=id).first()
    events = Events.objects.filter(event_fest=fest)
    print(fest.fest_img)
    return render(request,"Events/events.html",context={'events':events,'fest_poster':fest.fest_img})

@login_required(login_url='/auth/login')
def regevent(request,id):
    event = Events.objects.filter(pk=id).first()
    reg = Registered(event=event,user=request.user)
    reg.save()
    return redirect('/fests')

def getregevent(request):
    reg = Registered.objects.all();
    context={
        'reg':reg
    }
    return render(request,'RegEvents/regevents.html',context)
def cordinator(request):
    pass