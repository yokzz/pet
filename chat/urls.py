from django.urls import path 

from chat import views

urlpatterns = [
    path("", views.chats_view, name="chats"),
    path("/<str:room_name>", views.room_view, name="chat-room"),
]