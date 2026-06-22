from flask import render_template
from . import auth_bp

@auth_bp.route('/login')
def login ():
    return render_template('public/login.html')

@auth_bp.route('/registro')
def registro ():
    return render_template('public/registro.html')

