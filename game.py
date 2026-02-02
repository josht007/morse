import sys

#process a string to remove non-alphabetic characters       
def remove_non_alpha(s: str) -> str:

    if s == "":
        return ""
    rest = remove_non_alpha(s[1:])
    if ('A' <= s[0] <= 'Z') or ('a' <= s[0] <= 'z'):
        return s[0] + rest
    return rest

#process a string to convert all letters to lowercase
def to_lowercase(s: str) -> str:
    if s == "":
        return ""
    rest = to_lowercase(s[1:])
    c = s[0]
    if 'A' <= c <= 'Z':
        return chr(ord(c) + 32) + rest
    return c + rest

#check if a character is a vowel
def is_vowel(c: str) -> bool:
    return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or c == 'y'

#split a string into syllables
def split_syllables(s: str) -> list[str]:
    if s == "":
        return []
    
    if is_vowel(s[0]):
        if len(s) == 1:
            return [s[0]]
        else:
            return [s[0]] + split_syllables(s[1:])
    else:
        
        rest_syllables = split_syllables(s[1:])
        
        if rest_syllables == []:
            return [s]
        else:
            rest_syllables[0] = s[0] + rest_syllables[0]
            return rest_syllables

#add 'upu' after each syllable and combine into a single string
def add_upu(syllables: list[str]) -> str:
    if syllables == []:
        return ""
    if len(syllables) == 1:
        return syllables[0] + "upu"
    return syllables[0] + "upu-" + add_upu(syllables[1:])

#add 'oga' at the end of a string
def add_oga(s: str) -> str:
    return s + "oga"

def main() -> None:
    if len(sys.argv) > 1:
        print("Original:", sys.argv[1])
        cleaned = remove_non_alpha(sys.argv[1])
        print("Alphabetic only:", cleaned)
        lowered = to_lowercase(cleaned)
        print("Lowercase:", lowered)
        syllables = split_syllables(lowered)
        print("Syllables:", syllables)
        upu = add_upu(syllables)
        print("With UPU:", upu)
        final = add_oga(upu)
        print("Final:", final)
    else:
        print('Usage: python comp3007_w26_101299524_assignment_01_game.py "single word"')

if __name__ == "__main__":
    main()
  
