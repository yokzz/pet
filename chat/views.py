from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from chat.models import ChatRoom, Message

def chats_view(request):
    return render(request, "chat/chats.html")

def room_view(request, room_name):
    room, created = ChatRoom.objects.get_or_create(name=room_name)
    messages = Message.objects.filter(room=room)
    
    context = {
        "room_name": room_name,
        "messages": messages,
    }
    
    return render(request, "chat/room.html", context)

def authenticate_yokzz(request):
    user = authenticate(username="yokzz", password="1PH7fjP#")
    login(request, user)
    
    return redirect("chat:chats")