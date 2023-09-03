from django.contrib import admin

from .models import (
    AhciCategory, AhciJournal, Ahci,
    Erih,
    JcrCategory, JcrJournal, JcrScore, JcrScoreMore, JcrGroup
)

admin.site.register(AhciCategory)
admin.site.register(AhciJournal)
admin.site.register(Ahci)
admin.site.register(Erih)
admin.site.register(JcrCategory)
admin.site.register(JcrJournal)
admin.site.register(JcrScore)
admin.site.register(JcrScoreMore)
admin.site.register(JcrGroup)
