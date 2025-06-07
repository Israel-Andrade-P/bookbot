def get_word_count(text):
    return len(text.split())

def get_character_count(text):
    lower_text = text.lower()
    return {char:lower_text.count(char) for char in lower_text}

def sort_on(dict):
    return dict["num"]

def get_sorted_list(my_dict):
    sorted_list = [{"char":key, "num": my_dict[key]} for key in my_dict]

    sorted_list.sort(reverse=True, key=sort_on)     

    return sorted_list  






       
    
  
