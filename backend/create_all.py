from src.models.user import User
from src.models.food import Food
from src.models.favorites import Favorite

from src.server.instance import db

db.create_all()