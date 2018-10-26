from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from accounts.forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    """Return the index.html file"""
    return render(request,  'index.html')
    
# use decorator to ensure user is only logged out when logged in  
@login_required
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('index'))
    
def login(request):
    """Return a login page"""
    #redirect to the index page if user is authenticated
    if request.user.is_authenticated:
        return redirect(reverse('index'))
     #create an instance of the login form
    if request.method == "POST":
        #  create new login form with the data posted from the form 
        login_form = UserLoginForm(request.POST)
        # check that user is authenticated
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
           
            #if we have a user then log them in
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
                #redirect to the index page so the login page is not visible
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
                  
    else:
        #create an empty object
        login_form = UserLoginForm()

    return render(request, 'login.html', {'login_form': login_form})
def registration(request):
    """Render the registration page"""
    #redirect to the index page if user is authenticated
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
    # create an instance of the reg form using values within the pos request
     #  create new login form with the data posted from the form 
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {
        "registration_form": registration_form})
        
def user_profile(request):
    """The user's profile page"""
    # retrieve the user from the database
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {"profile": user})
    