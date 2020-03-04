from django.contrib import admin

from .models import Question,Choice,Dashboard

class QuestionAdmin(admin.ModelAdmin):
    list_display=('question_text','pub_date','choice')
    def choice(self, obj):
        return obj.choice_set.all() 


class DashboardAdmin(admin.ModelAdmin):
    list_display=('wom', 'customer' , 'contract_value', 'paid_by_customer_formated', 'unpaid_by_customer_formated','cost_paid', 'cost_to_finish', 'deadline', 'finish_estimation', 'invoice_sent', 'invoice_sent_days', 'pic', 'note')
    def paid_by_customer_formated(self , obj):
        return "%2f" % obj.paid_by_customer
    paid_by_customer_formated.short_description = "Paid by Customer"

    def unpaid_by_customer_formated(self , obj):
        return "%2f" % obj.unpaid_by_customer
    unpaid_by_customer_formated.short_description = "Unpaid by Customer"


admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Dashboard,DashboardAdmin)



# Register your models here.
