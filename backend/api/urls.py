from django.urls import path
from .views import *

urlpatterns = [
    path('usuarios', listar_usuarios),
    path('users', UsuarioView.as_view()),
    path('usuario/<int:pk>', UsuarioDetailView.as_view()),

    path('imoveis', ImovelView.as_view()),
    path('imovel/<int:pk>', ImovelDetailView.as_view()),

    path('contratos', ContratoView.as_view()),
    path('contrato/<int:pk>', ContratoDetailView.as_view()),

    path('pagamentos', PagamentoView.as_view()),
    path('pagamento/<int:pk>', PagamentoDetailView.as_view()),

]
