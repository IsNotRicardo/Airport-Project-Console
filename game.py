"""

HERE ARE ALL THE SQL COMMANDS TO EDIT THE DATABASE:

alter table game add target varchar(10);
alter table game add attempts int(8);
alter table game add difficulty int(8);
alter table game rename column co2_consumed to co2_limit;

"""

import geopy
import mysql
from geopy.distance import geodesic


# This function asks for the screen_name and checks if it already exists
def username():
    return False


def init_game(difficulty, distance):
    print(difficulty, distance)


def navigation_system():
    origin = geopy.Point(lat1, lon1)
    destination = geodesic(kilometers=d).destination(origin, b)

    lat2, lon2 = destination.latitude, destination.longitude
