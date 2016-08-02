from flask_bcrypt import (generate_password_hash, check_password_hash)
from flask_login import UserMixin
from peewee import *
from wtforms.fields import TextAreaField

# DATABASE = SqliteDatabase(':memory:')
DATABASE = SqliteDatabase('FavoriteOrders.db')


class BaseModel(Model):
    class Meta:
        database = DATABASE


class User(UserMixin, BaseModel):
    email = CharField(unique=True)
    password = CharField(max_length=100)

    @classmethod
    def create_user(cls, email, password):
        try:
            cls.create(
            email=email,
            password=generate_password_hash(password)
            )
        except:
            print "exception error"


class Burrito(BaseModel):
    protein = CharField(default="None") # chicken, beef
    rice = CharField(default="None") # brown, white, none
    bean = CharField(default="None") # black, pinto
    salsa = CharField(default="None")
    chesse = BooleanField(default=False)
    sour_cream = BooleanField(default=False)
    lettuce = BooleanField(default=False)
    extras = TextAreaField(default="")
    # email = CharField()
    user = ForeignKeyField(User, related_name="eats")
    # email = ForeignKeyField(User, related_name="eats")

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Burrito], safe=True)
    DATABASE.close()
