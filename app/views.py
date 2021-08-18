from django.shortcuts import render

# Create your views here.
def fun_app(request):
    d={'a':100,'b':200,'c':300}
    return render(request,'first.html',context=d)