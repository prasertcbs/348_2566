# author: Prasert Kanawattanachai
# github: https://github.com/prasertcbs/python_howto
# YouTube: https://youtu.be/ZEjrlRHhzJw

import random

def roll(n_dice=1):
    face=[
    """
      
  ⚪  
      
    """,
    """
    ⚪
      
⚪    
    """,
    """
    ⚪
  ⚪  
⚪    
    """,
    """
⚪  ⚪
      
⚪  ⚪
    """,
    """
⚪  ⚪
  ⚪  
⚪  ⚪
    """,
    """
⚪  ⚪
⚪  ⚪
⚪  ⚪
    """,
    ]

    for i in range(n_dice):
        n=random.randrange(0, 6) + 1 # 1-6
        print(face[n-1])

if __name__ == '__main__':
    roll()