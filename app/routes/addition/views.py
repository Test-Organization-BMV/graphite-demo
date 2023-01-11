from flask import render_template, request
from app.routes.addition import bp


@bp.route("/add", methods=["POST"])
def index():
    first_num = request.form.get('first_num', default=0, type=int)
    second_num = request.form.get('second_num', default=0, type=int)
    op = '+'
    result = 0
    return render_template('index.html', first_num=first_num, second_num=second_num, op=op, result=result)
