from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, viewsets
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
# Create your views here.
def sayHello(request):
    return HttpResponse("hello, world")

def index(request):
    return render(request, 'restaurant/index.html',{})

class MenuView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    authentication_classes=[authentication.TokenAuthentication]

class MenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
