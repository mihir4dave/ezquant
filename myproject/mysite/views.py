from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as loged
import re
from django.core.mail import send_mail
from .models import usertype
def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

# Create your views here.
def signup(request):

    if request.method == 'POST':
        uname= request.POST.get('username')
        email= request.POST.get('email')
        pass1= request.POST.get('password1')
        pass2= request.POST.get('password2')
        numb= request.POST.get('nums')
        myselect= request.POST.get('myselect')
        print(numb)
        print(email)
        print(pass1)
        print(uname)
        print(myselect)
        if pass1 != pass2:
            return HttpResponse("Your both passwords are not same")
        
        if len(uname) < 3:
            return HttpResponse("Name should be at least 3 characters.")

        # Validate email
        if not validate_email(email):
            return HttpResponse("Invalid email address.")

        # Validate number
        if len(numb) != 10 or not numb.isdigit():
            return HttpResponse("Number should be 10 digits.")

        # Validate password
        if len(pass1) < 6 or not any(c.isupper() for c in pass1) or not any(c in "!@#$%^&*" for c in pass1):
            return HttpResponse("Password should be at least 6 characters with one uppercase letter and one special character.")

        # Validate password confirmation


        
        else:
           my_user= User.objects.create_user(uname,email,pass1)
           my_user.myselect= myselect
           my_user.save()
           user_type = usertype(user=my_user, type=myselect)
           user_type.save()
           email = 'davemihir1310@gmail.com'
           message1 = "new user has been created"
           message= message1
           subject = 'User '
           email_from = 'shivdave1310@gmail.com'
           recipient_list = [email, 'davemihir1310@gmail.com']
           send_mail(subject, message1, email_from, recipient_list, fail_silently=False)
           return redirect('login')
        

    return render(request,'regestration.html')



def login(request):

    if request.method== 'POST':
        uname= request.POST.get('username')
        pass1= request.POST.get('password')
        
        user= authenticate(request,username= uname, password = pass1)
        if user is not None:
            loged(request, user)
            request.session['name']=uname
            return redirect('main')
        else:
            return HttpResponse("username or password is incorrect: yad rakh bhidu ")

        print(user.username)
    return render(request,'loginpage.html')

def logoutfun(request):
     logout(request)
     return redirect('login')



def main(request):
    name = request.session.get('name')
    users = User.objects.filter(username=name)
    
    if users.exists():
        user = users.first()  # Retrieve the first User object from the queryset
        print(user.username)
        
        # Retrieve the UserType for the user
        user_type = usert
        ype.objects.filter(user=user).first()
        
        if user_type:
            if user_type.type == 'client':
                context = {
                    'user': user,
                    'message': 'You are logged in as client',
                }
                return render(request, 'main.html', context)
            
            elif user_type.type == 'admin':
                context = {
                    'user': user,
                    'message': 'You are logged in as admin',
                }
                return render(request, 'main.html', context)

    return HttpResponse("User not found")



