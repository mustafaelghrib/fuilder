from ...models import (
    FormModel, PageModel,
    SectionModel, QuestionModel
)


class Form:

    def add_form(self, form_data):
        form = FormModel(title=form_data["title"], type=form_data["type"])
        form.save()
        return form

    def add_page(self, form, page_data):
        page = PageModel(title=page_data["title"], form=form)
        page.save()
        return page

    def add_section(self, page, section_data):
        section = SectionModel(title=section_data["title"], page=page)
        section.save()
        return section

    def add_question(self, section, question_data):
        question = QuestionModel(title=question_data["title"], section=section)
        question.save()
        return question
