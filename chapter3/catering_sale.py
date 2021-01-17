import pandas as pd
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def showDescribe(fileName, index):
    data = pd.read_excel(catering_sale, index_col= index)
    logging.debug(data.describe())


if __name__ == "__main__":
    catering_sale = './data/catering_sale.xls'
    showDescribe(catering_sale, u'日期')
    pass