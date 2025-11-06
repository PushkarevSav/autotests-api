from http import HTTPStatus

import allure
import pytest
from allure_commons.types import Severity

from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, \
    GetExercisesQuerySchema, GetExercisesResponseSchema, GetExerciseResponseSchema, UpdateExerciseRequestSchema, \
    UpdateExerciseResponseSchema
from fixtures.courses import CourseFixture
from fixtures.exercises import ExerciseFixture
from fixtures.files import FileFixture
from fixtures.users import UserFixture
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import assert_create_exercise_response, assert_get_exercise_response, \
    assert_update_exercise_response, assert_exercise_not_found_response, assert_get_exercises_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.exercises
@allure.tag(AllureTag.EXERCISES, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)  # Добавили epic
@allure.feature(AllureFeature.EXERCISES) # Добавили теги
@allure.parent_suite(AllureEpic.LMS)  # allure.parent_suite == allure.epic
@allure.suite(AllureFeature.EXERCISES)  # allure.suite == allure.feature
class TestExercises:

    @allure.tag(AllureTag.CREATE_ENTITY)  # Добавили тег
    @allure.title("Create exercise")
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.severity(Severity.BLOCKER)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    def test_create_exercises(self, function_user: UserFixture, function_course: CourseFixture,
                              function_file: FileFixture, exercise_client: ExercisesClient):
        request = CreateExerciseRequestSchema(course_id=function_course.response.course.id)
        response = exercise_client.create_exercise_api(request)
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_exercise_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag(AllureTag.GET_ENTITY)  # Добавили тег
    @allure.title("Get exercise")
    @allure.story(AllureStory.GET_ENTITIES)
    @allure.severity(Severity.BLOCKER)
    @allure.sub_suite(AllureStory.GET_ENTITIES)
    def test_get_exercise(self,
                          function_exercise: ExerciseFixture, exercise_client: ExercisesClient):
        response = exercise_client.get_exercise_api(function_exercise.response.exercise.id)
        response_data = GetExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_exercise_response(response_data, function_exercise.response)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag(AllureTag.UPDATE_ENTITY)
    @allure.story(AllureStory.UPDATE_ENTITY) # Добавили тег
    @allure.title("Update exercise")
    @allure.severity(Severity.CRITICAL)
    @allure.sub_suite(AllureStory.UPDATE_ENTITY)
    def test_update_exercises(self, function_exercise: ExerciseFixture, exercise_client: ExercisesClient):
        request = UpdateExerciseRequestSchema()
        response = exercise_client.update_exercise_api(request, exercise_id=function_exercise.response.exercise.id)
        response_data = UpdateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_exercise_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag(AllureTag.DELETE_ENTITY)
    @allure.story(AllureStory.DELETE_ENTITY)# Добавили тег
    @allure.title("Delete exercise")
    @allure.severity(Severity.CRITICAL)
    @allure.sub_suite(AllureStory.DELETE_ENTITY)
    def test_delete_exercise(self, function_exercise: ExerciseFixture, exercise_client: ExercisesClient):
        response = exercise_client.delete_exercise_api(exercise_id=function_exercise.response.exercise.id)
        assert_status_code(response.status_code, HTTPStatus.OK)

        get_response = exercise_client.get_exercise_api(exercise_id=function_exercise.response.exercise.id)
        data_response = InternalErrorResponseSchema.model_validate_json(get_response.text)

        assert_status_code(response.status_code, HTTPStatus.NOT_FOUND)

        assert_exercise_not_found_response(data_response)

        validate_json_schema(get_response.json(), data_response.model_json_schema())

    @allure.tag(AllureTag.GET_ENTITIES)  # Добавили тег
    @allure.title("Get exercises")
    @allure.story(AllureStory.GET_ENTITIES)
    @allure.severity(Severity.BLOCKER)
    @allure.sub_suite(AllureStory.GET_ENTITIES)

    def test_get_exercises(self, function_exercise: ExerciseFixture, exercise_client: ExercisesClient, function_course: CourseFixture):
        request = GetExercisesQuerySchema(course_id = function_course.response.course.id)
        response = exercise_client.get_exercises_api(request)
        response_data = GetExercisesResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)

        assert_get_exercises_response(response_data, [function_exercise.response])
        validate_json_schema(response.json(), response_data.model_json_schema())



