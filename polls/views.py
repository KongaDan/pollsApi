from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import *

def poll_list(request):
    MAX_OBJECTS= 20
    polls= Poll.objects.all()[:MAX_OBJECTS]
    #allows to get 20 objects
    data={
        "results": list(
            polls.values_list(
                'question',
                'created_by_id',
                'pub_date'
                ),
           
            )
    }
    
    return JsonResponse(data)

def poll_detail(request,pk):
    poll= get_object_or_404(Poll, pk=pk)
    data = {
        "results":{
            "question" : poll.question,
            "created_by": poll.created_by_id,
            "pub_date": poll.pub_date,
        }
    }
    return JsonResponse(data)
