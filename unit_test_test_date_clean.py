import unittest
import gls_preprocess_standard_update_v1 as clean_data
 
class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_case_1(self):
        d = clean_data.gls_preprocess('1/1/2016',None,None,None,None,None,None).gls_date()['date_modify_1'][0]
        self.assertEqual(d, '01-01-2016')

    def test_case_2(self):  
        d = clean_data.gls_preprocess('2014 mar 08',None,None,None,None,None,None).gls_date()['date_modify_1'][0]
        self.assertEqual(d, '08-03-2014')

    def test_case_3(self):  
        d = clean_data.gls_preprocess('08 mar 2014',None,None,None,None,None,None).gls_date()['date_modify_1'][0]
        self.assertEqual(d, '08-03-2014')

    def test_case_4(self):  
        d = clean_data.gls_preprocess('08 mar 14',None,None,None,None,None,None).gls_date()['date_modify_1'][0]
        self.assertEqual(d, '08-03-2014')

    def test_case_5(self):  
        d = clean_data.gls_preprocess('2014 mar 08',None,None,None,None,None,None).gls_date()['date_modify_1'][0]
        self.assertEqual(d, '08-03-2014')

    def test_case_6(self):  
        d = clean_data.gls_preprocess('2014 mar 08',None,None,None,None,None,None).gls_date()['date_modify_1'][0]
        self.assertEqual(d, '08-03-2014')

    def test_case_7(self):  
        d = clean_data.gls_preprocess('Mar 2014 03',None,None,None,None,None,None).gls_date()['date_modify_1'][0]
        self.assertEqual(d, '03-03-2014')

    def test_case_8(self):  
        d = clean_data.gls_preprocess('08 2014 mar',None,None,None,None,None,None).gls_date()['date_modify_1'][0]
        self.assertEqual(d, '08-03-2014')    
 
    def test_case_9(self):  
        d = clean_data.gls_preprocess('2014 03',None,None,None,None,None,None).gls_date()['date_modify_1'][0]
        self.assertEqual(d, '01-03-2014')

    def test_case_9(self):  
        d = clean_data.gls_preprocess('2014 03',None,None,None,None,None,None).gls_date()['date_modify_1'][0]
        self.assertEqual(d, '01-03-2014')   


    def test_case_10(self):  
        d = clean_data.gls_preprocess('04 14',None,None,None,None,None,None).gls_date()['date_modify_1'][0]
        self.assertEqual(d, '01-04-2014')

    def test_case_11(self):  
        d = clean_data.gls_preprocess('2014 08 03',None,None,None,None,None,None).gls_date()['date_modify_1'][0]
        self.assertEqual(d, '03-08-2014')   


    def test_case_12(self):  
        d = clean_data.gls_preprocess('1/9',None,None,None,None,None,None).gls_date()['date_modify_1'][0]
        self.assertEqual(d, '01-01-2009')

    def test_case_13(self):  
        d = clean_data.gls_preprocess('2014 3',None,None,None,None,None,None).gls_date()['date_modify_1'][0]
        self.assertEqual(d, '01-03-2014')

    def test_case_14(self):  
        d = clean_data.gls_preprocess('octobre 2011',None,None,None,None,None,None).gls_date()['date_modify_1'][0]
        self.assertEqual(d, 'wrong_date')   


    def test_case_15(self):  
        d = clean_data.gls_preprocess('2014 13',None,None,None,None,None,None).gls_date()['date_modify_1'][0]
        self.assertEqual(d, 'wrong_date')

    def test_case_16(self):  
        d = clean_data.gls_preprocess('14/13',None,None,None,None,None,None).gls_date()['date_modify_1'][0]
        self.assertEqual(d, 'wrong_date')   


    def test_case_17(self):  
        d = clean_data.gls_preprocess('2014 03',None,None,None,None,None,None).gls_date()['date_modify_1'][0]
        self.assertEqual(d, '01-03-2014')

    def test_case_18(self):  
        d = clean_data.gls_preprocess('Sep 1997',None,None,None,None,None,None).gls_date()['date_modify_1'][0]
        self.assertEqual(d, '01-09-1997')


    def test_case_19(self):  
        d = clean_data.gls_preprocess('7/3',None,None,None,None,None,None).gls_date()['date_modify_1'][0]
        self.assertEqual(d, '01-07-2003')

    def test_case_20(self):  
        d = clean_data.gls_preprocess('070-3',None,None,None,None,None,None).gls_date()['date_modify_1'][0]
        self.assertEqual(d, 'wrong_date')   


    def test_case_21(self):  
        d = clean_data.gls_preprocess('14 03',None,None,None,None,None,None).gls_date()['date_modify_1'][0]
        self.assertEqual(d, 'wrong_date')

    def test_case_22(self):  
        d = clean_data.gls_preprocess('01-01-2011',None,None,None,None,None,None).gls_date()['date_modify_1'][0]
        self.assertEqual(d, '01-01-2011')


    def test_case_23(self):  
        d = clean_data.gls_preprocess('2/3',None,None,None,None,None,None).gls_date()['date_modify_1'][0]
        self.assertEqual(d, '01-02-2003')


    def test_case_24(self):  
        d = clean_data.gls_preprocess('04/0',None,None,None,None,None,None).gls_date()['date_modify_1'][0]
        self.assertEqual(d, '01-04-2000')

    def test_case_25(self):  
        d = clean_data.gls_preprocess('10-2',None,None,None,None,None,None).gls_date()['date_modify_1'][0]
        self.assertEqual(d, '01-10-2002')

    def test_case_26(self):  
        d = clean_data.gls_preprocess('31-2',None,None,None,None,None,None).gls_date()['date_modify_1'][0]
        self.assertEqual(d, 'wrong_date')

    def test_case_27(self):  
        d = clean_data.gls_preprocess('2-12',None,None,None,None,None,None).gls_date()['date_modify_1'][0]
        self.assertEqual(d, '01-02-2012')




if __name__ == '__main__':
    unittest.main()