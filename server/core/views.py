from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from .models import ADMIN

# Create your views here.
@csrf_exempt
def user_login(request):
    if request.method == "POST":
        user_name = request.POST.get("user_name")
        pass_word = request.POST.get("pass_word")
        admins = ADMIN.objects.all()
        for admin in admins:
            if admin.username == user_name and admin.password == pass_word:
                print("Success")
                return HttpResponse("Authentication Success")
            elif admin.username == user_name and not admin.password == pass_word:
                return HttpResponse("Incorrect Password")
            else:
                print("Failed")
                return HttpResponse("Invalid Login Details")
    elif request.method == "GET":
        return HttpResponse("Server Connected")
