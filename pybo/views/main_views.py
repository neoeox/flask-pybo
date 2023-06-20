from flask import Blueprint, url_for, current_app
from werkzeug.utils import redirect

bp = Blueprint(name='main', import_name=__name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'


@bp.route('/')
def index():
    # 3 / 0  # 강제로 오류발생
    current_app.logger.info("INFO 레벨로 출력")
    return redirect(url_for('question._list'))

