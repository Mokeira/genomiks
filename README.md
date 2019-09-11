# Sequence Alignment - Understanding the Problem

## Global Alignment
There are 3 major steps involved when performing global alignment:
	+[Creating a scoring matrix](#step-1-creating-a-scoring-matrix)
	+Traceback
	+Align sequences

### Creating a Scoring Matrix
Given 2 sequences *S<sub>1</sub>* and *S<sub>2</sub>* where *len(S<sub>1</sub>)=L<sub>1</sub>* and *len(S<sub>2</sub>)=L<sub>2</sub>* and *L<sub>1</sub> > L<sub>2</sub>*, we want to create a *(L<sub>1</sub>+1)x(L<sub>2</sub>+1)* matrix that we will fill using a scoring system.

Once the matrix is filled, we will traceback from the largest value (usually in the top-right cell of the matrix) to the bottom-left of the matrix.

Following some traceback rules, we will create a sequence *S<sub>3</sub>* which will represent the sequence that maximizes the score and minimizes penalty based on our scoring system.

Below is an example to illustrate all the steps and rules followed when performing global alignment.

---

<font color="green">Globally align ATCG and TCG</font>

#### Step 1: Creating a Scoring Matrix
<font color="red">
	Rule: When creating the matrix, add a *gap character* to both sequences to create an extra row and column such that *(L<sub>1</sub>+=1) and (L<sub>2</sub>+=1)*
</font>

This **gap** allows for alignment maximization by enabling us to get as many arrangements of the sequences as possible.

<span style="color:red">Rule: Label the y-axis with one of the sequences written bottom-up and the x-axis with the other written left-right</span>

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
before filling in other cells, we set the value of the first cell in the gap row to 0.

||||||
----|----|----|----|---
G|.|.|.|.|
C|.|.|.|.|
T|.|.|.|.|
A|.|.|.|.|
gapRow|<span style="color:green">**0**</span>|.|.|.|
.|gapCol|T|C|G|

<span style="color:red">Rule: 
	*cell score from diagonal direction= s<sub>i</sub>+ match_or_mismatch_value* </span>

||||||
----|----|----|----|---
G|.|.|.|.|
C|.|.|.|.|
T|.|.|.|.|
A|.|cell_x|.|.|
gapRow|<span style="color:green">**s<sub>i</sub>**</span>|.|.|.|
.|gapCol|T|C|G|

*cell_x_score = s<sub>i</sub>_score+match_score(A,T)*

**match_score** is the value of a mismatch from our score system since *A* and *T* are not a match.

<span style="color:red">
	*Score from left,down direction= s<sub>i</sub>+ gap_score* 
</span>

||||||
----|----|----|----|---
G|.|.|.|.|
C|.|.|.|.|
T|.|.|.|.|
A|.|cell_x|.|.|
gapRow|.|<span style="color:green">**s<sub>i</sub>**</span>|.|.|
.|gapCol|T|C|G|

*cell_x_score = s<sub>i</sub>_score+gap_score*

*cell_y_score = s<sub>i</sub>_score+match_score(A,T)*


*final_cell_score = max(diagonal_score, vertical_score, horizontal_score)*














