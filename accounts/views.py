from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render

def register_user(request):
    if request.user.is_authenticated:
        return redirect('/logout')

    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/login')

    context = {
        'form':form
    }

    return render(request, 'accounts/register.html', context)

def login_user(request):

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()

            login(request, user)
            return redirect('/')

    else:
        form = AuthenticationForm()

    context = {
        'form': form
    }


    return render(request, 'accounts/login.html', context)

        

def logout_user(request):

    if request.user.is_authenticated:

        if request.method == 'POST':
            logout(request)
            return redirect('/login')

        return render(request, 'accounts/logout.html')

    
    return redirect('/login')