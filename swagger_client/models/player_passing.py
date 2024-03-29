# coding: utf-8

"""
    NFL v3 Stats

    NFL rosters, player stats, team stats, and fantasy stats API.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PlayerPassing(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'player_game_id': 'int',
        'player_id': 'int',
        'short_name': 'str',
        'name': 'str',
        'team': 'str',
        'number': 'int',
        'position': 'str',
        'position_category': 'str',
        'fantasy_position': 'str',
        'fantasy_points': 'float',
        'updated': 'str',
        'passing_attempts': 'int',
        'passing_completions': 'int',
        'passing_yards': 'int',
        'passing_touchdowns': 'int',
        'passing_interceptions': 'int',
        'passing_long': 'int',
        'passing_sacks': 'int',
        'passing_sack_yards': 'int',
        'passing_completion_percentage': 'float',
        'passing_yards_per_attempt': 'float',
        'passing_yards_per_completion': 'float',
        'passing_rating': 'float',
        'two_point_conversion_passes': 'int',
        'fumbles_lost': 'int'
    }

    attribute_map = {
        'player_game_id': 'PlayerGameID',
        'player_id': 'PlayerID',
        'short_name': 'ShortName',
        'name': 'Name',
        'team': 'Team',
        'number': 'Number',
        'position': 'Position',
        'position_category': 'PositionCategory',
        'fantasy_position': 'FantasyPosition',
        'fantasy_points': 'FantasyPoints',
        'updated': 'Updated',
        'passing_attempts': 'PassingAttempts',
        'passing_completions': 'PassingCompletions',
        'passing_yards': 'PassingYards',
        'passing_touchdowns': 'PassingTouchdowns',
        'passing_interceptions': 'PassingInterceptions',
        'passing_long': 'PassingLong',
        'passing_sacks': 'PassingSacks',
        'passing_sack_yards': 'PassingSackYards',
        'passing_completion_percentage': 'PassingCompletionPercentage',
        'passing_yards_per_attempt': 'PassingYardsPerAttempt',
        'passing_yards_per_completion': 'PassingYardsPerCompletion',
        'passing_rating': 'PassingRating',
        'two_point_conversion_passes': 'TwoPointConversionPasses',
        'fumbles_lost': 'FumblesLost'
    }

    def __init__(self, player_game_id=None, player_id=None, short_name=None, name=None, team=None, number=None, position=None, position_category=None, fantasy_position=None, fantasy_points=None, updated=None, passing_attempts=None, passing_completions=None, passing_yards=None, passing_touchdowns=None, passing_interceptions=None, passing_long=None, passing_sacks=None, passing_sack_yards=None, passing_completion_percentage=None, passing_yards_per_attempt=None, passing_yards_per_completion=None, passing_rating=None, two_point_conversion_passes=None, fumbles_lost=None):  # noqa: E501
        """PlayerPassing - a model defined in Swagger"""  # noqa: E501

        self._player_game_id = None
        self._player_id = None
        self._short_name = None
        self._name = None
        self._team = None
        self._number = None
        self._position = None
        self._position_category = None
        self._fantasy_position = None
        self._fantasy_points = None
        self._updated = None
        self._passing_attempts = None
        self._passing_completions = None
        self._passing_yards = None
        self._passing_touchdowns = None
        self._passing_interceptions = None
        self._passing_long = None
        self._passing_sacks = None
        self._passing_sack_yards = None
        self._passing_completion_percentage = None
        self._passing_yards_per_attempt = None
        self._passing_yards_per_completion = None
        self._passing_rating = None
        self._two_point_conversion_passes = None
        self._fumbles_lost = None
        self.discriminator = None

        if player_game_id is not None:
            self.player_game_id = player_game_id
        if player_id is not None:
            self.player_id = player_id
        if short_name is not None:
            self.short_name = short_name
        if name is not None:
            self.name = name
        if team is not None:
            self.team = team
        if number is not None:
            self.number = number
        if position is not None:
            self.position = position
        if position_category is not None:
            self.position_category = position_category
        if fantasy_position is not None:
            self.fantasy_position = fantasy_position
        if fantasy_points is not None:
            self.fantasy_points = fantasy_points
        if updated is not None:
            self.updated = updated
        if passing_attempts is not None:
            self.passing_attempts = passing_attempts
        if passing_completions is not None:
            self.passing_completions = passing_completions
        if passing_yards is not None:
            self.passing_yards = passing_yards
        if passing_touchdowns is not None:
            self.passing_touchdowns = passing_touchdowns
        if passing_interceptions is not None:
            self.passing_interceptions = passing_interceptions
        if passing_long is not None:
            self.passing_long = passing_long
        if passing_sacks is not None:
            self.passing_sacks = passing_sacks
        if passing_sack_yards is not None:
            self.passing_sack_yards = passing_sack_yards
        if passing_completion_percentage is not None:
            self.passing_completion_percentage = passing_completion_percentage
        if passing_yards_per_attempt is not None:
            self.passing_yards_per_attempt = passing_yards_per_attempt
        if passing_yards_per_completion is not None:
            self.passing_yards_per_completion = passing_yards_per_completion
        if passing_rating is not None:
            self.passing_rating = passing_rating
        if two_point_conversion_passes is not None:
            self.two_point_conversion_passes = two_point_conversion_passes
        if fumbles_lost is not None:
            self.fumbles_lost = fumbles_lost

    @property
    def player_game_id(self):
        """Gets the player_game_id of this PlayerPassing.  # noqa: E501


        :return: The player_game_id of this PlayerPassing.  # noqa: E501
        :rtype: int
        """
        return self._player_game_id

    @player_game_id.setter
    def player_game_id(self, player_game_id):
        """Sets the player_game_id of this PlayerPassing.


        :param player_game_id: The player_game_id of this PlayerPassing.  # noqa: E501
        :type: int
        """

        self._player_game_id = player_game_id

    @property
    def player_id(self):
        """Gets the player_id of this PlayerPassing.  # noqa: E501


        :return: The player_id of this PlayerPassing.  # noqa: E501
        :rtype: int
        """
        return self._player_id

    @player_id.setter
    def player_id(self, player_id):
        """Sets the player_id of this PlayerPassing.


        :param player_id: The player_id of this PlayerPassing.  # noqa: E501
        :type: int
        """

        self._player_id = player_id

    @property
    def short_name(self):
        """Gets the short_name of this PlayerPassing.  # noqa: E501


        :return: The short_name of this PlayerPassing.  # noqa: E501
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this PlayerPassing.


        :param short_name: The short_name of this PlayerPassing.  # noqa: E501
        :type: str
        """

        self._short_name = short_name

    @property
    def name(self):
        """Gets the name of this PlayerPassing.  # noqa: E501


        :return: The name of this PlayerPassing.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PlayerPassing.


        :param name: The name of this PlayerPassing.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def team(self):
        """Gets the team of this PlayerPassing.  # noqa: E501


        :return: The team of this PlayerPassing.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this PlayerPassing.


        :param team: The team of this PlayerPassing.  # noqa: E501
        :type: str
        """

        self._team = team

    @property
    def number(self):
        """Gets the number of this PlayerPassing.  # noqa: E501


        :return: The number of this PlayerPassing.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this PlayerPassing.


        :param number: The number of this PlayerPassing.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def position(self):
        """Gets the position of this PlayerPassing.  # noqa: E501


        :return: The position of this PlayerPassing.  # noqa: E501
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this PlayerPassing.


        :param position: The position of this PlayerPassing.  # noqa: E501
        :type: str
        """

        self._position = position

    @property
    def position_category(self):
        """Gets the position_category of this PlayerPassing.  # noqa: E501


        :return: The position_category of this PlayerPassing.  # noqa: E501
        :rtype: str
        """
        return self._position_category

    @position_category.setter
    def position_category(self, position_category):
        """Sets the position_category of this PlayerPassing.


        :param position_category: The position_category of this PlayerPassing.  # noqa: E501
        :type: str
        """

        self._position_category = position_category

    @property
    def fantasy_position(self):
        """Gets the fantasy_position of this PlayerPassing.  # noqa: E501


        :return: The fantasy_position of this PlayerPassing.  # noqa: E501
        :rtype: str
        """
        return self._fantasy_position

    @fantasy_position.setter
    def fantasy_position(self, fantasy_position):
        """Sets the fantasy_position of this PlayerPassing.


        :param fantasy_position: The fantasy_position of this PlayerPassing.  # noqa: E501
        :type: str
        """

        self._fantasy_position = fantasy_position

    @property
    def fantasy_points(self):
        """Gets the fantasy_points of this PlayerPassing.  # noqa: E501


        :return: The fantasy_points of this PlayerPassing.  # noqa: E501
        :rtype: float
        """
        return self._fantasy_points

    @fantasy_points.setter
    def fantasy_points(self, fantasy_points):
        """Sets the fantasy_points of this PlayerPassing.


        :param fantasy_points: The fantasy_points of this PlayerPassing.  # noqa: E501
        :type: float
        """

        self._fantasy_points = fantasy_points

    @property
    def updated(self):
        """Gets the updated of this PlayerPassing.  # noqa: E501


        :return: The updated of this PlayerPassing.  # noqa: E501
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this PlayerPassing.


        :param updated: The updated of this PlayerPassing.  # noqa: E501
        :type: str
        """

        self._updated = updated

    @property
    def passing_attempts(self):
        """Gets the passing_attempts of this PlayerPassing.  # noqa: E501


        :return: The passing_attempts of this PlayerPassing.  # noqa: E501
        :rtype: int
        """
        return self._passing_attempts

    @passing_attempts.setter
    def passing_attempts(self, passing_attempts):
        """Sets the passing_attempts of this PlayerPassing.


        :param passing_attempts: The passing_attempts of this PlayerPassing.  # noqa: E501
        :type: int
        """

        self._passing_attempts = passing_attempts

    @property
    def passing_completions(self):
        """Gets the passing_completions of this PlayerPassing.  # noqa: E501


        :return: The passing_completions of this PlayerPassing.  # noqa: E501
        :rtype: int
        """
        return self._passing_completions

    @passing_completions.setter
    def passing_completions(self, passing_completions):
        """Sets the passing_completions of this PlayerPassing.


        :param passing_completions: The passing_completions of this PlayerPassing.  # noqa: E501
        :type: int
        """

        self._passing_completions = passing_completions

    @property
    def passing_yards(self):
        """Gets the passing_yards of this PlayerPassing.  # noqa: E501


        :return: The passing_yards of this PlayerPassing.  # noqa: E501
        :rtype: int
        """
        return self._passing_yards

    @passing_yards.setter
    def passing_yards(self, passing_yards):
        """Sets the passing_yards of this PlayerPassing.


        :param passing_yards: The passing_yards of this PlayerPassing.  # noqa: E501
        :type: int
        """

        self._passing_yards = passing_yards

    @property
    def passing_touchdowns(self):
        """Gets the passing_touchdowns of this PlayerPassing.  # noqa: E501


        :return: The passing_touchdowns of this PlayerPassing.  # noqa: E501
        :rtype: int
        """
        return self._passing_touchdowns

    @passing_touchdowns.setter
    def passing_touchdowns(self, passing_touchdowns):
        """Sets the passing_touchdowns of this PlayerPassing.


        :param passing_touchdowns: The passing_touchdowns of this PlayerPassing.  # noqa: E501
        :type: int
        """

        self._passing_touchdowns = passing_touchdowns

    @property
    def passing_interceptions(self):
        """Gets the passing_interceptions of this PlayerPassing.  # noqa: E501


        :return: The passing_interceptions of this PlayerPassing.  # noqa: E501
        :rtype: int
        """
        return self._passing_interceptions

    @passing_interceptions.setter
    def passing_interceptions(self, passing_interceptions):
        """Sets the passing_interceptions of this PlayerPassing.


        :param passing_interceptions: The passing_interceptions of this PlayerPassing.  # noqa: E501
        :type: int
        """

        self._passing_interceptions = passing_interceptions

    @property
    def passing_long(self):
        """Gets the passing_long of this PlayerPassing.  # noqa: E501


        :return: The passing_long of this PlayerPassing.  # noqa: E501
        :rtype: int
        """
        return self._passing_long

    @passing_long.setter
    def passing_long(self, passing_long):
        """Sets the passing_long of this PlayerPassing.


        :param passing_long: The passing_long of this PlayerPassing.  # noqa: E501
        :type: int
        """

        self._passing_long = passing_long

    @property
    def passing_sacks(self):
        """Gets the passing_sacks of this PlayerPassing.  # noqa: E501


        :return: The passing_sacks of this PlayerPassing.  # noqa: E501
        :rtype: int
        """
        return self._passing_sacks

    @passing_sacks.setter
    def passing_sacks(self, passing_sacks):
        """Sets the passing_sacks of this PlayerPassing.


        :param passing_sacks: The passing_sacks of this PlayerPassing.  # noqa: E501
        :type: int
        """

        self._passing_sacks = passing_sacks

    @property
    def passing_sack_yards(self):
        """Gets the passing_sack_yards of this PlayerPassing.  # noqa: E501


        :return: The passing_sack_yards of this PlayerPassing.  # noqa: E501
        :rtype: int
        """
        return self._passing_sack_yards

    @passing_sack_yards.setter
    def passing_sack_yards(self, passing_sack_yards):
        """Sets the passing_sack_yards of this PlayerPassing.


        :param passing_sack_yards: The passing_sack_yards of this PlayerPassing.  # noqa: E501
        :type: int
        """

        self._passing_sack_yards = passing_sack_yards

    @property
    def passing_completion_percentage(self):
        """Gets the passing_completion_percentage of this PlayerPassing.  # noqa: E501


        :return: The passing_completion_percentage of this PlayerPassing.  # noqa: E501
        :rtype: float
        """
        return self._passing_completion_percentage

    @passing_completion_percentage.setter
    def passing_completion_percentage(self, passing_completion_percentage):
        """Sets the passing_completion_percentage of this PlayerPassing.


        :param passing_completion_percentage: The passing_completion_percentage of this PlayerPassing.  # noqa: E501
        :type: float
        """

        self._passing_completion_percentage = passing_completion_percentage

    @property
    def passing_yards_per_attempt(self):
        """Gets the passing_yards_per_attempt of this PlayerPassing.  # noqa: E501


        :return: The passing_yards_per_attempt of this PlayerPassing.  # noqa: E501
        :rtype: float
        """
        return self._passing_yards_per_attempt

    @passing_yards_per_attempt.setter
    def passing_yards_per_attempt(self, passing_yards_per_attempt):
        """Sets the passing_yards_per_attempt of this PlayerPassing.


        :param passing_yards_per_attempt: The passing_yards_per_attempt of this PlayerPassing.  # noqa: E501
        :type: float
        """

        self._passing_yards_per_attempt = passing_yards_per_attempt

    @property
    def passing_yards_per_completion(self):
        """Gets the passing_yards_per_completion of this PlayerPassing.  # noqa: E501


        :return: The passing_yards_per_completion of this PlayerPassing.  # noqa: E501
        :rtype: float
        """
        return self._passing_yards_per_completion

    @passing_yards_per_completion.setter
    def passing_yards_per_completion(self, passing_yards_per_completion):
        """Sets the passing_yards_per_completion of this PlayerPassing.


        :param passing_yards_per_completion: The passing_yards_per_completion of this PlayerPassing.  # noqa: E501
        :type: float
        """

        self._passing_yards_per_completion = passing_yards_per_completion

    @property
    def passing_rating(self):
        """Gets the passing_rating of this PlayerPassing.  # noqa: E501


        :return: The passing_rating of this PlayerPassing.  # noqa: E501
        :rtype: float
        """
        return self._passing_rating

    @passing_rating.setter
    def passing_rating(self, passing_rating):
        """Sets the passing_rating of this PlayerPassing.


        :param passing_rating: The passing_rating of this PlayerPassing.  # noqa: E501
        :type: float
        """

        self._passing_rating = passing_rating

    @property
    def two_point_conversion_passes(self):
        """Gets the two_point_conversion_passes of this PlayerPassing.  # noqa: E501


        :return: The two_point_conversion_passes of this PlayerPassing.  # noqa: E501
        :rtype: int
        """
        return self._two_point_conversion_passes

    @two_point_conversion_passes.setter
    def two_point_conversion_passes(self, two_point_conversion_passes):
        """Sets the two_point_conversion_passes of this PlayerPassing.


        :param two_point_conversion_passes: The two_point_conversion_passes of this PlayerPassing.  # noqa: E501
        :type: int
        """

        self._two_point_conversion_passes = two_point_conversion_passes

    @property
    def fumbles_lost(self):
        """Gets the fumbles_lost of this PlayerPassing.  # noqa: E501


        :return: The fumbles_lost of this PlayerPassing.  # noqa: E501
        :rtype: int
        """
        return self._fumbles_lost

    @fumbles_lost.setter
    def fumbles_lost(self, fumbles_lost):
        """Sets the fumbles_lost of this PlayerPassing.


        :param fumbles_lost: The fumbles_lost of this PlayerPassing.  # noqa: E501
        :type: int
        """

        self._fumbles_lost = fumbles_lost

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PlayerPassing, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PlayerPassing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
