from rest_framework import viewsets
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer
from django.conf import settings

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def create(self, request):
        # Save to SQLite AND MongoDB
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Save to SQLite
        self.perform_create(serializer)
        
        # Save to MongoDB
        notes_collection = settings.MONGO_DATABASE['notes']
        notes_collection.insert_one(request.data)
        
        return Response(serializer.data)