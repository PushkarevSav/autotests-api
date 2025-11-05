from httpx import Response
from setuptools.command.alias import alias

from clients.api_client import APIClient
from clients.exercises.exercises_schema import GetExercisesQuerySchema, CreateExerciseRequestSchema, \
    UpdateExerciseRequestSchema, GetExercisesResponseSchema, GetExerciseResponseSchema, CreateExerciseResponseSchema, \
    UpdateExerciseResponseSchema
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client


class ExercisesClient(APIClient):

    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Получение списка заданий для определенного курса.

        :param query: Словарь с coursesId
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get('/api/v1/exercises', params=query.model_dump(by_alias=True))

    def get_exercise_api(self, exercise_id) -> Response:
        """
        Получение информации о задании по exercise_id

        :param exercise_id: Номер задания
        :return:Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f'/api/v1/exercises/{exercise_id}')

    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Создание задания

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post('/api/v1/exercises', json=request.model_dump(by_alias =True))

    def update_exercise_api(self, request: UpdateExerciseRequestSchema, exercise_id) -> Response:
        """
        Обновления данных задания

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :param exercise_id: Номер задания
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f'/api/v1/exercises/{exercise_id}', json=request.modal_dump(by_alias =True))

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Удаление задания

        :param exercise_id: Номер задания
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f'/api/v1/exercises/{exercise_id}')

    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:

        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)


    def get_exercise(self, exercise_id) -> GetExerciseResponseSchema:
        response = self.get_exercise_api(exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:

        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)


    def update_exercise(self, request: UpdateExerciseRequestSchema, exercise_id) -> UpdateExerciseResponseSchema:

        response = self.update_exercise_api(request, exercise_id)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)

def exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создает экземпляр ExercisesClient c уже настроенным HTTP клиентом

    :return: Готовый к использованию ExercisesClient
    """
    return ExercisesClient(client = get_private_http_client(user))



