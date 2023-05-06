from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import Team
# Create your views here.

# def demo(request):
#     return HttpResponse("Hello World!")
# def about(request):
#     return render(request,"about.html")
# def contact(request):
#     return render(request, "democontact.html")

# def demo1(request):
#     name="India"
#     return render(request,"home.html",{'obj':name})
# def demo(request):
#     return  render(request,"home.html")
# def calculate(request):
#     x= int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res1=x+y
#     res2 = x - y
#     res3 = x * y
#     res4 = x / y
#     return  render(request,"result.html",{'result1':res1,'result2':res2,'result3':res3,'result4':res4})

def demo(request):
    obj = Place.objects.all()
    obj2 = Team.objects.all()
    return render(request,"index.html",{'result':obj,'result2':obj2})