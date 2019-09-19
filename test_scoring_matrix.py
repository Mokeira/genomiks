import unittest
from scoringMatrix import sequenceAligner

class TestScoringMatrix(unittest.TestCase):

	def test_sequence_aligner(self):
		seq1,seq2 = sequenceAligner('ATCG','TCG',[2,-2,-4]) 
		self.assertEqual(seq1,'ATCG')
		self.assertEqual(seq2,'_TCG')


		seq1,seq2 = sequenceAligner('AAAC','AGC',[1,-1,-2]) 
		self.assertEqual(seq1,'AAAC')
		self.assertEqual(seq2,'_AGC')
		
if __name__ == '__main__':
    unittest.main()

