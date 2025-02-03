def countchar():
    chars = "books/frankenstein.txt"
    with open(chars) as f:
        chars = f.read()
        chars = chars.lower()
        charcount = {}
        for char in chars:
            if char not in charcount:
                charcount[char] = 1
            else:
                charcount[char] += 1
        print(charcount)

if __name__ == "__main__":
    countchar()