from django.core.management.base import BaseCommand, CommandError
from trackingwip.models import Dashboard
from trackingwip.views import pars_vrp1100


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        data_list=pars_vrp1100()
        
        for data in data_list:
            obj,created=Dashboard.objects.update_or_create(
                wom=data["WOM"],defaults={
                    "customer":data["Customer"],
                    "contract_value":data["Contract"],
                    "paid_by_customer":data["Paid"],
                    "unpaid_by_customer":data["Unpaid"],
                    "pic":data["PIC"],
                    "finish_estimation":data["FinishEstimation"],
                    "cost_to_finish":data["CostFinish"]
                }

            )

