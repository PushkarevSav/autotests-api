from typing import TypedDict
from unittest.mock import patch

from httpx import Response

from clients.api_client import APIClient

class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запрос GET /api/v1/exercises
    """
    course_id: str

class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запрос POST /api/v1/exercises
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class UpdateExerciseRequestDict(TypedDict):

    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class ExercisesClient(APIClient):

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Получение списка заданий для определенного курса.

        :param query: Словарь с coursesId
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get('/api/v1/exercises', params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Получение информации о задании по exercise_id

        :param exercise_id: Номер задания
        :return:Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f'/api/v1/exercises/{exercise_id}')

    def create_exercise_api(self, request: CreateExerciseRequestDict ) -> Response:
        """
        Создание задания

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post('/api/v1/exercises', json=request)

    def update_exercise_api(self, request: UpdateExerciseRequestDict, exercise_id) -> Response:
        """
        Обновления данных задания

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :param exercise_id: Номер задания
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f'/api/v1/exercises/{exercise_id}', json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Удаление задания

        :param exercise_id: Номер задания
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f'/api/v1/exercises/{exercise_id}')





