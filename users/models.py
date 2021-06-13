from django.db import models
from PIL import Image
from django.contrib.auth.models import User
import datetime
from django.urls import reverse
clg_choices=[
("GCASC_MG" , "Government College of Arts, Science and Commerce, Khandola, Marcela Goa"),
("GCASC_SG" , "Government College of Arts, Science & Commerce, Sanquelim-Goa"),
("GCASC_QG" , "Government College of Arts, Science & Commerce, Quepem-Goa"),
("SSAGCAC","Sant Sohirobanath Ambiye Government College of Arts & Commerce, VIrnoda-Pernem, Goa"),
("GCCE","Government College of Commerce & Economics, Borda-Margao, Goa"),
("GCM","Goa College of Music, Kala Academys Complex, Campal, Panaji-Goa"),
("GCHS","Goa College of Home Science, Campal, Panaji, Goa"),

("SMCAC","Shree Mallikarjun College of Arts & Commerce, Canacona Goa"),
("NIE","Nirmala Institute of Education, Altinho Panaji, Goa"),
("DCAS","Dhempe College of Arts & Science, Panaji, Goa"),
("VMSCL","V.M. Salgaocar College of law, Miramar, Panaji Goa"),
("SSDCCE","S.S. Dempo College of Commerce & Economics, Altinho, Panaji, Goa"),
("CCE","College of Commerce and Economics, Ponda Goa"),
("CCASCW","Carmel College of Arts, Science & Commerce for Women, Nuvem Goa"),
("RCCA","Rosary College of Commerce & Art, Navelim Salcete Goa"),
("FACAC","Fr. Agnel College of Arts & Commerce, Pilar Goa"),
("NZCC","Narayan Zantye College of Commerce, Bicholim Goa"),
("SPCCFCAS","Smt. Parvatibi Chowgule Cultural Foundation's College of Arts & Science, Margao Goa"),
("CE","College of Education, Ponda Goa"),
("CASSPVCSVNSBCC","College of Arts, Sou. Sheela Premandand Vaidya College of Science & V.N.S. Bandekar College of Commerce, Assagao, Mapusa Goa"),
("SXCASC","St. Xavier's College of Arts, Science & Commerce, Mapusa Goa"),
("SVCCMS","S.V. College of Commerce & Management Studies, Telang Nagar, Khorlim, Mapusa Goa"),
("MESCAC","MES College of Arts & Commerce, Zuarinagar Goa"),
("VVMSDCCE","Vidya Vikas Mandal's Shree Damodar College of Commerce & Economics, Margao Goa"),
("VVMGRKCL","Vidya Vikas Mandal's Govind Ramnath Kare College of Law Margao, Goa."),
("CESCAC","Cuncolim Educational Society's College of Arts & Commerce, Cuncolim Salcete Goa"),
("PESCAS","PES's College of Arts & Science, Ponda Goa")]

gender_choices=[('F', 'Female'),
                ('M', "Male"),
                ('T', 'Transgender')]

status_choices=[('Verified', 'Verified'),
                ('Rejected', 'Rejected'),
                ('Processing', 'Processing')]

role_choices=[('Alumni', 'Alumni'),
              ('Directorate', 'Directorate'),
              ('College', 'College')]

def year_choices():
    return [(r,r) for r in range( datetime.date.today().year+1, 1970, -1)]

def current_year():
    return datetime.date.today().year

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    college = models.CharField(max_length=100, choices=clg_choices, null=True, blank=True)
    gender = models.CharField(max_length=15, choices=gender_choices, null=True, blank=True)
    status = models.CharField(max_length=10, choices=status_choices, default='Processing')
    is_profile_updated = models.BooleanField(default=False)
    roll_number = models.CharField(max_length=20, blank=True, null=True)
    passing_year = models.IntegerField(choices=year_choices(), null=True, blank=True)
    course = models.CharField(max_length=30, blank=True, null=True)
    mobile_number = models.IntegerField( blank=True, null=True)
    role = models.CharField(max_length=15, choices=role_choices, default='Alumni')

    def __str__(self):
        return f'{self.user.username} Profile'

    def get_absolute_url(self):
        return reverse('user-detailb', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)