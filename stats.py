def count_words(content):
  contents = content.split()
  return len(contents)

def count_characters(content):
  count = {}
  for char in content.lower():
    count[char] = count.get(char, 0) + 1
  return count

def sort_dict(char_dict):
  dict_list = []
  for k, v in char_dict.items():
    dict_list.append({"char": k, "num": v})
  dict_list.sort(key=lambda n: n["num"], reverse=True)
  return dict_list