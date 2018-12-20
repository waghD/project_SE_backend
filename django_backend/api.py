from rest_framework.routers import DefaultRouter
from logistics.views import FreighterViewSet,TruckViewSet,DestinationViewSet
from rest_framework_extensions.routers import NestedRouterMixin


class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    pass


router = NestedDefaultRouter()
freighters_router = router.register('freighters', FreighterViewSet)
freighters_router.register(
    'trucks', TruckViewSet,
    base_name='freighter-trucks',
    parents_query_lookups=['company']
)
freighters_router.register(
    'destinations',DestinationViewSet,
    base_name='freighter-destinations',
    parents_query_lookups=['company']
)
