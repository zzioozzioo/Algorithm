def solution(my_string):
    vowels = "aeiou"
    return "".join([c for c in my_string if c not in vowels])