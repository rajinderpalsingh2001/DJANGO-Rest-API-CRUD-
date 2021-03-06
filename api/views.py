from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import *
import io
# Create your views here.

@csrf_exempt
def student_details(request):
    if(request.method=='GET'):  #to fetch data (READ)
        json_data=request.body  #coming data
        stream=io.BytesIO(json_data)    #created io(input/output) stream
        pythondata=JSONParser().parse(stream)   #converted JSON to Python Data
        id=pythondata.get('id')     #from python converted data get value of variable(key)
        if id is not None:
            stu=Student.objects.get(id=id)      #get particular data
            serializer=StudentSerializer(stu)   #convert to python readable data
            json_data=JSONRenderer().render(serializer.data)    #from pythonreadable data to json data
            return HttpResponse(json_data,content_type='application/json')
        stu = Student.objects.all()     #get all data
        serializer = StudentSerializer(stu,many=True)   #many=True to allow fetch all data
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    if(request.method=='POST'): #to insert data (CREATE)
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=StudentSerializer(data=pythondata) #python data to complex data type
        if serializer.is_valid():   #if data is valid having no errors
            serializer.save()   #then save into table (it will call function create() from serializers.py)
            res={'msg':'Added Successfully'}    #python dictionary
            json_data=JSONRenderer().render(res)    #python dict to json
            return HttpResponse(json_data,content_type='application/json')

        # json_data = JSONRenderer().render(serializer.errors)    #if errors then return
        # return HttpResponse(json_data, content_type='application/json')
        return JsonResponse(serializer.errors,safe=False)

    if(request.method=='PUT'): #to update (UPDATE)
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=Student.objects.get(id=id)
        serializer = StudentSerializer(stu,data=pythondata,partial=True)
        if serializer.is_valid():   #if data is valid having no errors
            serializer.save()   #then save into table (it will call function create() from serializers.py)
            res={'msg':'Updated Successfully'}    #python dictionary
            json_data=JSONRenderer().render(res)    #python dict to json
            return HttpResponse(json_data,content_type='application/json')
        # json_data = JSONRenderer().render(serializer.errors)    #if errors then return
        # return HttpResponse(json_data, content_type='application/json')
        return JsonResponse(serializer.errors,safe=False)

    if(request.method=='DELETE'): #to delete (DELETE)
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res={'msg':'Data Deleted'}
        # json_data=JSONRenderer().render(res)
        # return HttpResponse(json_data,content_type='application/json')
        return JsonResponse(res,safe=False)