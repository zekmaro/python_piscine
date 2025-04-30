def slice_me(family: list, start: int, end: int) -> list:
	"""
	Slice a 2D array (list of lists) and return the sliced array.
	"""
	if not isinstance(family, list):
		raise TypeError("family must be a list")
	
	if not isinstance(start, int) or not isinstance(end, int):
		raise TypeError("start and end must be integers")
	
	if not all(all(isinstance(i, (int, float)) for i in sublist) for sublist in family):
		raise TypeError("all elements of family must be int or float")

	print(f"my shape is ({len(family)},{len(family[0])})")

	sliced_family = family[start:end]
	print(f"my new shape is {len(sliced_family)}x{len(sliced_family[0])}")

	return sliced_family
