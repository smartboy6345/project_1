from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def proj1(request):
    return HttpResponse('<h1><marquee>hi this project created sucessfully</h1></marquee>')
def jampandu(requst):
    return HttpResponse('<h1><marquee>this is giri from mangalagiri and hee is one who most comedy person</h1></marquee> ')