from django.shortcuts import render
from . models import *
from django.conf import settings
from django.http.response import JsonResponse
from formapp.models import *


def login(request):
    return render(request, 'adminlogin.html')


def fnlogin(request):
    try:
        if request.method == 'POST':
            username = request.POST['name']
            print(username)
            password = request.POST['password']
            print(password)
            logi_obj = adminlogin.objects.get(
                username=username, password=password)

            request.session['log'] = logi_obj.id

            return JsonResponse({'msg': 'You are logged in'})
    except Exception as e:
        print(e)


def dashboard(request):
    return render(request, 'dashboard.html')


def getdata(request):
    forms = Form.objects.filter(status=1)
    form_obj = [{'id': i.id, 'name': i.name, 'position': i.position,
                 'mobile': i.mobile, 'address': i.address} for i in forms]
    print(form_obj)

    return JsonResponse({'form': form_obj})


def deldata(request):
    delid = request.POST['id']
    print(delid)
    Form.objects.filter(id=delid).update(status=0)
    return JsonResponse({'msg': "data deleted succcessfully"})


def masters(request):
    logid = request.session.get('log')
    print(logid)
    logi = adminlogin.objects.get(id=logid)
    return JsonResponse({'user': logi.username, })


def logout(request):
    del request.session['log']
    return render(request, 'adminlogin.html')
