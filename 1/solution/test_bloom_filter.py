from bloom_filter import BloomFilter
from unittest.mock import Mock, patch
import pytest
import bitarray

class TestBloomFilter:
	def test_add_adds_word_to_filter(self):
		with patch("mmh3.hash", side_effect=[1, 2, 5]):
			filter = BloomFilter(size=10, number_of_hashes=3).add("apple")

			assert filter == bitarray.bitarray([0, 1, 1, 0, 0, 1, 0, 0, 0, 0])


	@pytest.mark.parametrize("mocked_hash, return_value", (([1, 2, 5], True), ([2, 5, 1], True), ([1, 4, 2], False)))
	def test_lookup_returns_result_based_on_the_trained_filter(self, mocked_hash, return_value):
		trained_filter = bitarray.bitarray([0, 1, 1, 0, 0, 1, 0, 0, 0, 0])

		with patch("mmh3.hash", side_effect=mocked_hash):
			bloom_filter = BloomFilter(size=10, number_of_hashes=3, filter=trained_filter)
			assert bloom_filter.lookup("apple") is return_value

