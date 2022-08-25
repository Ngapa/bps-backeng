from lib2to3.pytree import Base
from django.core.management.commands import BaseCommand
from faker import Faker
from bps.models import *


class Command(BaseCommand):
    help = "Command Information"

    def handle(self, *args, **kwargs):
        fake = Faker()

        fl = fake.pyfloat()
        print(fl)


# Inflasi.objects.create(sandang=0.3, sembako=0.2, perumahan=0.9, kesehatan=2.0, transportasi=1.2, informasi=0.4, rekreasi=0.2, penyedia_pangan = 1.8, perawatan_pribadi=3.0)
