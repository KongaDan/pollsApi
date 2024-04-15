from django.urls import path
from .views import *
from .apiview import PollDetail,PollList

urlpatterns = [
    path('polls/',PollList.as_view(), name="polls_list"),
    path('polls/<int:pk>',PollDetail.as_view(),name='poll_detail'),
]
