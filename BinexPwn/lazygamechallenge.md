# Lazy-game-challenge

Point: 30

## Category

Binary exploitation

## Question

I found an interesting game made by some guy named "John_123". It is some betting game. I made some small fixes to the game; see if you can still pwn this and steal $1000000 from me!

To get flag, pwn the server at: ```nc thekidofarcrania.com 10001```


## Solution

A very simple buffer overflow challenge. Simply have to put negative betting amount in order to exploit the program.

```
Welcome to the Game of Luck !. 

Rules of the Game :
(1) You will be Given 500$
(2) Place a Bet
(3) Guess the number what computer thinks of !
(4) computer's number changes every new time !.
(5) You have to guess a number between 1-10
(6) You have only 10 tries !.
(7) If you guess a number > 10, it still counts as a Try !
(8) Put your mind, Win the game !..
(9) If you guess within the number of tries, you win money !
(10) Good Luck !..

theKidOfArcrania:
  I bet you cannot get past $1000000!


Are you ready? Y/N : Y
Money you have : 500$
Place a Bet : -1000000

Loading : ⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛ 100%
The Game is On, Good Luck !..

Make a Guess : 
Sorry you didn't made it !
Play Again !...
Better Luck next Time !.

Sorry you lost some money !..
Your balance has been updated !.
Current balance :  : 
1000500$
What the... how did you get that money (even when I tried to stop you)!? I guess you beat me!

The flag is CTFlearn{}
```
## Improvement
None
