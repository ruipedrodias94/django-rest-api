from rest_framework import generics, permissions, mixins
import django_filters.rest_framework
from occurrences.models import OccurrenceModel
from .serializers import OccurrenceSerializer
from .permissions import IsAdminUserOrReadOnly


class OccurrenceUpdateView(generics.RetrieveUpdateAPIView):
    """
    OccurrenceUpdateView
    - Allows the Listing and update of occurrences
    - METHODS: GET, PUT
    """
    lookup_field = 'pk'
    queryset = OccurrenceModel.objects.all()
    serializer_class = OccurrenceSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

    # def get_queryset(self):
    #   query_set = OccurrenceModel.objects.all()
    #  query = self.request.GET.get("")


class OccurrenceCreateAndView(generics.ListAPIView, mixins.CreateModelMixin):
    """
    OccurrenceCreateAndView
    - Allows the creation and the listing of new occurrences
    - METHODS: POST, GET
    """
    lookup_field = 'pk'
    queryset = OccurrenceModel.objects.all()
    serializer_class = OccurrenceSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['user', 'category', ]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}
