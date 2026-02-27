from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import UsuarioView, UsuarioDetaildView, ImovelView, ImovelDetaildView, ContratoView, ContratoDetaildView, PagamentoView, PagamentoDetaildView
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


# urlpatterns = [
#     path('users', UsuarioView.as_view()),
#     path('usuario/<int:pk>', UsuarioDetaildView.as_view()),
#     path('imoveis', ImovelView.as_view()),
#     path('imovel/<int:pk>', ImovelDetaildView.as_view()),
#     path('contratos', ContratoView.as_view()),
#     path('contrato/<int:pk>', ContratoDetaildView.as_view()),
#     path('pagamentos', PagamentoView.as_view()),
#     path('pagamento/<int:pk>', PagamentoDetaildView.as_view()),
# ]

router = DefaultRouter()

router.register(r'users', UsuarioViewSet)
router.register(r'imoveis', ImovelViewSet)
router.register(r'pagamentos', PagamentoViewSet)
router.register(r'contratos', ContratoViewSet)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('', include(router.urls)),
]