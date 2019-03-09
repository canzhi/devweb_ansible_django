from django.contrib import admin

from .models import HostGroup, Host, Module, Argument

# Register your models here.

# admin.site.register(HostGroup)
# admin.site.register(Host)
# admin.site.register(Module)
# admin.site.register(Argument)

for item in [HostGroup, Host, Module, Argument]:
    admin.site.register(item)

