class Game :
    def __init__(self) :
        print('''            Welcome
              1 : Names Count
              2 : Divided By 
              3 : Sentence NO Duplicate ''')
        user_choice=int(input('Enter Game Number : '))
        if user_choice == 1:
             self.names_count()
          
        elif user_choice == 2 :
             self.divided_by()
        
        elif user_choice == 3:
             self.sentence_no_duplicate
        else:
            print(f'No game with this number : {user_choice}') 
    def names_count(self):
         names = (input("Enter names comma separated :")).split(',')
        # names=names.split(',')
         names_count = [len(x)  for x in names]
         print(names_count)
    def divided_by(self):
          print('Divided By ') 
    def sentence_no_duplicate(self):
            print('No duplicate')
         

g1=Game()
