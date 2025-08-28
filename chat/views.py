from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from chat.models import ChatRoom, Message

import datetime

import os

def chats_view(request):
    return render(request, "chat/chats.html")

def room_view(request, room_name):
    room, created = ChatRoom.objects.get_or_create(name=room_name)
    messages = Message.objects.filter(room=room)
    
    # current_date = datetime.date.today()
    
    # for message in messages:
    #     message_date = message.timestamp.date()
    #     if message_date == current_date:
    #         print(message_date)
    
    tz = request.session.get(os.environ.get("TZ_SESSION_KEY"))
    
    context = {
        "room_name": room_name,
        "messages": messages,
        "timezone": tz
    }
    
    return render(request, "chat/room.html", context)

def authenticate_yokzz(request):
    user = authenticate(username="yokzz", password="1PH7fjP#")
    login(request, user)
    
    return redirect("chat:chats")