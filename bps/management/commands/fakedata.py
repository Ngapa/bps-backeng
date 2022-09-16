from enum import unique
from django.core.management.base import BaseCommand
from faker import Faker
from bps.models import *

KECAMATAN = (
    'Dayeuhluhur',
    'Wanareja',
    'Majenang',
    'Cimanggu',
    'Karangpucung',
    'Cipari',
    'Sidareja',
    'Kedungreja',
    'Patimuan',
    'Gandrungmangu',
    'Bantarsari',
    'Kawunganten',
    'Kampung Laut',
    'Jeruklegi',
    'Kesugihan',
    'Adipala',
    'Maos',
    'Kroya',
    'Binangun',
    'Sampang',
    'Nusawungu',
    'Cilacap Selatan',
    'Cilacap Tengah',
    'Cilacap Utara',
)

KATEGORI_INFLASI = (
    "Inflasi",
    "Inflasi DoD",
    "Inflasi YoY"
)
KATEGORI_PDRB = (
    "PDRB Migas",
    "Distribusi PDRB Migas",
    "Laju Pertumbuhan PDRB Migas",
    "PDRB Non Migas",
    "Distribusi PDRB Non Migas",
    "Laju Pertumbuhan PDRB Non Migas",
)


class Command(BaseCommand):
    help = "Command Information"

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(3):
            fl = fake.pyfloat(left_digits=3, right_digits=3,
                              positive=True, max_value=200.0)
            fl1 = fake.pyfloat(left_digits=3, right_digits=3,
                               positive=True, max_value=200.0)
            fl2 = fake.pyfloat(left_digits=3, right_digits=3,
                               positive=True, max_value=200.0)
            fl3 = fake.pyfloat(left_digits=3, right_digits=3,
                               positive=True, max_value=200.0)
            fl4 = fake.pyfloat(left_digits=3, right_digits=3,
                               positive=True, max_value=200.0)
            fl5 = fake.pyfloat(left_digits=3, right_digits=3,
                               positive=True, max_value=200.0)
            fl0 = fake.pyfloat(left_digits=3, right_digits=3,
                               positive=True, max_value=200.0)
            fl7 = fake.pyfloat(left_digits=3, right_digits=3,
                               positive=True, max_value=200.0)
            kategori = fake.random_elements(
                elements=KATEGORI_INFLASI, unique=True)
            date = fake.date()

            Inflasi.objects.create(sandang=fl, sembako=fl1, perumahan=fl2, kesehatan=fl3, transportasi=fl4,
                                   informasi=fl5, rekreasi=fl0, penyedia_pangan=fl1, perawatan_pribadi=fl2, pendidikan=fl3, total_inflasi=fl7, tanggal=date)

        for _ in range(6):
            a = fake.pyfloat(left_digits=3, right_digits=3,
                             positive=True, max_value=200.0)
            b = fake.pyfloat(left_digits=3, right_digits=3,
                             positive=True, max_value=200.0)
            c = fake.pyfloat(left_digits=3, right_digits=3,
                             positive=True, max_value=200.0)
            d = fake.pyfloat(left_digits=3, right_digits=3,
                             positive=True, max_value=200.0)
            e = fake.pyfloat(left_digits=3, right_digits=3,
                             positive=True, max_value=200.0)
            f = fake.pyfloat(left_digits=3, right_digits=3,
                             positive=True, max_value=200.0)
            g = fake.pyfloat(left_digits=3, right_digits=3,
                             positive=True, max_value=200.0)
            h = fake.pyfloat(left_digits=3, right_digits=3,
                             positive=True, max_value=200.0)
            i = fake.pyfloat(left_digits=3, right_digits=3,
                             positive=True, max_value=200.0)
            j = fake.pyfloat(left_digits=3, right_digits=3,
                             positive=True, max_value=200.0)
            k = fake.pyfloat(left_digits=3, right_digits=3,
                             positive=True, max_value=200.0)
            l = fake.pyfloat(left_digits=3, right_digits=3,
                             positive=True, max_value=200.0)
            m = fake.pyfloat(left_digits=3, right_digits=3,
                             positive=True, max_value=200.0)
            n = fake.pyfloat(left_digits=3, right_digits=3,
                             positive=True, max_value=200.0)
            o = fake.pyfloat(left_digits=3, right_digits=3,
                             positive=True, max_value=200.0)
            p = fake.pyfloat(left_digits=3, right_digits=3,
                             positive=True, max_value=200.0)
            q = fake.pyfloat(left_digits=3, right_digits=3,
                             positive=True, max_value=200.0)
            r = fake.pyfloat(left_digits=3, right_digits=3,
                             positive=True, max_value=200.0)
            date = fake.date()
            kategori = fake.random_elements(
                elements=KATEGORI_PDRB, unique=True)

            Pdrb.objects.create(a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h,
                                i=i, j=j, k=k, l=l, m_n=m, o=n, p=o, q=p, r_s_t_u=q, total_pdrb=r, tanggal=date)
