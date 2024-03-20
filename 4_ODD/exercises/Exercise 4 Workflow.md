## Exercise 4: Workflow

#### Goal

Mimic the *write feature* ⇄ *test feature* workflow.

#### Tasks

In the `brew_potions.py` file complete the `make_python_expert_potion` function that makes the *Python expert* potion (instructions below).

Get Professor Snape to inspect your potion as shown for the example potion. Calling `inspection_by_snape` should never give you an error, so you will have to read what Snape does and says to find out what went wrong.

This is supposed to be easy and fun, so run the inspection often and make mistakes with the potion.

Use your git skills to commit the changes you made to a new branch, and create a pull request on Github.

##### Brewing instructions

Make a new potion called `python_expert` according to these instructions:

```
1. Set up a pewter cauldron and light a fire underneath it
2. Add fish eyes, unicorn hair and tea leaves
3. Let simmer for 2 hours
4. Have Snape inspect the potion (use target_potion='python_expert').
```

Use the `if __name__ =="__main__"` block in `brew_potions.py` to create the `python_expert` potion and call Snape to inspect the potion by calling `inspection_by_snape` . Make sure you actaully call the function you are editing and change the **target** potion for Snape to `"python_expert"`.

Note that if you copy from the `example_potion()` function, it is missing a crucial step. You can look at the `Potion()` class in `brewing/potion_class.by` for inspiration.
