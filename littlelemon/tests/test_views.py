from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework.test import APIClient
from rest_framework import status

class MenuViewTest(TestCase):
    def setUp(self):
        # Add test instances of Menu model
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Pizza", price=120, inventory=50)
        Menu.objects.create(title="Pasta", price=150, inventory=75)
        
        # Initialize the APIClient
        self.client = APIClient()
    
    def test_getall(self):
        # Retrieve all Menu objects
        response = self.client.get('http://127.0.0.1:8000/restaurant/menu/')  # Update with your actual endpoint
        
        # Get all Menu objects from database
        menus = Menu.objects.all()
        
        # Serialize the data
        serializer = MenuSerializer(menus, many=True)
        
        # Check that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Check that the serialized data equals the response data
        self.assertEqual(response.data, serializer.data)