from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from Inventory import views
# Create your views here.


def index(request):
    with open('Login/password', 'r') as f:
        password = str(f.readlines())
    if request.method == 'POST':
        #is save_password?
        if request.POST.get('save_password', None) is not None:
            request.session['save_password'] = True
        else:
            request.session['save_password'] = False

        password_input = request.POST.get('input_password', None)

        request.session['password'] = password_input
        if password_input is not None:
            if "['"+password_input+"']" == password:
                return HttpResponseRedirect('/Inventory/')

    if request.session['save_password']:
        return render(request, "Login/index.html", {'password': request.session['password'],
            'save_password': request.session['save_password']})
    else:
        return render(request, "Login/index.html", {'save_password': request.session['save_password']})
