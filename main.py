from flask import Flask, render_template
from utils import *

if __name__ == '__main__':
    candidates_file = 'candidates.json'

    candidates = load_candidates(candidates_file)

    app = Flask(__name__)


    @app.route("/")
    def page_main():
        return render_template('list.html', candidates=candidates)


    @app.route("/candidate/<int:id>")
    def page_candidates(id):
        candidate = get_candidate(candidates, id)
        return render_template('single.html', candidate=candidate)


    @app.route("/search/<candidate_name>")
    def page_search_candidates(candidate_name):
        candidates_with_name = get_candidates_by_name(candidates, candidate_name)
        return render_template('search.html', candidates_with_name=candidates_with_name, total_candidates_found=len(candidates_with_name))


    @app.route("/skill/<skill>")
    def page_skills(skill):
        candidates_with_skill = get_candidates_by_skill(candidates, skill)
        return render_template('skill.html', skill=skill, candidates_with_skill=candidates_with_skill, total_candidates_found=len(candidates_with_skill))


    app.run(host='127.0.0.1', port=5000)
