def ft_tqdm(lst: range) -> None:
    size = len(lst)

    for i, item in enumerate(lst, 1):
        progress = i / size
        width = 80  # not terminal width like tqdm
        filled = int(progress * width)
        bar = '█' * filled + ' ' * (width - filled)

        print(f"{int(progress*100):3}%|{bar}| {i}/{size}", end='\r')

        yield item
