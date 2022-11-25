from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    host = request.META["HTTP_HOST"]
    user_agent = request.META["HTTP_USER_AGENT"]
    user_ip = request.META['REMOTE_ADDR']

    return HttpResponse(f"""
        <p>Host: {host}</p>
        <p>User-agent: {user_agent}</p>
        <p>User-ip: {user_ip}</p>        
    """)


def error(request):
    return HttpResponse('<h1>К сожалению, произошла ошибка</h1>', status=400, reason="Incorect data")


def user(request, name="Underfined", name_folder="Underfined", num_post=0):
    return HttpResponse(f"""
        <p>Name: {name} </p>
        <p>Name-Folder: {name_folder} </p>
        <p>Post-Number: {num_post} </p>
    """)