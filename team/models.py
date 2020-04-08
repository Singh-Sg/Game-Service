from django.db import models


class TeamModel(models.Model):
    """
    Model for football team
    """

    name = models.CharField(max_length=50)
    club_state = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PlayerModel(models.Model):
    """
    Model for football playes
    """

    team = models.ForeignKey(TeamModel, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    jersey_number = models.IntegerField()
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name
