# infinite-monkey-theorem
An implementation of the infinite monkey theorem

The theorem states that a monkey hitting keys at random on a typewriter
keyboard for an infinite amount of time will almost surely type a given text, such as the com-
plete works of William Shakespeare. Well, suppose we replace a monkey with a Python func-
tion. How long do you think it would take for a Python function to generate just one sentence
of Shakespeare? The sentence we’ll shoot for is: “methinks it is like a weasel”
You are not going to want to run this one in the browser, so fire up your favorite Python IDE. The
way we will simulate this is to write a function that generates a string that is 27 characters long
by choosing random letters from the 26 letters in the alphabet plus the space. We will write
another function that will score each generated string by comparing the randomly generated
string to the goal.
A third function will repeatedly call generate and score, then if 100% of the letters are correct
we are done. If the letters are not correct then we will generate a whole new string. To make
it easier to follow your program’s progress this third function should print out the best string
generated so far and its score every 1000 tries.
