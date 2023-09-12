import datetime

from django.utils.translation import gettext as _
from django.db import models
from django.conf import settings
from django.contrib.auth.models import Contacts


class Category(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Tasks(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.user = None

    title = models.CharField(max_length=120)
    description = models.TextField(max_length=300)
    assigned_to = models.ManyToManyField(Contacts, related_name="assignee", blank=True)
    due_date = models.DateField(null=True)
    priority = models.CharField(max_length=15, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_tasks = models.JSONField(default=list, null=True)

    status = models.CharField(max_length=20)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created_at = models.DateField(_("Date"), default=datetime.date.today)
