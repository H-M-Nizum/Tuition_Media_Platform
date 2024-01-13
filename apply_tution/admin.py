from django.contrib import admin
from .models import ApplicationModel
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['applicant_name', 'tution_id', 'appaly_status', 'created_time', 'cancel']

    def applicant_name(self, obj):
        return obj.applicant.user.first_name

    def tution_id(self, obj):
        return obj.tution.id

    def save_model(self, request, obj, form, change):
        obj.save()
        if obj.appaly_status == "Selected":
            email_subject = "Your Application is selected"
            email_body = render_to_string('admin_email.html', {'user' : obj.applicant.user, 'tution' : obj.tution})
            
            email = EmailMultiAlternatives(email_subject , '', to=[obj.applicant.user.email])
            email.attach_alternative(email_body, "text/html")
            print('bal')
            email.send()
admin.site.register(ApplicationModel, ApplicationAdmin)