from django.core.management.base import BaseCommand
import csv
from buy.models import RetailOutlet
import argparse


class Command(BaseCommand):
    help = 'import libraries from a csv file'

    def add_arguments(self, parser):
        parser.add_argument('csvfile', type=argparse.FileType('r'))

    def handle(self, *args, **options):
        reader = csv.reader(options["csvfile"], delimiter=',', quotechar='"')

        for row in reader:
            retail = RetailOutlet(name=row[0], address=row[1], zip_code=int(row[2]), city=row[3], country=row[4], latitude=float(row[5]), longitude=float(row[6]))
            retail.save()

            print(', '.join(row))
