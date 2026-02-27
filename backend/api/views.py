from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario, Imovel, Contrato, Pagamento
from .serializers import UsuarioSerializer, ImovelSerializer, ContratoSerializer, PagamentoSerializer, RegisterSerializer
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .filters import UsuarioFilter




class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    # permission_classes = [IsAuthenticated]

    #filtro basico
    # def get_queryset(self):
    #     tipo = self.request.query_params.get('tipo')
    #     if tipo:
    #         self.queryset = self.queryset.filter(tipo=tipo)
        
    #     return self.queryset

    #Fitros declarativos
    filter_backends = [DjangoFilterBackend]
    filterset_class = UsuarioFilter

class ImovelViewSet(ModelViewSet):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer

    # def get_queryset(self):
    #     status = self.request.query_params.get('status')
    #     tipo = self.request.query_params.get('tipo')

    #     if status:
    #         self.queryset = self.queryset.filter(status=status)
    #     if tipo:
    #         self.queryset = self.queryset.filter(tipo=tipo)
        
    #     return self.queryset

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tipo', 'status']

class PagamentoViewSet(ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer

class ContratoViewSet(ModelViewSet):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'Usuario criado com sucesso'}, status=status.HTTP_201_CREATED)

class MeView(RetrieveAPIView):
    serializer_class = UsuarioSerializer

    def get_object(self, request):
        perfil, created = Usuario.objects.get_or_create(
            user = self.request.user,
            defaults={
                'nome': self.request.user.username,
                'email': self.request.user.email,
                'tipo': 'USER'
            }
        ) 

        return perfil








# ############################ GENERICS ##########################

# # class UsuarioView(ListCreateAPIView):
# #     queryset = Usuario.objects.all()
# #     serializer_class = UsuarioSerializer

# # class UsuarioDetaildView(RetrieveUpdateDestroyAPIView):
# #     queryset = Usuario.objects.all()
# #     serializer_class = UsuarioSerializer

# # # Imovel

# # class ImovelView(ListCreateAPIView):
# #     queryset = Imovel.objects.all()
# #     serializer_class = ImovelSerializer

# # class ImovelDetailView(RetrieveUpdateDestroyAPIView):
# #     queryset = Imovel.objects.all()
# #     serializer_class = ImovelSerializer

# # # Contrato

# # class ContratoView(ListCreateAPIView):
# #     queryset = Contrato.objects.all()
# #     serializer_class = ContratoSerializer

# # class ContratoDetailView(RetrieveUpdateDestroyAPIView):
# #     queryset = Contrato.objects.all()
# #     serializer_class = ContratoSerializer

# # # Pagamento

# # class PagamentoView(ListCreateAPIView):
# #     queryset = Pagamento.objects.all()
# #     serializer_class = PagamentoSerializer

# # class PagamentoDetailView(RetrieveUpdateDestroyAPIView):
# #     queryset = Pagamento.objects.all()
# #     serializer_class = PagamentoSerializer



# ############################ APIView ##############################

# class UsuarioView(APIView):
#     def get(self, request):
#         usuarios = Usuario.objects.all()
#         serializer = UsuarioSerializer(usuarios, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = UsuarioSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UsuarioDetaildView(APIView):
#     def get_object(self, pk):
#         return Usuario.objects.get(pk=pk)

#     def get(self, request, pk):
#         usuario = self.get_object(pk)
#         serializer = UsuarioSerializer(usuario)
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         usuario = self.get_object(pk)
#         serializer = UsuarioSerializer(usuario, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         usuario = self.get_object(pk)
#         usuario.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# ###################
# class ImovelView(APIView):
#     def get(self, request):
#         imoveis = Imovel.objects.all()
#         serializer = ImovelSerializer(imoveis, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = ImovelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ImovelDetaildView(APIView):
#     def get_object(self, pk):
#         return Imovel.objects.get(pk=pk)

#     def get(self, request, pk):
#         imovel = self.get_object(pk)
#         serializer = ImovelSerializer(imovel)
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         imovel = self.get_object(pk)
#         serializer = ImovelSerializer(imovel, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         imovel = self.get_object(pk)
#         imovel.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# ###################
# class ContratoView(APIView):
#     def get(self, request):
#         contratos = Contrato.objects.all()
#         serializer = ContratoSerializer(contratos, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = ContratoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ContratoDetaildView(APIView):
#     def get_object(self, pk):
#         return Contrato.objects.get(pk=pk)

#     def get(self, request, pk):
#         contrato = self.get_object(pk)
#         serializer = ContratoSerializer(contrato)
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         contrato = self.get_object(pk)
#         serializer = ContratoSerializer(contrato, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         contrato = self.get_object(pk)
#         contrato.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# ###################
# class PagamentoView(APIView):
#     def get(self, request):
#         pagamentos = Pagamento.objects.all()
#         serializer = PagamentoSerializer(pagamentos, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = PagamentoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class PagamentoDetaildView(APIView):
#     def get_object(self, pk):
#         return Pagamento.objects.get(pk=pk)

#     def get(self, request, pk):
#         pagamento = self.get_object(pk)
#         serializer = PagamentoSerializer(pagamento)
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         pagamento = self.get_object(pk)
#         serializer = PagamentoSerializer(pagamento, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         pagamento = self.get_object(pk)
#         pagamento.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# ###################





############################# ModelViewSet #########################

