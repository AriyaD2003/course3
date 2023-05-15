import pytest


class TestPostsDAO:

    ### ВСЕ ПОСТЫ

    def test_get_all_check_type(self, posts_dao):
        """  Проверяет, что получение всех постов работает"""
        posts = posts_dao.get_all()
        assert type(posts) == list, "Не получается список комментариев"
        assert len(posts) == 8

    def test_get_all_check_structure(self, posts_dao):
        """ Проверяет, что получение всех постов возвращает верную структуру"""
        posts = posts_dao.get_all()
        first_post = posts[0]
        keys_expected = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}
        first_post_keys = set(first_post.keys())
        assert first_post_keys == keys_expected, "Полученные ключи неверны"


    ### ОДИН ПОСТ

    parameters_get_by_pk = [1,2,3,4]
    @pytest.mark.parametrize("post_pk", parameters_get_by_pk)
    def test_get_by_pk_check_format_and_keys(self, posts_dao, post_pk):
        """ Проверяет, как работает получение поста по его id """

        post = posts_dao.get_by_pk(post_pk)


    def test_get_by_pk_check_not_exist(self, posts_dao):
        """ Проверяет, как работает получение несуществующего"""
        no_post = posts_dao.get_by_pk(0)
        assert no_post == None


    ### ПОСТЫ ПО ПОЛЬЗОВАТЕЛЮ

    post_parameters_by_user = [("leo", {1, 5}), ("larry", {4, 8}), ("hank", {3, 7})]

    @pytest.mark.parametrize("poster_name, post_pks_correct", post_parameters_by_user)
    def test_get_posts_by_user(self, posts_dao, poster_name, post_pks_correct):
        """ Проверяет, что поиск по пользователю работает верно"""

        posts = posts_dao.get_by_user(poster_name)
        post_pks = set()
        for post in posts:
            post_pks.add(post["pk"])

        assert post_pks == post_pks_correct

    ### ПОИСК ПОСТОВ

    post_parameters_search = [("тарелка", {1}), ("елки", {3}), ("проснулся", {4})]

    @pytest.mark.parametrize("query, post_pks_correct", post_parameters_search)
    def test_search_for_posts(self, posts_dao, query, post_pks_correct):
        """ Проверяет, что поиск работает"""
        posts = posts_dao.search(query)
        post_pks = set()
        for post in posts:
            post_pks.add(post["pk"])

        assert post_pks == post_pks_correct