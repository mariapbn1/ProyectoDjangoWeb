from django.contrib import admin
from gestionPedidos.models import Clientes, Articulos, Pedidos

# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display = ("nombre", "direccion", "tlfno")
    search_fields = ("nombre", "tlfno")


class ArticulosAdmin(admin.ModelAdmin):
    list_filter = ("seccion",) # -> Campo por el que vamos a filtrar


class PedidoAdmin(admin.ModelAdmin):
    list_display = ("numero", "fecha")
    list_filter = ("fecha",)
    date_hierarchy = "fecha"

admin.site.register(Clientes, ClientesAdmin) # -> Para que el panel de adminsitración tengamos dispoble la tabla de Clientes
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, PedidoAdmin)