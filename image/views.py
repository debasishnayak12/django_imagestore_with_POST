from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from .models import user
from .forms import UserForm
from django.http import JsonResponse,Http404
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def createuser(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({"status":True,"message":"Successfully user created"},status=201)
        # errors = {field: error[0] for field, error in form.errors.items()}
        errors = [field for field, error in form.errors.items()]
        return JsonResponse({'success': False, 'message': f'Please Enter {errors[0]}'}, status=400)
    else:
        return JsonResponse({"status":False,"message":"Method not allowed"},status=400)
    
@csrf_exempt
def getusers(request):
    if request.method == 'POST':
        users = user.objects.all()
        return JsonResponse({"status":True,"message":"Successfully fetched all users","data":list(users.values())},status=200)
    else:
        return JsonResponse({"status":False,"message":"Method not allowed"},status=400)
    
@csrf_exempt
def getuser(request):
    id = request.POST.get('id')
    print(id)
    if request.method == 'POST':
        if not id:
            return JsonResponse({"status":False,"message":"Please enter id"},status=400)
        try:
            users =get_object_or_404(user,id=id)
            data = {
                "id": users.id,
                "name": users.name,
                "image": users.image.url
            }
          
            return JsonResponse({"status":True,"message":"Successfully fetched user","data":data},status=200)
        except Http404:
            return JsonResponse({"status":False,"message":"User not found"},status=404)
    else:
        return JsonResponse({"status":False,"message":"Method not allowed"},status=400)
