#!/usr/bin/env python


class UserNotLoggedInException(Exception):
    pass


class Trip:
    pass


class UserSession:
    @staticmethod
    def get_logged_user():
        raise NotImplementedError("UserSession.get_logged_user() should not be invoked")


class TripDAO:
    @staticmethod
    def find_trips_by_user(user):
        raise NotImplementedError("TripDAO.find_trips_by_user() should not be invoked")


class User:
    def __init__(self):
        self.trips = []
        self.friends = []

    def add_friend(self, user):
        self.friends.append(user)

    def add_trip(self, trip):
        self.trips.append(trip)

    def get_friends(self):
        return self.friends


def get_trips_by_user(user):
    trip_list = []
    logged_user = UserSession.get_logged_user()
    is_friend = False
    if logged_user is not None:
        for friend in user.get_friends():
            if friend == logged_user:
                is_friend = True
                break
        if is_friend:
            trip_list = TripDAO.find_trips_by_user(user)
        return trip_list
    else:
        raise UserNotLoggedInException()


if __name__ == "__main__":
    pass
