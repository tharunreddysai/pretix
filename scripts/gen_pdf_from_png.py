import os
import img2pdf

image = '/Users/tharunreddy/Downloads/IIDC TICKET 2-min.png'

with open("output.pdf", "wb") as f:
    f.write(img2pdf.convert([image]))



