from fpdf import FPDF, HTMLMixin
import time
import random
import string

def writePDF():
  html = """
  oeuoeueouuoeuoeueoueueouohouenoeh noeth neoth uoneth uoen huonehu onetuh noeth uoenthu oentuh oent uhoenth uoentuh oentu onetu onet hnothu noethu oentuh onteuh oenthu oentuh onetuh onetuh oenthu onet uoneth unoethu noet uhoenth uoent uhonehu noethu noethu onetuh oenth unoethu oenthu onethu noethu oent huoent hoenth uoenth uone hunote huoent uhoneth note hutnoeh unote hunoeth uonet uoenth uonet uonethu oenthu oentuh oneth eu<br>
  oeuoeueouuoeuoeueoueueouoeu<br>
  """

  class MyFPDF(FPDF, HTMLMixin):
	  pass
	 
  pdf=MyFPDF()
  #First page
  pdf.add_page()
  pdf.set_font("Arial", size=72)
  pdf.cell(200, 30, txt="CHICKEN SOUP", ln=1, align="C")
  pdf.set_font("Arial", size=30)
  pdf.cell(200, 30, txt="FOR", ln=1, align="C")
  pdf.set_font("Arial", size=72)
  pdf.cell(200, 30, txt="NAME'S", ln=1, align="C")
  pdf.cell(200, 30, txt="SOUL", ln=1, align="C")

  pdf.add_page()
  pdf.set_font("Arial", size=30)
  pdf.cell(200, 30, txt="NAME'S", ln=1, align="C")
  pdf.write_html(html)

  fileName = "app/books/" + time.strftime("%d-%m-%Y_%X_") + ''.join([random.choice(string.ascii_letters + string.digits) for n in range(9)]) + ".pdf"
  
  pdf.output(fileName, "F")
