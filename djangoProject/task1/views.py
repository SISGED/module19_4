from django.shortcuts import render
from django.http import HttpResponse
from djangoProject.task1.forms import (UserRegister)
from django.views.generic import TemplateView

class platform(TemplateView):
    template_name = 'platform.html'

class cart_store(TemplateView):
    template_name = 'cart.html'

def games_store(request):
    mydict = {'games': ["Atomic Heart", "Cyberpunk 2077"]}
    context={
         'mydict': mydict,
    }
    return render(request, 'games.html', context)

def sign_up_by_html(request):
    users=['alex', 'max', 'vasy']
    info={}
    if request.method == 'POST':
        user_have=False
        username=request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))
        is_user = username in users
        if password==repeat_password:
            if age>=18:
                if is_user==False:
                    user_have=True
                else:
                    info['error'] = 'Пользователь уже существует'
            else:
                info['error'] = 'Вы должны быть старше 18'
        else:
            info['error']='Пароли не совпадают'

        if user_have:
            message=(f'Приветствуем, {username}!')
            print(message)
        else:
            message = info['error']
        return HttpResponse(message)
    return render(request, 'registration_page.html', info)


def sign_up_by_django(request):
    users=['alex', 'max', 'vasy']
    info={}
    if request.method == 'POST':
        user_have=False
        form = UserRegister(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = int(form.cleaned_data['age'])
            is_user = username in users
            if password==repeat_password:
                if age>=18:
                    if is_user==False:
                        user_have=True
                    else:
                        info['error'] = 'Пользователь уже существует'
                else:
                    info['error'] = 'Вы должны быть старше 18'
            else:
                info['error']='Пароли не совпадают'

            if user_have:
                message=(f'Приветствуем, {username}!')
                print(message)
            else:
                message = info['error']
        return HttpResponse(message)
    else:
        form = UserRegister()
    info['form']=form
    return render(request, 'registration_page.html', info)