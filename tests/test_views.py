from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    
    def setUp(self):
        Menu.objects.create(title="Burger", price=10, inventory=50)
        Menu.objects.create(title="Pizza", price=12, inventory=30)

    def test_getall(self):
        from django.urls import reverse
        response = self.client.get(reverse('menu-list'))

        menus = Menu.objects.all()
        serialized_data = MenuSerializer(menus, many=True).data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), serialized_data)