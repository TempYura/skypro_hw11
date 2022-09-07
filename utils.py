import json


def load_candidates(file):
    """Загружает данные из файла"""
    with open(file, 'r', encoding='utf-8') as f:
        all_candidates = json.load(f)

    return all_candidates


def get_candidate(all_candidates, id):
    """Возвращает кандидата по id"""

    for candidate in all_candidates:
        if candidate['id'] == id:
            return candidate
    return None


def get_candidates_by_name(all_candidates, name):
    """Возвращает список кандидатов по имени"""

    candidates_with_name = []

    for candidate in all_candidates:
        if name.lower() in candidate['name'].lower():
            candidates_with_name.append(candidate)

    return candidates_with_name


def get_candidates_by_skill(all_candidates, skill):
    """Возвращает список кандидатов по навыку"""

    skill_lower = skill.lower()
    candidates_with_skill = []

    for candidate in all_candidates:
        candidate_skills_list = candidate['skills'].lower().split(", ")

        if skill_lower in candidate_skills_list:
            candidates_with_skill.append(candidate)

    return candidates_with_skill


# тестирование функций
if __name__ == '__main__':
    candidates_file = 'candidates.json'

    decor = "\n" + "-" * 20
    print(f"{decor} load test")
    candidates = load_candidates(candidates_file)
    print(candidates)

    print(f"{decor} get all test")
    print(get_all(candidates))

    print(f"{decor} get by pk 2 test")
    print(get_candidate(candidates, 2))

    print(f"{decor} get by pk 333 test")
    print(get_candidate(candidates, 333))

    print(f"{decor} get by pk 'abc' test")
    print(get_candidate(candidates, "abc"))

    print(f"{decor} get by skill 'pythoN' test")
    print(get_candidates_by_skill(candidates, 'pythoN'))

    print(f"{decor} get by skill 'asdf' test")
    print(get_candidates_by_skill(candidates, 'asdf'))
