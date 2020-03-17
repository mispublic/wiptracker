from django.core.management.base import BaseCommand, CommandError
from trackingwip.models import Dashboard
from trackingwip.views import pars_saldousb


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        data_list=pars_saldousb()
        
        for data in data_list:
            obj,created=Dashboard.objects.update_or_create(
                wom=data["WOM"],defaults={
                    "customer":data["Customer"],
                    "cost_paid":data["Cost"],
                    "contract_value":data["Contract"],
                    "pic":data["PIC"],
                    "paid_by_customer":data["PaidbyCustomer"],
                    "unpaid_by_customer":data["Unpaid"],
                    "finish_estimation":data["FinishEstimation"],
                }

            )

