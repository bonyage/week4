from django.contrib.auth.models import User
from django.shortcuts import render
from hello_world import models
from django.shortcuts import HttpResponse
# Create your views here.
from django import forms
import re
from django.core.exceptions import ValidationError
#user_list = [
#]
def mobile_validate(value):
    mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError('The mobile number is not valid')

class UserInfo(forms.Form):
    #email = forms.EmailField(error_messages={'required':u'Email field cannot be null'})
    email = forms.EmailField(error_messages={'required': u'Email field cannot be null'})
    #username = forms.CharField()
    username = forms.EmailField(widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "Please enter a valid email address", "value": "", "required": "required", }),
        max_length=10, error_messages={"required": "Username cannot be null", })
    password = forms.CharField()
    mobile = forms.CharField()
    # user = User.objects.create_user('Carnivalios', 'blank.riza@gmail.com', '123asd')
    # user.first_name = 'Rifai'
    # user.last_name = 'Riza Kelvin'
    # user.save()

def user_list(request):
    obj = UserInfo()
    if request.method == "POST":
        user_input_obj = UserInfo(request.POST)
        if user_input_obj.is_valid():
            data = user_input_obj.clean()
            print(data)
            user = User.objects.create_user(user_input_obj.cleaned_data['username'], user_input_obj.cleaned_data['email'], user_input_obj.cleaned_data['password'])

            #user.mobile = user_input_obj.mobile
            user.save()
            #user = User.objects.create_user(obj.username, obj.email, obj.password)


            #user = User.objects.create_user('Carnivalios', 'blank.riza@gmail.com', '123asd')
            #user.first_name = 'Rifai'
            #user.last_name = 'Riza Kelvin'
            #user.save()
        else:
            error_msg = user_input_obj.errors
            return render(request, 'user_list.html', {'obj':user_input_obj, 'errors':error_msg})
    return render(request, 'user_list.html',{'obj':obj})

def index(request):
    #return HttpResponse("Hello World")
    if request.method == "POST":
        error = False
        title = request.POST.get("title", None)
        releaseDate = request.POST.get("releaseDate", None)
        duration = request.POST.get("duration", None)
        genre = request.POST.get("genre", None)
        synopsis = request.POST.get("synopsis", None)
        #user_dic = {"user":username,"pwd":password,"email":email}
        #user_list.append(user_dic)
        models.MovieInfo.objects.create(mTitle=title,mReleaseDate=releaseDate,mDuration=duration, mGenre=genre, mSynopsis=synopsis)
        #models.MovieInfo.objects.update(mTitle=title,mReleaseDate=releaseDate,mDuration=duration, mGenre=genre, mSynopsis=synopsis)
        #print(username,password,email)
    user_list = models.MovieInfo.objects.all()
    return render(request, "index.html",{"data":user_list})
