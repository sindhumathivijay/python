from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from tech.settings import BASE_URL
from volt.models import *
from django.contrib.auth.forms import UserCreationForm


@csrf_exempt
def login(request):
    stu = datas.objects.all()
    print(stu)

    return render(request, 'studentlogin.html', {'base_url': BASE_URL,'data':stu})

@csrf_exempt
def index(request):

    return render(request,'index.html',{'base_url':BASE_URL})

@csrf_exempt
def student_login(request):
    if request.method=="POST":
        data_html = {key: request.POST[key] for key in request.POST}
        try:
            x=datas.objects.get(user=data_html['user'])
            x.save()
            if x.passid != data_html['passid']:
                return render(request, 'studentlogin.html', {'error': 'password wrong', 'base_url': BASE_URL})
            obj = datas.objects.all()

            return render(request,'exammainpage.html',{'success':'Login success','base_url':BASE_URL,'user':data_html,'obj':obj})


        except datas.DoesNotExist:
            return render(request,'studentlogin.html',{'error':'user dosn\'t exist','base_url':BASE_URL})

    return render(request,'studentlogin.html',{'error':'user dosn\'t exist','base_url':BASE_URL})




@csrf_exempt
def student_signup(request):
    if request.method == 'POST':
        data_html1 = {key: request.POST[key] for key in request.POST}
        try:
            datas.objects.get(user=data_html1['user'])
            return render(request, 'studentsignup.html', {'error': 'user name already exist', 'base_url': BASE_URL})
        except datas.DoesNotExist:
            if data_html1['passid'] != data_html1['confirm_passid']:
                return render(request, 'studentsignup.html', {'error': 'password dosn\'t match', 'base_url': BASE_URL})

            obj = datas.objects.create(college=data_html1['college'],
                                       name=data_html1['name'],
                                       qualification=data_html1['qualification'],
                                       specialization=data_html1['specialization'],
                                       arrears=data_html1['arrears'],
                                       area_of_interest=data_html1['areas'],
                                       contact=data_html1['contact'],
                                       address=data_html1['address'],
                                       email=data_html1['email'],
                                       # gender=data_html1['msex'],
                                       day=data_html1['day'],
                                       month=data_html1['month'],
                                       year=data_html1['year'],
                                       photo=data_html1['photo'],
                                       proof=data_html1['proof'],
                                       user=data_html1['userid'],
                                       passid=data_html1['passid'],
                                       confirm_passid=data_html1['confirm_passid'])
            print('--------------------------------------------------------------------')
            return render(request, 'studentlogin.html', {'success': 'user saved', 'base_url': BASE_URL})
        except datas.KeyError:
            return render(request, 'studentsignup.html', {'error': 'enter the data', 'base_url': BASE_URL})
        # return render(request,'register.html',{'base_url':BASE_URL})
    else:
        return render(request, 'studentsignup.html', {'base_url': BASE_URL})

@csrf_exempt
def employees(request):
    return render(request,'login1.html',{'base_url':BASE_URL})

@csrf_exempt
def admin(request):
    return render(request,'adminlogin.html',{'base_url':BASE_URL})


@csrf_exempt
def jobseeker(request):
    return render(request,'createnewaccount.html',{'base_url':BASE_URL})


@csrf_exempt
def forgetpassword(request):
    return render(request,'forgetpassword.html',{'base_url':BASE_URL})

@csrf_exempt
def exammainpage(request):


    return render(request,'exammainpage.html',{'base_url':BASE_URL})

@csrf_exempt
def javaexam(request):


    if pythonmocktest:
        if request.method == "POST":
            username = request.POST['mark']

        return render(request,'javamocktest.html',{'base_url':BASE_URL})
    return render(request,'javaexam.html',{'base_url':BASE_URL})

@csrf_exempt
def pythonexam(request):
    if pythonmocktest:
        return render(request,'pythonmocktest.html',{'base_url':BASE_URL})


    return render(request,'pythonexam.html',{'base_url':BASE_URL})

@csrf_exempt
def phpexam(request):
    if phpmocktest:
        return render(request,'phpmocktest.html',{'base_url':BASE_URL})

    return render(request,'phpexam.html',{'base_url':BASE_URL})

@csrf_exempt
def signup(request):
    return render(request,'createnewaccount.html',{'base_url':BASE_URL})

@csrf_exempt
def applynow(request):
    return render(request,'applynow.html',{'base_url':BASE_URL})

@csrf_exempt
def fresher_signup(request):
    if request.method == 'POST':
        data_html1 = {key: request.POST[key] for key in request.POST}
        try:
            fresher.objects.get(email=data_html1['email'])
            return render(request, 'freshersignup.html', {'error': 'user name already exist', 'base_url': BASE_URL})
        except (fresher.DoesNotExist):

            # return render(request, 'studentsignup.html', {'error': 'password dosn\'t match', 'base_url': BASE_URL})

            obj = fresher.objects.create(name=data_html1['name'],
                                       degree=data_html1['degree'],
                                       year_of_pass=data_html1['pass'],
                                       skill=data_html1['skills'],
                                       mobile=data_html1['mobile'],
                                       present_address=data_html1['present'],
                                       permenant_address=data_html1['permenant'],
                                       day=data_html1['day'],
                                       month=data_html1['month'],
                                       year=data_html1['year'],
                                       email=data_html1['email'],
                                       passid=data_html1['passid'])
            print('--------------------------------------------------------------------')
            return render(request, 'fresherlogin.html', {'success': 'user saved', 'base_url': BASE_URL})

        except fresher.KeyError:
            return render(request, 'freshersignup.html', {'error': 'enter the data', 'base_url': BASE_URL})

    return render(request,'freshersignup.html',{'base_url':BASE_URL})

@csrf_exempt
def phpbasictest(request):
    if phpbasictest:
        return render(request,'phbbasictest.html',{'base_url':BASE_URL})
    return render(request,'phpbasictest.html',{'base_url':BASE_URL})

@csrf_exempt
def phpmocktest(request):
    return render(request,'phpmocktest.html',{'base_url':BASE_URL})

@csrf_exempt
def pythonbasictest(request):
    if pythonbasictest == True:
        return render(request, 'pythonmocktest.html', {'base_url': BASE_URL})
    return None

@csrf_exempt
def pythonmocktest(request):
    if request.method == 'POST':
        mark=request.POST['mark']
        x=datab(mark=mark)
        x.save()
        # data_html6 = {key: request.POST[key] for key in request.POST}
        # studts = datab.objects.all()
        # print(studts)
        # obj = datab.objects.create(mark=data_html6['mark'])
    return render(request,'pythonmocktest.html')

@csrf_exempt
def java_basictest(request):
    return render(request,'javabasictest.html',{'base_url':BASE_URL})

@csrf_exempt
def javamocktest(request):
    return render(request,'javamocktest.html',{'base_url':BASE_URL})

@csrf_exempt
def hrmanagerlogin(request):
    # if userid == admin1:

    return render(request,'hrmanagerlogin.html',{'base_url':BASE_URL})

@csrf_exempt
def technicalmanagerlogin(request):
    return render(request,'technicalmanagerlogin.html',{'base_url':BASE_URL})

@csrf_exempt
def hrpage(request):
    a = datab.objects.all()
    return render(request,'hrpage.html',{'base_url':BASE_URL})

@csrf_exempt
def teamleaderpage(request):
    return render(request,'teamleaderpage.html',{'base_url':BASE_URL})

@csrf_exempt
def addstu(request):
    return render(request,'addstudent.html',{'base_url':BASE_URL})
@csrf_exempt
def viewstu(request):
    return render(request,'viewstudent.html',{'base_url':BASE_URL})

@csrf_exempt
def ademp(request):
    return render(request,'addemployee.html',{'base_url':BASE_URL})

@csrf_exempt
def viewemp(request):
    return render(request,'viewemployee.html',{'base_url':BASE_URL})

@csrf_exempt
def admin1(request):
    return render(request,'admin1.html',{'base_url':BASE_URL})

@csrf_exempt
def technicalmanagerpage(request):
    return render(request,'technicalmanagerpage.html',{'base_url':BASE_URL})

@csrf_exempt
def teamleaderlogin(request):
    return render(request,'teamleaderlogin.html',{'base_url':BASE_URL})

@csrf_exempt
def fresherlogin(request):
    if request.method == "POST":
        data_html = {key: request.POST[key] for key in request.POST}
        data_html5 = {key: request.POST[key] for key in request.POST}
        try:
            x = fresher.objects.get(email=data_html['email'])
            y = forget_admin.objects.get(email=data_html5['email'])
            x.save()
            y.save()
            if x.passid != data_html['passid']:
                return render(request, 'fresherlogin.html', {'error': 'password wrong', 'base_url': BASE_URL})
            obj = fresher.objects.all()

            return render(request, 'exammainpage.html',{'success': 'Login success', 'base_url': BASE_URL, 'user': data_html, 'obj': obj})


        except fresher.DoesNotExist:
            return render(request, 'fresherlogin.html', {'error': 'user dosn\'t exist', 'base_url': BASE_URL})

            if y.passid != data_html5['passid']:
                return render(request, 'fresherlogin.html', {'error': 'password wrong', 'base_url': BASE_URL})
            obj = forget_admin.objects.all()

            return render(request, 'exammainpage.html',{'success': 'Login success', 'base_url': BASE_URL, 'user': data_html, 'obj': obj})


        except forget_admin.DoesNotExist:
            return render(request, 'fresherlogin.html', {'error': 'user dosn\'t exist', 'base_url': BASE_URL})

    return render(request, 'fresherlogin.html', {'error': 'user dosn\'t exist', 'base_url': BASE_URL})


@csrf_exempt
def experiencesignup(request):
    if request.method == 'POST':
        data_html1 = {key: request.POST[key] for key in request.POST}
        try:
            experience.objects.get(user=data_html1['email'])
            return render(request, 'experiencesignup.html', {'error': 'user name already exist', 'base_url': BASE_URL})
        except (experience.DoesNotExist):

            # return render(request, 'studentsignup.html', {'error': 'password dosn\'t match', 'base_url': BASE_URL})

            obj = experience.objects.create(name=data_html1['name'],
                                       domain=data_html1['domain'],
                                       position=data_html1['position'],
                                       notice=data_html1['notice'],
                                       last_ctc=data_html1['ctc'],
                                       expext_ctc=data_html1['expected'],
                                       reason=data_html1['reason'],
                                       mobile=data_html1['mobile'],
                                       location=data_html1['location'],
                                       experience=data_html1['experience'],
                                       skill=data_html1['skills'],
                                       qualification=data_html1['qualification'],
                                       user=data_html1['email'],
                                       passid=data_html1['passid'])
            print('--------------------------------------------------------------------')
            return render(request, 'experiencelogin.html', {'success': 'user saved', 'base_url': BASE_URL})

        except experience.KeyError:
            return render(request, 'experiencesignup.html', {'error': 'enter the data', 'base_url': BASE_URL})

    # return render(request,'freshersignup.html',{'base_url':BASE_URL})


    return render(request,'experiencesignup.html',{'base_url':BASE_URL})

@csrf_exempt
def experiencelogin(request):
    if request.method=="POST":
        data_html = {key: request.POST[key] for key in request.POST}
        try:
            x=experience.objects.get(user=data_html['userid'])
            x.save()
            if x.passid != data_html['passid']:
                return render(request, 'experiencelogin.html', {'error': 'password wrong', 'base_url': BASE_URL})
            obj = experience.objects.all()

            return render(request,'exammainpage.html',{'success':'Login success','base_url':BASE_URL,'user':data_html,'obj':obj})


        except experience.DoesNotExist:
            return render(request,'experiencelogin.html',{'error':'user dosn\'t exist','base_url':BASE_URL})

    return render(request,'experiencelogin.html',{'error':'user dosn\'t exist','base_url':BASE_URL})
    #
    #

    # return render(request,'experiencelogin.html',{'base_url':BASE_URL})

@csrf_exempt
def forgetpassword(request):
    if request.method == 'POST':
        data_html5 = {key: request.POST[key] for key in request.POST}
        try:
            forget_admin.objects.get(email=data_html5['email'])
            return render(request, 'forgetpassword.html', {'error': 'user name already exist', 'base_url': BASE_URL})
        except (forget_admin.DoesNotExist):

            # return render(request, 'studentsignup.html', {'error': 'password dosn\'t match', 'base_url': BASE_URL})

            obj = forget_admin.objects.create(email=data_html5['email'],
                                         passid=data_html5['passid'])
            print('--------------------------------------------------------------------')
            return render(request, 'fresherlogin.html', {'success': 'user saved', 'base_url': BASE_URL})

        except forget_admin.KeyError:
            return render(request, 'forgetpassword.html', {'error': 'enter the data', 'base_url': BASE_URL})

    # return render(request, 'freshersignup.html', {'base_url': BASE_URL})

    return render(request,'forgetpassword.html',{'base_url':BASE_URL})

