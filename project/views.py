from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout,logout as auth_logout



def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            print(request)

            # CHECK USER TYPE
            if user.is_superuser:
                print(user)
                return redirect('/master-admin/')   # for superuser
                
                #return redirect('/auth_logout/')
            elif user.is_staff:
                print(user)
                print("Staff")
                return redirect('/staff/')  # for staff user
            else:
                print(user)
                print("user")
                return redirect('/student/')

        return render(request, 'login.html', {'error': 'Invalid Username or Password!'})

    return render(request, 'login.html')


def logout_view(request):


    
    is_superuser = request.user.is_superuser
    auth_logout(request)

    if is_superuser:
        return redirect('/admin/')
    else:
        return redirect('/')
        
    

    