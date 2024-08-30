import os

from django.db.models import QuerySet
from rest_framework import serializers
from common.mixins.api_mixin import ApiMixin
from common.util.field_message import ErrMessage
from school.models import School
from drf_yasg import openapi


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"

    class Query(ApiMixin, serializers.Serializer):
        school_name = serializers.CharField(
            required=False, allow_null=True, error_messages=ErrMessage.char("学校名称")
        )

        def list(self, with_valid=True):
            if with_valid:
                self.is_valid(raise_exception=True)
            school_name = self.data.get("school_name")
            if not school_name:
                school_name = ""
            schools = School.objects.filter(name__contains=school_name)
            return [
                {
                    "code": school.code,
                    "name": school.name,
                    "f985": school.f985,
                    "f211": school.f211,
                    "p": school.p,
                    "c": school.c,
                    "qj": school.qj,
                    "answer_url": school.answer_url,
                    "dual_class": school.dual_class,
                    "nature": school.nature,
                    "level": school.level,
                }
                for school in schools
            ]

        @staticmethod
        def get_request_params_api():
            return openapi.Parameter(
                name="school_name",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=False,
            )

        @staticmethod
        def get_response_body_api():
            return openapi.Schema(
                type="object",
                required=[
                    "code",
                    "name",
                    "f985",
                    "f211",
                    "p",
                    "c",
                    "qj",
                    "answer_url",
                    "dual_class",
                    "nature",
                    "level",
                ],
                properties={
                    "code": openapi.Schema(type=openapi.TYPE_STRING),
                    "name": openapi.Schema(type=openapi.TYPE_STRING),
                    "f985": openapi.Schema(type=openapi.TYPE_STRING),
                    "f211": openapi.Schema(type=openapi.TYPE_STRING),
                    "p": openapi.Schema(type=openapi.TYPE_STRING),
                    "c": openapi.Schema(type=openapi.TYPE_STRING),
                    "qj": openapi.Schema(type=openapi.TYPE_STRING),
                    "answer_url": openapi.Schema(type=openapi.TYPE_STRING),
                    "dual_class": openapi.Schema(type=openapi.TYPE_STRING),
                    "nature": openapi.Schema(type=openapi.TYPE_STRING),
                    "level": openapi.Schema(type=openapi.TYPE_STRING),
                },
            )
