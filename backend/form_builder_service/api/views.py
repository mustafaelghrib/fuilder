from rest_framework import views, status
from rest_framework.response import Response

from .form_builder.builder.form_builder import FormBuilder
from .serializers import FormSerializer


class FormsAPI(views.APIView):

    @staticmethod
    def build_form(request):

        form_builder = FormBuilder()
        form = form_builder.build(request.data)

        return Response({
            "status": status.HTTP_200_OK,
            "message": "Form built successfully",
            "form": FormSerializer(form).data
        })

    def post(self, request):
        return self.build_form(request)
