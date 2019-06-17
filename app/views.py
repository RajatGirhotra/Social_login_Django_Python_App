from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import facebook
from rest_framework.authtoken.models import Token
import json

# Create your views here.
def login(request):
    return render(request, 'login.html')

@login_required
def home(request):
    return render(request, 'homepage.html')


@csrf_exempt
def login_view(request):
    """Function for login and register
        :return:token for authorization or error
    """
    data = json.loads(request.body.decode('utf-8'))
    access_token = data.get('accessToken')
    new_user = False
    try:
        graph = facebook.GraphAPI(access_token=access_token)
        user_info = graph.get_object()
    except facebook.GraphAPIError:
        return JsonResponse({'error': 'Invalid data'}, safe=False)
