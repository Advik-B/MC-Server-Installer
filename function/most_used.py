def prinput(*prompt:any , asker:any='>>>') -> any:
    print(*prompt)
    print()
    return input(asker)