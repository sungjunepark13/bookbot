path_to_file = "books/frankenstein.txt"

def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def countwords():
    count = 0
    words = main().split()
    for word in (words):
        count += 1
    return count

def countchar():
    chars = main().lower()
    charcount = {}
    for char in chars:
        if char not in charcount:
            charcount[char] = 1
        else:
            charcount[char] += 1
    return charcount
countchar = countchar()

def sortcharlist(countchar):
    sortchar = [{"char": letter, "count": count} for letter, count in countchar.items()]
    return sortchar
sortchar = sortcharlist(countchar)

def sort_key(sortchar):
    return sortchar["count"]

def report():
    
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{countwords()} words found in the document")
    
    sortchar.sort(reverse=True, key=sort_key)
    for letter in sortchar:
        if letter["char"].isalpha() == True:
            print(f"The '{letter["char"]}' character was found {letter["count"]} times")
    print("--- End Report ---")




if __name__ == "__main__":
    print(countwords())

if __name__ == "__main__":
    report()

