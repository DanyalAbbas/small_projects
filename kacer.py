from pdf2image import convert_from_path
from paddleocr import PaddleOCR
import os

ocr = PaddleOCR(
    use_doc_orientation_classify=False, 
    use_doc_unwarping=False, 
    use_textline_orientation=True,
    lang="en",
    enable_mkldnn=False
)

result = ocr.predict('check.pdf')


print(result)