import os

from flask import Flask, render_template, request, url_for
# from flask_table import Table, Col
from werkzeug.utils import redirect
# import individual_search
# import individual_search
from app import individual_search
from app import song
from app import app
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'test'
summoner_name = ""
duo_name = ""
game_list = ""
champion = ""
match_history_list = ""
individual_search_type = ""
riot_key = os.environ.get('RIOTAPI')
lastfm_key = os.environ.get('LASTFM')

stats = []


@app.route('/about')
def about():
    return 'The About Page'


@app.route('/')
@app.route('/home')
def home():
    song_data = song.getSong(lastfm_key)
    return render_template('home.html', artist=song_data.json()['recenttracks']['track'][0]['artist']['#text'],
                           song=song_data.json()['recenttracks']['track'][0]['name'])

@app.route('/coursework_experience')
def coursework_experience():

    return render_template('experience.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/resume')
def resume():
    return redirect("http://www.keepandshare.com/doc3/view.php?id=63274&da=y")


@app.route('/projects/karan.gg')
def karangg():
    return render_template('karangg.html')


# @app.route('/projects/karan.gg/individual_search/your_data', methods=['POST', 'GET'])
# def your_data():
#     if request.method == 'POST':
#         global game_list
#         global individual_search_type
#         global stats
#         global summoner_name
#         summoner_name = request.form.get('Summoner Name')
#         game_list = request.form.getlist('mycheckbox')
#         individual_search_type = "your_data"
#         print(champion)
#         stats = individual_search.your_search(summoner_name, game_list)
#         return redirect(url_for('individual_result'))
#     return render_template('your_data.html')


# @app.route('/projects/karan.gg/individual_search/specific_champion_wr', methods=['POST', 'GET'])
# def champion_wr():
#     if request.method == 'POST':
#         global champion
#         global game_list
#         global match_history_list
#         global individual_search_type
#         global stats
#         global summoner_name
#         summoner_name = request.form.get('Summoner Name')
#         champion = request.form.get('Champion')
#         game_list = request.form.getlist('mycheckbox')
#         match_history_list = request.form.getlist('Match_History')
#         print(champion)
#         individual_search_type = "champion_wr"
#         stats = individual_search.champion_search(summoner_name, champion, game_list, match_history_list)
#         return redirect(url_for('individual_result'))
#     return render_template('specific_champion_wr.html')


# @app.route('/projects/karan.gg/individual_search/duo_checker', methods=['POST', 'GET'])
# def duo_checker():
#     if request.method == 'POST':
#         global duo_name
#         global game_list
#         global individual_search_type
#         global stats
#         global summoner_name
#         summoner_name = request.form.get('account1')
#         duo_name = request.form.get('account2')
#         game_list = request.form.getlist('mycheckbox')
#         individual_search_type = "duo_checker"
#         stats = individual_search.duo_checker(summoner_name, duo_name, game_list)
#         return redirect(url_for('individual_result'))
#     return render_template('duo_checker.html')


# @app.route('/projects/karan.gg/individual_result')
# def individual_result():
#     # print(champion)
#     # if individual_search_type == "champion_wr":
#     #     table = individual_search.champion_search(summoner_name, champion, game_list, match_history_list)
#     # if individual_search_type == "your_data":
#     #     table = individual_search.your_search(summoner_name, game_list)
#     print(stats)
#     return render_template('individual_result.html', tbl=zip(*stats), name=summoner_name)
