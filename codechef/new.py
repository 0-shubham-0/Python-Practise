from doctr.models import ocr_predictor

model = ocr_predictor(det_arch='db_resnet50', reco_arch='crnn_vgg16_bn', pretrained=True)
from doctr.io import DocumentFile
# PDF
# pdf_doc = DocumentFile.from_pdf("path/to/your/doc.pdf")
# Webpage
# webpage_doc = DocumentFile.from_url("https://www.yoursite.com")
# Multiple page images
# multi_img_doc = DocumentFile.from_images(["path/to/page1.jpg", "path/to/page2.jpg"])

# Image
single_img_doc = DocumentFile.from_images("doctr\download.png")