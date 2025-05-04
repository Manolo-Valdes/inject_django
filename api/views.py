import inject

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from domain.contracts.Basic import IGreetings


@api_view(['GET'])
def hello_world(request):
    greetings: IGreetings = inject.instance(IGreetings)
    return Response({"message": greetings.hello('world')})


class MyView(APIView):
    def get(self, request):
        greetings: IGreetings = inject.instance(IGreetings)
        return Response({"message": greetings.hello('world')})
