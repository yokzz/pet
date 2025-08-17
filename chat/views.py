from django.shortcuts import render

def chats_view(request):
    return render(request, "chat/chats.html")

def room_view(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})