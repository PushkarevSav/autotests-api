from http.client import responses

import grpc
import  course_service_pb2
import course_service_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = course_service_pb2_grpc.CourseServiceStub(channel)

response = stub.GetCourses(course_service_pb2.GetCourseRequest(course_id="3"))
print(response)
