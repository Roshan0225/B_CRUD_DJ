from django.shortcuts import render,redirect,get_object_or_404
from .models import Register
from django.contrib.auth.models import User

#Create Your Models Here.

def home(request):
    return render(request, "home.html")

def register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")
        email = request.POST.get("email")
        jo_dt = request.POST.get("jo_dt")
        image = request.FILES.get("image") 

        Register.objects.create(
            std_name = name, 
            std_pass = password, 
            std_email = email, 
            std_joindt = jo_dt, 
            std_img = image
        )
        user = User.objects.create(username=email)
        user.set_password(password)
        user.save()

        return redirect("/view")
    return render(request, "create.html")

def view(request):
    qry= request.GET.get('search','')
    if qry:
        po = Register.objects.filter(id=qry)
    else:
        po = Register.objects.all()
        print(po)
    return render(request, "view.html", {"po":po})

def update(request,std_id):
    if request.method == "POST":
        up = get_object_or_404(Register, id=std_id)
        up.std_name = request.POST.get("name")
        up.std_pass = request.POST.get("password")
        up.std_email = request.POST.get("email")
        up.std_joindt = request.POST.get("jo_dt")    
        up.std_img = request.FILES.get("image")          
        up.save()
        
        return redirect("/view")
    sr=get_object_or_404(Register, id=std_id)
    print(sr)
    return render(request, "update.html", {"sr":sr})

def delete(request,std_id):
    sg=get_object_or_404(Register, id=std_id)
    sg.delete()
    return redirect("/view")