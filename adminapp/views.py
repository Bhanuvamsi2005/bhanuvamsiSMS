from django.shortcuts import render

# Create your views here.
def projecthomepage(request):
    return render(request, 'adminapp/ProjectHomePage.html')

def printpagecall(request):
    return render(request,'adminapp/printer.html')

def printpagelogic(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        print(f'User input: {user_input}')
    a1={'user_input':user_input}
    return render(request,'adminapp/printer.html',a1)

def exceptionpagecall(request):
    return render(request,'adminapp/ExceptionExample.html')

def exceptionpagelogic(request):
    if request.method=="POST":
        user_input=request.POST['user_input']
        result=None
        error_message=None
        try:
            num=int(user_input)
            result=10/num
        except Exception as e:
            error_message=str(e)
        return render(request,'adminapp/ExceptionExample.html',{'result':result,'error':error_message})

    return render(request,'adminapp/ExceptionExample.html')

import random
import string
def randompagecall(request):
    return render(request,'adminapp/randomex.html')

def randomlogic(request):
    if request.method == "POST":
        user_input=int(request.POST['user_input'])
        ran=''.join(random.sample(string.ascii_uppercase+string.digits,k=user_input))

    a1={'ran': ran}
    return render(request,'adminapp/randomex.html',a1)

def calpagecall(request):
    return render(request,'adminapp/cal.html')
def calculatorlogic(request):
    result = None
    if request.method == 'POST':
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))
        operation = request.POST.get('operation')

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else 'Infinity'

    return render(request, 'adminapp/cal.html', {'result': result})

from django.shortcuts import render, redirect,get_object_or_404
from .models import Task, StudentList
from .forms import TaskForm, StudentForm

from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from .forms import TaskForm
import datetime
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_task')

    else:
        form = TaskForm()
    tasks = Task.objects.all()
    return render(request, 'adminapp/add_task.html', {'form': form,'tasks':tasks})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('add_task')

def loginpagecall(request):
    return render(request,'adminapp/login.html')

def registerpagecall(request):
    return render(request,'adminapp/register.html')

import datetime
from datetime import datetime
from datetime import timedelta


def dateandtimepagecall(request):
    return render(request, 'adminapp/dateandtime.html')


def dateandtimepagelogic(request):
    if request.method == 'POST':
        num1 = int(request.POST['user_input'])
        x = datetime.now()
        print(x + timedelta(days=num1))
        result = x + timedelta(days=num1)
    return render(request, 'adminapp/dateandtime.html', {'result': result})

from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render
def UserRegisterPageCall(request):
    return render(request, 'adminapp/register.html')
def UserRegisterLogic(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['confirm_password']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return render(request, 'adminapp/register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'OOPS! Email already registered.')
                return render(request, 'adminapp/register.html')
            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=pass1
                )
                user.save()
                messages.info(request, 'Account created Successfully!')
                return render(request, 'adminapp/ProjectHomePage.html')
        else:
            messages.info(request, 'Passwords do not match.')
            return render(request, 'adminapp/register.html')
    else:
        return render(request, 'adminapp/register.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

def UserLoginPageCall(request):
    return render(request, 'adminapp/login.html')


from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def UserLoginLogic(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if len(username) == 10:
                # Redirect to StudentHomePage
                messages.success(request, 'Login successful as student!')
                return redirect('studentapp:studenthomepage')  # Replace with your student homepage URL name
                # return render(request, 'facultyapp/FacultyHomepage.html')
            elif len(username) == 4:
                # Redirect to FacultyHomePage
                # messages.success(request, 'Login successful as faculty!')
                return redirect('facultyapp:facultyhomepage')  # Replace with your faculty homepage URL name
                # return render(request, 'facultyapp/FacultyHomepage.html')
            else:
                # Invalid username length
                messages.error(request, 'Username length does not match student or faculty criteria.')
                return render(request, 'adminapp/login.html')
        else:
            # If authentication fails
            messages.error(request, 'Invalid username or password.')
            return render(request, 'adminapp/login.html')
    else:
        return render(request, 'adminapp/login.html')

def logout(request):
    auth.logout(request)
    return redirect('projecthomepage')



#def add_student(request):
 #   if request.method == 'POST':
  #      form = StudentForm(request.POST)
   #     if form.is_valid():
    #        form.save()
    #        return redirect('student_list')
    #else:
     #   form = StudentForm()
    #return render(request, 'adminapp/addstudent.html', {'form': form})

from django.contrib.auth.models import User
from .models import StudentList
from .forms import StudentForm
from django.shortcuts import redirect, render
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            register_number = form.cleaned_data['Register_Number']
            try:
                user = User.objects.get(username=register_number)
                student.user = user  # Assign the matching User to the student
            except User.DoesNotExist:
                form.add_error('Register_Number', 'No user found with this Register Number')
                return render(request, 'adminapp/addstudent.html', {'form': form})
            student.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'adminapp/addstudent.html', {'form': form})



def student_list(request):
    students = StudentList.objects.all()
    return render(request, 'adminapp/studentlist.html', {'students': students})

from .forms import UploadFileForm
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64


def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        df = pd.read_csv(file, parse_dates=['Date'], dayfirst=True)
        total_sales = df['Sales'].sum()
        average_sales = df['Sales'].mean()

        df['Month'] = df['Date'].dt.month
        monthly_sales = df.groupby('Month')['Sales'].sum()
        month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        monthly_sales.index = monthly_sales.index.map(lambda x: month_names[x - 1])

        plt.pie(monthly_sales, labels=monthly_sales.index, autopct='%1.1f%%')
        plt.title('Monthly Sales Distribution')

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
        buffer.close()

        return render(request, 'adminApp/chart.html',
                      {'total_sales': total_sales,
                       'average_sales': average_sales,
                       'chart': image_data})

    return render(request, 'adminApp/chart.html', {'form': UploadFileForm()})



from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .models import Feedback

@csrf_protect
def submit_feedback(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        description = request.POST['description']

        feedback = Feedback(name=name, email=email, phone=phone, description=description)
        feedback.save()

        return redirect('feedback_success')  # Redirect to a success page or another view
    return render(request, 'adminapp/feedback.html')

def feedback_success(request):
    return render(request, 'adminapp/feedback_success.html')

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .models import Contact

from django.shortcuts import render, redirect
from .models import Contact

def add_contact(request):
    if request.method == 'POST':
        # Retrieve data from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        description = request.POST.get('description')

        # Save the data to the Contact model
        feedback = Contact(name=name, email=email, phone=phone, description=description)
        feedback.save()

        return redirect('view_contacts')  # Redirect to the contact list page

    return render(request, 'adminapp/addcontact.html')

def view_contacts(request):
    # Retrieve all contacts from the database
    contacts = Contact.objects.all()
    return render(request, 'adminapp/addedcontact.html', {'contacts': contacts})
