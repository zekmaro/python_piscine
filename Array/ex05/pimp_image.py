import numpy as np
from load_image import show_image


def ft_invert(array) -> np.ndarray:
	"""Invert the colors of an image."""
	if not isinstance(array, np.ndarray):
		raise TypeError("array must be a numpy array")

	if array.ndim != 3 or array.shape[2] != 3:
		raise ValueError("array must be a 3D array with 3 channels (RGB)")

	inverted_array = 255 - array
	show_image(inverted_array)
	return inverted_array

def ft_red(array) -> np.ndarray:
	"""Extract the red channel from an image."""
	if not isinstance(array, np.ndarray):
		raise TypeError("array must be a numpy array")

	if array.ndim != 3 or array.shape[2] != 3:
		raise ValueError("array must be a 3D array with 3 channels (RGB)")

	red_array = np.zeros_like(array)
	red_array[:, :, 0] = array[:, :, 0]
	show_image(red_array)
	return red_array

def ft_green(array) -> np.ndarray:
	"""Extract the red channel from an image."""
	if not isinstance(array, np.ndarray):
		raise TypeError("array must be a numpy array")

	if array.ndim != 3 or array.shape[2] != 3:
		raise ValueError("array must be a 3D array with 3 channels (RGB)")

	red_array = np.zeros_like(array)
	red_array[:, :, 1] = array[:, :, 1]
	show_image(red_array)
	return red_array


def ft_blue(array) -> np.ndarray:
	"""Extract the red channel from an image."""
	if not isinstance(array, np.ndarray):
		raise TypeError("array must be a numpy array")

	if array.ndim != 3 or array.shape[2] != 3:
		raise ValueError("array must be a 3D array with 3 channels (RGB)")

	red_array = np.zeros_like(array)
	red_array[:, :, 2] = array[:, :, 2]
	show_image(red_array)
	return red_array

def ft_grey(array) -> np.ndarray:
	pass
