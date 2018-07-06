from django.shortcuts import render
from app_login.forms import UserForm, UserProfileInfoForm
# Create your views here.
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


def login(request):
    return render(request, "login/login.html", {})

def index(request):
    return render(request, 'app_login/index.html', {})

@login_required
def special(request):
    return HttpResponse("You are logged in,Nice")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile = profile.user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
                profile.save()
                registered = True
        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'app_login/registration.html',
                 {  'user_form': user_form,
                    'profile_form': profile_form,
                    'registered': registered
                 })

def user_login(request):
    if request.method == 'POST':
        username = request.POST.GET('username')
        password = request.POST.GET('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_activate:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print('Someone tried to login and failed')
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("Invalid login details supllied")
    else:
        return render(request,'app_login/login.hmtl',{})