from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from django.contrib.auth.forms import UserCreationForm

# Register your models here.
class UserCreateForm(UserCreationForm):
  class Meta:
    model = User
    fields = ('email','first_name','middle_name','last_name','phone_number','is_admin','is_staff')

class NewUserAdmin(UserAdmin):
  add_form=UserCreateForm
  add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','first_name','middle_name', 'last_name', 'password1', 'password2','phone_number' ),
        }),
    )
  list_display=('email','first_name','is_admin')
  search_fields=('email',)
  readonly_fields=('id',)
  filter_horizontal=()
  list_filter=()
  fieldsets=()
  ordering=('email',)
  
admin.site.register(User,NewUserAdmin)