from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Note
from .serializers import NoteSerializer
from django.conf import settings
from pymongo.errors import PyMongoError  # Import the error class to handle MongoDB errors

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def create(self, request, *args, **kwargs):
        # Save to SQLite AND MongoDB
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Save to SQLite
        self.perform_create(serializer)
        
        # Save to MongoDB
        try:
            notes_collection = settings.MONGO_DATABASE['notes']
            notes_collection.insert_one(request.data)
        except PyMongoError as e:
            # If MongoDB fails, handle the exception
            return Response(
                {'detail': f'MongoDB Error: {str(e)}'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
