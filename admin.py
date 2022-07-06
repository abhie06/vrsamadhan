from django.contrib import admin
from accc.models import Custom_Approver, Register
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import User
# Register your models here.

admin.site.register(Register)

class PersonAdmin(ImportExportModelAdmin):
    list_display = ('first_name','last_name','username','email','password1','password2')
admin.site.register(Custom_Approver)
