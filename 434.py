#!/usr/bin/env python
#-*- encoding: cp1251 -*-
import xlrd, xlwt
from xlutils.copy import copy

source_filename = "mask.xls"
destination_filename = "data.xls"

read_book = xlrd.open_workbook(source_filename, on_demand=True)  # Открываем исходный документ
read_sheet = read_book.get_sheet(0)  # Читаем из первого листа
write_book = copy(read_book)  # Копируем таблицу в память, в неё мы ниже будем записывать


write_sheet = write_book.get_sheet(0)  # Будем записывать в первый лист


write_book.save(destination_filename)  # Сохраняем таблицу
