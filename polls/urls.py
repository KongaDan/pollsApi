from django.urls import path
from .views import *
from .apiview import *

urlpatterns = [
    path('polls/',PollList.as_view(), name="polls_list"),
    path('polls/<int:pk>',PollDetail.as_view(),name='poll_detail'),
    path('choices/',ChoiceList.as_view(),name="choices_list"),
    path('vote/',CreateVote.as_view(),name="create_vote"),
]
