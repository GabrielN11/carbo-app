#Server instance
from src.server.instance import server

#Routes

from src.controller.auth import SignInRoute, SignUpRoute, RecoveryRoute
from src.controller.food import FoodByIdRoute, FoodListRoute, FoodRoute


if __name__ == "__main__":
    server.run()