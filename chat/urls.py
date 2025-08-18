from django.urls import path 

from chat import views

urlpatterns = [
    path("", views.chats_view, name="chats"),
    path("room/<str:room_name>/", views.room_view, name="chat-room"),
    path("authenticate/yokzz/", views.authenticate_yokzz, name="authenticate-yokzz")
]

app_name = "chat"