import yaml
from common.msg_utils import *
from mcap.mcap import get_cmc_stats, make_graph

from listener.utils import add_delete

"""
All functions below will correspond to commands that can be called in the bot.
We shall try to keep these short and general to maintain structure.
The available set of kwargs for each function will be:
    "in_msg":           The message sent in by the user,
    "usr_id":           The user's Telegram ID,
    "usr_name":         The user's Telegram Username
    "first_name":       The user's first name on Telegram,
    "mongo":            A connection to MongoDB
    
"""


with open("listener/paragraphs.yaml", "r") as stream:
    try:
        long_texts = yaml.safe_load(stream)
    except yaml.YAMLError as e:
        print(e)


def start(first_name=None, **kwargs):
    return long_texts["start"].format(first_name)


def help(**kwargs):
    return long_texts["help"]


def description(**kwargs):
    return [long_texts["description_0"], long_texts["description_1"]]


def future(**kwargs):
    return long_texts["future"]


def watchlist(usr_id=None, mongo=None, **kwargs):

    found_profile = [x for x in mongo["cusum"].watchList.find({"TGChatID": usr_id})]
    if found_profile == []:
        return "You haven't got a watchlist yet. Set one up automatically by adding a watch via\n/new {ticker} {type}_{agg}_{filter_percentage}"
    else:
        return build_watchlist_str(found_profile[0])


def stats(mongo=None, **kwargs):
    """
    NOTE: this makes a graph so returns the filename as a reference
    - we need a different wrapper here
    """
    stats = get_cmc_stats(mongo)
    return make_graph(stats)


def add_watch(**kwargs):
    return add_delete(action="add", **kwargs)


def delete_watch(**kwargs):
    return add_delete(action="delete", **kwargs)
