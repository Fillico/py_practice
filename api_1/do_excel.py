#!/usr/bin/python3
#-*- coding:utf-8 -*-
#作者：Fillico
#日期：2019/4/14

from openpyxl import load_workbook

class do_excel:
    def __init__(self,file_name,sheet_name):
        self.file_name=file_name
        self.sheet_name=sheet_name
    def read_excel(self):
        wb=load_workbook(filename=self.file_name)
        sheet=wb[self.sheet_name]