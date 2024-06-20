#exercise 1
import random
def get_words_from_file():
    with open("../word_list.txt", mode='r') as file:
        return file.readlines()
    
def get_random_sentence(length: int):
    words = get_words_from_file()
    sentence = ""
    for i in range(length):
        sentence += words[random.randint(0, len(words) - 1)].strip().lower() + " "
    sentence = sentence.strip()
    sentence += '.'
    sentence = sentence[0].upper() + sentence[1:]
    print(sentence)
    return sentence

def main():
    print("This program will create a random sentence with the number of words that you choose.")
    sentence_length = input("Enter the number of words you want the sentence to have (must be between 2 and 20):")
    try:
        if 1 < int(sentence_length) < 21:
            return get_random_sentence(int(sentence_length))
        else: 
            print("Sentence length must be between 2 and 20")
            main()

    except Exception as e:
        print(e) 
        print("You must enter a valid number between 2 and 20")
        main()

main()

#exercise 2
import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

print(json.loads(sampleJson)["company"]["employee"]["payable"]["salary"])
sampleJson = json.loads(sampleJson)
sampleJson["company"]["employee"]["birth_date"] = "20/04/1995"
with open("sample.json", mode='w') as newFile:
    newFile.write(json.dumps(sampleJson))

    