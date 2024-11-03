from django.shortcuts import render

# Create your views here.
def studenthomepage(request):
    return render(request,'studentapp/studenthomepage.html')


