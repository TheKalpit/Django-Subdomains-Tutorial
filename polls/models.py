from django.db import models


class Poll(models.Model):
    content = models.CharField(max_length=128)

    def __str__(self):
        return self.content


class PollOption(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    value = models.CharField(max_length=128)

    def __str__(self):
        return self.value
