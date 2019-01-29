from rest_framework.routers import DefaultRouter
from logistics.views import AirFreighterViewSet, RoadFreighterViewSet, RailFreighterViewSet,FreighterList,\
      TrainListViewSet, PlaneListViewSet, TruckListViewSet, \
      DriverViewSet
from rest_framework_extensions.routers import NestedRouterMixin


class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    pass


router = NestedDefaultRouter()
freighters_router = router.register('freighters', FreighterList)
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
driver_router = router.register('drivers', DriverViewSet)
