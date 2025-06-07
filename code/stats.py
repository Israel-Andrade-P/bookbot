def get_word_count(text):
    return len(text.split())

def get_character_count(text):
    lower_text = text.lower()
    return {char:lower_text.count(char) for char in lower_text}



       
    
  
