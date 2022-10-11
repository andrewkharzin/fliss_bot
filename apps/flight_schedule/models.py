import uuid
import datetime
from django.utils.text import slugify
from apps.directory.models import Airline, Register
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from apps.directory.models import Register

class UUID(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        abstract = True


class Abstract(UUID):
    create_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    update_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True

class FlightTask(Abstract):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='standBy')
        def get_by_slug(self, slug):
            return self.get(id=slug.rsplit('-', 1)[1])

    STATUS = (
        ('draft', 'Draft'),
        ('completed', 'Completed'),
        ('inprogress', 'InProgress'),
        ('canceled', 'Canceled'),
        ('standBy', 'StandBy')
    )
    tech_route = (
        ('arrival', 'Arrival'),
        ('departure', 'Departure')
    )

    user = models.ForeignKey(User, related_name='user_entries', on_delete=models.PROTECT) 
    task_date = models.DateField(_("Date"), auto_now=False, auto_now_add=False)
    technology = models.CharField(_("Tech"), choices=tech_route, max_length=15, default="")
    airline = models.ForeignKey(Airline, related_name='flight_airline', on_delete=models.PROTECT)
    aircraft_type = models.CharField(_("Aircraft"), max_length=50, default="")
    registration = models.ForeignKey(Register, related_name='flight_register', on_delete=models.PROTECT)
    flight = models.CharField(_("Flight"), max_length=6, default="")
    sched_time =models.TimeField(_("SCTA"), auto_now=False, auto_now_add=False, null=True, blank=True)
    route = models.CharField(_("From"), max_length=10, default="")
    payload = models.TextField(_("Payload"), default="")
    description = models.TextField(_("Description"), default="")
    status = models.CharField(_("Status"), choices=STATUS, max_length=15, default="draft")
    slug = models.SlugField(unique=True, editable=False)
    is_return = models.BooleanField(default=False)
    objects = models.Manager()
    postObjects = PostObjects()
 
    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.task_date}-f{self.id}')
        super(FlightTask, self).save(*args, **kwargs)


    class Meta:
        verbose_name = _("FlightTask")
        verbose_name_plural = _("FlightTasks")
        ordering = ('-status',)


    def __str__(self):
        return f"{self.task_date} - {self.technology.upper()} - {self.flight.upper()} "

    def get_absolute_url(self):
        return reverse("FlightTask_detail", kwargs={"pk": self.pk})
