from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import PlayerModel, TeamModel
from .serializers import PlayerSerializer, TeamSerializer
from .services import (CreatePlayerService, DeletePlayerService,
                       DetailPlayerService, GetPlayerService,
                       UpdatePlayerService)


class TeamListView(APIView):
    """
	List all team, or create a new team.
	"""

    def get(self, request):
        team = TeamModel.objects.all()
        serializer = TeamSerializer(team, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeamDetailView(APIView):
    """
	Retrieve, update or delete a team instance.
	"""

    def get_object(self, team_id):
        try:
            return TeamModel.objects.get(pk=team_id)
        except TeamModel.DoesNotExist:
            raise Http404

    def get(self, request, team_id):
        team = self.get_object(team_id)
        serializer = TeamSerializer(team)
        return Response(serializer.data)

    def put(self, request, team_id):
        team = self.get_object(team_id)
        serializer = TeamSerializer(team, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, team_id):
        team = self.get_object(team_id)
        team.delete()
        return Response({"delete": "success"}, status=status.HTTP_204_NO_CONTENT)


class PlayerListView(APIView):
    """
	List all player, or create a new team.
	"""

    def get(self, request, team_id):
        try:
            player = GetPlayerService.execute({"team_id": team_id})

            serializer = PlayerSerializer(player, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except TeamModel.DoesNotExist:
            return Response(
                {"ERROR": "Invalid team_id -{}".format(team_id)},
                status.HTTP_404_NOT_FOUND,
            )

    def post(self, request, team_id):
        try:
            serializer = PlayerSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serialize_data = serializer.validated_data
                player_id = CreatePlayerService.execute(
                    {"team_id": team_id, "serialize_data": serialize_data}
                )
                return Response(
                    {"PlayerId": player_id}, status=status.HTTP_201_CREATED,
                )
        except TeamModel.DoesNotExist:
            return Response(
                {"ERROR": "Invalid team_id -{}".format(team_id)},
                status.HTTP_404_NOT_FOUND,
            )


class PlayerDetailView(APIView):
    """
	Retrieve, update or delete a player instance.
	"""

    def get(self, request, team_id, player_id):
        try:
            player = DetailPlayerService.execute(
                {"team_id": team_id, "player_id": player_id}
            )
            serializer = PlayerSerializer(player)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except PlayerModel.DoesNotExist:
            return Response(
                {"ERROR": "Invalid player_id- {}".format(player_id)},
                status.HTTP_404_NOT_FOUND,
            )
        except TeamModel.DoesNotExist:
            return Response(
                {"ERROR": "Invalid team_id -{}".format(team_id)},
                status.HTTP_404_NOT_FOUND,
            )

    def put(self, request, team_id, player_id):
        try:
            serializer = PlayerSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serialize_data = serializer.validated_data
                player_id = UpdatePlayerService.execute(
                    {
                        "team_id": team_id,
                        "serialize_data": serialize_data,
                        "player_id": player_id,
                    }
                )
                return Response(
                    {"PlayerId": player_id}, status=status.HTTP_200_OK,
                )
        except PlayerModel.DoesNotExist:
            return Response(
                {"ERROR": "Invalid player_id- {}".format(player_id)},
                status.HTTP_404_NOT_FOUND,
            )
        except TeamModel.DoesNotExist:
            return Response(
                {"ERROR": "Invalid team_id -{}".format(team_id)},
                status.HTTP_404_NOT_FOUND,
            )

    def delete(self, request, team_id, player_id):
        try:
            DeletePlayerService.execute(
                {"team_id": team_id, "player_id": player_id,}
            )
            return Response({"Delete": "success"}, status=status.HTTP_204_NO_CONTENT)
        except PlayerModel.DoesNotExist:
            return Response(
                {"ERROR": "Invalid player_id- {}".format(player_id)},
                status.HTTP_404_NOT_FOUND,
            )
        except TeamModel.DoesNotExist:
            return Response(
                {"ERROR": "Invalid team_id -{}".format(team_id)},
                status.HTTP_404_NOT_FOUND,
            )
