from load_image import ft_load, show_image
import numpy as np
from PIL import Image
import sys


def get_center_box(shape, box_size=50):
    """Returns a (y1, y2, x1, x2) box centered in the image."""
    h, w, _ = shape
    cy, cx = h // 2, w // 2
    half = box_size // 2
    return (cy - half, cy + half, cx - half, cx + half)


def transpose_img(img_arr: np.ndarray) -> np.ndarray:
	"""Transpose the image array."""
	if not isinstance(img_arr, np.ndarray):
		raise TypeError("img_arr must be a numpy array")
	
	if img_arr.ndim != 3 or img_arr.shape[2] != 3:
		raise ValueError("img_arr must be a 3D array with 3 channels (RGB)")
	
	h, w, c = img_arr.shape
	transposed_img = np.empty((w, h, c), dtype=img_arr.dtype)

	for i in range(h):
		for j in range(w):
			transposed_img[j][i] = img_arr[i][j]

	return transposed_img


def main():
	"""Main function to test the ft_load function."""
	# Test with a valid image path
	img_arr = ft_load("animal.jpeg")
	print(img_arr)
	show_image(img_arr)
	box = get_center_box(img_arr.shape, 400)
	y1, y2, x1, x2 = box
	cropped = img_arr[y1:y2, x1:x2]
	new_img = Image.fromarray(cropped)
	new_img = np.array(new_img)
	show_image(new_img)
	transposed_img = transpose_img(new_img)
	mirrored_img = np.flipud(transposed_img)
	show_image(mirrored_img)


if __name__ == "__main__":
	try:
		main()
	except Exception as e:
		print(f"AssertionError: {e}")
		sys.exit(1)
