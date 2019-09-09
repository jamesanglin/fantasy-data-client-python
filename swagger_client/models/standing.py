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


class Standing(object):
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
        'season_type': 'int',
        'season': 'int',
        'conference': 'str',
        'division': 'str',
        'team': 'str',
        'name': 'str',
        'wins': 'int',
        'losses': 'int',
        'ties': 'int',
        'percentage': 'float',
        'points_for': 'int',
        'points_against': 'int',
        'net_points': 'int',
        'touchdowns': 'int',
        'division_wins': 'int',
        'division_losses': 'int',
        'conference_wins': 'int',
        'conference_losses': 'int',
        'team_id': 'int',
        'division_ties': 'int',
        'conference_ties': 'int',
        'global_team_id': 'int'
    }

    attribute_map = {
        'season_type': 'SeasonType',
        'season': 'Season',
        'conference': 'Conference',
        'division': 'Division',
        'team': 'Team',
        'name': 'Name',
        'wins': 'Wins',
        'losses': 'Losses',
        'ties': 'Ties',
        'percentage': 'Percentage',
        'points_for': 'PointsFor',
        'points_against': 'PointsAgainst',
        'net_points': 'NetPoints',
        'touchdowns': 'Touchdowns',
        'division_wins': 'DivisionWins',
        'division_losses': 'DivisionLosses',
        'conference_wins': 'ConferenceWins',
        'conference_losses': 'ConferenceLosses',
        'team_id': 'TeamID',
        'division_ties': 'DivisionTies',
        'conference_ties': 'ConferenceTies',
        'global_team_id': 'GlobalTeamID'
    }

    def __init__(self, season_type=None, season=None, conference=None, division=None, team=None, name=None, wins=None, losses=None, ties=None, percentage=None, points_for=None, points_against=None, net_points=None, touchdowns=None, division_wins=None, division_losses=None, conference_wins=None, conference_losses=None, team_id=None, division_ties=None, conference_ties=None, global_team_id=None):  # noqa: E501
        """Standing - a model defined in Swagger"""  # noqa: E501

        self._season_type = None
        self._season = None
        self._conference = None
        self._division = None
        self._team = None
        self._name = None
        self._wins = None
        self._losses = None
        self._ties = None
        self._percentage = None
        self._points_for = None
        self._points_against = None
        self._net_points = None
        self._touchdowns = None
        self._division_wins = None
        self._division_losses = None
        self._conference_wins = None
        self._conference_losses = None
        self._team_id = None
        self._division_ties = None
        self._conference_ties = None
        self._global_team_id = None
        self.discriminator = None

        if season_type is not None:
            self.season_type = season_type
        if season is not None:
            self.season = season
        if conference is not None:
            self.conference = conference
        if division is not None:
            self.division = division
        if team is not None:
            self.team = team
        if name is not None:
            self.name = name
        if wins is not None:
            self.wins = wins
        if losses is not None:
            self.losses = losses
        if ties is not None:
            self.ties = ties
        if percentage is not None:
            self.percentage = percentage
        if points_for is not None:
            self.points_for = points_for
        if points_against is not None:
            self.points_against = points_against
        if net_points is not None:
            self.net_points = net_points
        if touchdowns is not None:
            self.touchdowns = touchdowns
        if division_wins is not None:
            self.division_wins = division_wins
        if division_losses is not None:
            self.division_losses = division_losses
        if conference_wins is not None:
            self.conference_wins = conference_wins
        if conference_losses is not None:
            self.conference_losses = conference_losses
        if team_id is not None:
            self.team_id = team_id
        if division_ties is not None:
            self.division_ties = division_ties
        if conference_ties is not None:
            self.conference_ties = conference_ties
        if global_team_id is not None:
            self.global_team_id = global_team_id

    @property
    def season_type(self):
        """Gets the season_type of this Standing.  # noqa: E501


        :return: The season_type of this Standing.  # noqa: E501
        :rtype: int
        """
        return self._season_type

    @season_type.setter
    def season_type(self, season_type):
        """Sets the season_type of this Standing.


        :param season_type: The season_type of this Standing.  # noqa: E501
        :type: int
        """

        self._season_type = season_type

    @property
    def season(self):
        """Gets the season of this Standing.  # noqa: E501


        :return: The season of this Standing.  # noqa: E501
        :rtype: int
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this Standing.


        :param season: The season of this Standing.  # noqa: E501
        :type: int
        """

        self._season = season

    @property
    def conference(self):
        """Gets the conference of this Standing.  # noqa: E501


        :return: The conference of this Standing.  # noqa: E501
        :rtype: str
        """
        return self._conference

    @conference.setter
    def conference(self, conference):
        """Sets the conference of this Standing.


        :param conference: The conference of this Standing.  # noqa: E501
        :type: str
        """

        self._conference = conference

    @property
    def division(self):
        """Gets the division of this Standing.  # noqa: E501


        :return: The division of this Standing.  # noqa: E501
        :rtype: str
        """
        return self._division

    @division.setter
    def division(self, division):
        """Sets the division of this Standing.


        :param division: The division of this Standing.  # noqa: E501
        :type: str
        """

        self._division = division

    @property
    def team(self):
        """Gets the team of this Standing.  # noqa: E501


        :return: The team of this Standing.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this Standing.


        :param team: The team of this Standing.  # noqa: E501
        :type: str
        """

        self._team = team

    @property
    def name(self):
        """Gets the name of this Standing.  # noqa: E501


        :return: The name of this Standing.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Standing.


        :param name: The name of this Standing.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def wins(self):
        """Gets the wins of this Standing.  # noqa: E501


        :return: The wins of this Standing.  # noqa: E501
        :rtype: int
        """
        return self._wins

    @wins.setter
    def wins(self, wins):
        """Sets the wins of this Standing.


        :param wins: The wins of this Standing.  # noqa: E501
        :type: int
        """

        self._wins = wins

    @property
    def losses(self):
        """Gets the losses of this Standing.  # noqa: E501


        :return: The losses of this Standing.  # noqa: E501
        :rtype: int
        """
        return self._losses

    @losses.setter
    def losses(self, losses):
        """Sets the losses of this Standing.


        :param losses: The losses of this Standing.  # noqa: E501
        :type: int
        """

        self._losses = losses

    @property
    def ties(self):
        """Gets the ties of this Standing.  # noqa: E501


        :return: The ties of this Standing.  # noqa: E501
        :rtype: int
        """
        return self._ties

    @ties.setter
    def ties(self, ties):
        """Sets the ties of this Standing.


        :param ties: The ties of this Standing.  # noqa: E501
        :type: int
        """

        self._ties = ties

    @property
    def percentage(self):
        """Gets the percentage of this Standing.  # noqa: E501


        :return: The percentage of this Standing.  # noqa: E501
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this Standing.


        :param percentage: The percentage of this Standing.  # noqa: E501
        :type: float
        """

        self._percentage = percentage

    @property
    def points_for(self):
        """Gets the points_for of this Standing.  # noqa: E501


        :return: The points_for of this Standing.  # noqa: E501
        :rtype: int
        """
        return self._points_for

    @points_for.setter
    def points_for(self, points_for):
        """Sets the points_for of this Standing.


        :param points_for: The points_for of this Standing.  # noqa: E501
        :type: int
        """

        self._points_for = points_for

    @property
    def points_against(self):
        """Gets the points_against of this Standing.  # noqa: E501


        :return: The points_against of this Standing.  # noqa: E501
        :rtype: int
        """
        return self._points_against

    @points_against.setter
    def points_against(self, points_against):
        """Sets the points_against of this Standing.


        :param points_against: The points_against of this Standing.  # noqa: E501
        :type: int
        """

        self._points_against = points_against

    @property
    def net_points(self):
        """Gets the net_points of this Standing.  # noqa: E501


        :return: The net_points of this Standing.  # noqa: E501
        :rtype: int
        """
        return self._net_points

    @net_points.setter
    def net_points(self, net_points):
        """Sets the net_points of this Standing.


        :param net_points: The net_points of this Standing.  # noqa: E501
        :type: int
        """

        self._net_points = net_points

    @property
    def touchdowns(self):
        """Gets the touchdowns of this Standing.  # noqa: E501


        :return: The touchdowns of this Standing.  # noqa: E501
        :rtype: int
        """
        return self._touchdowns

    @touchdowns.setter
    def touchdowns(self, touchdowns):
        """Sets the touchdowns of this Standing.


        :param touchdowns: The touchdowns of this Standing.  # noqa: E501
        :type: int
        """

        self._touchdowns = touchdowns

    @property
    def division_wins(self):
        """Gets the division_wins of this Standing.  # noqa: E501


        :return: The division_wins of this Standing.  # noqa: E501
        :rtype: int
        """
        return self._division_wins

    @division_wins.setter
    def division_wins(self, division_wins):
        """Sets the division_wins of this Standing.


        :param division_wins: The division_wins of this Standing.  # noqa: E501
        :type: int
        """

        self._division_wins = division_wins

    @property
    def division_losses(self):
        """Gets the division_losses of this Standing.  # noqa: E501


        :return: The division_losses of this Standing.  # noqa: E501
        :rtype: int
        """
        return self._division_losses

    @division_losses.setter
    def division_losses(self, division_losses):
        """Sets the division_losses of this Standing.


        :param division_losses: The division_losses of this Standing.  # noqa: E501
        :type: int
        """

        self._division_losses = division_losses

    @property
    def conference_wins(self):
        """Gets the conference_wins of this Standing.  # noqa: E501


        :return: The conference_wins of this Standing.  # noqa: E501
        :rtype: int
        """
        return self._conference_wins

    @conference_wins.setter
    def conference_wins(self, conference_wins):
        """Sets the conference_wins of this Standing.


        :param conference_wins: The conference_wins of this Standing.  # noqa: E501
        :type: int
        """

        self._conference_wins = conference_wins

    @property
    def conference_losses(self):
        """Gets the conference_losses of this Standing.  # noqa: E501


        :return: The conference_losses of this Standing.  # noqa: E501
        :rtype: int
        """
        return self._conference_losses

    @conference_losses.setter
    def conference_losses(self, conference_losses):
        """Sets the conference_losses of this Standing.


        :param conference_losses: The conference_losses of this Standing.  # noqa: E501
        :type: int
        """

        self._conference_losses = conference_losses

    @property
    def team_id(self):
        """Gets the team_id of this Standing.  # noqa: E501


        :return: The team_id of this Standing.  # noqa: E501
        :rtype: int
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this Standing.


        :param team_id: The team_id of this Standing.  # noqa: E501
        :type: int
        """

        self._team_id = team_id

    @property
    def division_ties(self):
        """Gets the division_ties of this Standing.  # noqa: E501


        :return: The division_ties of this Standing.  # noqa: E501
        :rtype: int
        """
        return self._division_ties

    @division_ties.setter
    def division_ties(self, division_ties):
        """Sets the division_ties of this Standing.


        :param division_ties: The division_ties of this Standing.  # noqa: E501
        :type: int
        """

        self._division_ties = division_ties

    @property
    def conference_ties(self):
        """Gets the conference_ties of this Standing.  # noqa: E501


        :return: The conference_ties of this Standing.  # noqa: E501
        :rtype: int
        """
        return self._conference_ties

    @conference_ties.setter
    def conference_ties(self, conference_ties):
        """Sets the conference_ties of this Standing.


        :param conference_ties: The conference_ties of this Standing.  # noqa: E501
        :type: int
        """

        self._conference_ties = conference_ties

    @property
    def global_team_id(self):
        """Gets the global_team_id of this Standing.  # noqa: E501


        :return: The global_team_id of this Standing.  # noqa: E501
        :rtype: int
        """
        return self._global_team_id

    @global_team_id.setter
    def global_team_id(self, global_team_id):
        """Sets the global_team_id of this Standing.


        :param global_team_id: The global_team_id of this Standing.  # noqa: E501
        :type: int
        """

        self._global_team_id = global_team_id

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
        if issubclass(Standing, dict):
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
        if not isinstance(other, Standing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
