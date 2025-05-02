from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def show_image(img_array: np.ndarray):
	"""Display an image using matplotlib."""
	if not isinstance(img_array, np.ndarray):
		raise TypeError("img_array must be a numpy array")
	
	if img_array.ndim != 3 or img_array.shape[2] != 3:
		raise ValueError("img_array must be a 3D array with 3 channels (RGB)")
	
	plt.imshow(img_array, interpolation='none')
	plt.axis('on')
	plt.show()


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
	print(f"The shape of the image is: {img.shape}")
	return img
