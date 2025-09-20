from django.shortcuts import render

def hello(request):
    return render(request,"hello.html",{'name': 'Welcome to Add number program' })
# Create your views here.
def add(request):
    val1 = int(request.POST["num1"])
    val2 = int(request.POST["num2"]) 
    res = val1 + val2
    return render(request,"result.html",{'res': res})

