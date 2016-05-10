#!/usr/env python
import time
from Alfred import GoodreadsAssistant

if __name__ == "__main__":
	for i in range(100):
		book = GoodreadsAssistant.getBookFromGoodreads(1)
		print book.isbn13
		# time.sleep(1)