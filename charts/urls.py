from django.urls import path

from . import views

app_name = 'charts'

urlpatterns = [
    path("ahci/", views.ahci, name="ahci"),
    path("erih/", views.erih, name="erih"),
    path("jcr/scores/", views.jcr_scores, name="jcr_scores"),
]
