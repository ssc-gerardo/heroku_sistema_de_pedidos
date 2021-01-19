from rest_framework import viewsets

from .models import Cliente, Proveedor, Almacen, \
    Sucursal, Empresa, Articulo, \
    PedidoDetalleAlamcen, PedidoDetalleEmpresa, PedidoDetalleSucursal, \
    PedidoAlmacen, PedidoEmpresa, PedidoSucursal
from .serializers import \
    ClienteSerializer, ProveedorSerializer, ArticuloSerializer, \
    AlmacenSerializer, SucursalSerializer, EmpresaSerializer, \
    PedidoDetalleAlmacenSerializer, PedidoDetalleSucursalSerializer, \
    PedidoDetalleEmpresaSerializer, \
    PedidoAlmacenSerializer, PedidoSucursalSerializer, \
    PedidoEmpresaSerializer
# Create your views here.


class ClienteViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Cliente.objects.all().order_by('id')
    serializer_class = ClienteSerializer


class ProveedorViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Proveedor.objects.all().order_by('id')
    serializer_class = ProveedorSerializer


class AlmacenViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Almacen.objects.all().order_by('id')
    serializer_class = AlmacenSerializer


class SucursalViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Sucursal.objects.all().order_by('id')
    serializer_class = SucursalSerializer


class EmpresaViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Empresa.objects.all().order_by('id')
    serializer_class = EmpresaSerializer


class ArticuloViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Articulo.objects.all().order_by('id')
    serializer_class = ArticuloSerializer


class PedidoDetalleAlmacenViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = PedidoDetalleAlamcen.objects.all().order_by('id')
    serializer_class = PedidoDetalleAlmacenSerializer


class PedidoAlmacenViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    # queryset = PedidoAlmacen.objects.all().order_by('id')
    serializer_class = PedidoAlmacenSerializer
    # http_method_names = ['get']

    def get_queryset(self):
        queryset = PedidoAlmacen.objects.all()
        urgentes_platino = self.request.query_params.get(
            'urgentes_platino', None)
        if urgentes_platino is not None:
            print("hola!!")
            queryset = queryset.filter(
                cliente__tipo_de_cliente='PO', surtido=False, urgente=True)
        return queryset


class PedidoDetalleSucursalViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = PedidoDetalleSucursal.objects.all().order_by('id')
    serializer_class = PedidoDetalleSucursalSerializer


class PedidoSucursalViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = PedidoSucursal.objects.all().order_by('id')
    serializer_class = PedidoSucursalSerializer


class PedidoDetalleEmpresaViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = PedidoDetalleEmpresa.objects.all().order_by('id')
    serializer_class = PedidoDetalleEmpresaSerializer


class PedidoEmpresaViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = PedidoEmpresa.objects.all().order_by('id')
    serializer_class = PedidoEmpresaSerializer
