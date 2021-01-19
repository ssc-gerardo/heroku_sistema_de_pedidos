from rest_framework import serializers
from .models import Cliente, Proveedor, Almacen, \
    Sucursal, Empresa, Articulo, \
    PedidoAlmacen, PedidoSucursal, PedidoEmpresa, \
    PedidoDetalleSucursal, \
    PedidoDetalleEmpresa, \
    PedidoDetalleAlamcen


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'


class AlmacenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Almacen
        fields = '__all__'


class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = '__all__'


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'


class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = '__all__'


class PedidoDetalleAlmacenSerializer(serializers.ModelSerializer):

    articulo_descripcion = serializers.ReadOnlyField(
        source='articulo.descripcion')

    class Meta:
        model = PedidoDetalleAlamcen
        fields = '__all__'
        # fields = [
        #     'id', 'pedido', 'articulo', 'cantidad', 'articulo_descripcion']


class PedidoAlmacenSerializer(serializers.ModelSerializer):

    detalle = PedidoDetalleAlmacenSerializer(many=True, read_only=True)

    class Meta:
        model = PedidoAlmacen
        fields = '__all__'
        # fields = [
        #     'id',
        #     'cliente',
        #     'fecha_pedido',
        #     'fecha_surtido',
        #     'urgente',
        #     'almacen',
        #     'detalle']


class PedidoDetalleSucursalSerializer(serializers.ModelSerializer):

    articulo_descripcion = serializers.ReadOnlyField(
        source='articulo.descripcion')

    class Meta:
        model = PedidoDetalleSucursal
        fields = [
            'id', 'pedido', 'articulo', 'cantidad', 'articulo_descripcion']


class PedidoSucursalSerializer(serializers.ModelSerializer):

    detalle = PedidoDetalleSucursalSerializer(many=True, read_only=True)

    class Meta:
        model = PedidoSucursal
        fields = [
            'id',
            'cliente',
            'fecha_pedido',
            'fecha_surtido',
            'urgente',
            'sucursal',
            'detalle']


class PedidoDetalleEmpresaSerializer(serializers.ModelSerializer):

    articulo_descripcion = serializers.ReadOnlyField(
        source='articulo.descripcion')

    class Meta:
        model = PedidoDetalleEmpresa
        fields = [
            'id', 'pedido', 'articulo', 'cantidad', 'articulo_descripcion']


class PedidoEmpresaSerializer(serializers.ModelSerializer):

    detalle = PedidoDetalleEmpresaSerializer(many=True, read_only=True)

    class Meta:
        model = PedidoEmpresa
        fields = [
            'id',
            'cliente',
            'fecha_pedido',
            'fecha_surtido',
            'urgente',
            'empresa',
            'detalle']
