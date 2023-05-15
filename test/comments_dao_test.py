import pytest


class TestCommentsDAO:

    def test_get_comments_all_check_type(self, comments_dao):
        """ Все комментарии: Тестируем тип и количество полу"""
        comments = comments_dao.load_comments()
        assert type(comments) == list, "Не получается список комментариев"
        assert len(comments) == 20

    def test_get_comments_all_check_structure(self, comments_dao):
        """ Тестируем структуру комментариев"""
        comments = comments_dao.load_comments()
        first_comment = comments[0]
        keys_expected = {"post_id", "commenter_name", "comment", "pk"}
        first_comment_keys = set(first_comment.keys())
        assert first_comment_keys == keys_expected, "Полученные ключи неверны"


    def test_get_comments_by_post_ID_check_type(self, comments_dao):
        """ Тестируем получение комментариев к посту"""
        comments_for_post = comments_dao.get_comments_by_post_id(1)
        assert type(comments_for_post) == list, "Комментарии должны быть списком"

    comments_parameters_ids = [1, 2, 3, 4]

    @pytest.mark.parametrize("post_id", comments_parameters_ids)
    def test_get_comments_by_post_ID_check_type(self, comments_dao, post_id):

        """ Тестируем что полученные комментарию к каждому посту действительно к нему"""
        comments_for_post = comments_dao.get_comments_by_post_id(post_id)

        for comment in comments_for_post:
            assert comment["post_id"] == post_id
