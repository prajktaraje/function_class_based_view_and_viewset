from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer 


class student_api(APIView):
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
 
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data created'})


    def delete(self,request,pk=None,format=None):
       id=pk
       stu=Student.objects.get(pk=id)
       stu.delete()
       return Response({'data deleted'})


    def put(self,request,pk=None,format=None):
        id=request.data.get('id')
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({' complite data chenged'})

    def patch(self,request,pk=None,format=None): 
        id=request.data.get('id')
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'data partial chenged'})        
       






















    

    # if  request.method=='PUT':
    #     id=request.data.get('id')
    #     stu=Student.objects.get(pk=id)
    #     serializer=StudentSerializer(stu,data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({' complite data chenged'})

    # if  request.method=='PATCH':
    #     id=request.data.get('id')
    #     stu=Student.objects.get(pk=id)
    #     serializer=StudentSerializer(stu,data=request.data,partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'data partial chenged'})        


    # if request.method=='DELETE':
    #    id=pk
    #    stu=Student.objects.get(pk=id)
    #    stu.delete()
    #    return Response({'data deleted'})

