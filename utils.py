import json
from collections import defaultdict

def top_10_most_retweeted(path):
    most_retweeted = [{"retweetCount": 0} for _ in range(10)]

    with open(path) as file:
        lines = file.readlines()

    for line in lines:
        dict_line = json.loads(line)
        retweeted_times = dict_line["retweetCount"]

        if retweeted_times > most_retweeted[-1]["retweetCount"]:
            most_retweeted.append(dict_line)
            most_retweeted = sorted(most_retweeted, key=lambda x: x["retweetCount"], reverse=True)
            del most_retweeted[-1]

    content_of_most_retweeted = [tweet["content"] for tweet in most_retweeted]
    return content_of_most_retweeted


def top_10_users(path):
    users = defaultdict(int)

    with open(path) as file:
        lines = file.readlines()

    for line in lines:
        dict_line = json.loads(line)
        username = dict_line["user"]["username"]
        users[username] += 1

    users_dict = []
    for username in users.keys():
        users_dict.append({"username": username, "tweets": users[username]})

    ordered_users = sorted(users_dict, key=lambda x: x["tweets"], reverse=True)
    return ordered_users[0:10]
