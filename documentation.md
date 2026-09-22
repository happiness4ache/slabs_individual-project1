# Author: Nthabiseng

1)INVALID TYPES
Invalid Input-entering text like (abc)
-if a user enters a text like "abc" instead of a number the program will say ValueError and this simply means a Runtime Error because the program is running but it cannot change the text into an integer using int()

2) Invalid Input-out of range number like (150)
-if the user uses the number like 150 in a program it will say Semantic/Logic Error because the input is a number but cannot be outside the range of 0 to 100 so this value is not valid even though it is a valid number

3)ERROR CATEGORIES
-entering a text like abc in the program the program will show Runtime Error(Value Error)
-entering a number like 150 in the program it will show Semantic/Logic Error

4)TYPE CASTING AND RANGE VALIDATION
-the int() function changes the user's input from a text into am integer
-After changing the input the explicit range validation checks that the mark is between 0 and 100 for example if the user enters "75" the int() converts it into a 75 and the program still continues but if the user enters "abc" the int() cannot convert it into an integer and that's where the Value Error occurs.
-If the user enters 150 the value will be converted successfully but the range validation will identify it as invalid.
-So using type casting together with the range validation helps prevent incorrect values from being processed by the program
