from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':123,'b':546,'c':654}
    return render(request,'conditions.html',d)

def looping(request):
    d={'name':'Gavya'}
    return render(request,'loops.html',d)