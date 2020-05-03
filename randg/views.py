from django.shortcuts import render
import random

def randg(request):
    return render(request, 'randg/password_form.html')

def generate(request):
    length = int(request.GET.get('length',14)) #14 is default
    password = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('special'):
        characters.extend('@#$%^&*()_+!~')
    if request.GET.get('numbers'):
        characters.extend('1234567890')

    # challenge: make sure each appears in the Password
    # challenge: add an about view with a tag.

    for l in range(length):
        password += random.choice(characters)

    context = {'password': password}
    return render(request, 'randg/password_out.html', context)
