import sys

# Reference: https://en.wikipedia.org/wiki/Morse_code
MORSE = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..'
}

#first function, capitalizes all letters in a string
def uppercase(s: str) -> str:
    if s == "":
        return ""
    rest = uppercase(s[1:])
    c = s[0]
    if 'a' <= c <= 'z':
        return chr(ord(c) - 32) + rest
    return c + rest

#second function, splits a string into words at spaces
def split_words(s: str) -> list[str]:
    if s == "":
        return [""]
    result = split_words(s[1:])
    if s[0] == ' ':
        return [""] + result
    result[0] = s[0] + result[0]
    return result

#third function, converts a word to morse code
def word_to_morse(word: str) -> str:
    if word == "":
        return ""
    rest = word_to_morse(word[1:])
    if rest == "":
        return MORSE[word[0]]
    return MORSE[word[0]] + " " + rest

#fourth function, converts a list of words to morse code
def words_to_morse(words: list[str]) -> list[str]:
    if words == []:
        return []
    return [word_to_morse(words[0])] + words_to_morse(words[1:])


def main() -> None:

	if len(sys.argv) > 1 and all([x == ' ' or (65 <= ord(x) <= 90) or (97 <= ord(x) <= 122) for x in sys.argv[1]]):
		x = uppercase(sys.argv[1])
		print(x)
		x = split_words(x)
		print(x)
		x = words_to_morse(x)
		print(x)
	else:
		print("To use, run: python morse.py \"text with letters and spaces only\"") # replace this with a helpful phrase to explain the required command-line arguments to potential users


