# Generated by Django 2.2.10 on 2020-02-21 06:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("lbworkflow", "0003_auto_20200221_0438"),
    ]

    operations = [
        migrations.CreateModel(
            name="SimpleWorkFlow",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_on",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Created on"
                    ),
                ),
                (
                    "summary",
                    models.CharField(max_length=255, verbose_name="Summary"),
                ),
                (
                    "content",
                    models.TextField(blank=True, verbose_name="Content"),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Created by",
                    ),
                ),
                (
                    "pinstance",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="simpleworkflow",
                        to="lbworkflow.ProcessInstance",
                        verbose_name="Process instance",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
