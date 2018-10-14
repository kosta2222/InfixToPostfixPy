import unittest as u
from compilMy.compilMy import opn,tokenze
#import pdb
#pdb.set_trace()


class MyTests(u.TestCase):
    def tests(self):
        self.assertEqual(opn(tokenze("1.0 + 2.0 ;")),['1.0','2.0','+'])
        self.assertEqual(opn(tokenze("1 + 2 + 4 ;")),['1','2','+','4','+'])
        self.assertEqual(opn(tokenze("( 1 + 2 ) * 4 ;")),['1', '2', '+', '4', '*'])  #ERROR
        self.assertEqual(opn(tokenze("( 125 * ( ( 131 + 48 ) / 35 ) ) / 7.9  ;")),['125', '131', '48', '+', '35', '/', '*', '7.9', '/']) 
        self.assertEqual(opn(tokenze("( 1 + 2 / x + y ) * 4 ;")),None)
    def exc(self):
        self.assertRaises(RuntimeError,opn(tokenze("1 + ( 2 + 4   ;"))) 
        self.assertRaises(RuntimeError,opn(tokenze("1 +  2 + 4  ) + x  ;")))               
        
if __name__=="__main__":
    u.main()
    
    
    