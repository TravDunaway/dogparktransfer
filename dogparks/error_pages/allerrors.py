from flask import Blueprint,render_template

potential_error = Blueprint('potential_error',__name__)

@potential_error.app_errorhandler(404)
def error_404(error):
    '''
    Pages not found.
    '''
    return render_template('potential_error/404.html'), 404

@potential_error.app_errorhandler(403)
def error_403(error):
    '''
    Error
    '''
    return render_template('potential_error/403.html'), 403
