# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.


def validate_pubukprn(value):
    if value <= 10000000:
        raise ValidationError(
            _('%(value)s is too small'),
            params={'value': value},
        )
    if value >= 99999999:
    	raise ValidationError(
            _('%(value)s is too large'),
            params={'value': value},
        )


def validate_students(value):
	if value <= 0:
		raise ValidationError(
            _('%(value)s is too small'),
            params={'value': value},
        )

class Institution(models.Model):
	COUNTRY_CHOICES = (
	    ('UK', 'United Kingdom'),
	    ('US', 'United States'),
	)
	university_name = models.CharField(max_length=255)
	country = models.CharField(max_length=2, choices=COUNTRY_CHOICES,default='US')
	num_students = models.IntegerField(validators=[validate_students])
	description = models.TextField(default='')
	tuition = models.IntegerField()
	
	#old database columns
	#PUBUKPRN = models.IntegerField(validators=[validate_pubukprn])
	#APROutcome = models.CharField(max_length = 255)
	#TEFOutcome = models.CharField(max_length = 255)

	def __unicode__(self):
		return "%s" % (self.university_name)

