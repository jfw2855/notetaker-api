from django.shortcuts import render
#for initial setup testing
#from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer


# for initial setup testing
# def getRoutes(request):
#     return JsonResponse('test works',safe=False)


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)

#Gets all notes data
@api_view(['GET'])
def getNotes(request):
    #grabs all notes form psql
    notes = Note.objects.all()
    #serializes the python dicts into JSON
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


#Gets single note data
@api_view(['GET'])
def getNote(request,pk):
    #filters for note pk
    note = Note.objects.get(id=pk)
    #serializes the python dict into JSON
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

#Updates single note
@api_view(['PUT'])
def updateNote(request,pk):
    data = request.data
    note = Note.objects.get(id=pk)
    seralizer = NoteSerializer(instance=note,data=data)
    if seralizer.is_valid():
        seralizer.save()
    return Response(seralizer.data)
