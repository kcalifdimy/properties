


from django.contrib import admin
from properties.api.users.models import User, Profile
from django.utils.translation import gettext_lazy as _

#from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import UserAdmin


class MyUserAdmin(UserAdmin):
    model = User

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        #(_("Personal info"), {"fields": ("email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name','last_name','email', 'type', 'phone_number','password1', 'password2'),
        }),
    )

    list_display = ('first_name','last_name','email','phone_number', 'type', 'id')
    list_editable = ('first_name','last_name','email','phone_number', 'type')
    list_display_links = ('id',)
    list_per_page = 25
    search_fields = ('first_name',)
    ordering = ('email',)

admin.site.register(User, MyUserAdmin)





class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'photo', 'address')
    list_editable = ('bio', 'photo', 'address')



    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('user')
        return queryset


admin.site.register(Profile, UserProfileAdmin)
