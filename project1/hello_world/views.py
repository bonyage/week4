from django.shortcuts import render
from hello_world import models
from django.shortcuts import HttpResponse
# Create your views here.

#user_list = [
#]

def index(request):
    #return HttpResponse("Hello World")
    if request.method == "POST":
        title = request.POST.get("title", None)
        releaseDate = request.POST.get("releaseDate", None)
        duration = request.POST.get("duration", None)
        genre = request.POST.get("genre", None)
        synopsis = request.POST.get("synopsis", None)
        #user_dic = {"user":username,"pwd":password,"email":email}
        #user_list.append(user_dic)
        models.MovieInfo.objects.create(mTitle=title,mReleaseDate=releaseDate,mDuration=duration, mGenre=genre, mSynopsis=synopsis)
        #print(username,password,email)
    user_list = models.MovieInfo.objects.all()
    return render(request, "index.html",{"data":user_list})
