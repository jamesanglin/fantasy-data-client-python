# coding: utf-8

"""
    NFL v3 Stats

    NFL rosters, player stats, team stats, and fantasy stats API.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.default_api import DefaultApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_are_games_in_progress(self):
        """Test case for are_games_in_progress

        Are Games In Progress  # noqa: E501
        """
        pass

    def test_box_score_by_scoreid_v(self):
        """Test case for box_score_by_scoreid_v

        Box Score by ScoreID V3  # noqa: E501
        """
        pass

    def test_box_score_v(self):
        """Test case for box_score_v

        Box Score V3  # noqa: E501
        """
        pass

    def test_box_scores_delta_v(self):
        """Test case for box_scores_delta_v

        Box Scores Delta V3  # noqa: E501
        """
        pass

    def test_box_scores_v_simulation(self):
        """Test case for box_scores_v_simulation

        Box Scores V3 Simulation  # noqa: E501
        """
        pass

    def test_bye_weeks(self):
        """Test case for bye_weeks

        Bye Weeks  # noqa: E501
        """
        pass

    def test_daily_fantasy_players(self):
        """Test case for daily_fantasy_players

        Daily Fantasy Players  # noqa: E501
        """
        pass

    def test_daily_fantasy_scoring(self):
        """Test case for daily_fantasy_scoring

        Daily Fantasy Scoring  # noqa: E501
        """
        pass

    def test_dfs_slates_by_date(self):
        """Test case for dfs_slates_by_date

        DFS Slates by Date  # noqa: E501
        """
        pass

    def test_dfs_slates_by_week(self):
        """Test case for dfs_slates_by_week

        DFS Slates by Week  # noqa: E501
        """
        pass

    def test_fantasy_defense_game_stats(self):
        """Test case for fantasy_defense_game_stats

        Fantasy Defense Game Stats  # noqa: E501
        """
        pass

    def test_fantasy_defense_game_stats_by_team(self):
        """Test case for fantasy_defense_game_stats_by_team

        Fantasy Defense Game Stats by Team  # noqa: E501
        """
        pass

    def test_fantasy_defense_season_stats(self):
        """Test case for fantasy_defense_season_stats

        Fantasy Defense Season Stats  # noqa: E501
        """
        pass

    def test_fantasy_defense_season_stats_by_team(self):
        """Test case for fantasy_defense_season_stats_by_team

        Fantasy Defense Season Stats by Team  # noqa: E501
        """
        pass

    def test_fantasy_player_ownership_percentages_season_long(self):
        """Test case for fantasy_player_ownership_percentages_season_long

        Fantasy Player Ownership Percentages (Season-Long)  # noqa: E501
        """
        pass

    def test_fantasy_players_with_adp(self):
        """Test case for fantasy_players_with_adp

        Fantasy Players with ADP  # noqa: E501
        """
        pass

    def test_game_stats_by_season_deprecated_use_team_game_stats_instead(self):
        """Test case for game_stats_by_season_deprecated_use_team_game_stats_instead

        Game Stats by Season (Deprecated, use Team Game Stats instead)  # noqa: E501
        """
        pass

    def test_game_stats_by_week_deprecated_use_team_game_stats_instead(self):
        """Test case for game_stats_by_week_deprecated_use_team_game_stats_instead

        Game Stats by Week (Deprecated, use Team Game Stats instead)  # noqa: E501
        """
        pass

    def test_idp_fantasy_players_with_adp(self):
        """Test case for idp_fantasy_players_with_adp

        IDP Fantasy Players with ADP  # noqa: E501
        """
        pass

    def test_injuries(self):
        """Test case for injuries

        Injuries  # noqa: E501
        """
        pass

    def test_injuries_by_team(self):
        """Test case for injuries_by_team

        Injuries by Team  # noqa: E501
        """
        pass

    def test_league_leaders_by_season(self):
        """Test case for league_leaders_by_season

        League Leaders by Season  # noqa: E501
        """
        pass

    def test_league_leaders_by_week(self):
        """Test case for league_leaders_by_week

        League Leaders by Week  # noqa: E501
        """
        pass

    def test_legacy_box_score(self):
        """Test case for legacy_box_score

        Legacy Box Score  # noqa: E501
        """
        pass

    def test_legacy_box_scores(self):
        """Test case for legacy_box_scores

        Legacy Box Scores  # noqa: E501
        """
        pass

    def test_legacy_box_scores_active(self):
        """Test case for legacy_box_scores_active

        Legacy Box Scores Active  # noqa: E501
        """
        pass

    def test_legacy_box_scores_delta(self):
        """Test case for legacy_box_scores_delta

        Legacy Box Scores Delta  # noqa: E501
        """
        pass

    def test_legacy_box_scores_delta_current_week(self):
        """Test case for legacy_box_scores_delta_current_week

        Legacy Box Scores Delta (Current Week)  # noqa: E501
        """
        pass

    def test_legacy_box_scores_final(self):
        """Test case for legacy_box_scores_final

        Legacy Box Scores Final  # noqa: E501
        """
        pass

    def test_legacy_box_scores_live(self):
        """Test case for legacy_box_scores_live

        Legacy Box Scores Live  # noqa: E501
        """
        pass

    def test_news(self):
        """Test case for news

        News  # noqa: E501
        """
        pass

    def test_news_by_date(self):
        """Test case for news_by_date

        News by Date  # noqa: E501
        """
        pass

    def test_news_by_player(self):
        """Test case for news_by_player

        News by Player  # noqa: E501
        """
        pass

    def test_news_by_team(self):
        """Test case for news_by_team

        News by Team  # noqa: E501
        """
        pass

    def test_player_details_by_available(self):
        """Test case for player_details_by_available

        Player Details by Available  # noqa: E501
        """
        pass

    def test_player_details_by_free_agents(self):
        """Test case for player_details_by_free_agents

        Player Details by Free Agents  # noqa: E501
        """
        pass

    def test_player_details_by_player(self):
        """Test case for player_details_by_player

        Player Details by Player  # noqa: E501
        """
        pass

    def test_player_details_by_rookie_draft_year(self):
        """Test case for player_details_by_rookie_draft_year

        Player Details by Rookie Draft Year  # noqa: E501
        """
        pass

    def test_player_details_by_team(self):
        """Test case for player_details_by_team

        Player Details by Team  # noqa: E501
        """
        pass

    def test_player_game_red_zone_stats(self):
        """Test case for player_game_red_zone_stats

        Player Game Red Zone Stats  # noqa: E501
        """
        pass

    def test_player_game_red_zone_stats_inside_five(self):
        """Test case for player_game_red_zone_stats_inside_five

        Player Game Red Zone Stats Inside Five  # noqa: E501
        """
        pass

    def test_player_game_red_zone_stats_inside_ten(self):
        """Test case for player_game_red_zone_stats_inside_ten

        Player Game Red Zone Stats Inside Ten  # noqa: E501
        """
        pass

    def test_player_game_stats_by_player(self):
        """Test case for player_game_stats_by_player

        Player Game Stats by Player  # noqa: E501
        """
        pass

    def test_player_game_stats_by_team(self):
        """Test case for player_game_stats_by_team

        Player Game Stats by Team  # noqa: E501
        """
        pass

    def test_player_game_stats_by_week(self):
        """Test case for player_game_stats_by_week

        Player Game Stats by Week  # noqa: E501
        """
        pass

    def test_player_game_stats_by_week_delta(self):
        """Test case for player_game_stats_by_week_delta

        Player Game Stats by Week Delta  # noqa: E501
        """
        pass

    def test_player_game_stats_delta(self):
        """Test case for player_game_stats_delta

        Player Game Stats Delta  # noqa: E501
        """
        pass

    def test_player_season_red_zone_stats(self):
        """Test case for player_season_red_zone_stats

        Player Season Red Zone Stats  # noqa: E501
        """
        pass

    def test_player_season_red_zone_stats_inside_five(self):
        """Test case for player_season_red_zone_stats_inside_five

        Player Season Red Zone Stats Inside Five  # noqa: E501
        """
        pass

    def test_player_season_red_zone_stats_inside_ten(self):
        """Test case for player_season_red_zone_stats_inside_ten

        Player Season Red Zone Stats Inside Ten  # noqa: E501
        """
        pass

    def test_player_season_stats(self):
        """Test case for player_season_stats

        Player Season Stats  # noqa: E501
        """
        pass

    def test_player_season_stats_by_player(self):
        """Test case for player_season_stats_by_player

        Player Season Stats by Player  # noqa: E501
        """
        pass

    def test_player_season_stats_by_team(self):
        """Test case for player_season_stats_by_team

        Player Season Stats by Team  # noqa: E501
        """
        pass

    def test_player_season_third_down_stats(self):
        """Test case for player_season_third_down_stats

        Player Season Third Down Stats  # noqa: E501
        """
        pass

    def test_pro_bowlers(self):
        """Test case for pro_bowlers

        Pro Bowlers  # noqa: E501
        """
        pass

    def test_schedule(self):
        """Test case for schedule

        Schedule  # noqa: E501
        """
        pass

    def test_scores_by_season(self):
        """Test case for scores_by_season

        Scores by Season   # noqa: E501
        """
        pass

    def test_scores_by_week(self):
        """Test case for scores_by_week

        Scores by Week  # noqa: E501
        """
        pass

    def test_scores_by_week_simulation(self):
        """Test case for scores_by_week_simulation

        Scores by Week Simulation  # noqa: E501
        """
        pass

    def test_season_current(self):
        """Test case for season_current

        Season Current  # noqa: E501
        """
        pass

    def test_season_last_completed(self):
        """Test case for season_last_completed

        Season Last Completed  # noqa: E501
        """
        pass

    def test_season_upcoming(self):
        """Test case for season_upcoming

        Season Upcoming  # noqa: E501
        """
        pass

    def test_stadiums(self):
        """Test case for stadiums

        Stadiums  # noqa: E501
        """
        pass

    def test_standings(self):
        """Test case for standings

        Standings  # noqa: E501
        """
        pass

    def test_team_game_stats(self):
        """Test case for team_game_stats

        Team Game Stats  # noqa: E501
        """
        pass

    def test_team_season_stats(self):
        """Test case for team_season_stats

        Team Season Stats  # noqa: E501
        """
        pass

    def test_teams_active(self):
        """Test case for teams_active

        Teams (Active)  # noqa: E501
        """
        pass

    def test_teams_all(self):
        """Test case for teams_all

        Teams (All)  # noqa: E501
        """
        pass

    def test_teams_by_season(self):
        """Test case for teams_by_season

        Teams by Season  # noqa: E501
        """
        pass

    def test_timeframes(self):
        """Test case for timeframes

        Timeframes  # noqa: E501
        """
        pass

    def test_week_current(self):
        """Test case for week_current

        Week Current  # noqa: E501
        """
        pass

    def test_week_last_completed(self):
        """Test case for week_last_completed

        Week Last Completed  # noqa: E501
        """
        pass

    def test_week_upcoming(self):
        """Test case for week_upcoming

        Week Upcoming  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()