import string
import langdetect

def read_first_sentence(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            # Знаходимо перше речення
            first_sentence = text.split('.')[0]
            print("Перше речення:", first_sentence)

            # Видаляємо знаки пунктуації
            text_cleaned = text.translate(str.maketrans('', '', string.punctuation))

            # Розбиваємо на слова
            words = text_cleaned.split()

            # Розділяємо слова за мовами
            ukrainian_words = []
            english_words = []
            other_words = []

            for word in words:
                try:
                    lang = langdetect.detect(word)
                    if lang == 'uk':
                        ukrainian_words.append(word)
                    elif lang == 'en':
                        english_words.append(word)
                    else:
                        other_words.append(word)
                except langdetect.lang_detect_exception.LangDetectException:
                    pass  # Якщо неможливо визначити мову, пропускаємо слово


            ukrainian_words_sorted = sorted(ukrainian_words, key=str.lower)
            english_words_sorted = sorted(english_words, key=str.lower)
            other_words_sorted = sorted(other_words, key=str.lower)
            all = ukrainian_words_sorted + english_words_sorted + other_words_sorted

            print("\nOthers слова (по алфавіту):", all)

            print("\nКількість слів у тексті:", len(words))

    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
    except Exception as e:
        print(f"Сталася помилка при читанні файлу: {e}")

file_path = 'C:\Users\bogda\PycharmProjects\Py\Lab_5\Text.txt'
read_first_sentence(file_path)