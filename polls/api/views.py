from rest_framework import viewsets

from polls.api.serializers import PollSerializer
from polls.models import Poll


class PollViewSet(viewsets.ModelViewSet):
    serializer_class = PollSerializer
    queryset = Poll.objects
