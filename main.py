
from flask import Flask
import utils

app = Flask(__name__)


@app.route("/")
def main_page():
    """
    Главная страница
    :return: список всех кандидатов
    """
    return utils.get_all()


@app.route('/candidates/<int:pk>/')
def candidates(pk):
    """
    Страница с кандидатом по номеру его 'pk'
    :param pk: номер кандидата
    :return: информация о кандидате, строка
    """
    return utils.get_by_pk(pk)


@app.route('/skills/<skill>')
def get_skills(skill):
    """
    Страница с кандидатами по определенному навыку
    :param skill: необходимый навык
    :return: список кандидатов обладающих опрежелнным навыком, строка
    """
    return utils.get_by_skill(skill)


app.run(host='0.0.0.0', port=800)
