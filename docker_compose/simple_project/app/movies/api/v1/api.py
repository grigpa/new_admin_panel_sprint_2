from h11 import Response

from rest_framework import viewsets, permissions, generics, status

from .serializers import FilmWorkSerializer
from ...models import FilmWork


class FilmWorkViewSet(viewsets.ModelViewSet):
    queryset = FilmWork.objects.all()
    serializer_class = FilmWorkSerializer
    permission_classes = [permissions.AllowAny]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)