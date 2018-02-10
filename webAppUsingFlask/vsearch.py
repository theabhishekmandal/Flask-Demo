def search4letters(word: str,check: str)-> set:
    vowels = set(check)
    return vowels.intersection(set(word))


def search4vowels(word: str) -> set:
    vowels=set('aeiou')
    return vowels.intersection(set(word))
