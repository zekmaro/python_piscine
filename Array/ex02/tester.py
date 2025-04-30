from load_image import ft_load
import sys

def main():
	"""Main function to test the ft_load function."""
	# Test with a valid image path
	img = ft_load("landscape.jpg")
	print(f"The shape of the image is: {img.shape}")
	print(img)

if __name__ == "__main__":
	try:
		main()
	except Exception as e:
		print(f"AssertionError: {e}")
		sys.exit(1)
