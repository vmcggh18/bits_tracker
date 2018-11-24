from django.test import TestCase
from django.shortcuts import get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.models import User


# Create your tests here.

class TestViews(TestCase):
        # test login page loads
    def test_get_login_page(self):
        page = self.client.get("/accounts/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")
        # test home page loads on logout
    def test_logout(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
        #test that a user can log in
    def setUp(self):
        self.user = User.objects.create_user(
            username='admin1', email='admin1@example.com', password='secret')
    def test_user_can_login(self):
        response = self.client.post("/accounts/login/", {"username": "admin1", "password": "secret"})  
    def test_get_registration_page(self):
        page = self.client.get("/accounts/register/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration.html")
def test_get_profile_page(self):
        page = self.client.get("/accounts/profile/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "profile.html")
   

     
   
