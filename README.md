
# Sequence Alignment - Understanding the Problem
([Jump to: Translating problem to a coding challenge](#coding-challenge))

## Global Alignment
There are 3 major steps involved when performing global alignment:
+ [Creating a scoring matrix](#step-1-creating-a-scoring-matrix)
+ [Traceback](#step-2-tracing-back)
+ [Align sequences](#step-3-aligning-the-sequences)

Given 2 sequences *S<sub>1</sub>* and *S<sub>2</sub>* where *len(S<sub>1</sub>)=L<sub>1</sub>* and *len(S<sub>2</sub>)=L<sub>2</sub>* and *L<sub>1</sub> > L<sub>2</sub>*, we want to find the best way to align them. Sequence alignment is used to find similarities between sequences and deduce functional, structural, and evolutionary relationships.

Once the matrix is filled, we will traceback from the largest value (usually in the top-right cell of the matrix) to the bottom-left of the matrix.

Following some traceback rules, we will create an alignment which will sequence arrangement that maximizes the score and minimizes penalty based on our scoring system.

Below is an example to illustrate all the steps and rules followed when performing global alignment.

---

**_Globally align ATCG and TCG_**

#### Step 1: Creating a Scoring Matrix
+ Rule: When creating the matrix, add a **gap character** to both sequences to create an extra row and column such that  *(L<sub>1</sub>+=1)* and *(L<sub>2</sub>+=1)*

This gap allows for alignment maximization by enabling us to get as many arrangements of the sequences as possible.

+ Rule: Label the y-axis with one of the sequences written *bottom-up* and the x-axis with the other written *left-right*

||||||
----|----|----|----|---
G|.|.|.|.|
C|.|.|.|.|
T|.|.|.|.|
A|.|.|.|.|
gapRow|.|.|.|.|
.|gapCol|T|C|G|

For our example, we will use the scoring system below:

Score System||
----|----
Match|**+2**
Mismatch|**-2**
Gap|**-4**


Next, we want to fill in the scoring matrix.
Before filling in other cells, we set the value of the first cell in the gap row to 0.

||||||
----|----|----|----|---
G|.|.|.|.|
C|.|.|.|.|
T|.|.|.|.|
A|.|.|.|.|
gapRow|**0**|.|.|.|
.|gapCol|T|C|G|

We fill in the rest of the matrix starting from the bottom left.
+ Rule: *cell score from diagonal direction = s<sub>i</sub>_score+ cell_match_or_mismatch_value* 

||||||
----|----|----|----|---
G|.|.|.|.|
C|.|.|.|.|
T|.|.|.|.|
A|.|cell_x|.|.|
gapRow|**s<sub>i</sub>**|.|.|.|
.|gapCol|T|C|G|

*cell_x_score = s<sub>i</sub>_score+match_score(A,T)*

In the example above, **match_score** is the value of a mismatch from our score system since *A* and *T* are not a match.

*Score from left or down direction= s<sub>i</sub>_score+ gap_score* 


||||||
----|----|----|----|---
G|.|.|.|.|
C|.|.|.|.|
T|.|.|.|.|
A|.|cell_x|.|.|
gapRow|.|**s<sub>i</sub>**|cell_y|.|
.|gapCol|T|C|G|

*cell_x_score = s<sub>i</sub>_score+gap_score*

*cell_y_score = s<sub>i</sub>_score+gap_score*


*final_cell_score = max(diagonal_score, vertical_score, horizontal_score)*

---
Completed matrix with 2 examples on how to calculate cell score: 
![Image of completed scoring matrix](https://github.com/Mokeira/genomiks/blob/master/images/matrix_example.JPG "Completed scoring matrix")

---

#### Step 2: Tracing Back

+ Rule: While filling in the scoring matrix, draw arrows to each cell from the cell whose value maximized that cell's score.

We use these arrows to trace back to the 0<sup>th</sup> column from the cell with the highest value.
If, while tracing back, there are two or more paths, the one with the minimum cell score is chosen.
Once the optimal path is identified, we move on to the last step: aligning the sequences.

#### Step 3: Aligning the Sequences
The image below shows the completed matrix with the arrows drawn. The optimal path has been highlighted. Following this path, we will apply some simple rules to get our alignment.

![Image of completed scoring matrix](https://github.com/Mokeira/genomiks/blob/master/images/trace_example.JPG "Completed scoring matrix")

+ Rule: If the arrow does not point diagonally, we replace the character that the arrow is pointing towards with a gap.

For example, if the following occurs:

||||||
----|----|----|----|---
G|.|<--- cell_x|.|.|
C|.|.|.|.|
T|.|.|.|.|
A|.|.|.|.|
gapRow|.|.|.|.|
.|gapCol|T|C|G|	

we would replace **G** with **_** in our sequence and keep **T**

The path in our example only has diagonal arrows and gives us the following alignment:

	A T C G
	_ T C G
	_ represents a gap


### Coding Challenge
There is some sort of pattern followed when filling in the matrix.
1. Set the first cell in the gap_row to 0
	
	*cell<sub>0,0</sub> = 0*

2. Fill the first row and column
	
	*cell<sub>i,0 </sub> = -i(gap_score) or cell<sub>i,0 </sub> = cell<sub>i-1</sub> _score+gap_score*

	*cell<sub>0,j </sub> = -j(gap_score)*

3. Starting from cell in the second column,second-last row, fill in the rest of the matrix by taking *max(diagonal_val,horizontal_val,vertical_val)*


In fact, after reading more into this, I discovered the [*Needleman-Wunsch Algorithm*](https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm) that does exactly what we need to do.

Here is my implementation: [*scoringMatrix.py*](https://github.com/Mokeira/genomiks/blob/master/scoringMatrix.py)

Next steps:
+ add tests for scoringMatrix.py





