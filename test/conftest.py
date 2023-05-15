import pytest

from app.posts.dao.comments_dao import CommentsDAO

from app.posts.dao.posts_dao import PostsDAO


@pytest.fixture
def comments_dao():
    return CommentsDAO("app/posts/data/comments.json")

@pytest.fixture
def posts_dao():
    return PostsDAO("app/posts/data/data.json")