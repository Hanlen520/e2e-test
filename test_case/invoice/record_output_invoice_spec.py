import unittest
import sys
import os
from selenium import webdriver
import time
import random
from HTMLTestRunner import HTMLTestRunner
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../../'))
from .invoice_page import InvoicePage
from test_data.record_output_invoice_data import *
from util.enter_company_util import EnterCompany
from config import *


class RecordOutputInvoiceSpec(unittest.TestCase):
    ''' 记开票测试 '''

    def setUp(self):
        self.driver = webdriver.Chrome()
        EnterCompany(self.driver,Environment)
        self.invoice_page = InvoicePage(self.driver,'output')
        self.invoice_page.goToInvoice(BaseUrl)

    def test1(self):
        '''成功记录一笔开票-普票-税控自开测试'''

        outputInvoicePublic = ['1','普票','税控自开','内部代表']
        outputInvoiceNum = '00000000'
        outputInvoiceItems = [['1','1'],'管理部门','5%','41111','普票-税控自开-商品销售-5%-管理部门41111']
        self.invoice_page.recordOutputInvoice(outputInvoicePublic,outputInvoiceNum,outputInvoiceItems)

    def test2(self):
        '''成功记录多笔开票记录测试'''

        invoiceNumList = []
        for i in range(0,10):
            invoiceNumList.append(self.invoiceNum())
        outputInvoicePublic = ['1','普票','税控自开','内部代表']
        for outputInvoiceItems,outputInvoiceNum in zip(RecordCommonOutputInvoiceSelfData,invoiceNumList):
            self.invoice_page.recordOutputInvoice(outputInvoicePublic,outputInvoiceNum,outputInvoiceItems)
        self.invoice_page.goToInvoiceList(BaseUrl)
        self.assertEqual(BaseUrl + '/app/invoice/output-invoice',self.driver.current_url)

    # def test2(self):
    #     '''记所有类别的收票-专票'''

    #     invoice_page = InvoicePage(self.driver,'input')
    #     specialPublicInvoice = ['1','专票','内部代表']
    #     invoiceNumList = []
    #     for i in range(0,33):
    #         invoiceNumList.append(self.invoiceNum())

    #     for specialItems,invoiceNum in zip(RecordSpecialIncomeInvoiceData,invoiceNumList):
    #          invoice_page.recordSpecialIncomeInvoice(specialPublicInvoice,invoiceNum,specialItems)
    #     invoice_page.goToInvoiceList(BaseUrl)
    #     self.assertEqual(BaseUrl + '/app/invoice/input-invoice',self.driver.current_url)   

    #生成8位随机整数
    def invoiceNum(self):
        invoiceNum = ''
        for i in range(0,8) :
            invoiceNum = invoiceNum + str(random.randint(0,9))
        return invoiceNum

    def tearDown(self):
        self.driver.quit()
        

if __name__ == '__main__':
    unittest.main()
