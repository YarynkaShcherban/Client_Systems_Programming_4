from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'authors', AuthorViewSet, basename='authors')
router.register(r'books', BookViewSet, basename='books')
router.register(r'clients', ClientViewSet, basename='clients')
router.register(r'employees', EmployeeViewSet, basename='employees')
router.register(r'genres', GenreViewSet, basename='genres')
router.register(r'positions', PositionViewSet, basename='positions')
router.register(r'publishers', PublisherViewSet, basename='publishers')
router.register(r'purchases', PurchaseViewSet, basename='purchases')
router.register(r'purchase-details', PurchaseDetailViewSet,
                basename='purchase-details')
router.register(r'stores', StoreViewSet, basename='stores')

urlpatterns = router.urls