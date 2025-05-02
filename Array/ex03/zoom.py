import numpy as np
from PIL import Image


def ft_zoom(img_arr: np.ndarray, zoomed_area: tuple[int, int, int, int],
			scaling_factor: int) -> np.ndarray:
	"""Zoom in on a specific area of an image."""
	if not isinstance(img_arr, np.ndarray):
		raise TypeError("img_arr must be a numpy array")
	
	if img_arr.ndim != 3 or img_arr.shape[2] != 3:
		raise ValueError("img_arr must be a 3D array with 3 channels (RGB)")
	
	if not isinstance(zoomed_area, tuple) or len(zoomed_area) != 4:
		raise ValueError("zoomed_area must be a tuple of 4 integers")
	
	if not all(isinstance(i, int) for i in zoomed_area):
		raise ValueError("All elements of zoomed_area must be integers")
	
	if not isinstance(scaling_factor, int):
		raise TypeError("scaling_factor must be an integer")
	
	cropped_img = img_arr[zoomed_area[0]:zoomed_area[1], zoomed_area[2]:zoomed_area[3]]
	zoomed_img = Image.fromarray(cropped_img)
	arr_size = zoomed_img.size
	print(f"Original size: {arr_size}")
	new_size = (zoomed_img.size[0] * scaling_factor, zoomed_img.size[1] * scaling_factor)
	print(f"New size: {new_size}")
	zoomed_img = zoomed_img.resize(new_size, Image.LANCZOS)
	return np.array(zoomed_img)
