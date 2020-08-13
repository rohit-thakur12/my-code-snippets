

import glob
import fitz
import pandas as pd
import numpy as np
import os

import warnings
warnings.filterwarnings("ignore")

class ExtractPdfToExcel:
    """
        A class that returns a dataframe of data extracted from all the pdf present in the path provided.
        The dataframe will have three columns that will consist of the document name, page number 
        that it has extracted from and the text that it has extracted.
        
        Arguments:
            The class uses glob to create a list of all the pdf in a directory, so the only argument is takes
            if the path to all the files.
            
            E.g:
            path(required) = "C://User//files"
            
            The user need not complete the path name with the file names as we add "\\.*pdf" at the end. 
            
        Returns:
            
            A dataframe of extracted text.
    
    """
    
    def __init__(self,path):
        self.path = path
        
    def getPageText(self):
        df = pd.DataFrame()
        files = glob.glob(self.path + "\\*.pdf")
        
        for file in files:
            file_path = os.path.join(self.path,file)
            head_tail = os.path.split(file_path)
            docname = head_tail[1]
            pdf_document = file_path
            doc = fitz.open(pdf_document)
            pages = doc.pageCount
            for i in range(pages):
                page1 = doc.loadPage(i)
                page1text = page1.getText("text")
                page = pd.Series(page1text)
                temp_df = page.to_frame()
                temp_df['Docname'] = docname
                temp_df['Pagenumber'] = i
                df = df.append(temp_df, ignore_index=True)
        return df
