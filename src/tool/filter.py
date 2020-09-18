from flask import jsonify
from src.models import TourGroups, Tags, Price


def get_tag_name(tagId):
    tag = Tags.query.filter_by(id=tagId).one()
    return tag.name


def get_price_info(priceId):
    price = Price.query.filter_by(id=priceId).one()
    return {"price": price.price, "startDate": price.startDate}


def get_group_detail(group):
    tags = group.tags
    if tags == None:
        group.tags = None
    else:
        tags_list = tags.split(",")
        group.tags = [get_tag_name(tag) for tag in tags_list]

    priceId = group.price
    price_list = priceId.split(",")
    group.price = [get_price_info(priceId) for priceId in price_list]
    return group
