import constants
from app import app
from flask import render_template, request


@app.route('/hello', methods=['GET'])
def hello():
    # для каждого параметра get предусматриваем default value

    username = request.values.get('username')
    username = username if username else 'anonymous'

    gender = request.values.get('gender')
    gender = gender if gender else 'М'

    program_id = request.values.get('program')
    program_id = program_id if program_id else 0

    subject_id = request.values.getlist('subject[]')
    subject_id = subject_id if subject_id else []

    # формируем список из выбранных пользователем дисциплин
    subjects_select = [constants.subjects[int(i)] for i in subject_id]
    olympiad_id = request.values.getlist('olympiad[]')

    # формируем список из выбранных пользователем олимпиад
    olympiads_select = [constants.olympiads[int(i)] for i in olympiad_id]
    html = render_template(
        'hello.html',
        name=username,
        gender=gender,
        program=constants.programs[int(program_id)],
        program_list=constants.programs,
        len=len,
        subjects_select=subjects_select,
        subject_list=constants.subjects,
        olympiads_select=olympiads_select,
        olympiad_list=constants.olympiads
    )
    return html
