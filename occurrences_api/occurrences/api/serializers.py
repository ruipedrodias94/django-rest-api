from rest_framework import serializers
from occurrences.models import OccurrenceModel


class OccurrenceSerializer(serializers.ModelSerializer):
    """
    Occurrence Serializer
    - It shows all the fields in the Occurrence
    """

    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = OccurrenceModel
        fields = '__all__'

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_absolute_url(request)
