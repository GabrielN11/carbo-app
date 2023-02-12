#Server instance
from src.server.instance import server

#Routes

from src.controller.auth import SignInRoute, SignUpRoute, RecoveryRoute
from src.controller.food import FoodByIdRoute, FoodListRoute, FoodRoute, FoodByUserRoute
from src.controller.favorites import FavoriteRoute
from src.controller.user import UserRoute


if __name__ == "__main__":
    server.run()