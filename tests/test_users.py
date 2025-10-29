from http import HTTPStatus

import pytest

from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.base import assert_status_code
# Импортируем функцию для валидации JSON Schema
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_create_user_response

@pytest.mark.users  # Добавили маркировку users
@pytest.mark.regression  # Добавили маркировку regression
def test_create_user(public_users_client: PublicUsersClient):

    request = CreateUserRequestSchema()
    response = public_users_client.create_user_api(request)
    response_data = CreateUserResponseSchema.model_validate_json(response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)

    assert_create_user_response(request, response_data)
    # Проверяем, что тело ответа соответствует ожидаемой JSON-схеме
    validate_json_schema(response.json(), response_data.model_json_schema())