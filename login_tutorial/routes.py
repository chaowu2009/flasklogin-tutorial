"""Routes for core application."""
import os
from flask import Blueprint, render_template
from flask_assets import Environment, Bundle
from flask_login import current_user
from flask import current_app as app
from .models import User
from flask_login import login_required


# Blueprint Configuration
main_bp = Blueprint('main_bp', __name__,
                    template_folder='templates',
                    static_folder='static')

# Flask-Assets Configuration
assets = Environment(app)
Environment.auto_build = True
less_bundle = Bundle('src/less/dashboard.less',
                     filters='less,cssmin',
                     output='dist/css/dashboard.css',
                     extra={'rel': 'stylesheet/less'})
assets.register('less_all', less_bundle)
if app.config['FLASK_ENV'] == 'development':
    less_bundle.build(force=True)


@main_bp.route('/', methods=['GET'])
@login_required
def dashboard():
    """Serve logged in Dashboard."""
    return render_template('dashboard.html',
                           title='Flask-Login Tutorial.',
                           template='dashboard-template',
                           current_user=current_user,
                           body="You are now logged in!")
