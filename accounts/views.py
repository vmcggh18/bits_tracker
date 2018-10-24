from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from accounts.forms import UserLoginForm

# Create your views here.
def index(request):
    """Return the index.html file"""
    return render(request,  'index.html')
    

def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('index'))
    
def login(request):
    """Return a login page"""
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
            else:
                login_form.add_error(None, "Your username or password is incorrect")
                  
    else:
        #create an empty object
        login_form = UserLoginForm()

    return render(request, 'login.html', {'login_form': login_form})