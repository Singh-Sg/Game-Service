from rest_framework import serializers

from .models import PlayerModel, TeamModel


class TeamSerializer(serializers.ModelSerializer):
    """
	"""

    class Meta:
        model = TeamModel
        fields = "__all__"

    def create(self, validated_data):
        """
		Create and return a new `Team` instance, given the validated data.
		"""
        return TeamModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
	    Update and return an existing `Team` instance, given the validated data.
	    """
        instance.name = validated_data.get("name", instance.name)
        instance.club_state = validated_data.get("club_state", instance.club_state)
        instance.save()
        return instance


class PlayerSerializer(serializers.ModelSerializer):
    """
	"""

    team = serializers.IntegerField(required=False, source="team_id")

    class Meta:
        model = PlayerModel
        fields = "__all__"

    def update(self, instance, validated_data):
        """
	    Update and return an existing `Player` instance, given the validated data.
	    """
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.jersey_number = validated_data.get(
            "jersey_number", instance.jersey_number
        )
        instance.country = validated_data.get("country", instance.country)
        instance.save()
        return instance
