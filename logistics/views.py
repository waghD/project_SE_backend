from django.http import HttpResponse
from .models import FreightCompany
from .serializers import FreightListSerializer,FreightCompanySerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers


def index(request):
    return HttpResponse("Hello, world. You're at the logistics index.")


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'freighters': reverse('freighter-list', request=request, format=format)
    })


class FreighterList(generics.ListCreateAPIView):
    queryset = FreightCompany.objects.all()
    serializer_class = FreightListSerializer


class FreighterCompany(generics.RetrieveUpdateDestroyAPIView):
    queryset = FreightCompany.objects.all()
    serializer_class = FreightCompanySerializer


class FreighterHighlight(generics.GenericAPIView):
    queryset = FreightCompany.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        freighter = self.get_object()
        return Response(freighter.highlighted)
