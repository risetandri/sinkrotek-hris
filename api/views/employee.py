from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.application.usecase.employee import EmployeeUseCase
from core.infrastructure.repositories.employee import EmployeeRepository
from core.infrastructure.repositories.auth import AuthRepository
from ..serializers.employee import EmployeeSerializer

class EmployeeView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.usecase = EmployeeUseCase(
            EmployeeRepository(), 
            AuthRepository()
        )

    def get(self, request):
        try:
            employee = self.usecase.get_employee()
            serializer = EmployeeSerializer(employee, many=True)

            return Response({
                "status": True,
                "message": "Success",
                "data": serializer.data,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "status": False,
                "message": str(e),
                "data": []
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = EmployeeSerializer(
                data=request.data,
            )
            
            if serializer.is_valid():
                self.usecase.create_employee(request.data)

                return Response({
                    "status": True,
                    "message": "Success",
                    "data": request.data,
                }, status=status.HTTP_201_CREATED)

            return Response({
                "status": False,
                "message": "Error",
                "data": serializer.errors,
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                "status": False,
                "message": str(e),
                "data": []
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def put(self, request, employee_id):
        try:
            return Response({
                "id": 0,
            }, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({
                "message": "test",
            }, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, employee_id):
        try:
            return Response({
                "id": 0,
            }, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({
                "message": "test",
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
