from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from .forms import  UserForm,UserpForm,IdeaForm,InvestorForm,EntreForm
from .models import Userp,Idea, Entre,Investor
from django.http import HttpResponse
# from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from math import ceil;
from django.core.mail import send_mail
# Create your views here.

def home(request):
    user=False;
    print("HII")
    if request.user.is_authenticated:
        user=True;
        un=request.user.username;
        print(un);
        print(user);
        return render(request, 'home.html',{'user': user,'username':un});
    return render(request, 'home.html', {'user': user});

def investindex(request):
    iuser = Investor.objects.all()
    print(iuser)
    n = len(iuser)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))
    params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'iuser': iuser}
    print(iuser[3].user);
    return render(request, 'invest/index.html', params)

def entreindex(request):
    iuser = Idea.objects.all()
    print(iuser)
    n = len(iuser)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))
    params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'iuser': iuser}
    return render(request, 'entre/index.html', params)

def about(request):
    return render(request, 'about.html');

def contact(request):
    mail = False;
    if request.method == "POST":
        msg = request.POST.get("msg")
        name = request.POST.get("name")
        sub = request.POST.get("subject")
        email = request.POST.get("email")

        send_mail(
            sub + " from " + name,
            msg,
            email,
            [''], # Add receiver mail id here
            fail_silently=False,
        )
        print("mail Sent")
        mail = True;
        return render(request, 'contact.html', {'mail': mail});
    return render(request, 'contact.html', {'mail': mail});

def abc(request):
    mail=False;
    if request.method == "POST":
        msg = request.POST.get("msg")
        name = request.POST.get("name")
        sub = request.POST.get("sub")
        email = request.POST.get("email")

        send_mail(
            sub + " from " + name,
            msg,
            email,
            ['guptaprajul2000@gmail.com'],
            fail_silently=False,
        )
        print("mail Sent")
        mail=True;
        return render(request, 'abc.html',{'mail': mail});
    return render(request, 'abc.html',{'mail': mail});

def investinfo(request,username):
    iuser = Investor.objects.filter(id=username)

    # return render(request, 'shop/prodView.html', {'product': product[0]})
    print(iuser[0].user);
    return render(request, 'invest/about.html', {'iuser': iuser[0]});

def entreinfo(request,username):
    iuser = Idea.objects.filter(id=username)
    uuser1=User.objects.filter(username=iuser[0].user.username)
    uuser2 = Idea.objects.filter(user=uuser1[0])
    uuser = Userp.objects.filter(user=uuser1[0])
    iuser1 = Entre.objects.filter(user=uuser[0])
    # return render(request, 'shop/prodView.html', {'product': product[0]})
    print(uuser2);
    return render(request, 'Entre/about.html', {'iuser': iuser[0],'iuser1': iuser1[0],'iuser2': uuser2});

def ideah(request):
    iuser = Idea.objects.all()
    print(iuser)
    n = len(iuser)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))
    params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'iuser': iuser}
    return render(request, 'ideahome.html', params)

def ideainfo(request,username):
    iuser = Idea.objects.filter(id=username)

    # return render(request, 'shop/prodView.html', {'product': product[0]})
    print(iuser[0].user);
    return render(request, 'ideainfo.html', {'iuser': iuser[0]});

def entreidea(request):
    use = None
    if request.user.is_authenticated:
        reg=False;
        un=request.user.username
        print(un);
        if request.method == "POST":
            # reg=True;
            use = request.user
            title = request.POST.get("ititle")
            desc = request.POST.get("idesc")
            amount = request.POST.get("amount")
            days = request.POST.get("days")
            ldate = request.POST.get("ldate")
            # print(form.idea_title)
            # print(form.is_valid())
            new = Idea(user=use, idea_title=title, idea_desc=desc, amount=amount, no_of_days_req=days, last_date=ldate)
            # try:
            new.save()
            reg = True
            # usert=Entre(user=use,idea_title=new)
            # usert.save()
            # except(e):
            #      print(e)
            return render(request, 'entre/idea.html', {'user': use, 'reg':reg});
        else:
            return render(request, 'entre/idea.html',{'user' : use,'reg':reg, 'un':un});
    else:
        return render(request,'home.html');

@login_required
def logout_user(request):
    logout(request);
    # return HttpResponse("Logout sucessful");
    return redirect('Home');

def login_user(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password=request.POST.get('pass')
        user= authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('Home')
            else:
                return HttpResponse("Account not Active")
        else:
            print("Some one tried to login and failed!")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("Invalid Login details")
    else:
        return render(request, 'login.html');

def sign_up(request):
    registered=False
    print("hii")
    if request.method =="POST":
        user= User.objects.create_user(password = request.POST.get("password"), email = request.POST.get("email"), username=request.POST.get("Username"), first_name= request.POST.get("fname"), last_name= request.POST.get("lname"))
        is_entre = request.POST.get("is_entre")
        is_investor = request.POST.get("is_investor")
        if is_entre=="on":
            is_entre=True
            is_investor=False
        else:
            is_entre=False
            is_investor=True
        new = Userp(user=user,phone=request.POST.get("phone"),is_entre=is_entre,is_investor=is_investor)
        # try:
        new.save()
        registered = True
        if is_entre==True:
            usert=Entre(user=new);
        else:
            usert=Investor(user=new)
        usert.save();
        # except(e):
        #     print(e)
    return render(request, 'sign_in.html', {'registered': registered});

def moreinfo(request):
    use = None
    if request.user.is_authenticated:
        reg=False;
        un=request.user.username
        print(un);
        iuser = Userp.objects.get(user=request.user)
        print(iuser.is_entre);
        print(iuser.is_investor);
        if(iuser.is_entre == True):
            if request.method == "POST" and request.FILES['image']:
                use = request.user
                image = request.FILES.get("image")
                iuser1 = Entre.objects.get(user=iuser)
                iuser1.logo = image
                iuser1.save()
                reg = True
                # usert=Entre(user=use,idea_title=new)
                # usert.save()
                # except(e):
                #      print(e)
                return render(request, 'entre/update.html', {'user': use, 'reg':reg});
            else:
                return render(request, 'entre/update.html',{'user' : use,'reg':reg, 'un':un});
        else:
            if request.method == "POST" and request.FILES['image']:
                use = request.user
                total_funds = request.POST.get("funds")
                previous_proj = request.POST.get("prev_proj")
                image = request.FILES.get("image")
                iuser1 = Investor.objects.get(user=iuser)

                iuser1.total_funds=total_funds
                iuser1.previous_proj=previous_proj
                iuser1.logo=image
                iuser1.save()
                reg = True
                return render(request, 'invest/update.html', {'user': use, 'reg':reg});
            else:
                return render(request, 'invest/update.html',{'user' : use,'reg':reg, 'un':un});
    else:
        return render(request,'home.html');

