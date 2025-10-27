from pydantic import BaseModel, ConfigDict, Field


class Exercise(BaseModel):
    """
    Описание структуры задания
    """

    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str = Field(alias='courseId')
    max_score: int = Field(alias='maxScore')
    min_score: int = Field(alias='minScore')
    order_index: int = Field(alias='orderIndex')
    description: str
    estimated_time: str = Field(alias='estimatedTime')


class GetExercisesQuerySchema(BaseModel):
    """
    Описание структуры запрос GET /api/v1/exercises
    """
    course_id: str = Field(alias='courseId')


class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа GET /api/v1/exercises
    """

    exercises: list[Exercise]


class GetExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа /api/v1/exercises/{exercise_id}
    """
    exercise: Exercise


class CreateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запрос POST /api/v1/exercises
    """
    model_config = ConfigDict(populate_by_name=True)


    title: str
    course_id: str = Field(alias='courseId')
    max_score: int = Field(alias='maxScore')
    min_score: int = Field(alias='minScore')
    order_index: int = Field(alias='orderIndex')
    description: str
    estimated_time: str = Field(alias='estimatedTime')

class CreateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа POST /api/v1/exercises
    """

    exercise: Exercise

class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса PATCH /api/v1/exercises

    """
    title: str | None
    max_score: int | None = Field(alias='maxScore')
    min_score: int | None = Field(alias='minScore')
    order_index: int | None = Field(alias='orderIndex')
    description: str | None
    estimated_time: str | None = Field(alias='estimatedTime')

class UpdateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа PATCH /api/v1/exercises

    """
    exercise: Exercise