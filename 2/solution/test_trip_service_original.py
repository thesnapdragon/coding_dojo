from typing import List
from unittest.mock import patch

import pytest

from trip_service_original import (
    Trip,
    TripDAO,
    User,
    UserNotLoggedInException,
    UserSession,
    get_trips_by_user,
)


class TestTripServiceOriginal:
    @pytest.fixture
    def trips(self) -> List[Trip]:
        return [Trip()]

    def test_get_trips_by_user_raises_exception_when_not_logged_in(self):
        user = User()
        own_user = None

        with patch.object(UserSession, "get_logged_user", return_value=own_user):
            with pytest.raises(UserNotLoggedInException):
                get_trips_by_user(user)

    def test_get_trips_by_user_returns_empty_list_when_the_provided_user_is_not_a_friend(
        self,
    ):
        user = User()
        own_user = User()

        with patch.object(UserSession, "get_logged_user", return_value=own_user):
            assert get_trips_by_user(user) == []

    def test_get_trips_by_user_returns_list_of_trips_when_the_provided_user_is_a_friend(
        self, trips
    ):
        user = User()
        own_user = User()
        user.add_friend(own_user)

        with patch.object(
            UserSession, "get_logged_user", return_value=own_user
        ), patch.object(TripDAO, "find_trips_by_user", return_value=trips):
            assert get_trips_by_user(user) == trips
