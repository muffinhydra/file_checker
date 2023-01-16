from django.db import models


#TODO clean data in DB, there are still a lot of artifacts and exceptions 
class Signatures(models.Model):
    id = models.FloatField(db_column='ID', blank=True, primary_key=True)  # Field name made lowercase.
    hex_signature = models.CharField(db_column='Hex\xa0signature', max_length=1024, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    filename_extension = models.CharField(db_column='Filename extension', max_length=1024, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    description = models.CharField(db_column='Description', max_length=1024, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'signatures'
