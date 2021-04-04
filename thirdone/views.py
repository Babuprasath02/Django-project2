from django.shortcuts import render
from thirdone.models import third

# Create your views here.
def veh3(request):
    if request.method=="POST":
        if request.POST.get("prdct") and request.POST.get("wt"):
            thrd=third()
            thrd.prdct=request.POST.get("prdct")
            thrd.wt=request.POST.get("wt")
            thrd.save()
    return render(request,"vehicleC.html")


def getdb(request):
    value=third.objects.all()
    return render(request,"detailsc.html",{"data":value})
