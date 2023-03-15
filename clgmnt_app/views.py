from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
from clgmnt_app.models import Course,Student,Usermember
import os

# Create your views here.
def home(request):
    return render(request,'home.html')
def loginpage(request):
    return render(request,'loginpage.html')
def signup(request):
    course=Course.objects.all()
    return render(request,'signup.html',{'courses':course})

def addstudent(request):
    if request.user.is_authenticated:
        courses=Course.objects.all()

        return render(request,'addstudent.html',{'course':courses})
    return render(request,'loginpage.html')
def loginto(request):
    
    if request.method=="POST":
        username=request.POST['uname']
        password=request.POST['pswd']
        user=auth.authenticate(username=username,password=password)
    
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('adminhome')
            else:
                login(request,user)
                auth.login(request,user)
                messages.info(request,f'Welcome {username}')
                return redirect('teacherpage')
        else:
            messages.info(request,"Invalid username or password")
            return redirect('/')
    return render(request,'home.html')
def adminhome(request):
    if request.user.is_authenticated:
        return render(request,'adminhome.html')
    return render(request,'loginpage.html')
def course(request):
    if request.user.is_authenticated:
        return render(request,'course.html')
    return render(request,'loginpage.html')
def addcourse(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            cname=request.POST['cname']
            fees=request.POST['fee']
            courses=Course(corse_name=cname,fee=fees)
            courses.save()
            return redirect('course')
        return render(request,'course.html')
    return render(request,'loginpage.html')
def studentdb(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            student_name=request.POST['name']
            print(student_name)
            age=request.POST['age']
            print(age)
            student_address=request.POST['address']
            print(student_address)
            
            jdate=request.POST['date']
            print(jdate)
            email=request.POST['email']
            print(email)
            sel=request.POST['select']
            print(sel)
            course1=Course.objects.get(id=sel)
            print(course1)
            student=Student(student_name=student_name,age=age,address=student_address,joining_date=jdate,email=email,course=course1)
            student.save()
            return redirect('addstudent')
        return render(request,'addstudent.html')
    return render(request,'loginpage.html')
def showstudent(request):
    if request.user.is_authenticated:    
        student1=Student.objects.all()
        return render(request,'showstudent.html',{'students':student1})
    return render(request,'loginpage.html')

def edit(request,pk):
    if request.user.is_authenticated:
        studentdb=Student.objects.get(id=pk)
        course1=Course.objects.all()
        return render(request,'edit.html',{'students':studentdb,'courses':course1})
    return render(request,'loginpage.html')

def editdb(request,pk):
    if request.user.is_authenticated:
        if request.method=='POST':
            studentdb=Student.objects.get(id=pk)
            studentdb.student_name=request.POST['name']
            studentdb.age=request.POST['age']
            studentdb.address=request.POST['address']
            studentdb.joining_date=request.POST['date']
            studentdb.email=request.POST['email']
            student_course=request.POST['select']
            course1=Course.objects.get(id=student_course)
            studentdb.course=course1
            studentdb.save()
            return redirect('showstudent')
        return render(request,'edit.html')
    return render(request,'loginpage.html')

def Delete(request,pk):
    if request.user.is_authenticated:
        stud=Student.objects.get(id=pk)
        stud.delete()
        return redirect('showstudent')
    return render(request,'loginpage.html')
def register(request):
    
    if request.method=="POST":
        f_name=request.POST['fname']
        l_name=request.POST['lname']
        u_name=request.POST['uname']
        email=request.POST['email']
        pswd=request.POST['pswd']
        c_pswd=request.POST['cpswd']
        age=request.POST['age']
        address=request.POST['adrs']
        image=request.FILES.get('img')
        sel=request.POST['sel']
        course1=Course.objects.get(id=sel)
        
        if pswd==c_pswd:
            if User.objects.filter(username=u_name).exists():
                messages.info(request, 'This username already exists!!!!!!')
                return redirect('signup')
            else:
                user=User.objects.create_user(first_name=f_name,last_name=l_name,username=u_name,password=pswd,email=email)
                user.save()
                u=User.objects.get(id=user.id)
            
                member=Usermember(address=address,age=age,image=image,user=u,course=course1)
                member.save()
                # messages.info(request, 'You have successfully registered')
                return redirect('/')
            
        else:
            messages.info(request, 'Password doesnt match!!!!!!!')
            
            return redirect('signup')         
        
    else:
        return render(request,'signup.html')

def teacherpage(request):
    if request.user.is_authenticated:
        return render(request,'teacherpage.html')
    return render(request,'loginpage.html')

def showteacher(request):
    if request.user.is_authenticated:
        usermember=Usermember.objects.all()
        return render(request,'showteacher.html',{'user_member':usermember})
    return render(request,'loginpage.html')
def Delete_teacher(request,pk):
    if request.user.is_authenticated:
        usermember=Usermember.objects.get(id=pk)
        
        user=User.objects.get(id=usermember.user.id)
        
        user.delete()
        usermember.delete()
        return redirect('showteacher')
    return render(request,'loginpage.html')
def showprofile(request):
  
    user_id=request.user.id
    user1=Usermember.objects.get(user=user_id)
    return render(request,'showprofile.html',{'userid':user1})
    
def editprofile(request):
    if request.user.is_authenticated:
        user_id=request.user.id
    
        # current_user = request.user.id
        # print (current_user)
        user1=Usermember.objects.get(user_id=user_id)
        user2=User.objects.get(id=user_id)
        course=Course.objects.all()
        if request.method=="POST":
            if len(request.FILES)!=0:
                if len(user1.image)>0:
                    os.remove(user1.image.path)
                user1.image=request.FILES.get('img')
            user2.first_name=request.POST.get('fname')
            user2.last_name=request.POST.get('lname')
            user2.username=request.POST.get('uname')
            user2.password=request.POST.get('pswd')
            user2.email=request.POST.get('email')
            user1.age=request.POST.get('age')
            user1.address=request.POST.get('adrs')
            course=request.POST['sel']
            course1=Course.objects.get(id=course)
            user1.course=course1
            user1.save()
            user2.save()
            return redirect('showprofile1',user_id=user_id)
        
        return render(request,'editprofile.html',{'userid':user1,'course':course})
    return redirect('/')   
def showprofile1(request,user_id):
    user1=Usermember.objects.get(user=user_id)
    return render(request,'showprofile.html',{'userid':user1})
def Logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('/')

   