from django.contrib import admin
from .models import Reserva, Stand

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display=('cnpj','nome','categoria', 'quitado')

@admin.register(Stand)
class StandAdmin(admin.ModelAdmin):
    list_display=('localizacao','valor')

