from typing import List

import pytest

from trip_service import Trip, TripService, User, UserNotLoggedInException


class TestTripService:
    @pytest.fixture
    def trips(self) -> List[Trip]:
        return [Trip()]

    @pytest.fixture
    def fake_trip_dao(self, trips):
        class FakeTripDAO:
            @staticmethod
            def find_trips_by_user(user: User) -> List[Trip]:
                return trips

        return FakeTripDAO()

    def test_get_friend_trips_raises_exception_when_not_logged_in(self, fake_trip_dao):
        user = User()
        own_user = None

        with pytest.raises(UserNotLoggedInException):
            TripService(fake_trip_dao).get_friend_trips(own_user, user)

    def test_get_friend_trips_returns_empty_list_when_the_provided_user_is_not_a_friend(
        self, fake_trip_dao
    ):
        user = User()
        own_user = User()

        assert TripService(fake_trip_dao).get_friend_trips(own_user, user) == []

    def test_get_friend_trips_returns_list_of_trips_when_the_provided_user_is_a_friend(
        self, fake_trip_dao, trips
    ):
        user = User()
        own_user = User()
        user.add_friend(own_user)

        assert TripService(fake_trip_dao).get_friend_trips(own_user, user) == trips
