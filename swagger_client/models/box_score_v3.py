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

from swagger_client.models.fantasy_defense_game import FantasyDefenseGame  # noqa: F401,E501
from swagger_client.models.player_game import PlayerGame  # noqa: F401,E501
from swagger_client.models.quarter import Quarter  # noqa: F401,E501
from swagger_client.models.score import Score  # noqa: F401,E501
from swagger_client.models.scoring_detail import ScoringDetail  # noqa: F401,E501
from swagger_client.models.scoring_play import ScoringPlay  # noqa: F401,E501
from swagger_client.models.team_game import TeamGame  # noqa: F401,E501


class BoxScoreV3(object):
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
        'score': 'Score',
        'quarters': 'list[Quarter]',
        'team_games': 'list[TeamGame]',
        'player_games': 'list[PlayerGame]',
        'fantasy_defense_games': 'list[FantasyDefenseGame]',
        'scoring_plays': 'list[ScoringPlay]',
        'scoring_details': 'list[ScoringDetail]'
    }

    attribute_map = {
        'score': 'Score',
        'quarters': 'Quarters',
        'team_games': 'TeamGames',
        'player_games': 'PlayerGames',
        'fantasy_defense_games': 'FantasyDefenseGames',
        'scoring_plays': 'ScoringPlays',
        'scoring_details': 'ScoringDetails'
    }

    def __init__(self, score=None, quarters=None, team_games=None, player_games=None, fantasy_defense_games=None, scoring_plays=None, scoring_details=None):  # noqa: E501
        """BoxScoreV3 - a model defined in Swagger"""  # noqa: E501

        self._score = None
        self._quarters = None
        self._team_games = None
        self._player_games = None
        self._fantasy_defense_games = None
        self._scoring_plays = None
        self._scoring_details = None
        self.discriminator = None

        if score is not None:
            self.score = score
        if quarters is not None:
            self.quarters = quarters
        if team_games is not None:
            self.team_games = team_games
        if player_games is not None:
            self.player_games = player_games
        if fantasy_defense_games is not None:
            self.fantasy_defense_games = fantasy_defense_games
        if scoring_plays is not None:
            self.scoring_plays = scoring_plays
        if scoring_details is not None:
            self.scoring_details = scoring_details

    @property
    def score(self):
        """Gets the score of this BoxScoreV3.  # noqa: E501


        :return: The score of this BoxScoreV3.  # noqa: E501
        :rtype: Score
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this BoxScoreV3.


        :param score: The score of this BoxScoreV3.  # noqa: E501
        :type: Score
        """

        self._score = score

    @property
    def quarters(self):
        """Gets the quarters of this BoxScoreV3.  # noqa: E501


        :return: The quarters of this BoxScoreV3.  # noqa: E501
        :rtype: list[Quarter]
        """
        return self._quarters

    @quarters.setter
    def quarters(self, quarters):
        """Sets the quarters of this BoxScoreV3.


        :param quarters: The quarters of this BoxScoreV3.  # noqa: E501
        :type: list[Quarter]
        """

        self._quarters = quarters

    @property
    def team_games(self):
        """Gets the team_games of this BoxScoreV3.  # noqa: E501


        :return: The team_games of this BoxScoreV3.  # noqa: E501
        :rtype: list[TeamGame]
        """
        return self._team_games

    @team_games.setter
    def team_games(self, team_games):
        """Sets the team_games of this BoxScoreV3.


        :param team_games: The team_games of this BoxScoreV3.  # noqa: E501
        :type: list[TeamGame]
        """

        self._team_games = team_games

    @property
    def player_games(self):
        """Gets the player_games of this BoxScoreV3.  # noqa: E501


        :return: The player_games of this BoxScoreV3.  # noqa: E501
        :rtype: list[PlayerGame]
        """
        return self._player_games

    @player_games.setter
    def player_games(self, player_games):
        """Sets the player_games of this BoxScoreV3.


        :param player_games: The player_games of this BoxScoreV3.  # noqa: E501
        :type: list[PlayerGame]
        """

        self._player_games = player_games

    @property
    def fantasy_defense_games(self):
        """Gets the fantasy_defense_games of this BoxScoreV3.  # noqa: E501


        :return: The fantasy_defense_games of this BoxScoreV3.  # noqa: E501
        :rtype: list[FantasyDefenseGame]
        """
        return self._fantasy_defense_games

    @fantasy_defense_games.setter
    def fantasy_defense_games(self, fantasy_defense_games):
        """Sets the fantasy_defense_games of this BoxScoreV3.


        :param fantasy_defense_games: The fantasy_defense_games of this BoxScoreV3.  # noqa: E501
        :type: list[FantasyDefenseGame]
        """

        self._fantasy_defense_games = fantasy_defense_games

    @property
    def scoring_plays(self):
        """Gets the scoring_plays of this BoxScoreV3.  # noqa: E501


        :return: The scoring_plays of this BoxScoreV3.  # noqa: E501
        :rtype: list[ScoringPlay]
        """
        return self._scoring_plays

    @scoring_plays.setter
    def scoring_plays(self, scoring_plays):
        """Sets the scoring_plays of this BoxScoreV3.


        :param scoring_plays: The scoring_plays of this BoxScoreV3.  # noqa: E501
        :type: list[ScoringPlay]
        """

        self._scoring_plays = scoring_plays

    @property
    def scoring_details(self):
        """Gets the scoring_details of this BoxScoreV3.  # noqa: E501


        :return: The scoring_details of this BoxScoreV3.  # noqa: E501
        :rtype: list[ScoringDetail]
        """
        return self._scoring_details

    @scoring_details.setter
    def scoring_details(self, scoring_details):
        """Sets the scoring_details of this BoxScoreV3.


        :param scoring_details: The scoring_details of this BoxScoreV3.  # noqa: E501
        :type: list[ScoringDetail]
        """

        self._scoring_details = scoring_details

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
        if issubclass(BoxScoreV3, dict):
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
        if not isinstance(other, BoxScoreV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
