from django.shortcuts import render
from secondone.models import second

# Create your views here.
def veh2(request):
    if request.method=="POST":
        if request.POST.get("productname") and request.POST.get("weight"):
            sec=second()
            sec.productname=request.POST.get("productname")
            sec.weight=request.POST.get("weight")
            sec.save()
    return render(request,"vehicleB.html")

def getdb(request):
    data=second.objects.all()
    return render(request,"detailsb.html",{"key":data})
