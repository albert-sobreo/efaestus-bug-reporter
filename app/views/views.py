from django.core.exceptions import NON_FIELD_ERRORS
from django.http.response import JsonResponse
from django.shortcuts import redirect, render, HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login as auth_login, logout
from ..models import *

# Create your views here.
class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')

        return render(request, 'login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/')

        else:
            return HttpResponse(user)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')

class Home(View):
    def get(self, request):
        try:
            no = int(Bug.objects.latest('pk').bugCode.split('#')[1])
            no += 1
            newCode = "BUG#" + str(no).zfill(4)
        except: 
            newCode = "BUG#0000"

        context = {
            'bugCode': newCode,
            "bugs": Bug.objects.all().order_by('-pk')
        }
        return render(request, 'home.html', context)

class RecordBug(View):
    def post(self, request):
        bug = Bug()

        x = request.POST

        try:
            no = int(Bug.objects.latest('pk').bugCode.split('#')[1])
            no += 1
            newCode = "BUG#" + str(no).zfill(4)
        except: 
            newCode = "BUG#0000"
        
        
        if Bug.objects.latest('pk').bugCode == x['bugCode']:
            bug.bugCode = newCode
        else: 
            bug.bugCode = x["bugCode"]
        
        bug.mainFeature = x['mainFeature']
        bug.subFeature = x['subFeature']
        bug.bugTitle = x['bugTitle']
        bug.description = x['description']
        bug.priority = x['priority']
        bug.steps = x['steps']
        bug.expected = x['expected']
        bug.projectFolder = x['projectFolder']
        bug.discoveredBy = request.user
        bug.dateFound = x['dateFound']

        bug.save()

        return redirect('/')