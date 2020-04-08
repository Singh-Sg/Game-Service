from service_objects.services import Service

from .models import PlayerModel, TeamModel


class GetPlayerService(Service):
    """
    Return team players
	"""

    def process(self):
        team_id = self.data.get("team_id")
        players = PlayerModel.objects.filter(team_id=team_id)
        return players


class CreatePlayerService(Service):
    """
    Create Players
	"""

    def process(self):
        team = TeamModel.objects.get(pk=self.data.get("team_id"))
        first_name = self.data.get("serialize_data")["first_name"]
        last_name = self.data.get("serialize_data")["last_name"]
        jersey_number = self.data.get("serialize_data")["jersey_number"]
        country = self.data.get("serialize_data")["country"]

        # Creating player instance by given data.
        player = PlayerModel.objects.create(
            first_name=first_name,
            last_name=last_name,
            jersey_number=jersey_number,
            country=country,
            team=team,
        )
        return player.id


class DetailPlayerService(Service):
    """
    Get players details
	"""

    def process(self):
        team_id = self.data.get("team_id")
        player_id = self.data.get("player_id")
        players = PlayerModel.objects.get(team_id=team_id, pk=player_id)
        return players


class UpdatePlayerService(Service):
    """
    Update player details
	"""

    def process(self):
        team = TeamModel.objects.get(pk=self.data.get("team_id"))
        player_id = self.data.get("player_id")
        player = PlayerModel.objects.get(pk=player_id, team=team)
        player.first_name = self.data.get("serialize_data")["first_name"]
        player.last_name = self.data.get("serialize_data")["last_name"]
        player.jersey_number = self.data.get("serialize_data")["jersey_number"]
        player.country = self.data.get("serialize_data")["country"]
        player.save()
        return player.id


class DeletePlayerService(Service):
    """
    Delete Players
	"""

    def process(self):
        team_id = self.data.get("team_id")
        player_id = self.data.get("player_id")
        player = PlayerModel.objects.get(pk=player_id, team_id=team_id)
        player.delete()
