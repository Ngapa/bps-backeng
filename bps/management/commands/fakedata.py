from django.core.management.base import BaseCommand
from faker import Faker
from bps.models import *


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
            date = fake.date()

            Inflasi.objects.create(sandang=fl, sembako=fl1, perumahan=fl2, kesehatan=fl3, transportasi=fl4,
                                   informasi=fl5, rekreasi=fl0, penyedia_pangan=fl1, perawatan_pribadi=fl2, pendidikan=fl3, tanggal=date)

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
            date = fake.date()

            InflasiDod.objects.create(sandang=fl, sembako=fl1, perumahan=fl2, kesehatan=fl3, transportasi=fl4,
                                      informasi=fl5, rekreasi=fl0, penyedia_pangan=fl1, perawatan_pribadi=fl2, pendidikan=fl3, tanggal=date)

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
            date = fake.date()

            InflasiYoy.objects.create(sandang=fl, sembako=fl1, perumahan=fl2, kesehatan=fl3, transportasi=fl4,
                                      informasi=fl5, rekreasi=fl0, penyedia_pangan=fl1, perawatan_pribadi=fl2, pendidikan=fl3, tanggal=date)

        for _ in range(3):
            a = fake.pyint()
            b = fake.pyint()
            c = fake.pyint()
            d = fake.pyint()
            e = fake.pyint()
            f = fake.pyint()
            g = fake.pyint()
            h = fake.pyint()
            i = fake.pyint()
            j = fake.pyint()
            k = fake.pyint()
            l = fake.pyint()
            m = fake.pyint()
            n = fake.pyint()
            o = fake.pyint()
            p = fake.pyint()
            date = fake.date()

            PendudukLaki.objects.create(
                a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, i=i, j=j, k=k, l=l, m=m, n=n, o=o, p=p, tanggal=date)

        for _ in range(3):
            a = fake.pyint()
            b = fake.pyint()
            c = fake.pyint()
            d = fake.pyint()
            e = fake.pyint()
            f = fake.pyint()
            g = fake.pyint()
            h = fake.pyint()
            i = fake.pyint()
            j = fake.pyint()
            k = fake.pyint()
            l = fake.pyint()
            m = fake.pyint()
            n = fake.pyint()
            o = fake.pyint()
            p = fake.pyint()
            date = fake.date()

            PendudukPr.objects.create(
                a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, i=i, j=j, k=k, l=l, m=m, n=n, o=o, p=p, tanggal=date)

        for _ in range(1):
            a = fake.pyint()
            b = fake.pyint()
            c = fake.pyint()
            d = fake.pyint()
            e = fake.pyint()
            f = fake.pyint()
            g = fake.pyint()
            h = fake.pyint()
            i = fake.pyint()
            j = fake.pyint()
            k = fake.pyint()
            l = fake.pyint()
            m = fake.pyint()
            n = fake.pyint()
            o = fake.pyint()
            p = fake.pyint()
            date = fake.date()

            PendudukLakiKecamatan.objects.create(kec="Karangpucung",
                                                 a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, i=i, j=j, k=k, l=l, m=m, n=n, o=o, p=p, tanggal=date)

        for _ in range(1):
            a = fake.pyint()
            b = fake.pyint()
            c = fake.pyint()
            d = fake.pyint()
            e = fake.pyint()
            f = fake.pyint()
            g = fake.pyint()
            h = fake.pyint()
            i = fake.pyint()
            j = fake.pyint()
            k = fake.pyint()
            l = fake.pyint()
            m = fake.pyint()
            n = fake.pyint()
            o = fake.pyint()
            p = fake.pyint()
            date = fake.date()

            PendudukPrKecamatan.objects.create(kec="Karangpucung",
                                               a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, i=i, j=j, k=k, l=l, m=m, n=n, o=o, p=p, tanggal=date)
