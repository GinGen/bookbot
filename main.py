from stats import count_words, count_characters, sort_dict
import sys

def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  else:
    path = sys.argv[1]
    content = get_book_text(path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ---------")
    print(f"Found {count_words(content)} total words")
    print("--------- Character Count -------")
    for row in sort_dict(count_characters(content)):
      if row["char"].isalpha():
        print (f"{row["char"]}: {row["num"]}")
    print("============= END ===============")

main()