import pytest
from pydantic import BaseModel


from clients.exercises.exercises_client import ExercisesClient, exercises_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from fixtures.courses import CourseFixture
from fixtures.files import FileFixture
from tests.conftest import UserFixture


class ExerciseFixture(BaseModel):
    request: CreateExerciseRequestSchema
    response: CreateExerciseResponseSchema


@pytest.fixture()
def exercise_client(function_user: UserFixture) -> ExercisesClient:
    return exercises_client(function_user.authentication_user)


@pytest.fixture()
def function_exercise(exercise_client: ExercisesClient,
                      function_user: UserFixture,
                      function_file: FileFixture,
                      function_course: CourseFixture) -> ExerciseFixture:
    request = CreateExerciseRequestSchema(course_id=function_course.course.id)
    response = exercise_client.create_exercise(request)
    return ExerciseFixture(request = request, response = response)
