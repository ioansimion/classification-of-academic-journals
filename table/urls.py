from django.urls import path

from . import views

app_name = 'table'

urlpatterns = [
    path("base/", views.base, name="base"),
    path("home/", views.home, name="home"),

    path("ahci/", views.ahci, name="ahci"),
    path("erih/", views.erih, name="erih"),
    path("jcr/scores/", views.jcr_scores, name="jcr_scores"),
    path("jcr/scores/more/", views.jcr_scores_more, name="jcr_scores_more"),
    path("jcr/groups/", views.jcr_groups, name="jcr_groups"),

    path("jcr/detail/<int:journal_id>/", views.jcr_journal_detail, name="jcr_journal_detail"),
]
