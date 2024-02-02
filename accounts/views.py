from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from .forms import CreateUserForm, CreateStudentForm, CreateTeacherForm, LoginForm
from students.models import Student
from teachers.models import Teacher
from .models import CustomUser

@login_required
def profile_view(request):
    user = request.user
    account_type = user.user_type

    # empty variables
    teacher_subjects = None

    if account_type == 'Admin':
        account_info = user.admin
    elif account_type == 'Staff':
        account_info = user.staff
    elif account_type == 'Teacher':
        account_info = user.teacher
        teacher_subjects = account_info.subjects.all()
    elif account_type == 'Student':
        account_info = user.student
    elif account_type == 'Parent':
        account_info = user.parent
    
    context = {
        'account_info': account_info,
        'teacher_subjects': teacher_subjects
    }

    return render(request, 'accounts/profile.html', context=context)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                print(user)
                login(request, user)
                messages.success(request, 'Witaj')
                return redirect(reverse('home'))
            else:
                messages.success(request, 'Logowanie nieudane. Sprawdź login lub hasło.')
    else:
        form = LoginForm()
    context = {
        'form': form
    }

    return render(request, 'accounts/login.html', context=context)

def create_view(request):
    # empty values
    student_form = None
    teacher_form = None



    if request.method == 'POST':

        # tworzenie STUDENTA
        if request.POST['user_type'] == 'Student':
            user_form = CreateUserForm(request.POST)
            student_form = CreateStudentForm(request.POST)
            if user_form.is_valid() and student_form.is_valid():
                user = user_form.save(commit=False)
                user.save()

                class_id = student_form.cleaned_data['class_id']
                parent_id = student_form.cleaned_data['parent_id']

                created_student = Student.objects.get(student__username=user.username)
                created_student.class_id = class_id
                created_student.parent_id = parent_id

                created_student.save()

                return redirect(reverse('create'))
            else:
                print("nie valid form")

        # tworzenie NAUCZYCIELA
        if request.POST['user_type'] == 'Teacher':
            user_form = CreateUserForm(request.POST)
            teacher_form = CreateTeacherForm(request.POST)
            if user_form.is_valid() and teacher_form.is_valid():
                user = user_form.save(commit=False)
                user.save()

                subjects = teacher_form.cleaned_data['subjects']

                created_teacher = Teacher.objects.get(teacher__username=user.username)
                created_teacher.subjects.set(subjects)

                return redirect(reverse('create'))
            else:
                print("nie valid form")

        # tworzenie RODZICA
        if request.POST['user_type'] == 'Parent':
            user_form = CreateUserForm(request.POST)
            if user_form.is_valid():
                user = user_form.save(commit=False)
                user.save()

                return redirect(reverse('create'))
            else:
                print("nie valid form")
    else:
        user_form = CreateUserForm()
        student_form = CreateStudentForm()
        teacher_form = CreateTeacherForm()
    return render(request, 'accounts/create.html', {
        'user_form': user_form,
        'student_form': student_form,
        'teacher_form': teacher_form,
    })

def logout_view(request):
    logout(request)
    return redirect(reverse('home'))

