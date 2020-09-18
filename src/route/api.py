from flask import Blueprint, render_template, jsonify
from src.models import TourGroups, Tags, Price
from src.tool import filter

api = Blueprint('api', __name__)


@api.route("/", methods=["GET"])
def get_all_tourgroups():
    tourgroups = TourGroups.query.all()
    result = [filter.get_group_tag(group) for group in tourgroups]
    return jsonify(result)


@api.route("/group/<groupId>", methods=["GET"])
def get_each_tourgroups(groupId):
    group = TourGroups.query.filter_by(id=groupId).one()
    return jsonify(filter.get_group_tag(group))

