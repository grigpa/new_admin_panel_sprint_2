from rest_framework import serializers

from ...models import FilmWork


class FilmWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmWork
        fields = '__all__'
