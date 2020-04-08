from factory import SubFactory, django, fuzzy

from .models import PlayerModel, TeamModel

# Minimum value.
min_value = 111111111111
# Maximum value.
max_value = 9999999999999


class TeamFactory(django.DjangoModelFactory):
    """
    Factory-boy for Team Model
    """

    class Meta:
        model = TeamModel

    pk = fuzzy.FuzzyInteger(min_value, max_value)
    name = fuzzy.FuzzyText(length=10)
    club_state = fuzzy.FuzzyText(length=10)


class PlayerFactory(django.DjangoModelFactory):
    """
    Factory-boy for Player Model.
    """

    class Meta:
        model = PlayerModel

    pk = fuzzy.FuzzyInteger(min_value, max_value)
    team = SubFactory(TeamFactory)
    first_name = fuzzy.FuzzyText(length=10)
    last_name = fuzzy.FuzzyText(length=10)
    country = fuzzy.FuzzyText(length=10)
    jersey_number = fuzzy.FuzzyInteger(min_value, max_value)
