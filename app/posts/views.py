import logging
from json import JSONDecodeError
from os import abort
from flask import Blueprint, request, render_template, abort
from app.posts.dao.posts_dao import  PostsDAO
from app.posts.dao.comments_dao import CommentsDAO

main_blueprint = Blueprint('main_blueprint', __name__,  template_folder='templates')

from config import POST_PATH
from config import COMMENTS_PATH

posts_dao = PostsDAO(POST_PATH)
comments_dao = CommentsDAO(COMMENTS_PATH)

logger = logging.getLogger("basik")

@main_blueprint.route('/')
def posts_all():
    posts = posts_dao.get_all()
    return render_template("index.html", posts=posts)


@main_blueprint.route('/posts/<int:post_id>')
def posts_single(post_id):

    post = posts_dao.get_by_pk(post_id)
    comments = comments_dao.get_comments_by_post_id(post_id)
    comments_len = len(comments)

    return render_template("post.html", post=post, comments=comments, comments_len=comments_len)


@main_blueprint.route('/search')
def posts_search():
    s = request.args.get("s"," ")
    posts = posts_dao.search(s)
    posts_count = len(posts)
    return render_template("search.html", posts=posts, posts_count=posts_count,query=s)


@main_blueprint.route('/users/<username>')
def posts_user(username):

    posts = posts_dao.get_by_user(username)
    posts_count = len(posts)
    return render_template("user-feed.html", posts=posts, posts_count=posts_count)
