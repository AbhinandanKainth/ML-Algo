I have shuffled the journals-CSE file for more accuracy.
I have then calculated the correlation for CSE-journals.
m1.csv contains the Name,H-index,I-factor for the journals
Correlation=0.5030144454111805


Now I took the 80% data and formed the regression line.
Regression: Impact-factor = a*H-index + b 
eg.
a = 0.021457174864455596
b = 1.0355443927779062


Then I put the rest 20% data to the test. I calculated the Root mean square error and printed it in the Script1.py
eg. error = 1.5550668502438745

After getting the above regression line, I used this regression line to predict the values of Impact factor of the conferences.
m2.csv contains the Name of the conferences ,their H-index and predicted I-Factor










