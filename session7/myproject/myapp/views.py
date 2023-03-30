from django.shortcuts import render


# Create your views here.
def Home(request):
    #
    return render(request, 'Home.html')

def project(request):
    #
    return render(request, 'project.html')


