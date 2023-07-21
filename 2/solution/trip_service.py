#!/usr/bin/env python

from __future__ import annotations

from typing import List


class UserNotLoggedInException(Exception):
    pass


class Trip:
    pass


class User:
    def __init__(self):
        self.trips = []
        self.friends = []

    def add_friend(self, user: User) -> None:
        self.friends.append(user)

    def add_trip(self, trip: Trip) -> None:
        self.trips.append(trip)

    def get_friends(self) -> List[User]:
        return self.friends

    def is_friend_with(self, user: User) -> bool:
        return user in self.get_friends()


class TripService:
    def __init__(self, trip_dao: TripDAO):
        self._trip_dao = trip_dao

    def get_friend_trips(self, logged_user: User, friend: User) -> List[Trip]:
        if logged_user:
            if friend.is_friend_with(logged_user):
                return self._trip_dao.find_trips_by_user(friend)
            else:
                return []
        else:
            raise UserNotLoggedInException()


class UserSession:
    @staticmethod
    def get_logged_user() -> User:
        raise NotImplementedError("UserSession.get_logged_user() should not be invoked")


class TripDAO:
    @staticmethod
    def find_trips_by_user(user) -> List[Trip]:
        raise NotImplementedError("TripDAO.find_trips_by_user() should not be invoked")


if __name__ == "__main__":
    pass
