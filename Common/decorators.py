from django.shortcuts import render,redirect


def auth_manager(func):
    def wrapper(request,*args,**kwargs):
        if 'manager' in request.session:
            return func(request,*args,**kwargs)
        else:
            return redirect('Common:home')
    return wrapper



def auth_cce(func):
    def wrapper(request,*args,**kwargs):
        if 'cce' in request.session:
            return func(request,*args,**kwargs)
        else:
            return redirect('Common:home')
    return wrapper


def auth_technician(func):
    def wrapper(request,*args,**kwargs):
        if 'technician' in request.session:
            return func(request,*args,**kwargs)
        else:
            return redirect('Common:home')
    return wrapper