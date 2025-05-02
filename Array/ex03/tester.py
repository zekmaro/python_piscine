from load_image import ft_load, show_image
from zoom import ft_zoom
from PIL import Image
import sys


def get_center_box(shape, box_size=50):
    """Returns a (y1, y2, x1, x2) box centered in the image."""
    h, w, _ = shape
    cy, cx = h // 2, w // 2
    half = box_size // 2
    return (cy - half, cy + half, cx - half, cx + half)


def main():
	"""Main function to test the ft_load function."""
	# Test with a valid image path
	img_arr = ft_load("animal.jpeg")
	print(img_arr)
	show_image(img_arr)
	box = get_center_box(img_arr.shape, 400)
	zoomed_img_arr = ft_zoom(img_arr, box, 2)
	print(f"The shape of the new image is: {zoomed_img_arr.shape}")
	print(zoomed_img_arr)
	show_image(zoomed_img_arr)


if __name__ == "__main__":
	try:
		main()
	except Exception as e:
		print(f"AssertionError: {e}")
		sys.exit(1)
