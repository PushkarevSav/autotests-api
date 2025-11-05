from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, \
    ExerciseSchema, GetExerciseResponseSchema, GetExercisesResponseSchema, UpdateExerciseResponseSchema, \
    UpdateExerciseRequestSchema
from tools.assertions.base import assert_status_code, assert_equal, assert_length
from tools.assertions.errors import assert_internal_error_response


def assert_create_exercise_response(actual: CreateExerciseRequestSchema, expected: CreateExerciseResponseSchema):
    """
    Функция проверяет соответствие данных отправленных и полученных при создании задания
    :param actual: Запрос отправленный по API
    :param expected:  Ответ отправленный по API
    :return:  AssertError при ошибке сравнения
    """
    assert_equal(actual.title, expected.exercise.title, 'title')
    assert_equal(actual.course_id, expected.exercise.course_id, 'course_id')
    assert_equal(actual.max_score, expected.exercise.max_score, 'max_score')
    assert_equal(actual.min_score, expected.exercise.min_score, 'min_score')
    assert_equal(actual.order_index, expected.exercise.order_index, 'order_index')
    assert_equal(actual.description, expected.exercise.description, 'description')
    assert_equal(actual.estimated_time, expected.exercise.estimated_time, 'estimated_time')


def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
    Проверяет, что данные созданного задания соответствуют ожиданиям

    :param actual: Ответ API
    :param expected: Запрос API
    :return: AssertionError
    """

    assert_equal(actual.title, expected.title, 'title')
    assert_equal(actual.course_id, expected.course_id, 'course_id')
    assert_equal(actual.max_score, expected.max_score, 'max_score')
    assert_equal(actual.min_score, expected.min_score, 'min_score')
    assert_equal(actual.order_index, expected.order_index, 'order_index')
    assert_equal(actual.description, expected.description, 'description')
    assert_equal(actual.estimated_time, expected.estimated_time, 'estimated_time')


def assert_get_exercise_response(actual: GetExerciseResponseSchema, expected: CreateExerciseResponseSchema):
    """
    Проверяем созданное задание на соответствие отправленных данных
    :param actual: Запрос отправленный на отправку данных
    :param expected: Запрос отправленный на получение данных задания
    :return: AssertionError
    """

    assert_exercise(actual.exercise, expected.exercise)


def assert_update_exercise_response(actual: UpdateExerciseRequestSchema, expected: UpdateExerciseResponseSchema):
    """
    Проверяем обновление курса
    :param actual: Запрос к API
    :param expected: Ответ к API
    :return: возвращаем AssertionError в случае несовпадение полей
    """

    if actual.title is not None:
        assert_equal(actual.title, expected.exercise.title, 'title')
    if actual.max_score is not None:
        assert_equal(actual.max_score, expected.exercise.max_score, 'max_score')
    if actual.min_score is not None:
        assert_equal(actual.min_score, expected.exercise.min_score, 'min_score')
    if actual.order_index is not None:
        assert_equal(actual.order_index, expected.exercise.order_index, 'order_index')
    if actual.description is not None:
        assert_equal(actual.description, expected.exercise.description, 'description')
    if actual.estimated_time is not None:
        assert_equal(actual.estimated_time, expected.exercise.estimated_time, 'estimated_time')


def assert_exercise_not_found_response(actual: InternalErrorResponseSchema):
        """
        Функция для проверки ошибки, если файл не найден на сервере.

        :param actual: Фактический ответ.
        :raises AssertionError: Если фактический ответ не соответствует ошибке "File not found"
        """
        # Ожидаемое сообщение об ошибке, если файл не найден
        expected = InternalErrorResponseSchema(details="Exercise not found")
        # Используем ранее созданную функцию для проверки внутренней ошибки
        assert_internal_error_response(actual, expected)