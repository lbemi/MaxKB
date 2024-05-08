from rest_framework.views import Request

from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.views import APIView

from common.auth import TokenAuth, has_permissions
from common.constants.permission_constants import PermissionConstants
from common.response import result
from school.serializers.school_serializers import SchoolSerializer


class School(APIView):
    authentication_classes = [TokenAuth]

    @action(methods=['GET'], detail=False)
    @swagger_auto_schema(operation_summary="获取学校列表信息",
                         operation_id="获取学校列表信息",
                         query_serializer=SchoolSerializer.Query,
                         responses=result.get_api_response(
                             SchoolSerializer.Query.get_response_body_api()),
                         tags=['学校管理'])
    @has_permissions(PermissionConstants.USER_READ)
    def get(self, request: Request):
        return result.success(SchoolSerializer.Query(data={'school_name': request.query_params.get("school_name")}).list())
