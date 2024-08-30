import os

from django.db.models import QuerySet
from rest_framework import serializers
from common.mixins.api_mixin import ApiMixin
from common.util.field_message import ErrMessage
from school.models import School, Professional
from drf_yasg import openapi


class ProfessionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professional
        fields = "__all__"

    class Query(ApiMixin, serializers.Serializer):
        school_id = serializers.CharField(
            required=True, error_messages=ErrMessage.char("学校code")
        )
        professional_id = serializers.CharField(
            required=False, allow_null=True, error_messages=ErrMessage.char("专业code")
        )

        def list(self, with_valid=True):
            if with_valid:
                self.is_valid(raise_exception=True)
            school_id = self.data.get("school_id")
            professional_id = self.data.get("professional_id")
            professional_list = Professional.objects.filter(school_id=school_id)
            if professional_id:
                professional_list = professional_list.filter(id=professional_id)

            return [
                {
                    "id": professional.id,
                    "school_id": professional.school_id,
                    "special_id": professional.special_id,
                    "nation_feature": professional.nation_feature,
                    "province_feature": professional.province_feature,
                    "is_important": professional.is_important,
                    "limit_year": professional.limit_year,
                    "year": professional.year,
                    "level3_weight": professional.level3_weight,
                    "nation_first_class": professional.nation_first_class,
                    "xueke_rank_score": professional.xueke_rank_score,
                    "is_video": professional.is_video,
                    "special_name": professional.special_name,
                    "special_type": professional.special_type,
                    "type_name": professional.type_name,
                    "level3_name": professional.level3_name,
                    "level3_code": professional.level3_code,
                    "level2_name": professional.level2_name,
                    "level2_id": professional.level2_id,
                    "level2_code": professional.level2_code,
                    "code": professional.code,
                    "course": professional.course,
                }
                for professional in professional_list
            ]

        @staticmethod
        def get_request_params_api():
            return [
                openapi.Parameter(
                    name="school_id",
                    in_=openapi.IN_QUERY,
                    type=openapi.TYPE_STRING,
                    required=True,
                    description="供应名称",
                ),
                openapi.Parameter(
                    name="professional_id",
                    in_=openapi.IN_QUERY,
                    type=openapi.TYPE_STRING,
                    required=True,
                    description="模型类型",
                ),
            ]

        @staticmethod
        def get_response_body_api():
            return openapi.Schema(
                type="object",
                # required=[  ],
                properties={
                    "id": openapi.Schema(type=openapi.TYPE_STRING, description="id"),
                    "school_id": openapi.Schema(
                        type=openapi.TYPE_STRING, description="school_id"
                    ),
                    "special_id": openapi.Schema(
                        type=openapi.TYPE_STRING, description="special_id"
                    ),
                    "nation_feature": openapi.Schema(
                        type=openapi.TYPE_STRING, description="nation_feature"
                    ),
                    "province_feature": openapi.Schema(
                        type=openapi.TYPE_STRING, description="province_feature"
                    ),
                    "is_important": openapi.Schema(
                        type=openapi.TYPE_STRING, description="is_important"
                    ),
                    "limit_year": openapi.Schema(
                        type=openapi.TYPE_STRING, description="limit_year"
                    ),
                    "year": openapi.Schema(
                        type=openapi.TYPE_STRING, description="year"
                    ),
                    "level3_weight": openapi.Schema(
                        type=openapi.TYPE_STRING, description="level3_weight"
                    ),
                    "nation_first_class": openapi.Schema(
                        type=openapi.TYPE_STRING, description="nation_first_class"
                    ),
                    "xueke_rank_score": openapi.Schema(
                        type=openapi.TYPE_STRING, description="xueke_rank_score"
                    ),
                    "is_video": openapi.Schema(
                        type=openapi.TYPE_STRING, description="is_video"
                    ),
                    "special_name": openapi.Schema(
                        type=openapi.TYPE_STRING, description="special_name"
                    ),
                    "special_type": openapi.Schema(
                        type=openapi.TYPE_STRING, description="special_type"
                    ),
                    "type_name": openapi.Schema(
                        type=openapi.TYPE_STRING, description="type_name"
                    ),
                    "level3_name": openapi.Schema(
                        type=openapi.TYPE_STRING, description="level3_name"
                    ),
                    "level3_code": openapi.Schema(
                        type=openapi.TYPE_STRING, description="level3_code"
                    ),
                    "level2_name": openapi.Schema(
                        type=openapi.TYPE_STRING, description="level2_name"
                    ),
                    "level2_id": openapi.Schema(
                        type=openapi.TYPE_STRING, description="level2_id"
                    ),
                    "level2_code": openapi.Schema(
                        type=openapi.TYPE_STRING, description="level2_code"
                    ),
                    "code": openapi.Schema(
                        type=openapi.TYPE_STRING, description="code"
                    ),
                    "course": openapi.Schema(
                        type=openapi.TYPE_STRING, description="course"
                    ),
                },
            )
