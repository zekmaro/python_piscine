from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
	try:
		img = Image.open(path)
	except FileNotFoundError:
		raise FileNotFoundError(f"File {path} not found.")
	img = img.convert("RGB")
	img = np.array(img)
	return img
