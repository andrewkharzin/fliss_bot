from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
class Airline(models.Model):

    iata = models.CharField(_("Iata"), max_length=2, default="")
    icao = models.CharField(_("Icao"), max_length=3, default="")
    rus_code = models.CharField(_("Rus"), max_length=2, default="")
    comment_eng = models.CharField(_("Description eng"), max_length=85, default="")
    comment_rus = models.CharField(_("Description rus"), max_length=85, default="")
    country = models.CharField(_("Country"), max_length=85, default="")
    alliance = models.CharField(_("Alliance"), max_length=5, default="")
    lowcost = models.CharField(_("Lowcost"), max_length=1, default="")
    description = models.CharField(_("Description"), max_length=50, default="")
    logo = models.ImageField(_("Logo"), upload_to='media/airlines/logos/', default="media/airlines/logos/default_logo", blank=True, null=True)


    def __str__(self):
        return f"{self.iata.upper()}/{self.icao.upper()}"

    
class Register(models.Model):

    number = models.CharField(_("Number"), max_length=5, default="")
    ac_type = models.CharField(_("Type"), max_length=3, default="")
    co = models.CharField(_("@Co"), max_length=5, default="")
    mod = models.CharField(_("Modification"), max_length=4, default="")
    g_type = models.CharField(_("G_TYPE"), max_length=5, default="")
    description = models.CharField(_("Description"), max_length=50, default="")
    

    def __str__(self):
        return f"{self.number}"

    