from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet
from .views import index
from .views import CartViewSet, CartItemViewSet
from .views import OrderViewSet


router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'carts', CartViewSet)
router.register(r'cart-items', CartItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', index, name='index'),
    path('carts/<int:pk>/add-to-cart/', CartViewSet.as_view({'post': 'add_to_cart'}), name='add-to-cart'),
    path('carts/<int:pk>/remove-from-cart/', CartViewSet.as_view({'post': 'remove_from_cart'}), name='remove-from-cart'),
    path('carts/<int:pk>/update-cart-item/', CartViewSet.as_view({'post': 'update_cart_item'}), name='update-cart-item'),
    path('orders/create-order/', OrderViewSet.as_view({'post': 'create_order'}), name='create-order'),


]