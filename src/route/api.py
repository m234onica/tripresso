from flask import Blueprint, render_template
from src.models import TourGroups

api = Blueprint('api', __name__)
