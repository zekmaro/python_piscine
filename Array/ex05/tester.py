from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey


def main():

	array = ft_load("landscape.jpg")
	ft_invert(array)
	ft_red(array)
	ft_green(array)
	ft_blue(array)
	ft_grey(array)
	print(ft_invert.__doc__)


if __name__ == "__main__":
	try:
		main()
	except Exception as e:
		print(f"AssertionError: {e}")
		sys.exit(1)