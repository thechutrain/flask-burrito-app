from flask_bcrypt import (generate_password_hash, check_password_hash)
from flask_login import UserMixin
from peewee import *

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
            pass


class Taco(BaseModel):
    protein = CharField() # chicken, beef
    shell = CharField() # hard or soft
    chesse = BooleanField(default=False)
    email = ForeignKeyField(User, related_name="eats")

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Taco], safe=True)
    DATABASE.close()
