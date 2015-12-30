from django.shortcuts import render
from django.http import HttpResponse
import django
from django.conf import settings
from django.core.mail import send_mail
from .models import UserEmail


def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    return render(request, 'index.html')


def success(request):
    email = request.POST.get('email', '')
    newsletter = request.POST.get('checkbox', '')
    data = """
Hello there!

I wanted to personally write an email in order to welcome you to our platform.\
 We have worked day and night to ensure that you get the best service. I hope \
that you will continue to use our service. We send out a newsletter once a \
week. Make sure that you read it. It is usually very informative.

Cheers!
~ Yasoob
    """
    user = UserEmail(email=email)
    user.save()
    if newsletter == 'on':
        send_mail('Welcome!', data, "Yasoob",
                  [email], fail_silently=False)
    return render(request, 'success.html')
