from django.views import generic

from polls.models import Poll


class PollListView(generic.ListView):
    model = Poll
