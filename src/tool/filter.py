from src.models import TourGroups, Tags, Price

def get_tag_name(tagId):
    data = Tags.query.filter_by(id=tagId).one()
    return data.name


def get_group_tag(group):
    tags = group.tags
    if tags == None:
        group.tags = None
    else:
        tags_list = list(tags.split(","))
        group.tags = [get_tag_name(tag) for tag in tags_list]
    return group
