from pdf2image import convert_from_path
from paddleocr import PaddleOCR
import os
import numpy as np
import cv2

ocr_engine = PaddleOCR(use_angle_cls=True, lang='en')

def extract_text_with_ocr(pdf_path):
    print("  Starting OCR fallback (this may take a moment)...")
    full_text = ""
    
    pages = convert_from_path(pdf_path, dpi=200)
    print(f"  PDF converted to {len(pages)} images.")
    
    for i, page in enumerate(pages):
        img_array = np.array(page)
        img_bgr = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
        
        results = list(ocr_engine.predict(img_bgr))
        
        page_text = ""
        if results:
            res_obj = results[0]
            
            # Access the underlying dictionary if it's a PaddleX Result object
            data_dict = res_obj.res if hasattr(res_obj, 'res') else res_obj
            
            if isinstance(data_dict, dict) and 'rec_texts' in data_dict:
                for text_snippet in data_dict['rec_texts']:
                    if text_snippet: 
                        page_text += str(text_snippet) + "\n"
                
        full_text += page_text + "\n"
        print(f"  OCR complete for page {i + 1}/{len(pages)}")
        
    return full_text


print(extract_text_with_ocr("check.pdf"))