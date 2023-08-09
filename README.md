# Embedded Software Engineer Quiz Answers

### Question 1

The main idea of the code is to use the smallest rectangle size to form a square, as this will result in the largest possible square. Then, the process is repeated with the remaining piece. This simple procedure continues until the entire paper is used up.

### Question 2

The initial pattern observed was that the first letters in the output were changing in accordance with the most significant digit of the input. Consequently, the first step taken was a right bit-shift of 12 positions on the input to establish a connection between the most significant bits and the first letter. This analysis was conducted using Google Sheets, as illustrated in the image below:

![alt text](https://github.com/pedroneto1209/quiz-answers/blob/main/sheet_print.png)

Upon making this attempt, it became apparent that the relationship was not flawless. While it was indeed linked to magnitude, the connection wasn't entirely straightforward. Bearing this in mind, it became evident that the issue might be related to the base of the inputs. As the initial digits changed randomly with increasing inputs, I became certain that these digits were selected arbitrarily for this new base.

I used Python to discover the new base by looking for a digit pattern as explained in the question2_support.py comments. It them became clear that it was using base 62 with a different set of digits to represent. The question2.py script uses the CSV input to map all digits of the output to what values they should be in the default digit set of base 62. 

After this mapping, the values asked in the question were successfully founded as being: f(30001) = GIF; f(55555) = NOi; f(77788) = VNQ;
In the script I also implemented a accuracy test to secure 100% of the CSV rows fitted my function.