from flask import render_template,request,Blueprint
from puppycompanyblog.models import BlogPost
import sqlite3 as sql
#app = Flask(__name__)

core = Blueprint('core',__name__)

@core.route('/index')
def index():
    '''
    This is the home page view. Notice how it uses pagination to show a limited
    number of posts by limiting its query size and then calling paginate.
    '''
    page = request.args.get('page', 1, type=int)
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page, per_page=10)
    return render_template('index.html',blog_posts=blog_posts)

@core.route('/about')
def about():
    '''
    Example view of any other "core" page. Such as a info page, about page,
    contact page. Any page that doesn't really sync with one of the models.
    '''
    return render_template('about.html')

@core.route('/contact')
def contact():
    '''
    Example view of any other "core" page. Such as a info page, contact page,
    contact page. Any page that doesn't really sync with one of the models.
    '''
    return render_template('contact.html')

@core.route('/orders')
def orders():
    '''
    Example view of any other "core" page. Such as a info page, orders page,
    contact page. Any page that doesn't really sync with one of the models.
    '''

    con = sql.connect("data.sqlite")
    con.row_factory = sql.Row
    
    cur = con.cursor()
    cur.execute("select * from orders")
    
    rows = cur.fetchall(); 
    return render_template("orders.html",rows = rows)

    #return render_template('orders.html')
#if __name__ == '__main__':
   #app.run(debug = True)