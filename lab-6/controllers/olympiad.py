import constants
from app import app
from flask import render_template


@app.route('/olympiad/<olymp>')
def olympiad(olymp):
    html = render_template(
        'olympiad.html',
        olymp=olymp,
        discription=constants.olympiad_dict[olymp]
    )
    return html
