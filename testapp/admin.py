from django.contrib import admin
from .models import report, enggdetails
# Register your models here.
class reportadmin(admin.ModelAdmin):
    list_display = ['fullname_staff','username_staff','engg','total_points','feedbackpos', 'feedbackneg','feedbacknul','fedbackcomp']

class enggadmin(admin.ModelAdmin):
    list_display = ['engg_username', 'engg_fullname', 'complainid', 'point']
admin.site.register(report, reportadmin)
admin.site.register(enggdetails, enggadmin)

admin.site.site_header = "Feedback admin"
admin.site.site_title = 'Feedback form'