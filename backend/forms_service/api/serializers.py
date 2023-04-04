from rest_framework.serializers import ModelSerializer

from .models import *


class SliderSerializer(ModelSerializer):
    class Meta:
        model = SliderModel
        fields = [
            'question',
            'slider_id',
            'slider_min',
            'slider_max',
            'slider_step',
            'created_at',
            'updated_at'
        ]


class ResponseGroupItemSerializer(ModelSerializer):
    class Meta:
        model = ResponseGroupItemModel
        fields = [
            'response_group',
            'response_group_item_id',
            'response_group_item_title',
            'response_group_item_color',
            'created_at',
            'updated_at'
        ]


class ResponseGroupSerializer(ModelSerializer):

    response_group_items = ResponseGroupItemSerializer(many=True, read_only=True)

    class Meta:
        model = ResponseGroupModel
        fields = [
            'question',
            'response_group_id',
            'response_group_title',
            'response_group_items',
            'is_selected',
            'created_at',
            'updated_at'
        ]


class QuestionSerializer(ModelSerializer):

    class Meta:
        model = QuestionModel
        fields = [
            'section',
            'question_id',
            'title',
            'created_at',
            'updated_at'
        ]


class SectionSerializer(ModelSerializer):

    questions = QuestionSerializer(many=True, required=False)

    class Meta:
        model = SectionModel
        fields = [
            'page',
            'section_id',
            'title',
            'questions',
            'created_at',
            'updated_at'
        ]


class PageSerializer(ModelSerializer):

    sections = SectionSerializer(many=True, read_only=True)

    class Meta:
        model = PageModel
        fields = [
            'form',
            'page_id',
            'title',
            'sections',
            'created_at',
            'updated_at'
        ]


class FormSerializer(ModelSerializer):

    pages = PageSerializer(many=True, read_only=True)

    class Meta:
        model = FormModel
        fields = [
            'form_id',
            'title',
            'type',
            'pages',
            'created_at',
            'updated_at'
        ]
