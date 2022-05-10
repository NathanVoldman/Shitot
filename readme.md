# Effects of subroutining on code comprehension
**By: Nathan Voldman and Sagiv Yaari**
   
  ## Background:
  Programmers tend to use subroutines for both easier code comprehension and mostly code modularity. In this research we aim to investigate the effect of subroutinning and specifically the naming of subroutines on code comprehension.
    
## Research question:
Our main goal is to understand how splitting the code into subroutines effect the code clarity, specifically how their naming affect the time it takes to understand their functionality
### How does the naming of subroutines effect code clarity?
- Neutral names with no information about functionality (such as: A,B,C, Purple,Red,Green)
-  Short functional names (with partial information about functionality) - This is very common in coding
-  Long descriptive names (full function can be deduced from name)
    

##  Methodology:
  
We will test code comprehension by introducing the subjects with code that functions close to a normal code with nested functions. The functions will have either non informative names (e.g. “A”, “B”, “C”), shortened names with common abbreveations (e.g. “add”, “mult”, “pow”) or total information names (e.g. “addition”, “multiply”, “power”). The subject will be requested to predict the output of certain input and the time taken to answer (as long as the answer was correct) will be measured. We will create 3 of these types of functions and randomize the naming between subjects. We will create one baseline function with either fully informative or neutral names to standardize between subjects.

###  Website:
https://hygojanqikehlxpb.anvil.app/KVVPGJKUSKTSNVQN5EMXTE5N

##  Assignments:

1. write a 2-4 more functions for the pilot, preferably something that a programmer will encounter in his work -Done
2. start working on a platform to perform the experiment, write the pilot so we can run it - Done
3. write opening for questionair - Done
4. finalize time measurment - Done
5. Make sure everything is written to DB - Done
6. Finalize website design - Nathan
7. Think about what should we ask the programmers - Done
8. Think what should be the baseline question - Done
9. between screens: "Thank you! are you ready for the next one?" - Done
10. first question (Power.py) to be shown without names. check after pilot to see how hard it was
11. Write last screen text - Done
12. add option to skip questions - Done
13. add measuring of full time taking the survey - Done
14. Run the pilot! (by the end of next week) -Done
15. Start experiment (by 8.5.22)

## Questions for Pilot subjects:

- Did they understand or interpeted?
- what would have helped you understand better?
- how hard/easy was the first question
- how long did it take? (we can just measure it)
- did they use the pencil/paper?
- did writing the answer took a lot of time?
- were you spending a lot of time calculating the answer after you knew what the function does? in which questions?

## After Pilot:
1. Change the first question from power to CamelCase (easier)
2. Minor changes in CamelCase
3. Total time was below 20 min for 7 questions but 2.5-5 were on the first question, maybe we can show all questions in the experiment?
4. Average time per question (excluding the first one) was 70-100 seconds
5. Time for instructions was 87, 256, 424 seconds 
6. Add a more balanced way to show all questions (check what question was underrepresented and show it more) - Use profiles (see 13)
7. Remove counter in the top left of question form - Nathan
8. Move skip button to right of submit (but make it a hyperlink) - Nathan
9. Remove banner on top (check how it looks) - Nathan
10. Remove the guidance for pen and paper - Nathan
11. "Filter words with letter" - Sagiv
    - Delete 'this' maybe?
    - Think about maybe changing the letter in it instead
12. Schedule a meeting with Dror after tuesdays class
13. Add support for three profiles - Nathan
14. Add multiple as test question (instead of "power") - Sagiv
15. Draft a messeage to send with the questionnaire - Sagiv
