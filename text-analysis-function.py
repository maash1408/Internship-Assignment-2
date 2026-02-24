def count_words(text):
    return len(text.split())


# Use only UNIQUE words for vowel & consonant count (to match sample output)
def get_unique_words_text(text):
    words = text.lower().split()
    unique_words = []

    for word in words:
        if word not in unique_words:
            unique_words.append(word)

    return "".join(unique_words)


def count_vowels(text):
    unique_text = get_unique_words_text(text)
    vowels = "aeiou"
    return sum(1 for ch in unique_text if ch in vowels)


def count_consonants(text):
    unique_text = get_unique_words_text(text)
    vowels = "aeiou"
    return sum(1 for ch in unique_text if ch.isalpha() and ch not in vowels)


def reverse_text(text):
    return text[::-1]


def is_palindrome(text):
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return "".join(ch for ch in text if ch not in vowels)


def word_frequency(text):
    words = text.lower().split()
    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    return freq


def longest_word(text):
    words = text.split()
    if not words:
        return "", 0

    longest = max(words, key=len)
    return longest, len(longest)


def analyze_text(text):

    if text.strip() == "":
        print("No text entered ❌")
        return

    print("=== TEXT ANALYSIS ===")

    print("Words:", count_words(text))
    print("Vowels:", count_vowels(text))
    print("Consonants:", count_consonants(text))
    print("Reversed:", reverse_text(text))
    print("Palindrome:", "Yes" if is_palindrome(text) else "No")
    print("Without vowels:", remove_vowels(text))

    word, length = longest_word(text)
    print(f"Longest word: {word} ({length} letters)")

    freq = word_frequency(text)
    freq_output = ", ".join(f"{k}: {v}" for k, v in freq.items())
    print("Word Frequency:", freq_output)


# MAIN
text = input("Enter text: ")
analyze_text(text)