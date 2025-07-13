from django.shortcuts import render
def home(request):
    return render(request, 'home.html')
def mca101(request):
    return render(request, 'mca101.html')
def mca102(request):
    return render(request, 'mca102.html')
def mca103(request):
    return render(request, 'mca103.html')
# Create your views here.
