class Solution:
	def hammingDistance(self, x: int, y: int) -> int:

	differences = x^y
	print(differences)
	counter = 0

	while differences != 0:
		# clear the least significant bit
		differences &= differences-1
		counter += 1
return counter
