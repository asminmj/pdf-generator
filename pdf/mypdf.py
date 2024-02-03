from reportlab.pdfgen import canvas 

fileName = 'MyDoc.pdf'

pdf = canvas.Canvas(fileName)

pdf.save()