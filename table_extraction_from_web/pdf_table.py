"""
!pip install tabula

Run this in terminal before running the code
"""
import pandas as pd
import tabula

data=tabula.read_pdf("Pdf_name.pdf",pages=1)
