
import json


def load_candidates():
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


def get_by_skill(skill_name):
    for candidate in load_candidates():
        if skill_name in candidate['skills']:
            print(candidate['name'])
