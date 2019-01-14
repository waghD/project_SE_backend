from rest_framework.routers import DefaultRouter
from logistics.views import AirFreighterViewSet, RoadFreighterViewSet, RailFreighterViewSet,FreighterList,\
     DestinationViewSet, TruckViewSet, TrainViewSet, PlaneViewSet, TrainListViewSet, PlaneListViewSet, TruckListViewSet
from rest_framework_extensions.routers import NestedRouterMixin


class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    pass


router = NestedDefaultRouter()
freighters_router = router.register('freighters', FreighterList)
air_router = router.register('airfreight', AirFreighterViewSet)
air_router.register(
    'planes', PlaneListViewSet,
    base_name='freighter-planes',
    parents_query_lookups=['company']
)
air_router.register(
    'destinations', DestinationViewSet,
    base_name='freighter-destinations',
    parents_query_lookups=['company']
)
road_router = router.register('roadfreight', RoadFreighterViewSet)
road_router.register(
    'trucks', TruckListViewSet,
    base_name='freighter-vehicles',
    parents_query_lookups=['company']
)
road_router.register(
    'destinations', DestinationViewSet,
    base_name='freighter-destinations',
    parents_query_lookups=['company']
)
rail_router = router.register('railfreight', RailFreighterViewSet)
rail_router.register(
    'trains', TrainListViewSet,
    base_name='freighter-vehicles',
    parents_query_lookups=['company']
)
rail_router.register(
    'destinations', DestinationViewSet,
    base_name='freighter-destinations',
    parents_query_lookups=['company']
)
truck_router = router.register('trucks', TruckViewSet)
plane_router = router.register('planes', PlaneViewSet)
train_router = router.register('trains', TrainViewSet)
