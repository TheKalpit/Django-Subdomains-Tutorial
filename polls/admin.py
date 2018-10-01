from django.contrib import admin

from polls.models import PollOption, Poll


class PollOptionInline(admin.TabularInline):
    model = PollOption
    fields = ('value',)


class PollAdmin(admin.ModelAdmin):
    inlines = (PollOptionInline,)


admin.site.register(Poll, PollAdmin)
