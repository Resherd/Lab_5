import re

def sort_ukr_eng_words(words):
    
    ukr_words = [word for word in words if re.match(r'[а-щА-ЩЬьЮюЯяЇїІіЄєҐґ]', word)]
    eng_words = [word for word in words if re.match(r'[a-zA-Z]', word)]
    
    ukr_words_sorted = sorted(ukr_words, key=lambda x: x.lower())
    eng_words_sorted = sorted(eng_words, key=lambda x: x.lower())
    
    return ukr_words_sorted + eng_words_sorted

def read_and_sort_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            
            text = file.read()
            
            first_sentence = re.split(r'[.!?]', text)[0]
            
            words = re.findall(r'\b[а-яА-ЯёЁa-zA-Z]+\b', text)
            
            sorted_words = sort_ukr_eng_words(words)
            
            print(f"Перше речення: {first_sentence}")
            print(f"Відсортовані слова: {sorted_words}")
            print(f"Кількість слів: {len(sorted_words)}")
            
    except FileNotFoundError:
        print(f"Помилка: файл {filename} не знайдено.")
    except Exception as e:
        print(f"Помилка: {e}")

read_and_sort_file('text.txt')
