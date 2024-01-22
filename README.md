
Workshop dates: **14-15 March 2024**
====================================

Schedule
========

 - 09:30–11:00: lecture
 - 11:00–11:30: coffee break
 - 11:30–13:00: lecture
 - 13:00–14:00: lunch
 - 14:00–15:30: lecture
 - 15:30–16:00: coffee break
 - 16:00–17:30: lecture

Day 1
=====

Large-scale collaborative code development with git and GitHub (max 2h)
-----------------------------------------------------------------------
You are already using git daily for your code and papers. What are the
challenges when you are collaborating in a team, potentially distributed all
over the world? And what happens when someone you don't know starts using the
code you published on GitHub and wants to contribute back? Ever messed up your
git repo in a way that the only option left was copying all the files and start
over? Are you hesitant to fork, pull, push and create branches?

Following the standard workflows used in the development of the most popular
free and open source scientific Python packages, we are going to address these
and many other questions about a more professional approach to git.


High-performance Python: a sweeping overview of computer architecture (max 4h)
------------------------------------------------------------------------------
To write efficient code in Python that can be parallelized and be used on the
GPU at its full potential it is useful to understand the basics of modern
computer architecture. When is a computation CPU-bound? When is RAM the actual
bottleneck? What about I/O- or network-bound problems? What are the challenges
of using GPUs?

After understanding how CPU/GPU/RAM/storage and the network stack are connected
together, we'll develop an intuition of the trade-offs involved in programming
efficiently when our laptop seems not to be enough anymore for the data we need
to work with. We'll look at how code can be parallelized and the pitfalls you
may hit in the process.

Disclaimer: we are not going to present any specific library to do parallel or
GPU programming in Python. The objective of the lecture is to put you in
a position to understand where the bottlenecks in your code are, and to evaluate
trade-offs of the specific libraries you may want to use ;-)

Day 2
=====

Organizing, testing, documenting, and distributing scientific code (6h)
-----------------------------------------------------------------------
The hype about reproducible science seems to imply that putting on GitHub the
scripts that re-create the plots of your paper is all that is needed. Have you
ever tried to use code published by other scientists to do anything _else_ than
reproduce their plots? Have you been forced to learn how to manage docker
containers on the institute's cluster because the scientific software you wanted
to use could not be installed in any more useful way? Did you have to spend
precious months of your PhD by trying to figure out what the code of that
student who left the lab was doing? Did you have to re-write some of _your_ code
from scratch because you could not understand it anymore?

The goal of this lecture is to give you the minimal infrastructure needed to
make your code re-usable by others (and by your future self). You'll learn how
to organize your code following well established standards, how to publish your
code so that it can be installed by a simple `pip install`, how to make it
robust by linking testing with continuous integration, and, if there is time,
how to document it properly. 

