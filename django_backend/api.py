from rest_framework.routers import DefaultRouter
from logistics.views import AirFreighterViewSet, RoadFreighterViewSet, RailFreighterViewSet,FreighterList,\
      TrainListViewSet, PlaneListViewSet, TruckListViewSet, \
      DriverViewSet,SeaFreighterViewSet,ShipListViewSet, FeatureViewSet, PermissionsViewSet
from rest_framework_extensions.routers import NestedRouterMixin


class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    pass


router = NestedDefaultRouter()
freighters_router = router.register('freighters', FreighterList)
feature_router = router.register('features', FeatureViewSet)
permission_router = router.register('permissions', PermissionsViewSet)
air_router = router.register('airfreight', AirFreighterViewSet).register(
                        'planes', PlaneListViewSet,
                        base_name='freighter-planes',
                        parents_query_lookups=['company']
                    )
road_router = router.register('roadfreight', RoadFreighterViewSet)
road_router.register(
    'trucks', TruckListViewSet,
    base_name='freighter-vehicles',
    parents_query_lookups=['company']
)
rail_router = router.register('railfreight', RailFreighterViewSet)
rail_router.register(
    'trains', TrainListViewSet,
    base_name='freighter-vehicles',
    parents_query_lookups=['company']
)
ship_router = router.register('seafreight', SeaFreighterViewSet)
ship_router.register(
    'ships', ShipListViewSet,
    base_name='freighter-vehicles',
    parents_query_lookups=['company']
)
driver_router = router.register('drivers', DriverViewSet)
