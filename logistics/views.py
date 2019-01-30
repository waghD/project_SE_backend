from django.http import HttpResponse
from django.views.generic import CreateView,UpdateView, DeleteView
from .models import AirFreightCompany,RailwayFreightCompany,RoadFreightCompany,\
                     Truck, Plane, Train,  FreightCompany, Driver, Features, Ship,SeaFreightCompany
from .serializers import FeatureSerializer, PlaneListSerializer,TrainListSerializer, TruckListSerializer,\
                      DriverSerializer,AirFreightCompanySerializer,RailwayFreightCompanySerializer,\
                      RoadFreightCompanySerializer, FreightCompanySerializer ,SeaFreightCompanySerializer,\
                      ShipListSerializer
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


class FCDeleteView(LoginRequiredMixin, DeleteView):
    model = FreightCompany
    success_url = 'http://localhost:8100/dashboard'
    template_name = 'fc/fc_delete_form.html'


class PlaneCreateView(LoginRequiredMixin, CreateView):
    model = Plane
    fields = ('name', 'types', 'occupied', 'location', 'length', 'maxWeight', 'driver', 'goods', 'company', 'features')
    success_url = 'http://localhost:8100/dashboard'
    template_name = 'vehicles/vehicle_create_form.html'


class PlaneUpdateView(LoginRequiredMixin, UpdateView):
    model = Plane
    fields = ('name', 'types', 'occupied', 'location', 'length', 'maxWeight', 'driver', 'goods', 'company', 'features')
    success_url = 'http://localhost:8100/dashboard'
    template_name = 'vehicles/vehicle_update_form.html'


class PlaneDeleteView(LoginRequiredMixin, DeleteView):
    model = Plane
    success_url = 'http://localhost:8100/dashboard'
    template_name = 'vehicles/vehicle_delete_form.html'


class TrainCreateView(LoginRequiredMixin, CreateView):
    model = Train
    fields = ('name', 'types', 'occupied', 'location', 'length', 'maxWeight', 'driver', 'goods', 'company', 'features')
    success_url = 'http://localhost:8100/dashboard'
    template_name = 'vehicles/vehicle_create_form.html'


class TrainUpdateView(LoginRequiredMixin, UpdateView):
    model = Train
    fields = ('name', 'types', 'occupied', 'location', 'length', 'maxWeight', 'driver', 'goods', 'company', 'features')
    success_url = 'http://localhost:8100/dashboard'
    template_name = 'vehicles/vehicle_update_form.html'


class TrainDeleteView(LoginRequiredMixin, DeleteView):
    model = Train
    success_url = 'http://localhost:8100/dashboard'
    template_name = 'vehicles/vehicle_delete_form.html'


class ShipCreateView(LoginRequiredMixin, CreateView):
    model = Ship
    fields = ('name', 'types', 'occupied', 'location', 'length', 'maxWeight', 'driver', 'goods', 'company', 'features')
    success_url = 'http://localhost:8100/dashboard'
    template_name = 'vehicles/vehicle_create_form.html'


class ShipUpdateView(LoginRequiredMixin, UpdateView):
    model = Ship
    fields = ('name', 'types', 'occupied', 'location', 'length', 'maxWeight', 'driver', 'goods', 'company', 'features')
    success_url = 'http://localhost:8100/dashboard'
    template_name = 'vehicles/vehicle_update_form.html'


class ShipDeleteView(LoginRequiredMixin, DeleteView):
    model = Ship
    success_url = 'http://localhost:8100/dashboard'
    template_name = 'vehicles/vehicle_delete_form.html'


class TruckCreateView(LoginRequiredMixin, CreateView):
    model = Truck
    fields = ('name', 'licenseplate', 'emission_class','permission_until',
              'types', 'occupied', 'location', 'length', 'maxWeight', 'driver', 'goods', 'company', 'features')
    success_url = 'http://localhost:8100/dashboard'
    template_name = 'vehicles/vehicle_create_form.html'


class TruckUpdateView(LoginRequiredMixin, UpdateView):
    model = Truck
    fields = ('name', 'licenseplate', 'emission_class', 'permission_until',
              'types', 'occupied', 'location', 'length', 'maxWeight', 'driver', 'goods', 'company', 'features')
    success_url = 'http://localhost:8100/dashboard'
    template_name = 'vehicles/vehicle_update_form.html'


class TruckDeleteView(LoginRequiredMixin, DeleteView):
    model = Truck
    success_url = 'http://localhost:8100/dashboard'
    template_name = 'vehicles/vehicle_delete_form.html'


class FeatureCreateView(LoginRequiredMixin, CreateView):
    model = Features
    fields = '__all__'
    success_url = 'http://localhost:8100/dashboard'
    template_name = 'feature/feature_create_form.html'


class FeatureUpdateView(LoginRequiredMixin, UpdateView):
    model = Features
    fields = '__all__'
    success_url = 'http://localhost:8100/dashboard'
    template_name = 'feature/feature_update_form.html'


class FeatureDeleteView(LoginRequiredMixin, DeleteView):
    model = Features
    success_url = 'http://localhost:8100/dashboard'
    template_name = 'feature/feature_delete_form.html'


class DriverCreateView(LoginRequiredMixin, CreateView):
    model = Driver
    fields = '__all__'
    success_url = 'http://localhost:8100/dashboard'
    template_name = 'driver/driver_create_form.html'


class DriverUpdateView(LoginRequiredMixin, UpdateView):
    model = Driver
    fields = '__all__'
    success_url = 'http://localhost:8100/dashboard'
    template_name = 'driver/driver_update_form.html'


class DriverDeleteView(LoginRequiredMixin, DeleteView):
    model = Driver
    success_url = 'http://localhost:8100/dashboard'
    template_name = 'driver/driver_delete_form.html'


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


class ShipListViewSet(ReadOnlyModelViewSet, NestedViewSetMixin):
    serializer_class = ShipListSerializer

    def get_queryset(self):
        queryset = Ship.objects.all()
        return self.filter_queryset_by_parents_lookups(queryset)


class FeautureListViewSet(ReadOnlyModelViewSet, NestedViewSetMixin):
    serializer_class = FeatureSerializer
    queryset = Features.objects.all()


class AirFreighterViewSet(ReadOnlyModelViewSet, NestedViewSetMixin):
    serializer_class = AirFreightCompanySerializer
    filter_backends = (filters.SearchFilter,DjangoFilterBackend,)
    search_fields = ('name', 'location', 'permissions',)
    filter_fields = ('name', 'location', 'permissions',)
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


class SeaFreighterViewSet(ReadOnlyModelViewSet, NestedViewSetMixin):
    serializer_class = SeaFreightCompanySerializer
    queryset = SeaFreightCompany.objects.all()
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
