from .models import *
from .serializers import *
from rest_framework import generics

#obtenir une liste d'entites ou en creer ,autorise get et post
class PollList(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class=PollSerializer

#recuperer les details d'une entite , autorise get et destroy
class PollDetail(generics.RetrieveDestroyAPIView):
    queryset=Poll.objects.all()
    serializer_class= PollSerializer
    
    
class ChoiceList(generics.ListCreateAPIView):
    #queryset specifie l'ensemble des requetes initiales
    #serializer_class sera utiliser pour serialiser et deserialiser les donnees
    queryset=Choice.objects.all()
    serializer_class= ChoiceSerializer

#Permet de creer des entites
class CreateVote(generics.CreateAPIView):
    serializer_class= VoteSerializer
    
