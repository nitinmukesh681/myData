# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MyUser(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE,null = True, blank = True)
	email = models.CharField(max_length = 100,null = True,blank = True,unique = True)
	is_activeYesNo = models.BooleanField(default = False)
	full_address = models.CharField(max_length = 200,null = True,blank = True)
	accountType = models.CharField(max_length = 100, null = True, blank = True)
	isProfileComplete = models.BooleanField(default = False)
	created_date_time = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return '%s %s' % (self.user.username,self.accountType)

class NotificationMaster(models.Model):
	notification_is = models.TextField(null = True, blank = True)
	notification_date_time = models.DateTimeField(auto_now_add = True)
	notification_by = models.ForeignKey(MyUser,on_delete = models.CASCADE, null = True, blank = True)
	notification_read_yes_no = models.BooleanField(default = False)

	def __str__(self):
		return '%s' % (self.notification_is)

class DataModel(models.Model):
	last_addedOn = models.DateTimeField(auto_now_add = True)
	companyId = models.CharField(max_length = 15, null = True, blank = True)
	operationFormID = models.CharField(max_length = 15,null = True, blank = True)
	voyageId = models.CharField(max_length = 25,null = True, blank = True)
	BLdate = models.DateTimeField(null = True, blank = True)
	vesselId = models.CharField(max_length = 15,null = True, blank = True)
	VesselName = models.CharField(max_length = 350, null = True, blank = True)
	buyerId = models.CharField(max_length = 15,null = True, blank = True)
	buyerName = models.CharField(max_length = 350, null = True, blank = True)
	sellerId = models.CharField(max_length = 15,null = True, blank = True)
	sellerName = models.CharField(max_length = 350, null = True, blank = True)
	producerId = models.CharField(max_length = 15,null = True, blank = True)
	producerName = models.CharField(max_length = 350, null = True, blank = True)
	loadPortId = models.CharField(max_length = 25,null = True, blank = True)
	loadPortDefinition = models.CharField(max_length = 350, null = True, blank = True)
	loadCountryCode = models.CharField(max_length = 25,null = True, blank =True)
	loadCountry = models.CharField(max_length = 350, null = True, blank = True)
	dischargePortId = models.CharField(max_length = 25,null = True, blank = True)
	dischargePortDefinition = models.CharField(max_length = 350, null = True, blank = True)
	dischargeCountryCode = models.CharField(max_length = 25,null = True, blank = True)
	dischargeCountry = models.CharField(max_length = 150, null = True, blank = True)
	productId = models.CharField(max_length = 60, null = True, blank = True)
	productDefinition = models.CharField(max_length = 400,null = True, blank = True)
	
	operationLine = models.CharField(max_length = 20, null = True, blank = True)
	packingType = models.CharField(max_length = 25, null = True, blank = True)
	packingTypeDefinition = models.CharField(max_length = 250, null = True, blank = True)
	totalQuantity = models.CharField(max_length = 150, null = True, blank = True)
	ETALoadPort = models.CharField(max_length = 200, null = True, blank = True)
	lay = models.DateTimeField(null = True, blank = True)
	can = models.DateTimeField(null = True, blank = True)
	purchaseIncoterm = models.CharField(max_length = 15, null = True, blank = True)
	purchaseIncotermDefinition = models.CharField(max_length = 150, null = True, blank = True)
	salesIncoterm = models.CharField(max_length = 15, null = True, blank = True)
	salesIncotermDefinition = models.CharField(max_length = 150, null = True, blank = True)
	shipResp = models.CharField(max_length = 25,null = True, blank = True)
	shipRespDesc = models.CharField(max_length = 150, null = True, blank = True)
	tradeOperationsResponsible = models.CharField(max_length = 25,null = True, blank = True)
	tradeOperationsResponsibleDefinition = models.CharField(max_length = 150, null = True, blank = True)
	addUser = models.CharField(max_length = 30, null = True, blank = True)
	addDate = models.DateTimeField(null = True, blank = True)
	purchaseContractNo = models.CharField(max_length=25, null = True, blank = True)
	purchaseContractLine = models.CharField(max_length=25, null = True, blank = True)
	salesContractNo = models.CharField(max_length=25, null = True, blank = True)
	salesContractLine = models. CharField(max_length=25, null = True, blank = True)
	approvalId = models.CharField(max_length = 40, null = True, blank = True)
	approvalSubjectStatus = models.CharField(max_length = 150, null = True, blank = True)
	freightPMT = models.CharField(max_length = 50, null = True, blank = True)
	freightCurrency = models.CharField(max_length = 100, null = True, blank = True)
	loadingRate = models.CharField(max_length = 100,null = True, blank = True)
	dischargeRate = models.CharField(max_length = 25,null = True, blank = True)
	netBLQuantity = models.FloatField(null = True, blank = True)
	purchasePrice = models.FloatField(null = True, blank = True)
	salesPrice = models.FloatField(null = True, blank = True)
	netCommision = models.CharField(max_length = 150, null = True, blank = True)
	sample = models.CharField(max_length = 15, null = True, blank = True)

	def __str__(self):
		return '%s' % (self.id)
	# some of your models may have explicit ordering
	# class Meta:
	# 	ordering = ('loadPortDefinition')

class addAsearch(models.Model):
	fieldIs = models.CharField(max_length = 55, null = True, blank = True)
	fieldType = models.CharField(max_length = 25, null = True, blank = True)
	def __str__(self):
		return '%s' % (self.fieldIs)
