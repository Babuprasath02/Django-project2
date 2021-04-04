from django.shortcuts import render
from firstone.models import first

# Create your views here.
def veh1(request):
    if request.method=="POST":
        if request.POST.get("productname") and request.POST.get("weight"):
            frst=first()
            frst.productname=request.POST.get("productname")
            frst.weight=request.POST.get("weight")
            frst.save()
    return render(request,"vehicleA.html")


def getdb(request):
    qs=first.objects.all()
    return render(request,"details.html",{"alldata":qs})
    
