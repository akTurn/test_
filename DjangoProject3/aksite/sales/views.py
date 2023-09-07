
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Office
from .serializers import OfficeSerializer

class OfficeViewSet(viewsets.ModelViewSet):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
    #lookup_field = 'pk'  # Use the primary key for lookups

    def update(self, request, *args, **kwargs):
        # Your update logic here
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        # Your delete logic here
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




