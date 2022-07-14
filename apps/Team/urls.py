from django.urls import path

from apps.Team.views import team_view

app_name = 'Team'

urlpatterns = [
    path('', team_view, name='team_view'),
]