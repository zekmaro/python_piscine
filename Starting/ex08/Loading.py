def ft_tqdm(lst: range) -> None:
    """ft_tqdm(lst: range) -> None
    A simple implementation of tqdm to show progress in a loop.
    """
    for i in range(len(lst)):
        yield "█"