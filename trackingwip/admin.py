from django.contrib import admin,messages
from .models import Question,Choice,Dashboard

class NoLoginSite(admin.AdminSite):
    site_header = 'WIP Tracking'
    site_title = 'WIP Tracking'
    index_title = 'WIP Tracking'

    def login(self, request, extra_context=None):
        if not request.user.is_authenticated:
            from django.contrib.auth import authenticate, login as auth_login
            try:
                user = authenticate(request, username='anonymous', password="anonymous")
                auth_login(request, user)
            except:
                messages.add_message(request,messages.ERROR,"no anoymous user registered")
        return super().login(request,extra_context=extra_context)

class QuestionAdmin(admin.ModelAdmin):
    list_display=('question_text','pub_date','choice')
    def choice(self, obj):
        return obj.choice_set.all() 


class DashboardAdmin(admin.ModelAdmin):

    search_fields =('wom', 'customer', 'pic')

    personel={
        "940004" : "CHAIRUL ANWAR LUBIS",
        "871146" : "FERI SURYAKUSUMAH",
        "120003" : "TONI GUSTANI",
        "871454" : "DWI FADJAR DISTIANTONO",
        "871413" : "BUDI SETYONO",
        "871545" : "BAMBANG HARIYANTO",
        "920621" : "IRWAN WAHYU",
        "900056" : "TARYADI",
        "880141" : "MEINGKAR S.",
        "999086" : "MARGINATA SEBESTINA",
        "871520" : "AGUS WAWAN",
        "170013" : "EDI SUPRIADI AR",
        "821462" : "EDI SUPRIADI AR",
        "130012" : "ADITYO DWINANDA",
        "999055" : "AFIYAN NAJAT",
        "960057" : "RUDI PERMADI",
        


    }

    list_display=('wom', 'customer' , 'contract_value_formated',  'pic_name', 'paid_by_customer_formated', 'unpaid_by_customer_formated', 'cost_paid_formated', 'cost_to_finish_formated', 'deadline', 'finish_estimation', 'note')
    def paid_by_customer_formated(self , obj):
        return "{:0,.2f}".format(obj.paid_by_customer)
    paid_by_customer_formated.short_description = "Paid by Customer"
    paid_by_customer_formated.admin_order_field = "paid_by_customer"

    def unpaid_by_customer_formated(self , obj):
        return "{:0,.2f}".format(obj.unpaid_by_customer)
    unpaid_by_customer_formated.short_description = "Unpaid by Customer"
    unpaid_by_customer_formated.admin_order_field = "unpaid_by_customer"

    def contract_value_formated(self , obj):
        return "{:0,.2f}".format(obj.contract_value)
    contract_value_formated.short_description = "Value"
    contract_value_formated.admin_order_field = "contract_value"
    
    def cost_paid_formated(self , obj):
        return "{:0,.2f}".format(obj.cost_paid)
    cost_paid_formated.short_description = "Cost Paid"
    cost_paid_formated.admin_order_field = "cost_paid"

    def cost_to_finish_formated(self , obj):
        if obj.cost_to_finish:
            return "{:0,.2f}".format(obj.cost_to_finish)
        else :
            return "-"
    cost_to_finish_formated.short_description = "Cost to Finish"
    cost_to_finish_formated.admin_order_field = "cost_to_finish"

    def pic_name(self , obj):
        return obj.pic +" - "+self.personel.get(obj.pic,"")
    pic_name.short_description = "PIC"
    pic_name.admin_order_field = "pic"

no_login_site = NoLoginSite(name='no_login_site')
###admin.site.register(Question,QuestionAdmin)
###admin.site.register(Choice)
no_login_site.register(Dashboard,DashboardAdmin)



# Register your models here.
