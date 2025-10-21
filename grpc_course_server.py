import grpc
from concurrent import futures

import course_service_pb2
import course_service_pb2_grpc
from course_service_pb2_grpc import CourseServiceServicer


class CourseServiceServicer(course_service_pb2_grpc.CourseServiceServicer):
    def GetCourses(self, request, context):
        print(f'Получен запрос к методу GetCourses от пользователя: {request.course_id}')
        return course_service_pb2.GetCourseResponse(course_id=request.course_id,
                                                    title= 'Автотесты API',
                                                    description= 'Будем изучать написание API автотестов')

def serve():
    """Функция создает и запускает gRPC-сервер"""

    # Создаем сервер с использованием пула потоков (до 10 потоков)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

     # Регистрируем сервис UserService на сервере
    course_service_pb2_grpc.add_CourseServiceServicer_to_server(CourseServiceServicer(), server)

    # Настраиваем сервер для прослушивания порта 50051
    server.add_insecure_port('[::]:50051')

    # Запускаем сервер
    server.start()
    print("gRPC сервер запущен на порту 50051...")

    # Ожидаем завершения работы сервера
    server.wait_for_termination()

if __name__ == "__main__":
    serve()