import pytest
from http import HTTPStatus

POSTS_ENDPOINT = "/posts"


@pytest.mark.api
@pytest.mark.posts
class TestPosts:
    """
    Набор тестов для проверки REST API эндпоинта /posts.

    Тестируются:
    - получение поста (GET)
    - создание поста (POST)
    - обновление поста (PUT)
    - удаление поста (DELETE)
    - Получение несуществующего ресурса.
    """

    @pytest.mark.parametrize("post_id", [1, 5, 10])
    def test_get_post_by_id(self, session, base_url, post_id):
        """
        Проверяет получение поста по его ID.
        """
        response = session.get(f"{base_url}{POSTS_ENDPOINT}/{post_id}")

        assert response.status_code == HTTPStatus.OK

        data = response.json()
        expected_keys = {"userId", "id", "title", "body"}

        assert expected_keys.issubset(data.keys())
        assert data["id"] == post_id

    def test_get_posts_list(self, session, base_url):
        """
        Проверяет получение списка постов.
        """
        response = session.get(f"{base_url}{POSTS_ENDPOINT}")

        assert response.status_code == HTTPStatus.OK

        data = response.json()
        assert isinstance(data, list)

        expected_keys = {"userId", "id", "title", "body"}
        assert expected_keys.issubset(data[0].keys())

    def test_create_post(self, session, base_url):
        """
        Проверяет создание нового поста (POST).
        """
        payload = {"title": "test title", "body": "test body", "userId": 1}

        response = session.post(f"{base_url}{POSTS_ENDPOINT}", json=payload)

        assert response.status_code == HTTPStatus.CREATED

        data = response.json()
        expected_keys = {"title", "body", "userId", "id"}

        assert expected_keys.issubset(data.keys())
        assert data["title"] == payload["title"]
        assert data["body"] == payload["body"]
        assert data["userId"] == payload["userId"]

    def test_update_post(self, session, base_url):
        """
        Проверяет обновление существующего поста (PUT).
        """
        payload = {
            "id": 1,
            "title": "updated title",
            "body": "updated body",
            "userId": 1,
        }

        response = session.put(f"{base_url}{POSTS_ENDPOINT}/1", json=payload)

        assert response.status_code == HTTPStatus.OK

        data = response.json()

        expected_keys = {"userId", "id", "title", "body"}
        assert expected_keys.issubset(data.keys())

        assert data["title"] == payload["title"]
        assert data["body"] == payload["body"]

    def test_delete_post(self, session, base_url):
        """
        Проверяет удаление поста.
        """
        response = session.delete(f"{base_url}{POSTS_ENDPOINT}/1")

        assert response.status_code == HTTPStatus.OK

    def test_get_non_existing_post(self, session, base_url):
        """
        Несуществующий ресурс.
        """
        response = session.get(f"{base_url}{POSTS_ENDPOINT}/0")

        assert response.status_code == HTTPStatus.NOT_FOUND
