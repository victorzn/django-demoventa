#encoding:utf-8
from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
   	
    def __unicode__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(decimal_places=2,default=0, max_digits=5)

    def __unicode__(self):
        return self.nombre

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente)
    detalle_venta = models.ManyToManyField(Producto,through="DetalleVenta")
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(blank=True,decimal_places=2,default=0,editable=True,max_digits=9,null=True,verbose_name='Total')

    def __unicode__(self):
        return self.cliente.nombre

class DetalleVenta(models.Model):
    producto = models.ForeignKey(Producto)
    venta = models.ForeignKey(Venta)
    # precio_venta = models.DecimalField(blank=True,decimal_places=2,default=0,editable=True,max_digits=9,null=True,verbose_name='Precio Venta')
    cantidad = models.PositiveSmallIntegerField(blank=True,default=0,null=True)

    class Meta:
        verbose_name = "Detalle de Venta"
        verbose_name_plural = "Detalle de Venta"

    def __unicode__(self):
        return "%s = %s" % (self.producto.nombre, self.producto.precio)
