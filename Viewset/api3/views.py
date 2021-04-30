from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer 
from rest_framework import viewsets



class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)


    def retrive(self,request,pk=None):
        id=pk
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)


    def create(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data created'})


    def destroy(self,request,pk=None):
       id=pk
       stu=Student.objects.get(pk=id)
       stu.delete()
       return Response({'data deleted'})


    def update(self,request,pk=None):
        id=request.data.get('id')
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({' complite data chenged'})

    def partial_update(self,request,pk=None): 
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

