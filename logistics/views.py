from django.http import HttpResponse
from django.views.generic import CreateView,UpdateView
from .models import AirFreightCompany,RailwayFreightCompany,RoadFreightCompany,\
                     Truck, Plane, Train,  FreightCompany, Driver, Features
from .serializers import FeatureSerializer, PlaneListSerializer,TrainListSerializer, TruckListSerializer,\
                      DriverSerializer,AirFreightCompanySerializer,RailwayFreightCompanySerializer,\
                      RoadFreightCompanySerializer, FreightCompanySerializer
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin
from .permissions import IsOwnerOrReadOnly
from rest_framework import permissions,filters
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    return HttpResponse("Hello, world. You're at the logistics index.")


class FCCreateView(LoginRequiredMixin, CreateView):
    model = FreightCompany
    fields = ('name', 'type', 'location', 'rating', 'destinations', 'permissions', 'revenue', 'founding_year')
    success_url = 'http://localhost:8100/dashboard'
    template_name = 'fc/fc_create_form.html'


class FCUpdateView(LoginRequiredMixin, UpdateView):
    model = FreightCompany
    fields = ('name', 'type', 'location', 'rating', 'destinations', 'permissions', 'revenue', 'founding_year')
    success_url = 'http://localhost:8100/dashboard'
    template_name = 'fc/fc_update_form.html'


class PlaneCreateView(LoginRequiredMixin,CreateView):
    model = Plane
    fields = ('name', 'types', 'occupied', 'location', 'length', 'maxWeight', 'driver', 'goods', 'company', 'features')
    success_url = 'http://localhost:8100/dashboard'
    template_name = 'vehicles/vehicle_create_form.html'


class PlaneUpdateView(LoginRequiredMixin,UpdateView):
    model = Plane
    fields = ('name', 'types', 'occupied', 'location', 'length', 'maxWeight', 'driver', 'goods', 'company', 'features')
    success_url = 'http://localhost:8100/dashboard'
    template_name = 'vehicles/vehicle_update_form.html'


class TrainCreateView(LoginRequiredMixin, CreateView):
    model = Train
    fields = ('name', 'types', 'occupied', 'location', 'length', 'maxWeight', 'driver', 'goods', 'company', 'features')
    success_url = 'http://localhost:8100/dashboard'
    template_name = 'vehicles/vehicle_create_form.html'


class TrainUpdateView(LoginRequiredMixin,UpdateView):
    model = Train
    fields = ('name', 'types', 'occupied', 'location', 'length', 'maxWeight', 'driver', 'goods', 'company', 'features')
    success_url = 'http://localhost:8100/dashboard'
    template_name = 'vehicles/vehicle_update_form.html'


class TruckCreateView(LoginRequiredMixin, CreateView):
    model = Truck
    fields = ('name', 'types', 'occupied', 'location', 'length', 'maxWeight', 'driver', 'goods', 'company', 'features')
    success_url = 'http://localhost:8100/dashboard'
    template_name = 'vehicles/vehicle_create_form.html'


class TruckUpdateView(LoginRequiredMixin, UpdateView):
    model = Truck
    fields = ('name', 'types', 'occupied', 'location', 'length', 'maxWeight', 'driver', 'goods', 'company', 'features')
    success_url = 'http://localhost:8100/dashboard'
    template_name = 'vehicles/vehicle_update_form.html'


class FreighterList(ReadOnlyModelViewSet):
    serializer_class = FreightCompanySerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    filter_fields = ('name', 'location', 'rating', 'destinations', 'permissions', 'revenue', 'founding_year')
    search_fields = ('name', 'location', 'rating', 'destinations', 'permissions', 'revenue', 'founding_year')
    queryset = FreightCompany.objects.all()


class PlaneListViewSet(ReadOnlyModelViewSet, NestedViewSetMixin):
    serializer_class = PlaneListSerializer

    def get_queryset(self):
        queryset = Plane.objects.all()
        return self.filter_queryset_by_parents_lookups(queryset)


class TrainListViewSet(ReadOnlyModelViewSet, NestedViewSetMixin):
    serializer_class = TrainListSerializer

    def get_queryset(self):
        queryset = Train.objects.all()
        return self.filter_queryset_by_parents_lookups(queryset)


class TruckListViewSet(ReadOnlyModelViewSet, NestedViewSetMixin):
    serializer_class = TruckListSerializer

    def get_queryset(self):
        queryset = Truck.objects.all()
        return self.filter_queryset_by_parents_lookups(queryset)


class FeautureListViewSet(ReadOnlyModelViewSet, NestedViewSetMixin):
    serializer_class = FeatureSerializer
    queryset = Features.objects.all()


class AirFreighterViewSet(ReadOnlyModelViewSet, NestedViewSetMixin):
    serializer_class = AirFreightCompanySerializer
    filter_backends = (filters.SearchFilter,DjangoFilterBackend,)
    search_fields = ('name', 'type', 'location', 'permissions',)
    filter_fields = ('name', 'type', 'location', 'permissions',)
    queryset = AirFreightCompany.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


class RoadFreighterViewSet(ReadOnlyModelViewSet, NestedViewSetMixin):
    serializer_class = RoadFreightCompanySerializer
    filter_backends = (filters.SearchFilter,DjangoFilterBackend,)
    filter_fields = ('name', 'location', 'permissions',)
    search_fields = ('name', 'location', 'permissions',)
    queryset = RoadFreightCompany.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


class RailFreighterViewSet(ReadOnlyModelViewSet, NestedViewSetMixin):
    serializer_class = RailwayFreightCompanySerializer
    queryset = RailwayFreightCompany.objects.all()
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    filter_fields = ('name', 'location', 'permissions',)
    search_fields = ('name', 'location', 'permissions',)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


class DriverViewSet(ReadOnlyModelViewSet, NestedViewSetMixin):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FeatureViewSet(ReadOnlyModelViewSet, NestedViewSetMixin):
    serializer_class = FeatureSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    search_fields = ('name',)
    queryset = Features.objects.all()
