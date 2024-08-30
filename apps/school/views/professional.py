from rest_framework.views import Request

from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.views import APIView

from common.auth import TokenAuth, has_permissions
from common.constants.permission_constants import PermissionConstants
from common.response import result
from school.serializers.professional_serializers import ProfessionalSerializer


class Professional(APIView):
    authentication_classes = [TokenAuth]

    @action(methods=["GET"], detail=False)
    @swagger_auto_schema(
        operation_summary="获取专业信息",
        operation_id="获取专业信息",
        query_serializer=ProfessionalSerializer.Query,
        responses=result.get_api_response(
            ProfessionalSerializer.Query.get_response_body_api()
        ),
        tags=["专业管理"],
    )
    @has_permissions(PermissionConstants.USER_READ)
    def get(self, request: Request):
        school_id = request.query_params.get("school_id")
        professional_id = request.query_params.get("professional_id")
        return result.success(
            ProfessionalSerializer.Query(
                data={"school_id": school_id, "professional_id": professional_id}
            ).list()
        )
