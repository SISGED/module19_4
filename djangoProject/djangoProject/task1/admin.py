from django.contrib import admin
from .models import Buyer, Game


# python manage.py createsuperuser
# Username : admin
# Password: admin


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size')
    list_filter = ('size', 'cost')
    list_per_page = 20
    search_fields = ('title',)


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age')
    list_filter = ('balance', 'age')
    list_per_page = 30
    readonly_fields = ('balance',)
    search_fields = ('name',)