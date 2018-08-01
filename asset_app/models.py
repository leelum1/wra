from django.contrib.auth.models import AbstractUser
from django.db import models
from .choices import COMP_TYPES, SECTIONS
from data_app.choices import WATERSHEDS

class User(AbstractUser):
    phone_no = models.PositiveSmallIntegerField(blank=True, null=True)
    is_abstractor = models.BooleanField(default=False)
    is_watershed = models.BooleanField(default=False)
    is_operations = models.BooleanField(default=False)
    is_licensing = models.BooleanField(default=False)
    is_management = models.BooleanField(default=False)

class Employee(models.Model):
    emp_no = models.PositiveIntegerField(primary_key=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    dob = models.DateField(null=True, blank=True)
    designation = models.TextField(null=True, blank=True)
    salary_range = models.CharField(max_length=12, null=True, blank=True)
    date_start = models.DateField(null=True, blank=True)
    date_end = models.DateField(null=True, blank=True)
    category = models.CharField(max_length=45, null=True)
    section = models.CharField(max_length=80, null=True, blank=True, choices=SECTIONS)

    def __str__(self):
        return self.first_name + self.last_name

class Computer(models.Model):
    comp_no = models.CharField(max_length=12, primary_key=True)
    brand = models.CharField(max_length=45)
    model = models.CharField(max_length=45, null=True, blank=True)
    serial_no = models.CharField(max_length=45, null=True, blank=True)
    comp_type = models.CharField(max_length=45, choices=COMP_TYPES)
    value = models.FloatField(null=True, blank=True)
    lifespan = models.PositiveSmallIntegerField(null=True, blank=True)
    date_comm = models.DateField(null=True, blank=True)
    date_decomm = models.DateField(null=True, blank=True)
    emp_no = models.ForeignKey(Employee, to_field="emp_no", db_column="emp_no", null=True, blank=True)
    section = models.CharField(max_length=80, null=True, blank=True, choices=SECTIONS)
    needs_attn = models.BooleanField(default=False)
    remarks = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.comp_no

class Equipment(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.PositiveSmallIntegerField()
    description = models.TextField(null=True, blank=True)
    storage = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    vim = models.CharField(max_length=45, primary_key=True)
    licence_plate = models.CharField(max_length=12)
    model = models.CharField(max_length=45)
    value = models.FloatField(null=True, blank=True)
    lifespan = models.PositiveSmallIntegerField(null=True, blank=True)
    date_comm = models.DateField(null=True, blank=True)
    date_decomm = models. DateField(null=True, blank=True)
    section = models.CharField(max_length=80, null=True, blank=True, choices=SECTIONS)
    needs_attn = models.BooleanField(default=False)
    remarks = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.licence_plate
