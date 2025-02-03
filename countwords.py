def countwords():
    words = "books/frankenstein.txt"
    count = 0
    with open(words) as f:
        words = f.read()
        words = words.split()
        for word in (words):
            count += 1
    print(count)

if __name__ == "__main__":
    countwords()