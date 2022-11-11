from flask import render_template,request,Blueprint
from dogparks.models import Posts

core = Blueprint('core',__name__)

@core.route('/')
def index():
    '''
    The home page view. 
    '''
    page = request.args.get('page', 1, type=int)
    blog_posts = Posts.query.order_by(Posts.date.desc()).paginate(page=page, per_page=10)
    return render_template('index.html',blog_posts=blog_posts)

@core.route('/info')
def info():
    '''
    Example view.
    '''
    return render_template('info.html')
