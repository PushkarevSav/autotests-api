from http import HTTPStatus

import pytest

from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema

@pytest.mark.regression
@pytest.mark.authentication
def test_login():

    public_users_client = get_public_users_client()
    authentication_user_client = get_authentication_client()

    request_create_user = CreateUserRequestSchema()
    response_create_user = public_users_client.create_user(request_create_user)

    authentication_user = LoginRequestSchema(
        email=request_create_user.email,
        password=request_create_user.password
    )

    login_response = authentication_user_client.login_api(authentication_user)
    login_response_data = LoginResponseSchema.model_validate_json(login_response.text)

    assert_status_code(login_response.status_code, HTTPStatus.OK)
    assert_login_response(login_response_data)

    validate_json_schema(login_response.json(), login_response_data.model_json_schema())


