from django.db import models


# Create your models here.


class Cliente(models.Model):
    TIPOS_DE_CLIENTE = [
        ('NO', 'NOMRAL'),
        ('PL', 'PLATA'),
        ('OR', 'ORO'),
        ('PO', 'PLATINO'),
    ]
    nombre = models.CharField(max_length=50, null=False, blank=False)
    codigo = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        unique=True)
    foto = models.ImageField(
        upload_to="images/",
        blank=True,
        null=True)
    dreccion = models.CharField(
        max_length=200,
        null=False,
        blank=False)
    tipo_de_cliente = models.CharField(
        max_length=2,
        choices=TIPOS_DE_CLIENTE,
        default='NO')

    def __str__(self):
        return '{}-{}-{}'.format(
            self.codigo,
            self.nombre,
            self.tipo_de_cliente
        )

    class Meta:
        verbose_name_plural = "Clientes"


class Proveedor(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    direccion = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Proeedores"


class Almacen(models.Model):
    codigo = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.codigo

    class Meta:
        verbose_name_plural = "Almacenes"


class Sucursal(models.Model):
    referncia = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        unique=True)
    codigo = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.codigo

    class Meta:
        verbose_name_plural = "Almacenes"


class Empresa(models.Model):
    referncia = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        unique=True
    )
    codigo_de_socio = models.CharField(max_length=50, null=False, blank=False)
    detalle_pedido = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return '{}-{}'.format(self.codigo_de_socio, self.referncia)

    class Meta:
        verbose_name_plural = "Empresas"


class Articulo(models.Model):
    codigo = models.IntegerField(
        null=False,
        blank=False,
        unique=True)
    descripcion = models.CharField(max_length=200, null=False, blank=False)
    proveedores = models.ManyToManyField(Proveedor)

    def __str__(self):
        return '{}-{}'.format(self.codigo, self.descripcion)

    class Meta:
        verbose_name_plural = "Articulos"


class PedidoAlmacen(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_pedido = models.DateField(auto_now_add=True)
    fecha_surtido = models.DateField(null=True, blank=True)
    urgente = models.BooleanField(default=False)
    surtido = models.BooleanField(default=False)
    almacen = models.ForeignKey(
        Almacen, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Pedidos Almacen"


class PedidoSucursal(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_pedido = models.DateField(auto_now_add=True)
    fecha_surtido = models.DateField(null=True, blank=True)
    urgente = models.BooleanField(default=False)
    surtido = models.BooleanField(default=False)
    sucursal = models.ForeignKey(
        Sucursal, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Pedidos Sucursal"


class PedidoEmpresa(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_pedido = models.DateField(auto_now_add=True)
    fecha_surtido = models.DateField(null=True, blank=True)
    urgente = models.BooleanField(default=False)
    surtido = models.BooleanField(default=False)
    empresa = models.ForeignKey(
        Empresa, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Pedidos Empresa"


class PedidoDetalleAlamcen(models.Model):

    pedido = models.ForeignKey(
        PedidoAlmacen, related_name='detalle', on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.DO_NOTHING)
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return '{}-{}-{}'.format(
            self.pedido,
            self.articulo,
            self.cantidad)

    class Meta:
        verbose_name_plural = "Detalles de pedido a Almacen"


class PedidoDetalleSucursal(models.Model):

    pedido = models.ForeignKey(
        PedidoSucursal, related_name='detalle', on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.DO_NOTHING)
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return '{}-{}-{}-{}'.format(
            self.id,
            self.pedido,
            self.articulo,
            self.cantidad)

    class Meta:
        verbose_name_plural = "Detalles de pedido a Sucursal"


class PedidoDetalleEmpresa(models.Model):

    pedido = models.ForeignKey(
        PedidoEmpresa, related_name='detalle', on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.DO_NOTHING)
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return '{}-{}-{}-{}'.format(
            self.id,
            self.pedido,
            self.articulo,
            self.cantidad)

    class Meta:
        verbose_name_plural = "Detalles de pedido a Empresa"
