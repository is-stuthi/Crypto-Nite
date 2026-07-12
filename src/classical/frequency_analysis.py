from collections import Counter
def main():
    print("Frequency Analysis")
    print("===================")
    print("Enter your message:")
    text=input()
    text=text.upper()
    only_text = "".join([char for char in text if char.isalpha()])
    frequencies = Counter(only_text)
    sorted_frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
    for key, value in sorted_frequencies:
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()