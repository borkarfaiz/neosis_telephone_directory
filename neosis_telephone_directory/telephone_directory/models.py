from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model
from django.db import models

from model_utils.models import TimeStampedModel

UserModel = get_user_model()

class Contacts(TimeStampedModel):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255,)
    middle_name = models.CharField(max_length=255, blank=True, default="")
    last_name = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    # Mobile number validation has been added for Indian Numbers only
    mobile_number = models.CharField(max_length=10, validators=[
        RegexValidator(regex=r"^[6-9]\d{9}", message="Enter Valid Mobile Number")
    ])
    landline_number = models.CharField(max_length=12, validators=[
        RegexValidator(regex=r"\d{5}([- ]?)\d{6}", message="Enter Valid Mobile Number")
    ])
