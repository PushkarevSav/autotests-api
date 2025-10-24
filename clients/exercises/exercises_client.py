from typing import TypedDict


from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client

class Exercise(TypedDict):
    """
    Описание структуры задания
    """

    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запрос GET /api/v1/exercises
    """
    courseId: str


class GetExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа GET /api/v1/exercises
    """

    exercises: list[Exercise]


class GetExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа /api/v1/exercises/{exercise_id}
    """
    exercise: Exercise


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

class CreateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа POST /api/v1/exercises
    """

    exercise: Exercise

class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса PATCH /api/v1/exercises

    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class UpdateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа PATCH /api/v1/exercises

    """
    exercise: Exercise

class ExercisesClient(APIClient):

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Получение списка заданий для определенного курса.

        :param query: Словарь с coursesId
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get('/api/v1/exercises', params=query)

    def get_exercise_api(self, exercise_id) -> Response:
        """
        Получение информации о задании по exercise_id

        :param exercise_id: Номер задания
        :return:Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f'/api/v1/exercises/{exercise_id}')

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
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

    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:

        response = self.get_exercises_api(query)
        return response.json()

    def get_exercise(self, exercise_id) -> GetExerciseResponseDict:
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def create_exercise(self, request: CreateExerciseRequestDict) -> CreateExerciseResponseDict:

        response = self.create_exercise_api(request)
        return response.json()


    def update_exercise(self, request: UpdateExerciseRequestDict, exercise_id) -> UpdateExerciseResponseDict:

        response = self.update_exercise_api(request, exercise_id)
        return response.json()


def exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Функция создает экземпляр ExercisesClient c уже настроенным HTTP клиентом

    :return: Готовый к использованию ExercisesClient
    """
    return ExercisesClient(client = get_private_http_client(user))



