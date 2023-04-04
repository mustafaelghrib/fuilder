from .builder import Builder
from ..products.form import Form


class FormBuilder(Builder):

    _form: Form = Form()

    def build(self, data):
        form = self._form.add_form(data)
        for page_data in data["pages"]:
            page = self._form.add_page(form, page_data)
            for section_data in page_data["sections"]:
                section = self._form.add_section(page, section_data)
                for question_data in section_data["questions"]:
                    self._form.add_question(section, question_data)
        return form





