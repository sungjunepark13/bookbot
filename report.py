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
