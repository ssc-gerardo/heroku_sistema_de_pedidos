from django.urls import path, include
from rest_framework import routers
from .views import ClienteViewSet, ProveedorViewSet, AlmacenViewSet, \
    SucursalViewSet, EmpresaViewSet, ArticuloViewSet, \
    PedidoDetalleAlmacenViewSet, PedidoDetalleEmpresaViewSet,\
    PedidoDetalleSucursalViewSet, \
    PedidoEmpresaViewSet, PedidoSucursalViewSet, PedidoAlmacenViewSet


router = routers.DefaultRouter()
router.register(r'cliente', ClienteViewSet)
router.register(r'proveedor', ProveedorViewSet)
router.register(r'almacen', AlmacenViewSet)
router.register(r'sucursal', SucursalViewSet)
router.register(r'empresa', EmpresaViewSet)
router.register(r'articulo', ArticuloViewSet)

router.register(r'pedido_detalle_almacen', PedidoDetalleAlmacenViewSet)
router.register(r'pedido_detalle_sucursal', PedidoDetalleSucursalViewSet)
router.register(r'pedido_detalle_empresa', PedidoDetalleEmpresaViewSet)

router.register(
    r'pedido_almacen', PedidoAlmacenViewSet, basename='PedidoAlmacen')
router.register(r'pedido_sucursal', PedidoSucursalViewSet)
router.register(r'pedido_empresa', PedidoEmpresaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
