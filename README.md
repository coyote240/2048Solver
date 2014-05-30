# 2048 Solver in Python

## Why?

By now you've seen plenty of 2048 variants in any number of languages.  That's
the way it goes with popular, simple games.  While I may have missed the hype
I'm happy to share my personal explorations in the space.

Plagued by a mild obsession with the game, I decided to start thinking about the
problem a bit more broadly and make for myself a project to tinker with when I
was in the mood.  I figure, better to spend the idle tinkering than midlessly
sliding tless back and forth.

## Features

While the ultimate purpose of the project would be to write a program to "solve"
the 2048 game, at the very least the game must be implemented before it can be
solved.  I have chosen to implement the game in Python as a series of basic
objects from which further explorations may be built.

* A Board class, representing the state of the board at any point in the game
and being responsible for implementing the rules - largely complete
* A Game class, very much a work in progress, to manage game play and scoring
* A Display class.  Any board state may be output to SVG.
* A Storage class, that ultimately all board states may be stored in a local
SQLite3 database, as well as any games played.

In addition, I've gone on a couple of larks for my own amusement:

* Unit tests, so far focused on the Board class.  The problem is complex enough
that the tests have helped to ensure an accurate outcome.
* An iPython notebook - just to try it out.  I have used the notebook as one
would in scientific computing, explaining my findings regarding the game and how
I've chosen to solve problems.

The iPython notebook may be found here:
http://nbviewer.ipython.org/github/coyote240/2048Solver/blob/master/2048Solver.ipynb

## The Graph

I've had fun thinking about the problem of 2048.  I'm not especially strong at
maths, but better at logic.  Looking at any give state of the board, there are a
finite number of states that basically break down as:

valid moves * empty cells * 2

where 2 is the number of possible values of the random cell added at the end of
each turn.

As the player only has control over the valid move chosen, I do not intend to
explore the entirety of the game graph.  That means that the number of possible
next board states is limited to:

valid moves * (empty cells - 1)

## The Solver

Thus far I have implemented the game as a Board and Game class.  After a few
iterations where the state of the Board object changed with each move, I've
rewritten the Board class to be stateless.  Each mutator operation returns a new
board state, leaving the instance itself intact.  This allows for a basic search
algorithm:

For each game state:

* pull each next valid state
* evaluate each next state based upon:
    * point value of change
    * number of empty cells

## Possible Experiments

* Board state abstraction.
    * represent the board using relative scores rather than absolute scores
    * store abstracted states in a separate table
* Joseki
    * Given abstracted states, are there potential heuristics that can be
    gleaned from extended play?
