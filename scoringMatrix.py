def sequenceAligner(seq1, seq2,score):
    scores={
    'match': score[0],
    'mismatch': score[1],
    'gap': score[2]
    }

    m = len(seq1)
    n = len(seq2)

    #m+1xn+1 scoring matrix
    scoring_matrix = [[None]*(n+1) for i in range (m+1)]

    #init row1 and col1
    scoring_matrix[0][0] = 0

    for x in range(1,m+1):
        scoring_matrix[x][0]= x*scores['gap']

    for x in range(1,n+1):
        scoring_matrix[0][x]= x*scores['gap']


    #calculate cell scores for other cells
    for x in range(1,m+1):
        for y in range(1,n+1):
            checkMatch(seq1,seq2,x,y)
            diagonal_score = scoring_matrix[x-1][y-1]+scores['match']
            vertical_score = scoring_matrix[x][y-1]+ scores['gap']
            horizontal_score = scoring_matrix[x-1][y]+ scores['gap']
            scoring_matrix[x][y] = max(diagonal_score,vertical_score,horizontal_score)

    for i in scoring_matrix[::-1]:
        print(i)

def checkMatch(seq1,seq2,m,n):
    if seq1[m-1]==seq2[n-1]:
        return 'match'
    else:
        return 'mismatch'

#sequenceAligner[seq1,seq2,[score]
#score=[match,mismatch,gap]
sequenceAligner('ATCG','TCG',[2,-2,-4])