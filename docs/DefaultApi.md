# swagger_client.DefaultApi

All URIs are relative to *http://api.sportsdata.io/v3/nfl/stats*

Method | HTTP request | Description
------------- | ------------- | -------------
[**are_games_in_progress**](DefaultApi.md#are_games_in_progress) | **GET** /{format}/AreAnyGamesInProgress | Are Games In Progress
[**box_score_by_scoreid_v**](DefaultApi.md#box_score_by_scoreid_v) | **GET** /{format}/BoxScoreByScoreIDV3/{scoreid} | Box Score by ScoreID V3
[**box_score_v**](DefaultApi.md#box_score_v) | **GET** /{format}/BoxScoreV3/{season}/{week}/{hometeam} | Box Score V3
[**box_scores_delta_v**](DefaultApi.md#box_scores_delta_v) | **GET** /{format}/BoxScoresDeltaV3/{season}/{week}/{playerstoinclude}/{minutes} | Box Scores Delta V3
[**box_scores_v_simulation**](DefaultApi.md#box_scores_v_simulation) | **GET** /{format}/SimulatedBoxScoresV3/{numberofplays} | Box Scores V3 Simulation
[**bye_weeks**](DefaultApi.md#bye_weeks) | **GET** /{format}/Byes/{season} | Bye Weeks
[**daily_fantasy_players**](DefaultApi.md#daily_fantasy_players) | **GET** /{format}/DailyFantasyPlayers/{date} | Daily Fantasy Players
[**daily_fantasy_scoring**](DefaultApi.md#daily_fantasy_scoring) | **GET** /{format}/DailyFantasyPoints/{date} | Daily Fantasy Scoring
[**dfs_slates_by_date**](DefaultApi.md#dfs_slates_by_date) | **GET** /{format}/DfsSlatesByDate/{date} | DFS Slates by Date
[**dfs_slates_by_week**](DefaultApi.md#dfs_slates_by_week) | **GET** /{format}/DfsSlatesByWeek/{season}/{week} | DFS Slates by Week
[**fantasy_defense_game_stats**](DefaultApi.md#fantasy_defense_game_stats) | **GET** /{format}/FantasyDefenseByGame/{season}/{week} | Fantasy Defense Game Stats
[**fantasy_defense_game_stats_by_team**](DefaultApi.md#fantasy_defense_game_stats_by_team) | **GET** /{format}/FantasyDefenseByGameByTeam/{season}/{week}/{team} | Fantasy Defense Game Stats by Team
[**fantasy_defense_season_stats**](DefaultApi.md#fantasy_defense_season_stats) | **GET** /{format}/FantasyDefenseBySeason/{season} | Fantasy Defense Season Stats
[**fantasy_defense_season_stats_by_team**](DefaultApi.md#fantasy_defense_season_stats_by_team) | **GET** /{format}/FantasyDefenseBySeasonByTeam/{season}/{team} | Fantasy Defense Season Stats by Team
[**fantasy_player_ownership_percentages_season_long**](DefaultApi.md#fantasy_player_ownership_percentages_season_long) | **GET** /{format}/PlayerOwnership/{season}/{week} | Fantasy Player Ownership Percentages (Season-Long)
[**fantasy_players_with_adp**](DefaultApi.md#fantasy_players_with_adp) | **GET** /{format}/FantasyPlayers | Fantasy Players with ADP
[**game_stats_by_season_deprecated_use_team_game_stats_instead**](DefaultApi.md#game_stats_by_season_deprecated_use_team_game_stats_instead) | **GET** /{format}/GameStats/{season} | Game Stats by Season (Deprecated, use Team Game Stats instead)
[**game_stats_by_week_deprecated_use_team_game_stats_instead**](DefaultApi.md#game_stats_by_week_deprecated_use_team_game_stats_instead) | **GET** /{format}/GameStatsByWeek/{season}/{week} | Game Stats by Week (Deprecated, use Team Game Stats instead)
[**idp_fantasy_players_with_adp**](DefaultApi.md#idp_fantasy_players_with_adp) | **GET** /{format}/FantasyPlayersIDP | IDP Fantasy Players with ADP
[**injuries**](DefaultApi.md#injuries) | **GET** /{format}/Injuries/{season}/{week} | Injuries
[**injuries_by_team**](DefaultApi.md#injuries_by_team) | **GET** /{format}/Injuries/{season}/{week}/{team} | Injuries by Team
[**league_leaders_by_season**](DefaultApi.md#league_leaders_by_season) | **GET** /{format}/SeasonLeagueLeaders/{season}/{position}/{column} | League Leaders by Season
[**league_leaders_by_week**](DefaultApi.md#league_leaders_by_week) | **GET** /{format}/GameLeagueLeaders/{season}/{week}/{position}/{column} | League Leaders by Week
[**legacy_box_score**](DefaultApi.md#legacy_box_score) | **GET** /{format}/BoxScore/{season}/{week}/{hometeam} | Legacy Box Score
[**legacy_box_scores**](DefaultApi.md#legacy_box_scores) | **GET** /{format}/BoxScores/{season}/{week} | Legacy Box Scores
[**legacy_box_scores_active**](DefaultApi.md#legacy_box_scores_active) | **GET** /{format}/ActiveBoxScores | Legacy Box Scores Active
[**legacy_box_scores_delta**](DefaultApi.md#legacy_box_scores_delta) | **GET** /{format}/BoxScoresDelta/{season}/{week}/{minutes} | Legacy Box Scores Delta
[**legacy_box_scores_delta_current_week**](DefaultApi.md#legacy_box_scores_delta_current_week) | **GET** /{format}/RecentlyUpdatedBoxScores/{minutes} | Legacy Box Scores Delta (Current Week)
[**legacy_box_scores_final**](DefaultApi.md#legacy_box_scores_final) | **GET** /{format}/FinalBoxScores | Legacy Box Scores Final
[**legacy_box_scores_live**](DefaultApi.md#legacy_box_scores_live) | **GET** /{format}/LiveBoxScores | Legacy Box Scores Live
[**news**](DefaultApi.md#news) | **GET** /{format}/News | News
[**news_by_date**](DefaultApi.md#news_by_date) | **GET** /{format}/NewsByDate/{date} | News by Date
[**news_by_player**](DefaultApi.md#news_by_player) | **GET** /{format}/NewsByPlayerID/{playerid} | News by Player
[**news_by_team**](DefaultApi.md#news_by_team) | **GET** /{format}/NewsByTeam/{team} | News by Team
[**player_details_by_available**](DefaultApi.md#player_details_by_available) | **GET** /{format}/Players | Player Details by Available
[**player_details_by_free_agents**](DefaultApi.md#player_details_by_free_agents) | **GET** /{format}/FreeAgents | Player Details by Free Agents
[**player_details_by_player**](DefaultApi.md#player_details_by_player) | **GET** /{format}/Player/{playerid} | Player Details by Player
[**player_details_by_rookie_draft_year**](DefaultApi.md#player_details_by_rookie_draft_year) | **GET** /{format}/Rookies/{season} | Player Details by Rookie Draft Year
[**player_details_by_team**](DefaultApi.md#player_details_by_team) | **GET** /{format}/Players/{team} | Player Details by Team
[**player_game_red_zone_stats**](DefaultApi.md#player_game_red_zone_stats) | **GET** /{format}/PlayerGameRedZoneStats/{season}/{week} | Player Game Red Zone Stats
[**player_game_red_zone_stats_inside_five**](DefaultApi.md#player_game_red_zone_stats_inside_five) | **GET** /{format}/PlayerGameRedZoneInsideFiveStats/{season}/{week} | Player Game Red Zone Stats Inside Five
[**player_game_red_zone_stats_inside_ten**](DefaultApi.md#player_game_red_zone_stats_inside_ten) | **GET** /{format}/PlayerGameRedZoneInsideTenStats/{season}/{week} | Player Game Red Zone Stats Inside Ten
[**player_game_stats_by_player**](DefaultApi.md#player_game_stats_by_player) | **GET** /{format}/PlayerGameStatsByPlayerID/{season}/{week}/{playerid} | Player Game Stats by Player
[**player_game_stats_by_team**](DefaultApi.md#player_game_stats_by_team) | **GET** /{format}/PlayerGameStatsByTeam/{season}/{week}/{team} | Player Game Stats by Team
[**player_game_stats_by_week**](DefaultApi.md#player_game_stats_by_week) | **GET** /{format}/PlayerGameStatsByWeek/{season}/{week} | Player Game Stats by Week
[**player_game_stats_by_week_delta**](DefaultApi.md#player_game_stats_by_week_delta) | **GET** /{format}/PlayerGameStatsByWeekDelta/{season}/{week}/{minutes} | Player Game Stats by Week Delta
[**player_game_stats_delta**](DefaultApi.md#player_game_stats_delta) | **GET** /{format}/PlayerGameStatsDelta/{minutes} | Player Game Stats Delta
[**player_season_red_zone_stats**](DefaultApi.md#player_season_red_zone_stats) | **GET** /{format}/PlayerSeasonRedZoneStats/{season} | Player Season Red Zone Stats
[**player_season_red_zone_stats_inside_five**](DefaultApi.md#player_season_red_zone_stats_inside_five) | **GET** /{format}/PlayerSeasonRedZoneInsideFiveStats/{season} | Player Season Red Zone Stats Inside Five
[**player_season_red_zone_stats_inside_ten**](DefaultApi.md#player_season_red_zone_stats_inside_ten) | **GET** /{format}/PlayerSeasonRedZoneInsideTenStats/{season} | Player Season Red Zone Stats Inside Ten
[**player_season_stats**](DefaultApi.md#player_season_stats) | **GET** /{format}/PlayerSeasonStats/{season} | Player Season Stats
[**player_season_stats_by_player**](DefaultApi.md#player_season_stats_by_player) | **GET** /{format}/PlayerSeasonStatsByPlayerID/{season}/{playerid} | Player Season Stats by Player
[**player_season_stats_by_team**](DefaultApi.md#player_season_stats_by_team) | **GET** /{format}/PlayerSeasonStatsByTeam/{season}/{team} | Player Season Stats by Team
[**player_season_third_down_stats**](DefaultApi.md#player_season_third_down_stats) | **GET** /{format}/PlayerSeasonThirdDownStats/{season} | Player Season Third Down Stats
[**pro_bowlers**](DefaultApi.md#pro_bowlers) | **GET** /{format}/ProBowlers/{season} | Pro Bowlers
[**schedule**](DefaultApi.md#schedule) | **GET** /{format}/Schedules/{season} | Schedule
[**scores_by_season**](DefaultApi.md#scores_by_season) | **GET** /{format}/Scores/{season} | Scores by Season 
[**scores_by_week**](DefaultApi.md#scores_by_week) | **GET** /{format}/ScoresByWeek/{season}/{week} | Scores by Week
[**scores_by_week_simulation**](DefaultApi.md#scores_by_week_simulation) | **GET** /{format}/SimulatedScores/{numberofplays} | Scores by Week Simulation
[**season_current**](DefaultApi.md#season_current) | **GET** /{format}/CurrentSeason | Season Current
[**season_last_completed**](DefaultApi.md#season_last_completed) | **GET** /{format}/LastCompletedSeason | Season Last Completed
[**season_upcoming**](DefaultApi.md#season_upcoming) | **GET** /{format}/UpcomingSeason | Season Upcoming
[**stadiums**](DefaultApi.md#stadiums) | **GET** /{format}/Stadiums | Stadiums
[**standings**](DefaultApi.md#standings) | **GET** /{format}/Standings/{season} | Standings
[**team_game_stats**](DefaultApi.md#team_game_stats) | **GET** /{format}/TeamGameStats/{season}/{week} | Team Game Stats
[**team_season_stats**](DefaultApi.md#team_season_stats) | **GET** /{format}/TeamSeasonStats/{season} | Team Season Stats
[**teams_active**](DefaultApi.md#teams_active) | **GET** /{format}/Teams | Teams (Active)
[**teams_all**](DefaultApi.md#teams_all) | **GET** /{format}/AllTeams | Teams (All)
[**teams_by_season**](DefaultApi.md#teams_by_season) | **GET** /{format}/Teams/{season} | Teams by Season
[**timeframes**](DefaultApi.md#timeframes) | **GET** /{format}/Timeframes/{type} | Timeframes
[**week_current**](DefaultApi.md#week_current) | **GET** /{format}/CurrentWeek | Week Current
[**week_last_completed**](DefaultApi.md#week_last_completed) | **GET** /{format}/LastCompletedWeek | Week Last Completed
[**week_upcoming**](DefaultApi.md#week_upcoming) | **GET** /{format}/UpcomingWeek | Week Upcoming


# **are_games_in_progress**
> bool are_games_in_progress(format)

Are Games In Progress

Returns <code>true</code> if there is at least one game being played at the time of the request or <code>false</code> if there are none.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.

try:
    # Are Games In Progress
    api_response = api_instance.are_games_in_progress(format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->are_games_in_progress: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 

### Return type

**bool**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **box_score_by_scoreid_v**
> BoxScoreV3 box_score_by_scoreid_v(format, scoreid)

Box Score by ScoreID V3

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
scoreid = 'scoreid_example' # str | The ScoreID of the game. Possible values include: <code>16247</code>, <code>16245</code>, etc.

try:
    # Box Score by ScoreID V3
    api_response = api_instance.box_score_by_scoreid_v(format, scoreid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->box_score_by_scoreid_v: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **scoreid** | **str**| The ScoreID of the game. Possible values include: &lt;code&gt;16247&lt;/code&gt;, &lt;code&gt;16245&lt;/code&gt;, etc. | 

### Return type

[**BoxScoreV3**](BoxScoreV3.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **box_score_v**
> BoxScoreV3 box_score_v(format, season, week, hometeam)

Box Score V3

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
season = 'season_example' # str | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
week = 'week_example' # str | Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         
hometeam = 'hometeam_example' # str | Abbreviation of a team playing in this game. Example: <code>WAS</code>.

try:
    # Box Score V3
    api_response = api_instance.box_score_v(format, season, week, hometeam)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->box_score_v: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **season** | **str**| Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **week** | **str**| Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | 
 **hometeam** | **str**| Abbreviation of a team playing in this game. Example: &lt;code&gt;WAS&lt;/code&gt;. | 

### Return type

[**BoxScoreV3**](BoxScoreV3.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **box_scores_delta_v**
> list[BoxScoreV3] box_scores_delta_v(format, season, week, playerstoinclude, minutes)

Box Scores Delta V3

This method returns all box scores for a given season and week, but only returns player stats that have changed in the last X minutes. You can also filter by type of player stats to include, such as traditional fantasy players, IDP players or all players.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
season = 'season_example' # str | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
week = 'week_example' # str | Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         
playerstoinclude = 'playerstoinclude_example' # str | The subcategory of players to include in the returned PlayerGame records. Possible values include:<br><br> <code>all</code> Returns all players<br> <code>fantasy</code> Returns traditional fantasy players (QB, RB, WR, TE, K, DST)<br> <code>idp</code> Returns traditional fantasy players and IDP players.
minutes = 'minutes_example' # str | Only returns player statistics that have changed in the last X minutes.  You specify how many minutes in time to go back.  Valid entries are:<br><code>1</code>,  <code>2</code>, etc.         

try:
    # Box Scores Delta V3
    api_response = api_instance.box_scores_delta_v(format, season, week, playerstoinclude, minutes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->box_scores_delta_v: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **season** | **str**| Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **week** | **str**| Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | 
 **playerstoinclude** | **str**| The subcategory of players to include in the returned PlayerGame records. Possible values include:&lt;br&gt;&lt;br&gt; &lt;code&gt;all&lt;/code&gt; Returns all players&lt;br&gt; &lt;code&gt;fantasy&lt;/code&gt; Returns traditional fantasy players (QB, RB, WR, TE, K, DST)&lt;br&gt; &lt;code&gt;idp&lt;/code&gt; Returns traditional fantasy players and IDP players. | 
 **minutes** | **str**| Only returns player statistics that have changed in the last X minutes.  You specify how many minutes in time to go back.  Valid entries are:&lt;br&gt;&lt;code&gt;1&lt;/code&gt;,  &lt;code&gt;2&lt;/code&gt;, etc.          | 

### Return type

[**list[BoxScoreV3]**](BoxScoreV3.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **box_scores_v_simulation**
> list[BoxScoreV3] box_scores_v_simulation(format, numberofplays)

Box Scores V3 Simulation

Gets simulated live box scores of NFL games, covering the Conference Championship games on January 21, 2018.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
numberofplays = 'numberofplays_example' # str | The number of plays to progress in this NFL live game simulation. Example entries are <code>0</code>, <code>1</code>, <code>2</code>, <code>3</code>, <code>150</code>, <code>200</code>, etc.

try:
    # Box Scores V3 Simulation
    api_response = api_instance.box_scores_v_simulation(format, numberofplays)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->box_scores_v_simulation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **numberofplays** | **str**| The number of plays to progress in this NFL live game simulation. Example entries are &lt;code&gt;0&lt;/code&gt;, &lt;code&gt;1&lt;/code&gt;, &lt;code&gt;2&lt;/code&gt;, &lt;code&gt;3&lt;/code&gt;, &lt;code&gt;150&lt;/code&gt;, &lt;code&gt;200&lt;/code&gt;, etc. | 

### Return type

[**list[BoxScoreV3]**](BoxScoreV3.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bye_weeks**
> list[Bye] bye_weeks(format, season)

Bye Weeks

Get bye weeks for the teams during a specified NFL season. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
season = 'season_example' # str |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         

try:
    # Bye Weeks
    api_response = api_instance.bye_weeks(format, season)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->bye_weeks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **season** | **str**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 

### Return type

[**list[Bye]**](Bye.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **daily_fantasy_players**
> list[DailyFantasyPlayer] daily_fantasy_players(format, _date)

Daily Fantasy Players

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
_date = '_date_example' # str |            The date of the contest for which you're pulling players           <code>2014-SEP-21</code>,           <code>2014-NOV-15</code>, etc         

try:
    # Daily Fantasy Players
    api_response = api_instance.daily_fantasy_players(format, _date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->daily_fantasy_players: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **_date** | **str**|            The date of the contest for which you&#39;re pulling players           &lt;code&gt;2014-SEP-21&lt;/code&gt;,           &lt;code&gt;2014-NOV-15&lt;/code&gt;, etc          | 

### Return type

[**list[DailyFantasyPlayer]**](DailyFantasyPlayer.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **daily_fantasy_scoring**
> list[DailyFantasyScoring] daily_fantasy_scoring(format, _date)

Daily Fantasy Scoring

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
_date = '_date_example' # str | The date of the contest for which you're pulling players           <code>2014-SEP-21</code>,           <code>2014-NOV-15</code>, etc

try:
    # Daily Fantasy Scoring
    api_response = api_instance.daily_fantasy_scoring(format, _date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->daily_fantasy_scoring: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **_date** | **str**| The date of the contest for which you&#39;re pulling players           &lt;code&gt;2014-SEP-21&lt;/code&gt;,           &lt;code&gt;2014-NOV-15&lt;/code&gt;, etc | 

### Return type

[**list[DailyFantasyScoring]**](DailyFantasyScoring.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dfs_slates_by_date**
> list[DfsSlate] dfs_slates_by_date(format, _date)

DFS Slates by Date

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
_date = '_date_example' # str | The date of the slates. <br>Examples: <code>2017-SEP-25</code>, <code>2017-10-31</code>.

try:
    # DFS Slates by Date
    api_response = api_instance.dfs_slates_by_date(format, _date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->dfs_slates_by_date: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **_date** | **str**| The date of the slates. &lt;br&gt;Examples: &lt;code&gt;2017-SEP-25&lt;/code&gt;, &lt;code&gt;2017-10-31&lt;/code&gt;. | 

### Return type

[**list[DfsSlate]**](DfsSlate.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dfs_slates_by_week**
> list[DfsSlate] dfs_slates_by_week(format, season, week)

DFS Slates by Week

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
season = 'season_example' # str | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
week = 'week_example' # str | Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         

try:
    # DFS Slates by Week
    api_response = api_instance.dfs_slates_by_week(format, season, week)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->dfs_slates_by_week: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **season** | **str**| Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **week** | **str**| Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | 

### Return type

[**list[DfsSlate]**](DfsSlate.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fantasy_defense_game_stats**
> list[FantasyDefenseGame] fantasy_defense_game_stats(format, season, week)

Fantasy Defense Game Stats

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
season = 'season_example' # str |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
week = 'week_example' # str |            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         

try:
    # Fantasy Defense Game Stats
    api_response = api_instance.fantasy_defense_game_stats(format, season, week)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->fantasy_defense_game_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **season** | **str**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **week** | **str**|            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | 

### Return type

[**list[FantasyDefenseGame]**](FantasyDefenseGame.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fantasy_defense_game_stats_by_team**
> FantasyDefenseGame fantasy_defense_game_stats_by_team(format, season, week, team)

Fantasy Defense Game Stats by Team

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
season = 'season_example' # str | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
week = 'week_example' # str | Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         
team = 'team_example' # str | Abbreviation of the team. Example: <code>WAS</code>.

try:
    # Fantasy Defense Game Stats by Team
    api_response = api_instance.fantasy_defense_game_stats_by_team(format, season, week, team)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->fantasy_defense_game_stats_by_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **season** | **str**| Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **week** | **str**| Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | 
 **team** | **str**| Abbreviation of the team. Example: &lt;code&gt;WAS&lt;/code&gt;. | 

### Return type

[**FantasyDefenseGame**](FantasyDefenseGame.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fantasy_defense_season_stats**
> list[FantasyDefenseSeason] fantasy_defense_season_stats(format, season)

Fantasy Defense Season Stats

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
season = 'season_example' # str |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         

try:
    # Fantasy Defense Season Stats
    api_response = api_instance.fantasy_defense_season_stats(format, season)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->fantasy_defense_season_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **season** | **str**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 

### Return type

[**list[FantasyDefenseSeason]**](FantasyDefenseSeason.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fantasy_defense_season_stats_by_team**
> FantasyDefenseSeason fantasy_defense_season_stats_by_team(format, season, team)

Fantasy Defense Season Stats by Team

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
season = 'season_example' # str | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
team = 'team_example' # str | Abbreviation of the team. Example: <code>WAS</code>.

try:
    # Fantasy Defense Season Stats by Team
    api_response = api_instance.fantasy_defense_season_stats_by_team(format, season, team)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->fantasy_defense_season_stats_by_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **season** | **str**| Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **team** | **str**| Abbreviation of the team. Example: &lt;code&gt;WAS&lt;/code&gt;. | 

### Return type

[**FantasyDefenseSeason**](FantasyDefenseSeason.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fantasy_player_ownership_percentages_season_long**
> list[PlayerOwnership] fantasy_player_ownership_percentages_season_long(format, season, week)

Fantasy Player Ownership Percentages (Season-Long)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
season = 'season_example' # str | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
week = 'week_example' # str | Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         

try:
    # Fantasy Player Ownership Percentages (Season-Long)
    api_response = api_instance.fantasy_player_ownership_percentages_season_long(format, season, week)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->fantasy_player_ownership_percentages_season_long: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **season** | **str**| Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **week** | **str**| Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | 

### Return type

[**list[PlayerOwnership]**](PlayerOwnership.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fantasy_players_with_adp**
> list[FantasyPlayer] fantasy_players_with_adp(format)

Fantasy Players with ADP

This method returns a comprehensive list of draftable fantasy football players, including QB, RB, WR, TE, K and DEF.  Players are sorted by ADP (AverageDraftPosition).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.

try:
    # Fantasy Players with ADP
    api_response = api_instance.fantasy_players_with_adp(format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->fantasy_players_with_adp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 

### Return type

[**list[FantasyPlayer]**](FantasyPlayer.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_stats_by_season_deprecated_use_team_game_stats_instead**
> list[Game] game_stats_by_season_deprecated_use_team_game_stats_instead(format, season)

Game Stats by Season (Deprecated, use Team Game Stats instead)

Game stats for a specified season.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
season = 'season_example' # str |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         

try:
    # Game Stats by Season (Deprecated, use Team Game Stats instead)
    api_response = api_instance.game_stats_by_season_deprecated_use_team_game_stats_instead(format, season)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->game_stats_by_season_deprecated_use_team_game_stats_instead: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **season** | **str**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 

### Return type

[**list[Game]**](Game.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **game_stats_by_week_deprecated_use_team_game_stats_instead**
> list[Game] game_stats_by_week_deprecated_use_team_game_stats_instead(format, season, week)

Game Stats by Week (Deprecated, use Team Game Stats instead)

Game stats for a specified season and week.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
season = 'season_example' # str |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
week = 'week_example' # str |            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         

try:
    # Game Stats by Week (Deprecated, use Team Game Stats instead)
    api_response = api_instance.game_stats_by_week_deprecated_use_team_game_stats_instead(format, season, week)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->game_stats_by_week_deprecated_use_team_game_stats_instead: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **season** | **str**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **week** | **str**|            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | 

### Return type

[**list[Game]**](Game.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **idp_fantasy_players_with_adp**
> list[FantasyPlayer] idp_fantasy_players_with_adp(format)

IDP Fantasy Players with ADP

This method returns the top 300+ IDP Fantasy Players for the current or upcoming season, ordered by AverageDraftPositionIDP.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.

try:
    # IDP Fantasy Players with ADP
    api_response = api_instance.idp_fantasy_players_with_adp(format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->idp_fantasy_players_with_adp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 

### Return type

[**list[FantasyPlayer]**](FantasyPlayer.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **injuries**
> list[Injury] injuries(format, season, week)

Injuries

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
season = 'season_example' # str |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
week = 'week_example' # str |            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         

try:
    # Injuries
    api_response = api_instance.injuries(format, season, week)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->injuries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **season** | **str**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **week** | **str**|            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | 

### Return type

[**list[Injury]**](Injury.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **injuries_by_team**
> list[Injury] injuries_by_team(format, season, week, team)

Injuries by Team

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
season = 'season_example' # str |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
week = 'week_example' # str |            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         
team = 'team_example' # str | Abbreviation of the team. Example: <code>WAS</code>.

try:
    # Injuries by Team
    api_response = api_instance.injuries_by_team(format, season, week, team)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->injuries_by_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **season** | **str**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **week** | **str**|            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | 
 **team** | **str**| Abbreviation of the team. Example: &lt;code&gt;WAS&lt;/code&gt;. | 

### Return type

[**list[Injury]**](Injury.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **league_leaders_by_season**
> list[PlayerSeason] league_leaders_by_season(format, season, position, column)

League Leaders by Season

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
season = 'season_example' # str |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
position = 'position_example' # str | Playerâ€™s position that you would like to filter by.
column = 'column_example' # str | Response member you would like results sorted by.

try:
    # League Leaders by Season
    api_response = api_instance.league_leaders_by_season(format, season, position, column)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->league_leaders_by_season: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **season** | **str**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **position** | **str**| Playerâ€™s position that you would like to filter by. | 
 **column** | **str**| Response member you would like results sorted by. | 

### Return type

[**list[PlayerSeason]**](PlayerSeason.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **league_leaders_by_week**
> list[PlayerGame] league_leaders_by_week(format, season, week, position, column)

League Leaders by Week

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str |            Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.         
season = 'season_example' # str |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
week = 'week_example' # str |            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         
position = 'position_example' # str | Playerâ€™s position that you would like to filter by.
column = 'column_example' # str | Response member you would like results sorted by.

try:
    # League Leaders by Week
    api_response = api_instance.league_leaders_by_week(format, season, week, position, column)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->league_leaders_by_week: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|            Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.          | 
 **season** | **str**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **week** | **str**|            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | 
 **position** | **str**| Playerâ€™s position that you would like to filter by. | 
 **column** | **str**| Response member you would like results sorted by. | 

### Return type

[**list[PlayerGame]**](PlayerGame.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **legacy_box_score**
> BoxScore legacy_box_score(format, season, week, hometeam)

Legacy Box Score

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
season = 'season_example' # str |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
week = 'week_example' # str |            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         
hometeam = 'hometeam_example' # str | Abbreviation of the home team. Example: <code>WAS</code>.

try:
    # Legacy Box Score
    api_response = api_instance.legacy_box_score(format, season, week, hometeam)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->legacy_box_score: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **season** | **str**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **week** | **str**|            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | 
 **hometeam** | **str**| Abbreviation of the home team. Example: &lt;code&gt;WAS&lt;/code&gt;. | 

### Return type

[**BoxScore**](BoxScore.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **legacy_box_scores**
> list[BoxScore] legacy_box_scores(format, season, week)

Legacy Box Scores

This method returns all box scores for a given season and week.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
season = 'season_example' # str |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
week = 'week_example' # str |            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         

try:
    # Legacy Box Scores
    api_response = api_instance.legacy_box_scores(format, season, week)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->legacy_box_scores: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **season** | **str**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **week** | **str**|            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | 

### Return type

[**list[BoxScore]**](BoxScore.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **legacy_box_scores_active**
> list[BoxScore] legacy_box_scores_active(format)

Legacy Box Scores Active

This method returns box scores for all games that are either in-progress or have been updated within the last 30 minutes.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.

try:
    # Legacy Box Scores Active
    api_response = api_instance.legacy_box_scores_active(format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->legacy_box_scores_active: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 

### Return type

[**list[BoxScore]**](BoxScore.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **legacy_box_scores_delta**
> list[BoxScore] legacy_box_scores_delta(format, season, week, minutes)

Legacy Box Scores Delta

This method returns all box scores for a given season and week, but only returns player stats that have changed in the last X minutes.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
season = 'season_example' # str | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
week = 'week_example' # str | Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         
minutes = 'minutes_example' # str | Only returns player statistics that have changed in the last X minutes.  You specify how many minutes in time to go back.  Valid entries are:<br>           <code>1</code> or <code>2</code>.         

try:
    # Legacy Box Scores Delta
    api_response = api_instance.legacy_box_scores_delta(format, season, week, minutes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->legacy_box_scores_delta: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **season** | **str**| Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **week** | **str**| Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | 
 **minutes** | **str**| Only returns player statistics that have changed in the last X minutes.  You specify how many minutes in time to go back.  Valid entries are:&lt;br&gt;           &lt;code&gt;1&lt;/code&gt; or &lt;code&gt;2&lt;/code&gt;.          | 

### Return type

[**list[BoxScore]**](BoxScore.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **legacy_box_scores_delta_current_week**
> list[BoxScore] legacy_box_scores_delta_current_week(format, minutes)

Legacy Box Scores Delta (Current Week)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
minutes = 'minutes_example' # str | Only returns player statistics that have changed in the last X minutes.  You specify how many minutes in time to go back.  Valid entries are:<br>           <code>1</code> or <code>2</code>.         

try:
    # Legacy Box Scores Delta (Current Week)
    api_response = api_instance.legacy_box_scores_delta_current_week(format, minutes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->legacy_box_scores_delta_current_week: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **minutes** | **str**| Only returns player statistics that have changed in the last X minutes.  You specify how many minutes in time to go back.  Valid entries are:&lt;br&gt;           &lt;code&gt;1&lt;/code&gt; or &lt;code&gt;2&lt;/code&gt;.          | 

### Return type

[**list[BoxScore]**](BoxScore.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **legacy_box_scores_final**
> list[BoxScore] legacy_box_scores_final(format)

Legacy Box Scores Final

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.

try:
    # Legacy Box Scores Final
    api_response = api_instance.legacy_box_scores_final(format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->legacy_box_scores_final: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 

### Return type

[**list[BoxScore]**](BoxScore.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **legacy_box_scores_live**
> list[BoxScore] legacy_box_scores_live(format)

Legacy Box Scores Live

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.

try:
    # Legacy Box Scores Live
    api_response = api_instance.legacy_box_scores_live(format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->legacy_box_scores_live: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 

### Return type

[**list[BoxScore]**](BoxScore.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **news**
> list[News] news(format)

News

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.

try:
    # News
    api_response = api_instance.news(format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->news: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 

### Return type

[**list[News]**](News.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **news_by_date**
> list[News] news_by_date(format, _date)

News by Date

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
_date = '_date_example' # str | The date of the news. <br>Examples: <code>2017-JUL-31</code>, <code>2017-SEP-01</code>.

try:
    # News by Date
    api_response = api_instance.news_by_date(format, _date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->news_by_date: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **_date** | **str**| The date of the news. &lt;br&gt;Examples: &lt;code&gt;2017-JUL-31&lt;/code&gt;, &lt;code&gt;2017-SEP-01&lt;/code&gt;. | 

### Return type

[**list[News]**](News.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **news_by_player**
> list[News] news_by_player(format, playerid)

News by Player

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str |            Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.         
playerid = 'playerid_example' # str | Each NFL player has a unique ID assigned by FantasyData. Player IDs can be determined by pulling player related data. Example:<code>14257</code>.

try:
    # News by Player
    api_response = api_instance.news_by_player(format, playerid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->news_by_player: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|            Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.          | 
 **playerid** | **str**| Each NFL player has a unique ID assigned by FantasyData. Player IDs can be determined by pulling player related data. Example:&lt;code&gt;14257&lt;/code&gt;. | 

### Return type

[**list[News]**](News.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **news_by_team**
> list[News] news_by_team(format, team)

News by Team

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
team = 'team_example' # str | Abbreviation of the team. Example: <code>WAS</code>.

try:
    # News by Team
    api_response = api_instance.news_by_team(format, team)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->news_by_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **team** | **str**| Abbreviation of the team. Example: &lt;code&gt;WAS&lt;/code&gt;. | 

### Return type

[**list[News]**](News.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **player_details_by_available**
> list[Player] player_details_by_available(format)

Player Details by Available

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.

try:
    # Player Details by Available
    api_response = api_instance.player_details_by_available(format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->player_details_by_available: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 

### Return type

[**list[Player]**](Player.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **player_details_by_free_agents**
> list[Player] player_details_by_free_agents(format)

Player Details by Free Agents

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.

try:
    # Player Details by Free Agents
    api_response = api_instance.player_details_by_free_agents(format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->player_details_by_free_agents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 

### Return type

[**list[Player]**](Player.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **player_details_by_player**
> PlayerDetail player_details_by_player(format, playerid)

Player Details by Player

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
playerid = 'playerid_example' # str | Each NFL player has a unique ID assigned by FantasyData. Player IDs can be determined by pulling player related data. Example:<code>732</code>.

try:
    # Player Details by Player
    api_response = api_instance.player_details_by_player(format, playerid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->player_details_by_player: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **playerid** | **str**| Each NFL player has a unique ID assigned by FantasyData. Player IDs can be determined by pulling player related data. Example:&lt;code&gt;732&lt;/code&gt;. | 

### Return type

[**PlayerDetail**](PlayerDetail.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **player_details_by_rookie_draft_year**
> list[Player] player_details_by_rookie_draft_year(format, season)

Player Details by Rookie Draft Year

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
season = 'season_example' # str | Year of the season.<br>Examples: <code>2018</code>, <code>2019</code>, etc.

try:
    # Player Details by Rookie Draft Year
    api_response = api_instance.player_details_by_rookie_draft_year(format, season)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->player_details_by_rookie_draft_year: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **season** | **str**| Year of the season.&lt;br&gt;Examples: &lt;code&gt;2018&lt;/code&gt;, &lt;code&gt;2019&lt;/code&gt;, etc. | 

### Return type

[**list[Player]**](Player.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **player_details_by_team**
> list[PlayerDetail] player_details_by_team(format, team)

Player Details by Team

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
team = 'team_example' # str | Abbreviation of the team. Example: <code>WAS</code>.

try:
    # Player Details by Team
    api_response = api_instance.player_details_by_team(format, team)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->player_details_by_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **team** | **str**| Abbreviation of the team. Example: &lt;code&gt;WAS&lt;/code&gt;. | 

### Return type

[**list[PlayerDetail]**](PlayerDetail.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **player_game_red_zone_stats**
> list[PlayerGameRedZone] player_game_red_zone_stats(format, season, week)

Player Game Red Zone Stats

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
season = 'season_example' # str | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
week = 'week_example' # str | Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         

try:
    # Player Game Red Zone Stats
    api_response = api_instance.player_game_red_zone_stats(format, season, week)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->player_game_red_zone_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **season** | **str**| Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **week** | **str**| Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | 

### Return type

[**list[PlayerGameRedZone]**](PlayerGameRedZone.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **player_game_red_zone_stats_inside_five**
> list[PlayerGameRedZone] player_game_red_zone_stats_inside_five(format, season, week)

Player Game Red Zone Stats Inside Five

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
season = 'season_example' # str | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
week = 'week_example' # str | Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         

try:
    # Player Game Red Zone Stats Inside Five
    api_response = api_instance.player_game_red_zone_stats_inside_five(format, season, week)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->player_game_red_zone_stats_inside_five: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **season** | **str**| Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **week** | **str**| Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | 

### Return type

[**list[PlayerGameRedZone]**](PlayerGameRedZone.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **player_game_red_zone_stats_inside_ten**
> list[PlayerGameRedZone] player_game_red_zone_stats_inside_ten(format, season, week)

Player Game Red Zone Stats Inside Ten

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
season = 'season_example' # str | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
week = 'week_example' # str | Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         

try:
    # Player Game Red Zone Stats Inside Ten
    api_response = api_instance.player_game_red_zone_stats_inside_ten(format, season, week)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->player_game_red_zone_stats_inside_ten: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **season** | **str**| Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **week** | **str**| Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | 

### Return type

[**list[PlayerGameRedZone]**](PlayerGameRedZone.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **player_game_stats_by_player**
> PlayerGame player_game_stats_by_player(format, season, week, playerid)

Player Game Stats by Player

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
season = 'season_example' # str |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
week = 'week_example' # str |            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         
playerid = 'playerid_example' # str | Each NFL player has a unique ID assigned by FantasyData. Player IDs can be determined by pulling player related data. Example:<code>732</code>.

try:
    # Player Game Stats by Player
    api_response = api_instance.player_game_stats_by_player(format, season, week, playerid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->player_game_stats_by_player: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **season** | **str**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **week** | **str**|            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | 
 **playerid** | **str**| Each NFL player has a unique ID assigned by FantasyData. Player IDs can be determined by pulling player related data. Example:&lt;code&gt;732&lt;/code&gt;. | 

### Return type

[**PlayerGame**](PlayerGame.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **player_game_stats_by_team**
> list[PlayerGame] player_game_stats_by_team(format, season, week, team)

Player Game Stats by Team

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
season = 'season_example' # str |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
week = 'week_example' # str |            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         
team = 'team_example' # str | Abbreviation of the team. Example: <code>WAS</code>.

try:
    # Player Game Stats by Team
    api_response = api_instance.player_game_stats_by_team(format, season, week, team)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->player_game_stats_by_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **season** | **str**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **week** | **str**|            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | 
 **team** | **str**| Abbreviation of the team. Example: &lt;code&gt;WAS&lt;/code&gt;. | 

### Return type

[**list[PlayerGame]**](PlayerGame.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **player_game_stats_by_week**
> list[PlayerGame] player_game_stats_by_week(format, season, week)

Player Game Stats by Week

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
season = 'season_example' # str |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
week = 'week_example' # str |            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         

try:
    # Player Game Stats by Week
    api_response = api_instance.player_game_stats_by_week(format, season, week)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->player_game_stats_by_week: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **season** | **str**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **week** | **str**|            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | 

### Return type

[**list[PlayerGame]**](PlayerGame.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **player_game_stats_by_week_delta**
> list[PlayerGame] player_game_stats_by_week_delta(format, season, week, minutes)

Player Game Stats by Week Delta

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
season = 'season_example' # str |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
week = 'week_example' # str |            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         
minutes = 'minutes_example' # str | Only returns player statistics that have changed in the last X minutes.  You specify how many minutes in time to go back.  Valid entries are:<br>           <code>1</code> or <code>2</code>.         

try:
    # Player Game Stats by Week Delta
    api_response = api_instance.player_game_stats_by_week_delta(format, season, week, minutes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->player_game_stats_by_week_delta: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **season** | **str**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **week** | **str**|            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | 
 **minutes** | **str**| Only returns player statistics that have changed in the last X minutes.  You specify how many minutes in time to go back.  Valid entries are:&lt;br&gt;           &lt;code&gt;1&lt;/code&gt; or &lt;code&gt;2&lt;/code&gt;.          | 

### Return type

[**list[PlayerGame]**](PlayerGame.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **player_game_stats_delta**
> list[PlayerGame] player_game_stats_delta(format, minutes)

Player Game Stats Delta

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
minutes = 'minutes_example' # str |            Only returns player statistics that have changed in the last X minutes.  You specify how many minutes in time to go back.  Valid entries are:           <code>1</code> or <code>2</code>.         

try:
    # Player Game Stats Delta
    api_response = api_instance.player_game_stats_delta(format, minutes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->player_game_stats_delta: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **minutes** | **str**|            Only returns player statistics that have changed in the last X minutes.  You specify how many minutes in time to go back.  Valid entries are:           &lt;code&gt;1&lt;/code&gt; or &lt;code&gt;2&lt;/code&gt;.          | 

### Return type

[**list[PlayerGame]**](PlayerGame.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **player_season_red_zone_stats**
> list[PlayerSeasonRedZone] player_season_red_zone_stats(format, season)

Player Season Red Zone Stats

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
season = 'season_example' # str | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         

try:
    # Player Season Red Zone Stats
    api_response = api_instance.player_season_red_zone_stats(format, season)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->player_season_red_zone_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **season** | **str**| Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 

### Return type

[**list[PlayerSeasonRedZone]**](PlayerSeasonRedZone.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **player_season_red_zone_stats_inside_five**
> list[PlayerSeasonRedZone] player_season_red_zone_stats_inside_five(format, season)

Player Season Red Zone Stats Inside Five

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
season = 'season_example' # str | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         

try:
    # Player Season Red Zone Stats Inside Five
    api_response = api_instance.player_season_red_zone_stats_inside_five(format, season)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->player_season_red_zone_stats_inside_five: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **season** | **str**| Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 

### Return type

[**list[PlayerSeasonRedZone]**](PlayerSeasonRedZone.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **player_season_red_zone_stats_inside_ten**
> list[PlayerSeasonRedZone] player_season_red_zone_stats_inside_ten(format, season)

Player Season Red Zone Stats Inside Ten

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
season = 'season_example' # str | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         

try:
    # Player Season Red Zone Stats Inside Ten
    api_response = api_instance.player_season_red_zone_stats_inside_ten(format, season)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->player_season_red_zone_stats_inside_ten: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **season** | **str**| Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 

### Return type

[**list[PlayerSeasonRedZone]**](PlayerSeasonRedZone.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **player_season_stats**
> list[PlayerSeason] player_season_stats(format, season)

Player Season Stats

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
season = 'season_example' # str |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         

try:
    # Player Season Stats
    api_response = api_instance.player_season_stats(format, season)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->player_season_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **season** | **str**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 

### Return type

[**list[PlayerSeason]**](PlayerSeason.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **player_season_stats_by_player**
> PlayerSeason player_season_stats_by_player(format, season, playerid)

Player Season Stats by Player

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
season = 'season_example' # str |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
playerid = 'playerid_example' # str | Each NFL player has a unique ID assigned by FantasyData. Player IDs can be determined by pulling player related data. Example:<code>732</code>.

try:
    # Player Season Stats by Player
    api_response = api_instance.player_season_stats_by_player(format, season, playerid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->player_season_stats_by_player: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **season** | **str**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **playerid** | **str**| Each NFL player has a unique ID assigned by FantasyData. Player IDs can be determined by pulling player related data. Example:&lt;code&gt;732&lt;/code&gt;. | 

### Return type

[**PlayerSeason**](PlayerSeason.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **player_season_stats_by_team**
> list[PlayerSeason] player_season_stats_by_team(format, season, team)

Player Season Stats by Team

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
season = 'season_example' # str |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
team = 'team_example' # str | Abbreviation of the team. Example: <code>WAS</code>.

try:
    # Player Season Stats by Team
    api_response = api_instance.player_season_stats_by_team(format, season, team)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->player_season_stats_by_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **season** | **str**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **team** | **str**| Abbreviation of the team. Example: &lt;code&gt;WAS&lt;/code&gt;. | 

### Return type

[**list[PlayerSeason]**](PlayerSeason.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **player_season_third_down_stats**
> list[PlayerSeasonThirdDown] player_season_third_down_stats(format, season)

Player Season Third Down Stats

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
season = 'season_example' # str |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         

try:
    # Player Season Third Down Stats
    api_response = api_instance.player_season_third_down_stats(format, season)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->player_season_third_down_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **season** | **str**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 

### Return type

[**list[PlayerSeasonThirdDown]**](PlayerSeasonThirdDown.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pro_bowlers**
> list[PlayerInfo] pro_bowlers(format, season)

Pro Bowlers

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
season = 'season_example' # str | Year of the season <br>Examples: <code>2016</code>, <code>2017</code>

try:
    # Pro Bowlers
    api_response = api_instance.pro_bowlers(format, season)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->pro_bowlers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **season** | **str**| Year of the season &lt;br&gt;Examples: &lt;code&gt;2016&lt;/code&gt;, &lt;code&gt;2017&lt;/code&gt; | 

### Return type

[**list[PlayerInfo]**](PlayerInfo.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedule**
> list[Schedule] schedule(format, season)

Schedule

Game schedule for a specified season.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
season = 'season_example' # str | Year of the season (with optional season type).<br>Examples: <code>2018</code>, <code>2018PRE</code>, <code>2018POST</code>, <code>2018STAR</code>, <code>2019</code>, etc.

try:
    # Schedule
    api_response = api_instance.schedule(format, season)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **season** | **str**| Year of the season (with optional season type).&lt;br&gt;Examples: &lt;code&gt;2018&lt;/code&gt;, &lt;code&gt;2018PRE&lt;/code&gt;, &lt;code&gt;2018POST&lt;/code&gt;, &lt;code&gt;2018STAR&lt;/code&gt;, &lt;code&gt;2019&lt;/code&gt;, etc. | 

### Return type

[**list[Schedule]**](Schedule.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scores_by_season**
> list[Score] scores_by_season(format, season)

Scores by Season 

Game scores for a specified season.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
season = 'season_example' # str | Year of the season (with optional season type).<br>Examples: <code>2018</code>, <code>2018PRE</code>, <code>2018POST</code>, <code>2018STAR</code>, <code>2019</code>, etc.

try:
    # Scores by Season 
    api_response = api_instance.scores_by_season(format, season)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->scores_by_season: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **season** | **str**| Year of the season (with optional season type).&lt;br&gt;Examples: &lt;code&gt;2018&lt;/code&gt;, &lt;code&gt;2018PRE&lt;/code&gt;, &lt;code&gt;2018POST&lt;/code&gt;, &lt;code&gt;2018STAR&lt;/code&gt;, &lt;code&gt;2019&lt;/code&gt;, etc. | 

### Return type

[**list[Score]**](Score.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scores_by_week**
> list[Score] scores_by_week(format, season, week)

Scores by Week

Get game scores for a specified week of a season.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
season = 'season_example' # str |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
week = 'week_example' # str |            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         

try:
    # Scores by Week
    api_response = api_instance.scores_by_week(format, season, week)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->scores_by_week: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **season** | **str**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **week** | **str**|            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | 

### Return type

[**list[Score]**](Score.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scores_by_week_simulation**
> list[Score] scores_by_week_simulation(format, numberofplays)

Scores by Week Simulation

Gets simulated live scores of NFL games, covering the Conference Championship games on January 21, 2018.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
numberofplays = 'numberofplays_example' # str | The number of plays to progress in this NFL live game simulation. Example entries are <code>0</code>, <code>1</code>, <code>2</code>, <code>3</code>, <code>150</code>, <code>200</code>, etc.

try:
    # Scores by Week Simulation
    api_response = api_instance.scores_by_week_simulation(format, numberofplays)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->scores_by_week_simulation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **numberofplays** | **str**| The number of plays to progress in this NFL live game simulation. Example entries are &lt;code&gt;0&lt;/code&gt;, &lt;code&gt;1&lt;/code&gt;, &lt;code&gt;2&lt;/code&gt;, &lt;code&gt;3&lt;/code&gt;, &lt;code&gt;150&lt;/code&gt;, &lt;code&gt;200&lt;/code&gt;, etc. | 

### Return type

[**list[Score]**](Score.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **season_current**
> int season_current(format)

Season Current

Year of the current NFL season. This value changes on July 1st. The earliest season for Fantasy data is 2001. The earliest season for Team data is 1985. The earliest season for Fantasy data is 2001. The earliest season for Team data is 1985.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.

try:
    # Season Current
    api_response = api_instance.season_current(format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->season_current: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 

### Return type

**int**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **season_last_completed**
> int season_last_completed(format)

Season Last Completed

Year of the most recently completed season. this value changes immediately after the Super Bowl. The earliest season for Fantasy data is 2001. The earliest season for Team data is 1985.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.

try:
    # Season Last Completed
    api_response = api_instance.season_last_completed(format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->season_last_completed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 

### Return type

**int**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **season_upcoming**
> int season_upcoming(format)

Season Upcoming

Year of the current NFL season, if we are in the mid-season. If we are in the off-season, then year of the next upcoming season. This value changes immediately after the Super Bowl. The earliest season for Fantasy data is 2001. The earliest season for Team data is 1985.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.

try:
    # Season Upcoming
    api_response = api_instance.season_upcoming(format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->season_upcoming: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 

### Return type

**int**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stadiums**
> list[Stadium] stadiums(format)

Stadiums

This method returns all stadiums.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.

try:
    # Stadiums
    api_response = api_instance.stadiums(format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->stadiums: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 

### Return type

[**list[Stadium]**](Stadium.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **standings**
> list[Standing] standings(format, season)

Standings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
season = 'season_example' # str |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         

try:
    # Standings
    api_response = api_instance.standings(format, season)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->standings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **season** | **str**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 

### Return type

[**list[Standing]**](Standing.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_game_stats**
> list[TeamGame] team_game_stats(format, season, week)

Team Game Stats

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
season = 'season_example' # str |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
week = 'week_example' # str |            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         

try:
    # Team Game Stats
    api_response = api_instance.team_game_stats(format, season, week)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->team_game_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **season** | **str**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 
 **week** | **str**|            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | 

### Return type

[**list[TeamGame]**](TeamGame.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_season_stats**
> list[TeamSeason] team_season_stats(format, season)

Team Season Stats

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
season = 'season_example' # str |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         

try:
    # Team Season Stats
    api_response = api_instance.team_season_stats(format, season)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->team_season_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **season** | **str**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 

### Return type

[**list[TeamSeason]**](TeamSeason.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_active**
> list[Team] teams_active(format)

Teams (Active)

Gets all active teams.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.

try:
    # Teams (Active)
    api_response = api_instance.teams_active(format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->teams_active: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 

### Return type

[**list[Team]**](Team.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_all**
> list[Team] teams_all(format)

Teams (All)

Gets all teams, including pro bowl teams.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.

try:
    # Teams (All)
    api_response = api_instance.teams_all(format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->teams_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 

### Return type

[**list[Team]**](Team.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_by_season**
> list[Team] teams_by_season(format, season)

Teams by Season

List of teams playing in a specified season.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
season = 'season_example' # str |            Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         

try:
    # Teams by Season
    api_response = api_instance.teams_by_season(format, season)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->teams_by_season: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **season** | **str**|            Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | 

### Return type

[**list[Team]**](Team.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **timeframes**
> list[Timeframe] timeframes(format, type)

Timeframes

Get detailed information about past, present, and future timeframes.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
type = 'type_example' # str | The type of timeframes to return.  Valid entries are <code>current</code> or <code>upcoming</code> or <code>completed</code> or <code>recent</code> or <code>all</code>.

try:
    # Timeframes
    api_response = api_instance.timeframes(format, type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->timeframes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 
 **type** | **str**| The type of timeframes to return.  Valid entries are &lt;code&gt;current&lt;/code&gt; or &lt;code&gt;upcoming&lt;/code&gt; or &lt;code&gt;completed&lt;/code&gt; or &lt;code&gt;recent&lt;/code&gt; or &lt;code&gt;all&lt;/code&gt;. | 

### Return type

[**list[Timeframe]**](Timeframe.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **week_current**
> int week_current(format)

Week Current

Number of the current week of the NFL season. This value usually changes on Tuesday nights or Wednesday mornings at midnight EST. Week number is an integer between 1 and 21 or the word current. Weeks 1 through 17 are regular season weeks. Weeks 18 through 21 are post-season weeks.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.

try:
    # Week Current
    api_response = api_instance.week_current(format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->week_current: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 

### Return type

**int**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **week_last_completed**
> int week_last_completed(format)

Week Last Completed

         Number of the last completed week in the current NFL season. This value changes immediately after the last game of the week is completed and the data is available. This usually happens right after the Monday night game.         Week number is an integer between 1 and 21 or the word current. Weeks 1 through 17 are regular season weeks. Weeks 18 through 21 are post-season weeks.       

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.

try:
    # Week Last Completed
    api_response = api_instance.week_last_completed(format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->week_last_completed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 

### Return type

**int**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **week_upcoming**
> int week_upcoming(format)

Week Upcoming

Number of the upcoming week of the NFL season. This value changes immediately after the final game of the week is completed. We consider upcoming week to be the current week, until current week is over. Week number is an integer between 1 and 21 or the word current. Weeks 1 through 17 are regular season weeks. Weeks 18 through 21 are post-season weeks.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
format = 'format_example' # str | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.

try:
    # Week Upcoming
    api_response = api_instance.week_upcoming(format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->week_upcoming: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | 

### Return type

**int**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

