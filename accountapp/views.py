from django.shortcuts import render
from django.shortcuts import render
# Create your views here.


def hello_world(request):
    if request.method == 'Post' :
            return render(request, 'accountapp/hello_world.html',
                  context={'text':'GET METHOD!'})
    else:
            return render(request, 'accountapp/hello_world.html',
                  context={'text':'GET METHOD!'})