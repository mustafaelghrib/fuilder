from uuid import uuid4

from django.db import models


class FormModel(models.Model):

    class Meta:
        db_table = "api_forms"

    form_id = models.UUIDField(primary_key=True, default=uuid4, editable=False, db_index=True)

    title = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    tag = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title


class PageModel(models.Model):

    class Meta:
        db_table = "api_pages"

    page_id = models.UUIDField(primary_key=True, default=uuid4, editable=False, db_index=True)

    title = models.CharField(max_length=100, blank=True, default='Untitled Page')

    created_at = models.DateTimeField(auto_now=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    form = models.ForeignKey(
        FormModel,
        related_name='pages',
        on_delete=models.CASCADE,
        null=True,
        db_index=True
    )

    def __str__(self):
        return self.title


class SectionModel(models.Model):

    class Meta:
        db_table = "api_sections"

    section_id = models.UUIDField(primary_key=True, default=uuid4, editable=False, db_index=True)

    title = models.CharField(max_length=100, blank=True, default='Untitled Section')

    created_at = models.DateTimeField(auto_now=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    page = models.ForeignKey(
        PageModel,
        related_name='sections',
        on_delete=models.CASCADE,
        null=True,
        db_index=True
    )

    def __str__(self):
        return self.title


class QuestionModel(models.Model):

    class Meta:
        db_table = "api_questions"

    question_id = models.UUIDField(primary_key=True, default=uuid4, editable=False, db_index=True)

    title = models.CharField(max_length=255, blank=True, default='Untitled Question')
    type = models.CharField(max_length=255, default='Number')
    is_required = models.BooleanField(default=False)
    is_multi_select = models.BooleanField(default=False)
    is_date = models.BooleanField(default=False)
    is_time = models.BooleanField(default=False)
    answer_value = models.TextField(blank=True)
    answer_image = models.FileField(upload_to='answers/', null=True)
    image = models.FileField(upload_to='questions/', null=True)

    created_at = models.DateTimeField(auto_now=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    section = models.ForeignKey(
        SectionModel,
        related_name='questions',
        on_delete=models.CASCADE,
        null=True,
        db_index=True
    )

    def __str__(self):
        return self.title


class ResponseGroupModel(models.Model):

    class Meta:
        db_table = "api_response_groups"

    response_group_id = models.UUIDField(primary_key=True, default=uuid4, editable=False, db_index=True)
    response_group_title = models.CharField(max_length=255, blank=True, default='Untitled Response Group')
    is_selected = models.BooleanField(default=False, null=True, blank=True)

    created_at = models.DateTimeField(auto_now=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    question = models.OneToOneField(
        QuestionModel, related_name='response_group',
        on_delete=models.CASCADE,
        blank=True,
        null=True, db_index=True
    )

    def __str__(self):
        return self.response_group_title


class ResponseGroupItemModel(models.Model):

    class Meta:
        db_table = "api_response_group_items"

    response_group_item_id = models.UUIDField(primary_key=True, default=uuid4, editable=False, db_index=True)
    response_group_item_title = models.CharField(max_length=255, blank=True, default='Untitled Response Group Item')
    response_group_item_color = models.CharField(max_length=255, blank=True, default='#707070')

    created_at = models.DateTimeField(auto_now=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    response_group = models.ForeignKey(
        ResponseGroupModel,
        related_name='response_group_items',
        on_delete=models.CASCADE,
        null=True, db_index=True
    )

    def __str__(self):
        return self.response_group_item_title


class SliderModel(models.Model):

    class Meta:
        db_table = "api_sliders"

    slider_id = models.UUIDField(primary_key=True, default=uuid4, editable=False, db_index=True)
    slider_min = models.IntegerField(default=10, blank=True)
    slider_max = models.IntegerField(default=100, blank=True)
    slider_step = models.IntegerField(default=10, blank=True)

    created_at = models.DateTimeField(auto_now=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    question = models.OneToOneField(
        QuestionModel, related_name='slider',
        on_delete=models.CASCADE,
        blank=True,
        null=True, db_index=True
    )

    def __str__(self):
        return self.slider_min
