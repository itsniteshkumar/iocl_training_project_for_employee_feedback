from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from testapp.models import report, enggdetails
from testapp import ml
# Create your views here.
def home_view(request):
    return render(request, 'testapp/home.html')
@login_required(login_url='login')
def staff_form(request):
    request.session.set_expiry(0)
    name = User.objects.only('first_name','last_name').filter(is_staff=True)
    current_user = request.user
    u_name = current_user.first_name +" "+ current_user.last_name
    u_username = current_user.username
    if request.method == 'POST':
        nameandusername = request.POST['enggdetails']
        point = request.POST['pointt']
        info = request.POST['engginfo']
        dct = ml.sentiment_scores(info)
        print(dct)
        negative = str(float(dct['neg'])*100) + " " + "%"
        positive = str(float(dct['pos'])*100) + " " + "%"
        neutral = str(float(dct['neu'])*100)+ " " + "%"
        cpd = ""
        if float(dct["compound"]) >= 0.05:
            cpd = "Positive"
        elif float(dct["compound"]) <= -0.05:
            cpd = "Negative"
        else:
            cpd = "Neutral"
        print(positive,negative,neutral)
        complain_id = request.POST['complainid']
        rst = report(fullname_staff = u_name, username_staff = u_username, complain_id = complain_id, engg = nameandusername,total_points = point, feedbacktxt = info,
        feedbackpos = positive, feedbackneg = negative, feedbacknul = neutral, fedbackcomp = cpd)
        engg = enggdetails(engg_username = nameandusername.split("(")[1].split(")")[0], engg_fullname = nameandusername.split("(")[0], complainid = complain_id, point = point)
        rst.save()
        engg.save()
        return redirect('home')
    return render(request,'testapp/staff_form.html',{"fname":name})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = auth.authenticate(username=username,password = password)
            if user is not None:
                if user.is_staff == False:
                    request.session.set_expiry(0)
                    auth.login(request,user)
                    return redirect('staffform')
                else:
                    return redirect('logout')
            else:
                # err = {'error':'username or password not matched'}
                messages.error(request, 'wrong username or password')
                return render(request,'testapp/login.html')

        except ObjectDoesNotExist:
            return render(request,'testapp/login.html',{'err':'please contact to our admin for registration'})
    else:
        return render(request,'testapp/login.html')
def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return render(request,'testapp/logout.html')
    else:
        return render(request,'testapp/home.html')