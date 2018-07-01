from django.shortcuts import render
from app_login.forms import userForm, UserProfileInfoForm
# Create your views here.

def login(request):
    return render(request, "login/login.html", {})

def index(request):
    return render(request, 'app_login/index.html', {})

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
                register = True
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
