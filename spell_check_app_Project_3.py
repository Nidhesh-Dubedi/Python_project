from spellchecker import SpellChecker

class SpellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()


    def correct_text(self,text):
        words = text.split() #hello world ['hello','world']
        corrected_words = []   


        for word in words:
            corrected_word = self.spell.correction(word)
            if corrected_word != word.lower():
                   print(f"Correcting '{word}' to '{corrected_word}'") 
                   corrected_words.append(corrected_word) 
            else:
                 print("Your text is perfect!!")
         
         #step 4: returning the corrected text          

        return ' '.join(corrected_words)
    

    def run(self):
         print("\n ----spell checker----")

         while True:
              text = input('Enter text to check (or type "exit" to quit)')

              if text.lower() == "exit":
                   print("Closing the program......") 
                   break
              
              corrected_text = self.correct_text(text)
              print(f"Corrected Text : {corrected_text}")

#step 6: runnning the program

if __name__ == "__main__":
     SpellCheckerApp().run()
    
              

