from django.shortcuts import render
from . models import *
from django.conf import settings
from django.http.response import JsonResponse
from django.http import JsonResponse
# Create your views here.


def fnforms(request):
    return render(request, 'form.html')


def datatransfer(request):
    try:
        if request.method == 'POST':
            name = request.POST['name']
            print(name)
            position = request.POST['position']
            print(position)
            mobile = request.POST['mobile']
            print(mobile)
            address = request.POST['address']
            print(address)
            status = 1
            forms = Form(name=name, position=position,
                         mobile=mobile, address=address, status=status)
            forms.save()
            return JsonResponse({'msg': 'Data Saved successfully'})
    except Exception as e:
        print(e)
