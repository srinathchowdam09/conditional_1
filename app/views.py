from django.shortcuts import render


def srinath(request):


    sri={'a':10,'b':20}
    return render(request,'srinath.html',sri)

# Create your views here.
