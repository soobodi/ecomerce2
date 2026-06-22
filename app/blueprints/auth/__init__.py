from flask import Blueprint

auth_bp = Blueprint(
    'auth', 
    __name__, 
    template_folder='../../template_folder/public'
)

from . import routes