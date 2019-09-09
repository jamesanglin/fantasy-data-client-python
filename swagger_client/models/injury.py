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


class Injury(object):
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
        'injury_id': 'int',
        'season_type': 'int',
        'season': 'int',
        'week': 'int',
        'player_id': 'int',
        'name': 'str',
        'position': 'str',
        'number': 'int',
        'team': 'str',
        'opponent': 'str',
        'body_part': 'str',
        'status': 'str',
        'practice': 'str',
        'practice_description': 'str',
        'updated': 'str',
        'declared_inactive': 'bool',
        'team_id': 'int',
        'opponent_id': 'int'
    }

    attribute_map = {
        'injury_id': 'InjuryID',
        'season_type': 'SeasonType',
        'season': 'Season',
        'week': 'Week',
        'player_id': 'PlayerID',
        'name': 'Name',
        'position': 'Position',
        'number': 'Number',
        'team': 'Team',
        'opponent': 'Opponent',
        'body_part': 'BodyPart',
        'status': 'Status',
        'practice': 'Practice',
        'practice_description': 'PracticeDescription',
        'updated': 'Updated',
        'declared_inactive': 'DeclaredInactive',
        'team_id': 'TeamID',
        'opponent_id': 'OpponentID'
    }

    def __init__(self, injury_id=None, season_type=None, season=None, week=None, player_id=None, name=None, position=None, number=None, team=None, opponent=None, body_part=None, status=None, practice=None, practice_description=None, updated=None, declared_inactive=None, team_id=None, opponent_id=None):  # noqa: E501
        """Injury - a model defined in Swagger"""  # noqa: E501

        self._injury_id = None
        self._season_type = None
        self._season = None
        self._week = None
        self._player_id = None
        self._name = None
        self._position = None
        self._number = None
        self._team = None
        self._opponent = None
        self._body_part = None
        self._status = None
        self._practice = None
        self._practice_description = None
        self._updated = None
        self._declared_inactive = None
        self._team_id = None
        self._opponent_id = None
        self.discriminator = None

        if injury_id is not None:
            self.injury_id = injury_id
        if season_type is not None:
            self.season_type = season_type
        if season is not None:
            self.season = season
        if week is not None:
            self.week = week
        if player_id is not None:
            self.player_id = player_id
        if name is not None:
            self.name = name
        if position is not None:
            self.position = position
        if number is not None:
            self.number = number
        if team is not None:
            self.team = team
        if opponent is not None:
            self.opponent = opponent
        if body_part is not None:
            self.body_part = body_part
        if status is not None:
            self.status = status
        if practice is not None:
            self.practice = practice
        if practice_description is not None:
            self.practice_description = practice_description
        if updated is not None:
            self.updated = updated
        if declared_inactive is not None:
            self.declared_inactive = declared_inactive
        if team_id is not None:
            self.team_id = team_id
        if opponent_id is not None:
            self.opponent_id = opponent_id

    @property
    def injury_id(self):
        """Gets the injury_id of this Injury.  # noqa: E501


        :return: The injury_id of this Injury.  # noqa: E501
        :rtype: int
        """
        return self._injury_id

    @injury_id.setter
    def injury_id(self, injury_id):
        """Sets the injury_id of this Injury.


        :param injury_id: The injury_id of this Injury.  # noqa: E501
        :type: int
        """

        self._injury_id = injury_id

    @property
    def season_type(self):
        """Gets the season_type of this Injury.  # noqa: E501


        :return: The season_type of this Injury.  # noqa: E501
        :rtype: int
        """
        return self._season_type

    @season_type.setter
    def season_type(self, season_type):
        """Sets the season_type of this Injury.


        :param season_type: The season_type of this Injury.  # noqa: E501
        :type: int
        """

        self._season_type = season_type

    @property
    def season(self):
        """Gets the season of this Injury.  # noqa: E501


        :return: The season of this Injury.  # noqa: E501
        :rtype: int
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this Injury.


        :param season: The season of this Injury.  # noqa: E501
        :type: int
        """

        self._season = season

    @property
    def week(self):
        """Gets the week of this Injury.  # noqa: E501


        :return: The week of this Injury.  # noqa: E501
        :rtype: int
        """
        return self._week

    @week.setter
    def week(self, week):
        """Sets the week of this Injury.


        :param week: The week of this Injury.  # noqa: E501
        :type: int
        """

        self._week = week

    @property
    def player_id(self):
        """Gets the player_id of this Injury.  # noqa: E501


        :return: The player_id of this Injury.  # noqa: E501
        :rtype: int
        """
        return self._player_id

    @player_id.setter
    def player_id(self, player_id):
        """Sets the player_id of this Injury.


        :param player_id: The player_id of this Injury.  # noqa: E501
        :type: int
        """

        self._player_id = player_id

    @property
    def name(self):
        """Gets the name of this Injury.  # noqa: E501


        :return: The name of this Injury.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Injury.


        :param name: The name of this Injury.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def position(self):
        """Gets the position of this Injury.  # noqa: E501


        :return: The position of this Injury.  # noqa: E501
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this Injury.


        :param position: The position of this Injury.  # noqa: E501
        :type: str
        """

        self._position = position

    @property
    def number(self):
        """Gets the number of this Injury.  # noqa: E501


        :return: The number of this Injury.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this Injury.


        :param number: The number of this Injury.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def team(self):
        """Gets the team of this Injury.  # noqa: E501


        :return: The team of this Injury.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this Injury.


        :param team: The team of this Injury.  # noqa: E501
        :type: str
        """

        self._team = team

    @property
    def opponent(self):
        """Gets the opponent of this Injury.  # noqa: E501


        :return: The opponent of this Injury.  # noqa: E501
        :rtype: str
        """
        return self._opponent

    @opponent.setter
    def opponent(self, opponent):
        """Sets the opponent of this Injury.


        :param opponent: The opponent of this Injury.  # noqa: E501
        :type: str
        """

        self._opponent = opponent

    @property
    def body_part(self):
        """Gets the body_part of this Injury.  # noqa: E501


        :return: The body_part of this Injury.  # noqa: E501
        :rtype: str
        """
        return self._body_part

    @body_part.setter
    def body_part(self, body_part):
        """Sets the body_part of this Injury.


        :param body_part: The body_part of this Injury.  # noqa: E501
        :type: str
        """

        self._body_part = body_part

    @property
    def status(self):
        """Gets the status of this Injury.  # noqa: E501


        :return: The status of this Injury.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Injury.


        :param status: The status of this Injury.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def practice(self):
        """Gets the practice of this Injury.  # noqa: E501


        :return: The practice of this Injury.  # noqa: E501
        :rtype: str
        """
        return self._practice

    @practice.setter
    def practice(self, practice):
        """Sets the practice of this Injury.


        :param practice: The practice of this Injury.  # noqa: E501
        :type: str
        """

        self._practice = practice

    @property
    def practice_description(self):
        """Gets the practice_description of this Injury.  # noqa: E501


        :return: The practice_description of this Injury.  # noqa: E501
        :rtype: str
        """
        return self._practice_description

    @practice_description.setter
    def practice_description(self, practice_description):
        """Sets the practice_description of this Injury.


        :param practice_description: The practice_description of this Injury.  # noqa: E501
        :type: str
        """

        self._practice_description = practice_description

    @property
    def updated(self):
        """Gets the updated of this Injury.  # noqa: E501


        :return: The updated of this Injury.  # noqa: E501
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this Injury.


        :param updated: The updated of this Injury.  # noqa: E501
        :type: str
        """

        self._updated = updated

    @property
    def declared_inactive(self):
        """Gets the declared_inactive of this Injury.  # noqa: E501


        :return: The declared_inactive of this Injury.  # noqa: E501
        :rtype: bool
        """
        return self._declared_inactive

    @declared_inactive.setter
    def declared_inactive(self, declared_inactive):
        """Sets the declared_inactive of this Injury.


        :param declared_inactive: The declared_inactive of this Injury.  # noqa: E501
        :type: bool
        """

        self._declared_inactive = declared_inactive

    @property
    def team_id(self):
        """Gets the team_id of this Injury.  # noqa: E501


        :return: The team_id of this Injury.  # noqa: E501
        :rtype: int
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this Injury.


        :param team_id: The team_id of this Injury.  # noqa: E501
        :type: int
        """

        self._team_id = team_id

    @property
    def opponent_id(self):
        """Gets the opponent_id of this Injury.  # noqa: E501


        :return: The opponent_id of this Injury.  # noqa: E501
        :rtype: int
        """
        return self._opponent_id

    @opponent_id.setter
    def opponent_id(self, opponent_id):
        """Sets the opponent_id of this Injury.


        :param opponent_id: The opponent_id of this Injury.  # noqa: E501
        :type: int
        """

        self._opponent_id = opponent_id

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
        if issubclass(Injury, dict):
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
        if not isinstance(other, Injury):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other