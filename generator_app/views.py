from django.shortcuts import render
from django.http import HttpResponse

import random
# Create your views here.

def home(request):
    return render(request, 'generator_app/index.html', {'password': 'samplepwd123'})
    # return HttpResponse("Sample text from HttpResponse")

def password(request):

    lower_chars = list('abcdefghijklmnopqrstuvwxyz')
    numbers = [1,2,3,4,5,6,7,8,9,0]
    spl_chars = list('!@#$%^&*()_+')
    upper_chars = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    pwd_length = int(request.GET.get('length'))
    uppercase_flag = request.GET.get('uppercase')
    numbers_flag = request.GET.get('numbers')
    spl_char_flag = request.GET.get('specialchar')

    generated_pwd = ''
    for i in range(pwd_length):
        while len(generated_pwd) <= pwd_length:
            generated_pwd += random.choice(lower_chars)
            if uppercase_flag:
                generated_pwd += random.choice(upper_chars)
            if numbers_flag:
                generated_pwd += str(random.choice(numbers))
            if spl_char_flag:
                generated_pwd += str(random.choice(spl_chars))

    return render(request, 'generator_app/password.html', {'password': generated_pwd})