from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
	"""Load an image from a file and convert it to a numpy array."""
	if not isinstance(path, str):
		raise TypeError("path must be a string")
	try:
		img = Image.open(path)
	except FileNotFoundError:
		raise FileNotFoundError(f"File {path} not found.")
	img = img.convert("RGB")
	img = np.array(img)
	return img
