from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.http import StreamingHttpResponse, JsonResponse

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

from AI_HealthTrainer import health_trainer
from datetime import datetime, timedelta

global start_time, end_time, exercise_name

def get_feedback(request):
    feedback_text = health_trainer.send_feedback()
    data = {'textData': feedback_text}
    print(data)
    return JsonResponse(data)

def video_feed(request):
    #return StreamingHttpResponse(health_trainer.generate_frames(), content_type='application/json')
    return StreamingHttpResponse(health_trainer.generate_frames(), content_type='multipart/x-mixed-replace; boundary=frame')

# @csrf_protect
# def submit_form_view(request):
#     if request.method == 'POST':
#         form = YourForm(request.POST)
#         if form.is_valid():
#             # 폼이 유효한 경우 처리
#             # ...
#     else:
#         form = YourForm()


def camera(request):
    # set = 2
    # reps = 4
    # rest = 10
    if request.method == 'POST':
        set = request.POST['sets']
        reps = request.POST['reps']
        rest = request.POST['rest']
    return render(request, "Structures/camera.html", {'sets_value': set, 'reps_value': reps, 'rest_value': rest})


def set_time(request):
    global exercise_name
    exercise_name = request.GET.get('exercise_name')
    return render(request, "Structures/time.html")

def completion(request):
    return render(request, "Structures/completion.html")
    return render(request, "Structures/camera.html")


def homepage(request):
    return render(request, "Structures/homepage.html")

def login(request):
    return render(request, "Structures/login.html")

def home(request):
    return render(request, "Structures/mypage.html")

def exercise(request):
    return render(request, "Structures/exercise.html")

def time(request):
    return render(request, "Structures/time.html")

def goal(request):
    return render(request, "Structures/goal.html")

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login') 
    else:
        form = UserCreationForm()
    return render(request, 'Structures/signup.html', {'form': form})



# def index(request):
#     return render(request, 'index.html')