import mmh3
import bitarray
from typing import Optional

class BloomFilter:
	def __init__(self, size: int, number_of_hashes: int, filter: Optional[list] = None):
		self._size = size
		self._number_of_hashes = number_of_hashes
		if filter:
			self._filter = bitarray.bitarray(filter)
		else:
			self._filter = bitarray.bitarray(size)
			self._filter.setall(0)

	def add(self, element: str) -> list:
		for i in range(self._number_of_hashes):
			index = mmh3.hash(element, i)
			self._filter[index % self._size] = 1
		return self._filter

	def lookup(self, element: str) -> bool:
		for i in range(self._number_of_hashes):
			index = mmh3.hash(element, i)
			if self._filter[index % self._size] == 0:
				return False
		return True


if __name__ == '__main__':
	from pathlib import Path

	dictionary = Path("/usr/share/dict/words").read_text().split("\n")
	bloom_filter = BloomFilter(size=100_000_000, number_of_hashes=100)
	for word in dictionary:
		bloom_filter.add(word)

	while True:
		word_to_check = input("Give me a word\n")

		if bloom_filter.lookup(word_to_check):
			print("Possibly correct!\n")
		else:
			print("Not correct!\n")


