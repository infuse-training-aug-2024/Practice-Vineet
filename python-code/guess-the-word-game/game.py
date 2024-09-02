import json
import random
import sys

class Game:
    def __init__(self):
        self.score = 0
        self. lives = 3
        self.username = ""
        self.question_array = list()
        self.answer_array = list()
        self.generate_word = ""
    
    
    def get_word(self):
        with open("words.txt", 'r') as file:
            words = file.read().split(",")
            word = random.choice(words).strip()
        return word
    
    def setup(self):
        self.generated_word = self.get_word()
        self.question_array = ["?" for i in range(len(self.generated_word))]
        self.answer_array = list(self.generated_word)
        
    def is_guessed_word_correct(self, guessed_word):
        if guessed_word in self.answer_array:
            return True
        else:
            return False

    def save_user_info(self):
        data = {"username": self.username, "score": self.score}
        with open('info.json', 'r') as f:
            file_data = json.load(f)
            if isinstance(file_data, dict):
                file_data = [file_data]

        file_data.append(data)

        with open('info.json', 'w') as f:
            json.dump(file_data, f, indent=4)

        
    def start_game(self):
        #options
        option = int(input("1-> View Score \n2-> Start Quiz"))
        if(option==1):
            #generate all the score list
            f = open('info.json')
            data = json.load(f)
            print(data)
            i=0
            for ele in data:
                i += 1
                name = ele["username"]
                score = ele["score"]
                print("Player " + str(i))
                print("name = " + name)
                print("score = " + str(score))

            f.close()
        elif(option == 2):
            self.setup()
            self.username = input("Enter you username: ")
            while(self.lives > 0):
                
                print(self.question_array)
                print(self.answer_array)
                
                print("lives left: ", self.lives)
                
                guessed_word = input("Guess a letter or the whole word: ")

                if(guessed_word == self.generated_word or self.question_array == self.answer_array):
                    print("Winner Winner chicken dinner")
                    self.score += 1
                    self.save_user_info()
                    sys.exit()
                    
                if(len(guessed_word)==1 and self.is_guessed_word_correct(guessed_word)):
                    guessed_word_index = self.answer_array.index(guessed_word)
                    self.question_array[guessed_word_index] = self.answer_array[guessed_word_index]
                    
                else:
                    print("Incorrect. You lose a life")
                    self.lives -= 1


                if(self.lives == 0):
                    print("You lost! The secret word was ", self.generated_word)
                    self.save_user_info()
                    sys.exit()
