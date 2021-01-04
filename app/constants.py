from flask import Flask
from riotwatcher import LolWatcher, ApiError
import plotly.graph_objects as go
import json

app = Flask(__name__)
API_KEY = 'RGAPI-c6e4e7be-124e-46e2-bab2-de3ac3369699'
#
# watcher = LolWatcher(API_KEY)
# my_name = 'Notorious YNO'  # input("Enter your name:")
# my_region = 'na1'
# full_team = []
# your_te   am = []
# latest = watcher.data_dragon.versions_for_region(my_region)['n']['champion']
# static_champ_list = watcher.data_dragon.champions(latest, False, 'en_US')
#
# champ_dict = {}
# for key in static_champ_list['data']:
#     row = static_champ_list['data'][key]
#     champ_dict[row['key']] = row['id']
#
# # me = watcher.summoner.by_name(my_region, my_name)
# # my_summoner_name = me['name']
# # my_summoner_level = me['summonerLevel']
# # my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
# # my_id = me['id']
# """
# try:
#     current_game = watcher.spectator.by_summoner(my_region, my_id)
#     full_team = current_game['participants']
#     in_game = True
# except ApiError as err:
#     if err.response.status_code == 404:
#         in_game = False
#     elif err.response.status_code == 429:
#         in_game = False
#         print("rate limit exceeded")
# """
#
#
# def individual_search():
#     stats = []
#     ranked_solo = []
#     ranked_flex = []
#     aram = []
#     norms = []
#     # your_ranks
#     try:
#         account = input("Enter your ign: ")
#         player = watcher.summoner.by_name(my_region, account)
#         ranked_list = watcher.league.by_summoner(my_region, player['id'])
#         my_matches = watcher.match.matchlist_by_account(my_region, player['accountId'])
#         match_list = my_matches['matches']
#         match_counter = 0
#         aram_wins = 0
#         aram_losses = 0
#         norms_wins = 0
#         norms_losses = 0
#         for match_counter in range(0, 100):
#             current_match = match_list[match_counter]
#             match_counter += 1
#             info = ""
#             if current_match['queue'] == 450:
#                 match_info = watcher.match.by_id(my_region, current_match['gameId'])
#                 player_number = -1
#                 for x in match_info['participantIdentities']:
#                     if x['player']['summonerName'] == player['name']:
#                         for a in match_info['participants']:
#                             player_number += 1
#                             if a['participantId'] == x['participantId']:
#                                 break
#                 player_game_info = match_info['participants'][player_number]
#                 if player_game_info['stats']['win']:
#                     aram_wins += 1
#                 else:
#                     aram_losses += 1
#             elif current_match['queue'] <= 410:
#                 match_info = watcher.match.by_id(my_region, current_match['gameId'])
#                 player_number = -1
#                 for x in match_info['participantIdentities']:
#                     if x['player']['summonerName'] == player['name']:
#                         for a in match_info['participants']:
#                             player_number += 1
#                             if a['participantId'] == x['participantId']:
#                                 break
#                 player_game_info = match_info['participants'][player_number]
#                 if player_game_info['stats']['win']:
#                     norms_wins += 1
#                 else:
#                     norms_losses += 1
#         if not watcher.league.by_summoner(my_region, player['id']):
#             ranked_solo = ["N/A", "N/A", "N/A", "N/A"]
#             ranked_flex = ["N/A", "N/A", "N/A", "N/A"]
#
#         elif watcher.league.by_summoner(my_region, player['id'])[0]['queueType'] == "RANKED_SOLO_5x5":
#             solo_info = watcher.league.by_summoner(my_region, player['id'])[0]
#             ranked_solo.append(solo_info['tier'] + " " + solo_info['rank'])  # Tier and Division ex; GOLD IV
#             ranked_solo.append(solo_info['leaguePoints'])  # LP
#             ranked_solo.append(round((solo_info['wins'] / (solo_info['losses'] + solo_info['wins']) * 100), 2))
#             ranked_solo.append((solo_info['losses'] + solo_info['wins']))  # Total games
#             ranked_flex = ["N/A", "N/A", "N/A", "N/A"]
#             if len(watcher.league.by_summoner(my_region, player['id'])) > 1:
#                 flex_info = watcher.league.by_summoner(my_region, player['id'])[1]
#                 ranked_flex = [flex_info['tier'] + " " + flex_info['rank'], flex_info['leaguePoints'],
#                                round((flex_info['wins'] / (flex_info['losses'] + flex_info['wins']) * 100), 2),
#                                (flex_info['losses'] + flex_info['wins'])]
#         else:
#             flex_info = watcher.league.by_summoner(my_region, player['id'])[0]
#             ranked_flex.append(flex_info['tier'] + " " + flex_info['rank'])  # Tier and Division ex; GOLD IV
#             ranked_flex.append(flex_info['leaguePoints'])  # LP
#             ranked_flex.append(round((flex_info['wins'] / (flex_info['losses'] + flex_info['wins']) * 100), 2))
#             ranked_flex.append((flex_info['losses'] + flex_info['wins']))  # Total games
#             ranked_solo = ["N/A", "N/A", "N/A", "N/A"]
#             if len(watcher.league.by_summoner(my_region, player['id'])) > 1:
#                 solo_info = watcher.league.by_summoner(my_region, player['id'])[1]
#                 ranked_solo = [solo_info['tier'] + " " + solo_info['rank'], solo_info['leaguePoints'],
#                                round((solo_info['wins'] / (solo_info['losses'] + solo_info['wins']) * 100), 2),
#                                (solo_info['losses'] + solo_info['wins'])]
#
#         norms.append("N/A")
#         norms.append("N/A")
#         try:
#             norms.append(round((norms_wins / (norms_wins + norms_losses) * 100), 2))
#         except ZeroDivisionError as err:
#             norms.append("N/A")
#         norms.append(norms_wins + norms_losses)
#
#         aram.append("N/A")
#         aram.append("N/A")
#         try:
#             aram.append(round((aram_wins / (aram_wins + aram_losses) * 100), 2))
#         except ZeroDivisionError as err:
#             aram.append("N/A")
#         aram.append(aram_wins + aram_losses)
#
#         header = [account, "Ranked Solo/Duo", "Ranked Flex", "Norms", "ARAM"]
#
#         left_bar = ["Rank", "LP", "Win Rate", "Total Games"]
#
#         stats.append(left_bar)
#         stats.append(ranked_solo)
#         stats.append(ranked_flex)
#         stats.append(norms)
#         stats.append(aram)
#
#         fig = go.Figure(data=[go.Table(
#             header=dict(values=header,
#                         line_color='darkslategray',
#                         fill_color='lightgray',
#                         align='left',
#                         font=dict(color='white', size=12),
#                         height=40),
#             cells=dict(
#                 values=stats, line_color='darkslategray', fill_color='white', align='left',
#                 font_size=12,
#                 height=30))
#         ])
#
#         fig.update_layout(width=800, height=1000)
#         fig.show()
#     except ApiError as err:
#         if err.response.status_code == 404:
#             print("Name doesn't exists")
#         elif err.response.status_code == 429:
#             print("Rate limit exceeded")
#         else:
#             print(err.response.status_code)
#             print("Other error")
#
#
# def team_search():
#     global max_games, total_summoners
#     in_game = False
#     try:
#         team = [input("Enter your lobby").split(" joined the lobby")[0], input().split(" joined the lobby")[0],
#                 input().split(" joined the lobby")[0], input().split(" joined the lobby")[0],
#                 input().split(" joined the lobby")[0]]
#         # print(team)
#         max_games = int(input("How many games do you want to show"))
#         assert len(team) > 0
#         total_summoners = min(len(team), 5)
#         for x in range(0, len(team)):
#             full_team.append(watcher.summoner.by_name(my_region, team[x]))
#             in_game = True
#
#         if in_game:
#             # print(total_summoners)
#             player = ["Name", "Rank", "Current LP", "Win Rate", "Total Games", "Match History"]
#             player_names = [""]
#             your_team.append(player)
#             column_ord = []
#             column_wid = []
#             recent_games_played = 0
#             for i in range(0, total_summoners):
#                 player = []
#                 temp = 0
#                 assert total_summoners != 0
#                 person = full_team[i]
#
#                 if len(watcher.league.by_summoner(my_region, person['id'])) == 1:
#                     temp = watcher.league.by_summoner(my_region, person['id'])[0]
#                 else:
#                     if watcher.league.by_summoner(my_region, person['id'])[0]['queueType'] == "RANKED_SOLO_5x5":
#                         temp = watcher.league.by_summoner(my_region, person['id'])[0]
#                     else:
#                         temp = watcher.league.by_summoner(my_region, person['id'])[1]
#
#                 player_names.append("Summoner " + str(i + 1))  # Summoner number
#                 player.append(person['name'])  # IGN
#                 player.append(temp['tier'] + " " + temp['rank'])  # Tier and Division ex; GOLD IV
#                 player.append(temp['leaguePoints'])  # LP
#                 player.append(round((temp['wins'] / (temp['losses'] + temp['wins']) * 100), 2))  # Win rate percentage
#                 player.append((temp['losses'] + temp['wins']))  # Total games
#                 # Adds last 10 champs played
#                 # player.append("Recent Match History")
#                 my_matches = watcher.match.matchlist_by_account(my_region, person['accountId'])
#                 match_counter = 0
#
#                 match_list = my_matches['matches']
#                 # print(match_list)
#                 recent_games_played = 0
#                 while recent_games_played < max_games:
#                     if match_counter == 100:
#                         break
#                     current_match = match_list[match_counter]
#                     match_counter += 1
#                     info = ""
#                     if current_match['queue'] == 420:
#                         match_info = watcher.match.by_id(my_region, current_match['gameId'])
#                         player_number = -1
#                         for x in match_info['participantIdentities']:
#                             if x['player']['summonerName'] == person['name']:
#                                 for a in match_info['participants']:
#                                     player_number += 1
#                                     if a['participantId'] == x['participantId']:
#                                         break
#                         # player_number += -2
#                         # print(player_number)
#                         player_game_info = match_info['participants'][player_number]
#                         info += champ_dict[str(player_game_info['championId'])]
#                         info += "  " + str(player_game_info['stats']['kills']) + "/" \
#                                 + str(player_game_info['stats']['deaths']) \
#                                 + "/" + str(player_game_info['stats']['assists']) + "\n"
#                         recent_games_played += 1
#                         player.append(info)
#
#                 column_wid.append(len(person['name']) * 10)
#                 column_ord.append(i + 1)
#                 your_team.append(player)
#
#                 # print(watcher.league.by_summoner(my_region, person['id']))
#             fig = go.Figure(data=[go.Table(
#                 header=dict(values=player_names,
#                             line_color='darkslategray',
#                             fill_color='lightgray',
#                             align='left',
#                             font=dict(color='white', size=12),
#                             height=40),
#                 cells=dict(
#                     values=your_team, line_color='darkslategray', fill_color='white', align='left',
#                     font_size=12,
#                     height=30))
#             ])
#
#             fig.update_layout(width=1100, height=1500)
#             fig.show()
#     except ApiError as err:
#         if err.response.status_code == 404:
#             in_game = False
#             print("Name doesn't exist")
#         elif err.response.status_code == 429:
#             in_game = False
#             print("rate limit exceeded")
#         else:
#             in_game = False
#
#
# # team_search()
# individual_search()
# # print(my_summoner_name)
# # print("Summoner level", my_summoner_level)
# # print(my_ranked_stats)
# # print(len(your_team))
# # print(your_team[0])
