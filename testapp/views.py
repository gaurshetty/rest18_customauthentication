from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, \
    DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
from .authentications import CustomAuthentication, CustomKeyBasedAuth


class EmployeeModelViewsSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # authentication_classes = [CustomAuthentication]
    authentication_classes = [CustomKeyBasedAuth]
    permission_classes = [IsAuthenticated, IsAdminUser]
