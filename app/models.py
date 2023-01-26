from django.db import models


class FileSignatures(models.Model):
    """
    The FileSignatures class is a Django model representing a file signature.
    It is used to store information about a file format, including its description, header, extension, class, offset and trailer.

    Attributes:
    file_description (CharField): A brief description of the file format.
    header (CharField): The hexadecimal representation of the first few bytes of the file, known as the file header.
    extension (CharField): The file extension associated with the file format.
    class_field (CharField): The class of the file format.
    offset (CharField): The offset at which the file's signature can be found.
    trailer (CharField): The hexadecimal representation of the last bytes of the file, known as the file trailer.

    Methods:
    None

    Note:
    The class also contains the inner Meta class for database related configurations."""

    file_description = models.CharField(max_length=70, blank=True, null=True)
    header = models.CharField(max_length=167, blank=True, null=True)
    extension = models.CharField(max_length=31, blank=True, null=True)
    class_field = models.CharField(
        db_column="class", max_length=21, blank=True, null=True
    )  # Field renamed because it was a Python reserved word.
    offset = models.CharField(max_length=7, blank=True, null=True)
    trailer = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "file_signatures"
