from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .factory import PlayerFactory, TeamFactory
from .models import PlayerModel, TeamModel


class TestTeam(APITestCase):
    """
	This class includes test cases for Team happy path.
	"""

    def setUp(self):
        """
		Setup function used to create temporary record for test cases.
		"""
        self.name = "CSK"
        self.club_state = "MP"
        self.team = []
        # Create multiple service plan object using loop.
        for _ in range(3):
            team = TeamFactory()
            self.team.append(
                {"pk": team.pk, "name": team.name, "club_state": team.club_state,}
            )
        self.team_list_url = reverse("team_list")
        self.team_detail_url = reverse("team_detail", args=[self.team[0]["pk"]])
        self.data = {
            "name": self.name,
            "club_state": self.club_state,
        }

    def test_team_list_all(self):
        """
		Test case for team list.
		"""
        response = self.client.get(self.team_list_url, {}, format="json")
        # Check status code for success url.
        assert response.status_code == status.HTTP_200_OK
        # Check length of response data with created data.
        assert len(response.data) == len(self.team)

    def test_team_create(self):
        """
		Test case for create team.
		"""
        response = self.client.post(self.team_list_url, data=self.data, format="json")
        # Check returned response is integer.
        assert type(response.data["id"]) == int
        # Check status code for success url.
        assert response.status_code == status.HTTP_201_CREATED
        team = TeamModel.objects.get(pk=response.data["id"])
        assert team.name == self.data["name"]
        assert team.club_state == self.data["club_state"]

    def test_team_detail(self):
        """
		Test case for team get detail.
		"""
        response = self.client.get(self.team_detail_url, {}, format="json")
        # Check status code for success url.
        assert response.status_code == status.HTTP_200_OK
        assert response.data["id"] == self.team[0]["pk"]

    def test_team_update(self):
        """
		Test case for update team.
		"""
        response = self.client.put(self.team_detail_url, data=self.data, format="json")
        # Check status code for success url.
        assert response.status_code == status.HTTP_200_OK
        # Check returned response is integer.
        assert type(response.data["id"]) == int
        team = TeamModel.objects.get(pk=response.data["id"])
        assert team.name == self.data["name"]
        assert team.club_state == self.data["club_state"]

    def test_team_delete(self):
        """
		Test case for team delete.
		"""
        response = self.client.delete(self.team_detail_url, {}, format="json")
        # Check status code for success url.
        assert response.status_code == status.HTTP_204_NO_CONTENT


class TestPlayer(APITestCase):
    """
	This class includes test cases for Player's happy path.
	"""

    def setUp(self):
        """
		Setup function used to create temporary record for test cases.
		"""
        self.first_name = "Rohit"
        self.last_name = "Thakur"
        self.country = "Indore"
        self.jersey_number = 111
        self.data = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "country": self.country,
            "jersey_number": self.jersey_number,
        }
        self.team = TeamFactory()
        # Creating multiple objects and appending into a list.
        self.player_list = []
        for _ in range(3):
            player = PlayerFactory(team=self.team,)
            self.player_list.append(
                {
                    "pk": player.pk,
                    "first_name": player.first_name,
                    "last_name": player.last_name,
                    "country": player.country,
                    "jersey_number": player.jersey_number,
                }
            )

        self.player_list_url = reverse("player_list", args=[self.team.id],)
        self.player_detail_url = reverse(
            "player_detail", args=[self.team.id, self.player_list[0]["pk"],],
        )

    def test_player_list_all(self):
        """
		Test case for player list.
		"""
        response = self.client.get(self.player_list_url, {}, format="json")
        # Check status code for success url.
        assert response.status_code == status.HTTP_200_OK
        # Check length of response data with created data.
        assert len(response.data) == len(self.player_list)

    def test_player_create(self):
        """
		Test case for create team.
		"""
        response = self.client.post(self.player_list_url, data=self.data, format="json")
        # Check returned response is integer.
        assert type(response.data["PlayerId"]) == int
        # Check status code for success url.
        assert response.status_code == status.HTTP_201_CREATED
        player = PlayerModel.objects.get(pk=response.data["PlayerId"])
        # Checking response data with created data in setup.
        assert player.first_name == self.data["first_name"]
        assert player.last_name == self.data["last_name"]
        assert player.country == self.data["country"]
        assert player.jersey_number == self.data["jersey_number"]

    def test_player_detail(self):
        """
		Test case for player get detail.
		"""
        response = self.client.get(self.player_detail_url, {}, format="json")
        # Check status code for success url.
        assert response.status_code == status.HTTP_200_OK
        assert response.data["id"] == self.player_list[0]["pk"]

    def test_player_update(self):
        """
		Test case for update player.
		"""
        response = self.client.put(
            self.player_detail_url, data=self.data, format="json"
        )

        # Check returned response is integer.
        assert type(response.data["PlayerId"]) == int
        # Check status code for success url.
        assert response.status_code == status.HTTP_200_OK
        player = PlayerModel.objects.get(pk=response.data["PlayerId"])
        assert player.first_name == self.data["first_name"]
        assert player.last_name == self.data["last_name"]
        assert player.country == self.data["country"]
        assert player.jersey_number == self.data["jersey_number"]

    def test_player_delete(self):
        """
		Test case for player delete.
		"""
        response = self.client.delete(self.player_detail_url, {}, format="json")
        # Check status code for success url.
        assert response.status_code == status.HTTP_204_NO_CONTENT
