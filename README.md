# Purpose
Dive into tests and TDD by sharing experience and practicing together
- Practical workshop, mainly with examples
- Think programming as communicating 
  * Simple, clear, robust code
  * Maintainable, scalable, undestandable
  * Effective, resilient to change

# Why tests?
- Make sure the code works as expected
- Detect edge cases
- Feel confident to refactor without being afraid of breaking the entire pipeline
- Your teammates can understand your
functions by looking at your tests
- Prevent unexpected output
- Simplifies updating code
- Increases overall efficiency of developing code
- Helps to detect edge cases
- And most importantly prevents you from pushing any broken code into production!

# Persona
- A developer in the beginning of a journey to become the best developer she/he can be. 
With a background in exact sciences, he/she has heard about tests but does not practice TDD.
She/he has some software patterns in mind from recent learning, but limited experience in structuring code.
Using Python to script but would like to explore more software engineering to improve. 

# Disclaimer
Sharing is caring! This is part of a learning journey. I am much more a curious individual than an expert. The objective is to share my learnings so far while enabling us to collaborate, learn and connect around an important topic. I assume that independently of your experience, you are curious to learn, courageous to ask and share and, finally, respectfull about the stage each one is right now.

# Community
In Slack: [#tdd-test-driven-development](https://app.slack.com/client/T02JL00JU/C01SP39JDFU/thread/C8W3SUK17-1622572475.035100).

# Requirements
- VSC
- Python
- git
- github account with Equinor
- Camera

# Story

Warning: the workshop is based on our own work together. 
You will find imperfections or questionable things, let's discuss them.

We will go through:
1. Check that all requirements are in place for all
2. Have a short pause (if needed, eventual catch-up with missing requirements)
3. Present a problem to solve
4. Demonstrate TDD while working together (~peer-programming)
5. After each step, a pause for:
    - sharing the work
    - discussing key topics/challenges
    - catching up
6. Conclude with a recap

Commit early and often!
Good practices for a commit, by [Chris Beams](https://chris.beams.io/posts/git-commit/)

## 1. Does everyone have the requirements?
- VSC: terminal type "code" and VSC should open
- python --version 
- a virtual environment (how to?)
  * "python -m venv tdd_venv", ".\tdd_venv\Scripts\activate" (Windows) or "source tdd_venv/bin/activate" (unix)
- git --version, black --version
- github: clone repository locally (where Github Actions is setup)
  * some may need:
  [Github/git cheat-sheet](https://training.github.com/downloads/github-git-cheat-sheet/)
  [Connecting to Github with ssh](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh)
  [Configure test with VSC (ctrl+shift+P, Python: Configure tests)](https://code.visualstudio.com/docs/python/testing)

## 2. The problem: String calculator¹

### Step 1:

The method can take up to two numbers, separated by commas, and will return their sum.
For example "" or "1" or "1,2" as inputs.
For an empty string it will return 0.

The cycle is as follows:

0. Make a list of tests we know we need to have working
1. Add a little test: write just enough of a test to fail
2. Run all tests and fail
3. Make a little change: write just enough code to make it pass
4. Run the tests and succeed
5. Refactor to remove duplication: clean up the mess made getting the test to pass

Discussion:
- Being able to take teeny-tiny steps, not necessarily doing it
- Add items to our to-do list rather than addressing them all at once
- Commit early and often!
- Let's try: Test pipeline, continuous integration
- Remember to save changes :-) 
- DRY: Don't Repeat Yourself!
- @pytest.mark.parametrize to run multiple test cases
- Debugging with test (tools?)

### Step 2
Allow the Add method to handle an unknown amount of numbers.

### Step 3
Allow the Add method to handle new lines between numbers (instead of commas):
- The following input is ok: “1\n2,3” (will equal 6)
- The following input is NOT ok: “1,\n” (not need to prove it - just clarifying)


# Conclusion
- What was useful?
- What was not?
- Let's try: Test pipeline, continuous integration
- Remember to save changes :-) 
- DRY: Don't Repeat Yourself!

# Additional comments

1. Why should we test? 
    - Intention of code, documentation coverage (in/out), confidence (failing test)
    - Bugg (regression test)
    - Refactoring (know the desired behaviour)
    - Using testing to review
2. TDD:
- avoid spaguetti code
- if it is hard to write a test: rethink about what you are trying to code
- side effects (non obvious behaviour/not main goal)
3. Continuous integration
- Test in Github actions (or Circle CI, Jenkins)
- Features: scalable 

# Additional resources
- TDD chanel

# References:
¹ https://kata-log.rocks/string-calculator-kata
