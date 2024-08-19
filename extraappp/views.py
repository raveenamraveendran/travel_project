from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if  request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info (request,'invalid credential')
            return redirect('login')

    return render(request,'login.html')

def registration(request):
     if request.method=='POST':
        username=request.POST['username']
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        email=request.POST['email']
        password1=request.POST['password']
        password2=request.POST['password2']

        if  password1== password2:
            if User.objects.filter(username=username).exists():
               messages.info(request,'username already exist')
               return redirect('registration')

            elif User.objects.filter(email=email).exists():
                  messages.info(request, 'email already exist')
                  return redirect('registration')
            else:
                use=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password1)
                use.save();
                print('use created')
                return redirect('login')

        else:
              messages.info(request,'password not matched')
              return redirect('registration')

        # return redirect('/')

     return render(request,'registration.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
