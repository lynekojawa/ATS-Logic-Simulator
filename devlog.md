# Devlog - post Deployment
(7/27) Planning to update my ATS. 
Here are the list of things to update.<br>
1. stemming issue
2. refactoring the files into three -constant, engine, ui
3. scoring: skill_match and total overall score. <br>
this will begin tomorrow (7/28) :D
(7/28)<br>
Recalibrating Orion, from left off. Plan is set.<br>
1. dividing one files into three.: worked on constants.py and scoring engine
Orion needs to retrained, he started project with providing code. which is not ideal.
and both podo-gemini and podo-gpt didn't detected it
(7/29)<br>
started with finishing: ui_dashboard.py file
Here is how I am going to update the engine, it is kinda hard to detect what's important<br>
so I am going to make user to decide pick important section like qualification, duties <br>
the basic global scoring will remain same but the reverse skill match will work as above stated<br>
then missing words will from the from user decided area. <br> 
GPT ran away ugh! for real?
(7/31)<br>
Todo-list<br>
Overall signal: leave as it is, signal score: match rate with Duties and Qualifications for better matching result<br>
Hybrid interface: Enigne will pull out the list of the headers, then USER will select the important area. 
Stemming issues. 
UI update.<br>
Scoring ENGINE - TODO LIST
1. Stemming
2. Header detector: pull out the header (start with this)
3. zone tracker: will content area for header
4. add scoring: for signal zone
Personal comments on Gemini, they works really well from when room tokens are above 150K which is interesting.
(8/3)
Issue resolved stemming: the singular and plural was the issue, enhacned stemming logic 
connecting 2 ui first then if time allows move 3,4. 