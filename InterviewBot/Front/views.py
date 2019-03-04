from django.shortcuts import render
from Front.forms import UserForm,UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def welcome(request):
    return render(request,'welcome.html')
def complete(request):
    return render(request,'done.html')
def register(request):

    registered=False

    if(request.method=="POST"):
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)

        if(user_form.is_valid() and profile_form.is_valid()):
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user

            if('profile_pic' in request.FILES):
                profile.profile_pic=request.FILES['profile_pic']
            profile.save()

            registered=True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()
    return render(request,'Registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('welcome'))

@login_required
def special(request):
    HttpResponse('you are logged in !! nice')


@login_required
def Interview(request,count=0):
    maxc=3
    questions1=["tell me about yourself?","where are you from?","what are your hobbies?"]
    if(count==maxc):
        return HttpResponseRedirect(reverse('complete'))
    else:
        count+=1
        return render(request,'Interview.html',{'questions1':questions1[count-1],'c':count})

def user_login(request):
    if(request.method=='POST'):
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if(user):
            if(user.is_active):
                login(request,user)
                user_test=user
                return HttpResponseRedirect(reverse('welcome'))
            else:
                return HttpResponse("ACCOUNT IS NOT ACTIVE")
        else:
            print("someone tried to access account unauthenically and failed")
            print("Username {} and password {}".format(username,password))
            return HttpResponse("invalid login details")
    else:
        return render(request,'Login.html',{})
