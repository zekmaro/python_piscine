from time import sleep


def ft_tqdm(lst: range):
    """
    A simple implementation of tqdm to show progress in a loop.
    """
    BAR_WIDTH = 128
    BLOCK_CHAR = '█'
    length = len(lst)
    for count, item in enumerate(lst, 1):
        percent = count / length
        bar_length = int(percent * BAR_WIDTH)
        bar = BLOCK_CHAR * bar_length + ' ' * (BAR_WIDTH - bar_length)
        print(f"\r{int(percent*100)}%|{bar}| {count}/{length}", end="")
        sleep(0.001)
        yield item
    print()
