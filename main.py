class Game :
    
    def __init__(self) :
        while True:
               print('''            Welcome
              1 : Names Count
              2 : Divided By 
              3 : Sentence NO Duplicate ''')
               user_choice=int(input('Enter Game Number : '))
               if user_choice == 1:
                    self.names_count()
                    
               elif user_choice == 2 :
                    self.divided_by()
               
               elif user_choice == 3 :
                    self.sentence_no_duplicate()
                         
               else:
                    print(f'No game with this number : {user_choice}') 
               playAgain=input('press any key to play again, n for exit')    
               if playAgain=='n':
                    break
           

    def names_count(self):
         names = (input("Enter names comma separated :")).split(',')
        # names=names.split(',')
         names_count = [len(x)  for x in names]
         print(names_count)
    
    def divided_by(self):
          x=int(input('Enter first number : '))
          y=int(input('Enter second number : '))
          result=[]
          for n in range(1,101):
               if n%x and n%y ==0:
                    result.append(n)
          print(result)          
                  

    def sentence_no_duplicate(self):
       
         sentence=input('Enter Sentence : ')
         words=sentence.split(' ')
         words_no_duplicate = []
         for w in words :
               if w not in words_no_duplicate :
                    words_no_duplicate.append(w)

         print('_'.join(words_no_duplicate))
         print(' '.join(words_no_duplicate))
      

           
         

g1=Game()
