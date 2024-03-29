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


class PlayerPunting(object):
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
        'punts': 'int',
        'punt_average': 'float',
        'punt_inside20': 'int',
        'punt_touchbacks': 'int',
        'punt_yards': 'int'
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
        'punts': 'Punts',
        'punt_average': 'PuntAverage',
        'punt_inside20': 'PuntInside20',
        'punt_touchbacks': 'PuntTouchbacks',
        'punt_yards': 'PuntYards'
    }

    def __init__(self, player_game_id=None, player_id=None, short_name=None, name=None, team=None, number=None, position=None, position_category=None, fantasy_position=None, fantasy_points=None, updated=None, punts=None, punt_average=None, punt_inside20=None, punt_touchbacks=None, punt_yards=None):  # noqa: E501
        """PlayerPunting - a model defined in Swagger"""  # noqa: E501

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
        self._punts = None
        self._punt_average = None
        self._punt_inside20 = None
        self._punt_touchbacks = None
        self._punt_yards = None
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
        if punts is not None:
            self.punts = punts
        if punt_average is not None:
            self.punt_average = punt_average
        if punt_inside20 is not None:
            self.punt_inside20 = punt_inside20
        if punt_touchbacks is not None:
            self.punt_touchbacks = punt_touchbacks
        if punt_yards is not None:
            self.punt_yards = punt_yards

    @property
    def player_game_id(self):
        """Gets the player_game_id of this PlayerPunting.  # noqa: E501


        :return: The player_game_id of this PlayerPunting.  # noqa: E501
        :rtype: int
        """
        return self._player_game_id

    @player_game_id.setter
    def player_game_id(self, player_game_id):
        """Sets the player_game_id of this PlayerPunting.


        :param player_game_id: The player_game_id of this PlayerPunting.  # noqa: E501
        :type: int
        """

        self._player_game_id = player_game_id

    @property
    def player_id(self):
        """Gets the player_id of this PlayerPunting.  # noqa: E501


        :return: The player_id of this PlayerPunting.  # noqa: E501
        :rtype: int
        """
        return self._player_id

    @player_id.setter
    def player_id(self, player_id):
        """Sets the player_id of this PlayerPunting.


        :param player_id: The player_id of this PlayerPunting.  # noqa: E501
        :type: int
        """

        self._player_id = player_id

    @property
    def short_name(self):
        """Gets the short_name of this PlayerPunting.  # noqa: E501


        :return: The short_name of this PlayerPunting.  # noqa: E501
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this PlayerPunting.


        :param short_name: The short_name of this PlayerPunting.  # noqa: E501
        :type: str
        """

        self._short_name = short_name

    @property
    def name(self):
        """Gets the name of this PlayerPunting.  # noqa: E501


        :return: The name of this PlayerPunting.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PlayerPunting.


        :param name: The name of this PlayerPunting.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def team(self):
        """Gets the team of this PlayerPunting.  # noqa: E501


        :return: The team of this PlayerPunting.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this PlayerPunting.


        :param team: The team of this PlayerPunting.  # noqa: E501
        :type: str
        """

        self._team = team

    @property
    def number(self):
        """Gets the number of this PlayerPunting.  # noqa: E501


        :return: The number of this PlayerPunting.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this PlayerPunting.


        :param number: The number of this PlayerPunting.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def position(self):
        """Gets the position of this PlayerPunting.  # noqa: E501


        :return: The position of this PlayerPunting.  # noqa: E501
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this PlayerPunting.


        :param position: The position of this PlayerPunting.  # noqa: E501
        :type: str
        """

        self._position = position

    @property
    def position_category(self):
        """Gets the position_category of this PlayerPunting.  # noqa: E501


        :return: The position_category of this PlayerPunting.  # noqa: E501
        :rtype: str
        """
        return self._position_category

    @position_category.setter
    def position_category(self, position_category):
        """Sets the position_category of this PlayerPunting.


        :param position_category: The position_category of this PlayerPunting.  # noqa: E501
        :type: str
        """

        self._position_category = position_category

    @property
    def fantasy_position(self):
        """Gets the fantasy_position of this PlayerPunting.  # noqa: E501


        :return: The fantasy_position of this PlayerPunting.  # noqa: E501
        :rtype: str
        """
        return self._fantasy_position

    @fantasy_position.setter
    def fantasy_position(self, fantasy_position):
        """Sets the fantasy_position of this PlayerPunting.


        :param fantasy_position: The fantasy_position of this PlayerPunting.  # noqa: E501
        :type: str
        """

        self._fantasy_position = fantasy_position

    @property
    def fantasy_points(self):
        """Gets the fantasy_points of this PlayerPunting.  # noqa: E501


        :return: The fantasy_points of this PlayerPunting.  # noqa: E501
        :rtype: float
        """
        return self._fantasy_points

    @fantasy_points.setter
    def fantasy_points(self, fantasy_points):
        """Sets the fantasy_points of this PlayerPunting.


        :param fantasy_points: The fantasy_points of this PlayerPunting.  # noqa: E501
        :type: float
        """

        self._fantasy_points = fantasy_points

    @property
    def updated(self):
        """Gets the updated of this PlayerPunting.  # noqa: E501


        :return: The updated of this PlayerPunting.  # noqa: E501
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this PlayerPunting.


        :param updated: The updated of this PlayerPunting.  # noqa: E501
        :type: str
        """

        self._updated = updated

    @property
    def punts(self):
        """Gets the punts of this PlayerPunting.  # noqa: E501


        :return: The punts of this PlayerPunting.  # noqa: E501
        :rtype: int
        """
        return self._punts

    @punts.setter
    def punts(self, punts):
        """Sets the punts of this PlayerPunting.


        :param punts: The punts of this PlayerPunting.  # noqa: E501
        :type: int
        """

        self._punts = punts

    @property
    def punt_average(self):
        """Gets the punt_average of this PlayerPunting.  # noqa: E501


        :return: The punt_average of this PlayerPunting.  # noqa: E501
        :rtype: float
        """
        return self._punt_average

    @punt_average.setter
    def punt_average(self, punt_average):
        """Sets the punt_average of this PlayerPunting.


        :param punt_average: The punt_average of this PlayerPunting.  # noqa: E501
        :type: float
        """

        self._punt_average = punt_average

    @property
    def punt_inside20(self):
        """Gets the punt_inside20 of this PlayerPunting.  # noqa: E501


        :return: The punt_inside20 of this PlayerPunting.  # noqa: E501
        :rtype: int
        """
        return self._punt_inside20

    @punt_inside20.setter
    def punt_inside20(self, punt_inside20):
        """Sets the punt_inside20 of this PlayerPunting.


        :param punt_inside20: The punt_inside20 of this PlayerPunting.  # noqa: E501
        :type: int
        """

        self._punt_inside20 = punt_inside20

    @property
    def punt_touchbacks(self):
        """Gets the punt_touchbacks of this PlayerPunting.  # noqa: E501


        :return: The punt_touchbacks of this PlayerPunting.  # noqa: E501
        :rtype: int
        """
        return self._punt_touchbacks

    @punt_touchbacks.setter
    def punt_touchbacks(self, punt_touchbacks):
        """Sets the punt_touchbacks of this PlayerPunting.


        :param punt_touchbacks: The punt_touchbacks of this PlayerPunting.  # noqa: E501
        :type: int
        """

        self._punt_touchbacks = punt_touchbacks

    @property
    def punt_yards(self):
        """Gets the punt_yards of this PlayerPunting.  # noqa: E501


        :return: The punt_yards of this PlayerPunting.  # noqa: E501
        :rtype: int
        """
        return self._punt_yards

    @punt_yards.setter
    def punt_yards(self, punt_yards):
        """Sets the punt_yards of this PlayerPunting.


        :param punt_yards: The punt_yards of this PlayerPunting.  # noqa: E501
        :type: int
        """

        self._punt_yards = punt_yards

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
        if issubclass(PlayerPunting, dict):
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
        if not isinstance(other, PlayerPunting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
