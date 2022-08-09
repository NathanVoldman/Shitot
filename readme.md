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
https://OOLOM7GHMKT3YB3T.anvil.app/Y2GZ5EYA3AQYVLFP3GP7VGCF

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
8. Move skip button to right of submit (but make it different design) - Done
9. Remove banner on top (check how it looks) - Done
10. Remove the guidance for pen and paper - Done
11. "Filter words with letter" - Sagiv
    - Delete 'this' maybe? - N/A
    - Think about maybe changing the letter in it instead - Done
12. Schedule a meeting with Dror after tuesdays class
13. Add support for three profiles - Done
14. Add multiple as test question (instead of "power") - Done
15. Draft a message to send with the questionnaire - Sagiv

## Final Experiment:

### Expections:
We expected that programmers will have a better performance on understanding code blocks with detailed names, over code blocks with obscured names.
Then we expected that the results will show eithr of the two:
- Performance on partial names is closer to performance on detailed names:

![image](https://user-images.githubusercontent.com/49371700/183606694-2a56c637-6194-4f85-a78a-cd5e32bb1509.png)
- Performance on partial names is closer to performance to obscured names:

![image](https://user-images.githubusercontent.com/49371700/183606881-85389a0c-c28c-410a-9cb8-a0b0370f61b2.png)


### Hypothesis:
- We hypothesize that the second option is the more likely: Performance on partial names is closer to performance to obscured names

### Metadata:
- Number of participants was 33
- Median time to answer a question: 72 seconds
- Median time to finish answering the quiz: 465 seconds
- Median number of questions answered by participant: 5 out of 6

### Raw Results:
#### Per question:
![image](https://user-images.githubusercontent.com/49371700/183607543-eb4a2dcd-f780-4b72-a66a-f60f0418a78a.png)
#### Aggregated:
![image](https://user-images.githubusercontent.com/49371700/183607671-ab66b694-60a5-4c06-b7a6-51aeb50b22ba.png)

### Interpreted results:
- When looking at the aggregated results, we can divide the participating developers into 3 subgroups:
   - Experts:
      fdsfds
