from django.shortcuts import render

from .models import ChatModel
from accounts.models import CustomUser

# Create your views here.
def index(request):
    return render(request, "chat/chat.html")

def room(request, username):
    user_obj = CustomUser.objects.get(username=username)
    
    if request.user.id > user_obj.id:
        thread_name = f'chat_{request.user.id}-{user_obj.id}'
    else:
        thread_name = f'chat_{user_obj.id}-{request.user.id}'

    print(f'To jest ta wartosc thread_name: {thread_name}')

    # thread_name = f'chat/{user_obj}'

    message_objs = ChatModel.objects.filter(thread_name=thread_name)

    context = {
        "user": user_obj,
        'messages': message_objs
        }
    
    print(message_objs)

    return render(request, "chat/room.html", context=context)