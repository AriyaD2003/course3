import logging
from flask import Blueprint, jsonify
from app.posts.dao.posts_dao import PostsDAO
from app.posts.dao.comments_dao import CommentsDAO
from config import POST_PATH, COMMENTS_PATH

api_blueprint = Blueprint('api_blueprint', __name__)

posts_dao = PostsDAO(POST_PATH)
comments_dao = CommentsDAO(COMMENTS_PATH)

logger = logging.getLogger("basik")

@api_blueprint.route('/api/posts/')
def posts_all():
    logger.debug("Запрошенны все посты через API")
    posts = posts_dao.get_all()
    return jsonify(posts)


@api_blueprint.route('/api/posts/<int:post_pk>/')
def posts_one(post_pk):
    logger.debug("Запрошен пост с pk {post_pk} через API")
    post = posts_dao.get_by_pk(post_pk)
    return jsonify({"content": "Страничка одного поста"})
