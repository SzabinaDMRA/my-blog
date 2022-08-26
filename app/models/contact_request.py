import datetime

from peewee import Model, AutoField, CharField, DateField, DateTimeField, BooleanField
from app.database_managment import DatabaseManagment

database_object = DatabaseManagment()


class ContactRequest(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    email = CharField(max_length=50)
    category = CharField(max_length=80)
    priority = CharField(max_length=25)
    message = CharField(max_length=255)
    created_at = DateField(null=False, default=datetime.datetime.now)
    updated_at = DateField(null=False, default=datetime.datetime.now)

    class Meta:
        database = database_object.postgresql_database_connection()
        table_name = "user_contact_request"

    @classmethod
    def update(cls, __data=None, **update):
        """
        This Method Update updated_date When Get Option User Model
        :param __data:
        :param update:
        :return:
        """
        update["updated_at"] = datetime.datetime.now()

        return super(ContactRequest, cls).update(__data, **update)

    def __str__(self):
        return f"name:{self.name} email:{self.email} category:{self.category} priority:{self.priority} message:{self.message}"
