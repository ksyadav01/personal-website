from flask import Flask, render_template, request, url_for
# from flask_table import Table, Col
from werkzeug.utils import redirect
# import individual_search
# import individual_search
from . import individual_search
from app import app
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'test'
summoner_name = ""
duo_name = ""
game_list = ""
champion = ""
match_history_list = ""
individual_search_type = ""
stats = []


@app.route('/about')
def about():
    return 'The About Page'


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', author='Karan')


@app.route('/projects/karan.gg/individual_search')
def individual_searchs():
    return render_template('individual_search.html')


@app.route('/projects/karan.gg/individual_search/your_data', methods=['POST', 'GET'])
def your_data():
    if request.method == 'POST':
        global game_list
        global individual_search_type
        global stats
        global summoner_name
        summoner_name = request.form.get('Summoner Name')
        game_list = request.form.getlist('mycheckbox')
        individual_search_type = "your_data"
        print(champion)
        stats = individual_search.your_search(summoner_name, game_list)
        return redirect(url_for('individual_result'))
    return render_template('your_data.html')


@app.route('/projects/karan.gg/individual_search/specific_champion_wr', methods=['POST', 'GET'])
def champion_wr():
    if request.method == 'POST':
        global champion
        global game_list
        global match_history_list
        global individual_search_type
        global stats
        global summoner_name
        summoner_name = request.form.get('Summoner Name')
        champion = request.form.get('Champion')
        game_list = request.form.getlist('mycheckbox')
        match_history_list = request.form.getlist('Match_History')
        print(champion)
        individual_search_type = "champion_wr"
        stats = individual_search.champion_search(summoner_name, champion, game_list, match_history_list)
        return redirect(url_for('individual_result'))
    return render_template('specific_champion_wr.html')


@app.route('/projects/karan.gg/individual_search/duo_checker', methods=['POST', 'GET'])
def duo_checker():
    if request.method == 'POST':
        global duo_name
        global game_list
        global individual_search_type
        global stats
        global summoner_name
        summoner_name = request.form.get('account1')
        duo_name = request.form.get('account2')
        game_list = request.form.getlist('mycheckbox')
        individual_search_type = "duo_checker"
        stats = individual_search.duo_checker(summoner_name, duo_name, game_list)
        return redirect(url_for('individual_result'))
    return render_template('duo_checker.html')


@app.route('/projects/karan.gg/individual_result')
def individual_result():
    # print(champion)
    # if individual_search_type == "champion_wr":
    #     table = individual_search.champion_search(summoner_name, champion, game_list, match_history_list)
    # if individual_search_type == "your_data":
    #     table = individual_search.your_search(summoner_name, game_list)
    print(stats)
    return render_template('individual_result.html', tbl=zip(*stats), name=summoner_name)


# @app.route('/individual_result', methods=['POST', 'GET'])
# def individual_result():
#     if request.method == 'GET':
#         return f"The URL /data is accessed directly. Try going to '/form' to submit form"
#     if request.method == 'POST':
#         form_data = request.form
#         print(form_data)
#         return render_template('individual_result.html', form_data=form_data)
