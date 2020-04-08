from django.contrib import admin
from django.urls import path

from .views import (PlayerDetailView, PlayerListView, TeamDetailView,
                    TeamListView)

urlpatterns = [
    path("team/", TeamListView.as_view(), name="team_list"),
    path("team/<int:team_id>/", TeamDetailView.as_view(), name="team_detail"),
    path("team/<int:team_id>/player/", PlayerListView.as_view(), name="player_list"),
    path(
        "team/<int:team_id>/player/<int:player_id>/",
        PlayerDetailView.as_view(),
        name="player_detail",
    ),
]
