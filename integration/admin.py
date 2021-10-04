from django.contrib import admin
from django.forms.models import modelform_factory
from integration.models import  *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import UserAdmin
from django.forms import ModelForm



class UserExtensionForm(ModelForm):
    fields = ('token')

class UserExtensionInLine(admin.StackedInline):
    model = IntegrationUser
    form = UserExtensionForm
    can_delete = False
    fieldsets = (
        (None, {
            'fields': ('token',)
        }),)


class UserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'get_token', 'email', 'get_groups')
    search_fields = ('first_name', 'last_name', 'username')
    list_filter = ('groups', 'is_active')
    inlines = (UserExtensionInLine, )
    fieldsets_top = (
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
    )
    normaluser_fieldsets = (
        (('Permissions'), {'fields': ('is_active', 'is_staff',
                                      'groups')}),
    )
    superuser_fieldsets = (
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                      'groups', 'user_permissions')}),
    )
    admin_fieldsets = (
        (('Permissions'), {'fields': ('is_active', 'is_staff',
                                      'groups')}),
    )
    fieldsets_bottom = (
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    def get_groups(self, obj):
        if obj.groups is not None:
            groups_output = []
            groups = obj.groups.all()
            for p in groups:
                groups_output.append(p.name)
            return ", ".join(groups_output)
        else:
            return ""

    get_groups.short_description = 'Groups'
    get_groups.admin_order_field = 'groups'


    def get_token(self, obj):
        if hasattr(obj, 'integrationuser') and obj.integrationuser.token is not None:
            return obj.integrationuser.token
        else:
            return  ""

    get_token.short_description = 'Token'
    get_token.admin_order_field = 'Token'



class DealAdministration(admin.ModelAdmin):
    list_display = ('dealId', 'dealname', 'amount', 'closedate', 'dealtype','dealstage')
    search_fields = ('dealname',)


# Register your models here.

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Deal, DealAdministration)
