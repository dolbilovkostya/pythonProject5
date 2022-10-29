
import json


def load_candidates():
    """
    Загрузка файла с кандидатами
    :return: список кандидатов в формате list[dict]
    """
    with open('candidates.json', 'r') as file:
        candidates = json.load(file)
    return candidates


def get_all():
    """Главная страница"""
    candidates: list[dict] = load_candidates()
    result = '<pre>'
    for candidate in candidates:
        result += f"""
            {candidate['name']}
            {candidate['position']}
            {candidate['skills']}\n"""

    result += '</pre>'
    return result


def get_by_pk(pk):
    """
    Получение кандидата по номеру 'pk'
    :param pk: номер кандидата
    :return: строку со ссылкой на фото кандидата, именем, должностью и навыками
    """
    result: str = '<pre>'
    for candidate in load_candidates():
        if pk == candidate['pk']:
            result += f""" 
                {candidate['picture']}\n
                {candidate['name']}\n
                {candidate['position']}\n
                {candidate['skills']}\n"""

    result += '</pre>'
    return result


def get_by_skill(skill):
    """
    Получение списка кандидатов обладающих определенным навыком
    :param skill: необхожимый навык
    :return: список кандидатов в виде строки
    """
    result = '<pre>'
    for candidate in load_candidates():
        if skill in candidate['skills']:
            result += f"""
                {candidate['name']}
                {candidate['position']}
                {candidate['skills']}\n"""

    result += '</pre>'
    return result
