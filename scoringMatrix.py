import math

def sequenceAligner(seq1, seq2,score):
    scores={
    'match': score[0],
    'mismatch': score[1],
    'gap': score[2]
    }

    m = len(seq1)
    n = len(seq2)

    #(m+1)x(n+1) scoring
    scoring_matrix = [[None]*(n+1) for i in range (m+1)]
    #trace_matrix keeps track of previous cells that maximized value of each cell
    #we will use this to trace-back
    trace_matrix=[[None]*(n+1) for i in range (m+1)]

    #init row1 and col1
    scoring_matrix[0][0] = 0

    for x in range(1,m+1):
        scoring_matrix[x][0]= x*scores['gap']

    for x in range(1,n+1):
        scoring_matrix[0][x]= x*scores['gap']

    #store position and value of max value in matrix
    max_score = -math.inf
    max_pos = -1

    #calculate cell scores for other cells
    for x in range(1,m+1):
        for y in range(1,n+1):
            m_check = checkMatch(seq1,seq2,x,y)
            diagonal_score = scoring_matrix[x-1][y-1]+scores[m_check]
            vertical_score = scoring_matrix[x][y-1]+ scores['gap']
            horizontal_score = scoring_matrix[x-1][y]+ scores['gap']
            max_val = max(diagonal_score,vertical_score,horizontal_score)
            scoring_matrix[x][y] = max_val

            if max_val == diagonal_score:
                trace_matrix[x][y] = [x-1,y-1]
            elif max_val == vertical_score:
                trace_matrix[x][y] = [x,y-1]
            else:
                trace_matrix[x][y]=[x-1,y]

            if max_val>max_score:
                max_score = max_val
                max_pos = y

    trace=[]
    temp = [len(scoring_matrix)-1,max_pos]
    seq1_align=[]
    seq2_align=[]


    while True:
        if temp == None:
            break;

        trace+=[scoring_matrix[temp[0]][temp[1]]]

        #pos1,pos2 will be used during alignmnent to determine 'arrow direction'
        pos1, pos2 = temp[:], temp[:]

        temp = trace_matrix[temp[0]][temp[1]]
        pos2 = temp[:] if temp != None else pos2

        #alignment
        if pos1[0]==pos2[0]: #vertical arrow
            seq1_align+=[seq1[m-1]]
            seq2_align+=['_']

        elif pos1[1]==pos2[1]:#horizontal arrow
            seq1_align+=[' ']
            seq2_align+=[seq2[n-1]]

        else: #diagonal arriw
            seq1_align+=[seq1[m-1]]
            seq2_align+=[seq2[n-1]]

        m-=1
        n-=1

    print('Completed scoring matrix:\n',*[i  for i in scoring_matrix[::-1]], sep='\n')
    #print(f'\nValues in optimal trace-back path: {trace}')
    print(f"\nAligned sequences:\n {''.join(seq1_align[::-1])} \n {''.join(seq2_align[::-1])}")

def checkMatch(seq1,seq2,m,n):
    if seq1[m-1]==seq2[n-1]:
        return 'match'
    else:
        return 'mismatch'

#sequenceAligner[seq1,seq2,[[match_score,mismatch_score,gap_score]]
sequenceAligner('ATCG','TCG',[2,-2,-4])