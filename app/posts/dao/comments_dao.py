import json


class CommentsDAO:

    def __init__(self, path):
        self.path = path

    def load_comments(self):
        with open(self.path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def get_comments_all(self):

        comments = self.load_comments()
        return comments

    def get_comments_by_post_id(self, post_id):
        comments_all = self.load_comments()
        comments_by_pk = []
        for comment in comments_all:
            if comment["post_id"] == post_id:
                comments_by_pk.append(comment)
        return comments_by_pk
