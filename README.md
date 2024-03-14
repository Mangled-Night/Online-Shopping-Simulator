# Online-Shopping-Simulators
A repo to place my completed small project

This series of projects was based on making a program to simulate a customer shopping in an online store. There is only a limited stock of items and a cart so customers can go through the store and pick up
whatever and however many items they want. There is no actual system to purchase the items in real life, just, more so acting as if you did go to an online store with infinite money and buying what you want.
There is a system in place for any user errors and/or mishaps with inputs  

In version 1, I had brute-forced the idea of shopping by repeating if-else statements. While it did end up working, the program size ended up being very massive in size and in general, 
if you are repeating the same line of code all over your project, then there is simply a better way of writing the program.
This is where I redid the program but with a different approach and more features. Since version 1 was simply too ineffective and took up a lot of time to make any progress, 
it wasn't fully completed. version 2 is fully completed however and is also functional.

New Features:
 - This time, I opted to use a series of recursive functions rather than have a bunch of if-else statements, to improve how the program functioned along with other functions to also help improve program functionality. This would also help me achieve 
another goal I had wanted, being able to go backward.
- In the first iteration, you couldn't go backward, once you chose an isle you had to commit to it to the end before being able to go to a different one.
In the second iteration, you now can, and this includes selecting items, you can even back out then.
- Another feature I wanted to add is removing items from the cart since at nearly any point a customer could go into their cart 
while shopping and removing items from their cart, while it would be possible to implement that, currently it is only possible to do so after you are done shopping.
- Another new feature I added was being able to search the store for items. An algorithm I made iterates through the store and tries to find the best matching items to what you are looking for
not every item in the world will be there but it is possible to search and see what comes close and what is there


Python Modules needed
- random
- colorama 
