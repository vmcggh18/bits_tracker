from django.test import TestCase
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from accounts.forms import UserLoginForm, UserRegistrationForm
# Create your tests here.

class TestViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='admin', email='admin@example.com', password='user01')
        # test login page loads
    def test_get_login_page(self):
        page = self.client.get("/accounts/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")
        #test can login
    def test_login(self):
        # Get login page
        response = self.client.get('/accounts/accounts/login/')
        # Check response code
        self.assertEquals(response.status_code, 200)
        #log the user in
        valid_data = {"username": "admin", 
        "password": "user01"}
        form = UserRegistrationForm(data=valid_data)
        form.is_valid()
        # Check response code
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        
    def test_user_can_login_and_logout(self):
        response = self.client.post('/accounts/accounts/login/', {'username': 'admin', 'password': 'user01'})
        user = auth.get_user(self.client)
        self.assertEqual(user.is_authenticated(), True)   
        self.client.post('/accounts/accounts/logout/')
        self.assertEqual(user.is_authenticated(), True) 
        
    def test_logout(self):
        self.user = User()
        User.objects.create_user(username='admin1', password='user01') 
        self.client.login(username='admin', password='secret')
        response = self.client.get('/accounts/accounts/logout/')
        self.assertEqual(response.status_code, 302)
        
    def test_get_registration_page(self):
        page = self.client.get("/accounts/register/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration.html")
        
    def test_registerationForm_data_is_valid(self):
        valid_data = {"email": "admin@example.com", 
        "password": "user01", 
        "username": "admin"}
        form = UserRegistrationForm(data=valid_data)
        form.is_valid()
        self.assertTrue(form.errors)    

    def test_registration(self):
        url = reverse('registration')
        # test req method GET
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        response = self.client.post(url, {})
        self.assertEqual(response.status_code, 200)
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    # def test_correct_message_on_successful_registeration(self):
    #     valid_data = {"email": "admin@example.com", 
    #     "password": "user01", 
    #     "username": "admin"}
    #     form = UserRegistrationForm(data=valid_data)
    #     form.is_valid()
    #     self.assertEqual(form.errors['username'], [u'A user with that username already exists.'])
        
    def tearDown(self):
        del self.user
  
    def test_profile_page_can_be_returned_if_logged_in(self):
        self.user = User.objects.create_user(username='admin1', password='user011')
        login = self.client.login(username='admin1', password='user011')
        page = self.client.get("/accounts/profile/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "profile.html")
        
    # def test_get_index_page_on_authentication(self):
    #      self.user = User.objects.create_user(username='admin12', password='user012')
    #      login = self.client.login(username='admin12', password='user012')
    #      url = reverse('index')
    #      user = auth.get_user(self.client)
    #      self.assertEqual(user.is_authenticated(), True)  
    #      response = self.client.get(url)
    #      self.assertEqual(response.status_code, 200)
        
    
        
        
 
   
