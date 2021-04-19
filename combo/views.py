from django.shortcuts import render
from django.http import JsonResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Language, City
import json

# from barcode import EAN13
# from barcode.writer import ImageWriter

import qrcode
from PIL import Image
from pyzbar.pyzbar import decode

from googletrans import Translator, constants

import python_weather
from python_weather import Client
import asyncio


async def main(location):
	client = python_weather.Client()
	weather = await client.find(location)
	await client.close()
	print(weather)
	return weather

def home(request):

    context = {
        'show': 'home.html'
    }
    return render(request, 'combo.html', context=context)


def tran(request):
    lang= Language.objects.all()
    context = {
        'show': 'tran.html',
        'lang': lang
    }
    return render(request, 'combo.html', context=context)

@csrf_exempt
def detect(request):
    if request.method=='POST':
        print(request.body)
        data= json.loads(request.body)
        print(data)
        lang= Translator().detect(data['sentence']).lang
        print(lang)
        return JsonResponse({'lang':lang})


@csrf_exempt
def translate(request):
    if request.method=='POST':
        print(request.body)
        data= json.loads(request.body)
        print(data)
        lang= Translator().translate(**data)
        print(lang)
        data={
            'text': lang.text,
            'pronunciation': lang.pronunciation,
        }
        return JsonResponse(data)


def code(request):
    context = {
        'show': 'code.html'
    }

    return render(request, 'combo.html', context=context)


@csrf_exempt
def fromqr(request):
    if request.method=='POST':
        print(request.FILES)
        data= request.FILES['myFile']
        print(data)
        img = Image.open(data)
        result= decode(img)[0].data.decode("utf-8")
        
        data={
            'text':result,
        }
        return JsonResponse(data)

import base64
import io

@csrf_exempt
def toqr(request):
    if request.method=='POST':
        print(request.body)
        data= json.loads(request.body)['text']
        print(data)
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )

        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="green")        
        # byteimg=io.BytesIO()
        img.save('qrcode.png')
        # print(open(byteimg))
        # byteimg.seek(0)
        img=open('qrcode.png', 'rb')
        image_data = base64.b64encode(img.read()).decode('utf-8')
        print(image_data)

        data={
            'qrcode':image_data,
        }
        return JsonResponse(data)



def weather(request):
    city=[]
    for i in City.objects.all():
        city.append(i.city)
    context = {
        'show': 'weather.html',
        'city': city
    }

    return render(request, 'combo.html', context=context)

from django.core.serializers import serialize

@csrf_exempt
def getweather(request):

    if request.method== 'POST':
        print(request.body)

        res= json.loads(request.body)
        print(res)

        weather= asyncio.run(main(res['location'].capitalize()))
        
        data={
            'weather': [],
            'info': []
        }
        i=[]
        for forecast in weather.forecast:
            data['weather'].append({'day':str(forecast.date.day), 'sky':forecast.sky_text, 'temp':forecast.temperature})

        info=serialize('json', City.objects.filter(city=res['location'].title()))
        print(json.loads(info))
        data['info']=json.loads(info)[0]['fields']


        print(data)


    return JsonResponse(data)
