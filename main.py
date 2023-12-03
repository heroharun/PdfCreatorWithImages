from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from PIL import Image
import os
import re

def resimleri_pdfye_donustur(dizin, pdf_adresi):
    # PDF oluştur
    pdf = canvas.Canvas(pdf_adresi, pagesize=letter)
    width, height = letter

    # Belirtilen dizindeki resim dosyalarını adlarına göre sırala
    resim_dosyalari = sorted([dosya for dosya in os.listdir(dizin) if dosya.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp'))],
                             key=lambda x: int(re.search(r'\d+', x).group()))

    for sayfa_numarasi, resim_dosyasi in enumerate(resim_dosyalari, start=1):
        # Resmi PDF'ye ekle
        resim_yolu = os.path.join(dizin, resim_dosyasi)
        pdf.drawInlineImage(resim_yolu, 0, 0, width, height)

        # Sayfa numarasını ekleyin
        pdf.setFont("Helvetica", 12)
        pdf.drawString(10, 10, f"Sayfa {sayfa_numarasi}")

        # Yeni bir sayfa ekleyerek bir sonraki resim için hazırlık yap
        pdf.showPage()

    # PDF dosyasını kaydet
    pdf.save()

# if __name__ == "__main__":
#     dizin = "1.pdf"
#     pdf_adresi = "1a.pdf"
#
#     resimleri_pdfye_donustur(dizin, pdf_adresi)
#     print(f"{pdf_adresi} oluştu)")


if __name__ == "__main__":
    dizin = "2.pdf"
    pdf_adresi = "2a.pdf"
    resimleri_pdfye_donustur(dizin, pdf_adresi)
    print(f"{pdf_adresi} oluşturuldu.")

    dizin = "3.pdf"
    pdf_adresi = "3a.pdf"
    resimleri_pdfye_donustur(dizin, pdf_adresi)
    print(f"{pdf_adresi} oluşturuldu.")

    dizin = "4.pdf"
    pdf_adresi = "4a.pdf"
    resimleri_pdfye_donustur(dizin, pdf_adresi)
    print(f"{pdf_adresi} oluşturuldu.")

    dizin = "5.pdf"
    pdf_adresi = "5a.pdf"
    resimleri_pdfye_donustur(dizin, pdf_adresi)
    print(f"{pdf_adresi} oluşturuldu.")

    dizin = "6.pdf"
    pdf_adresi = "6a.pdf"
    resimleri_pdfye_donustur(dizin, pdf_adresi)
    print(f"{pdf_adresi} oluşturuldu.")

    dizin = "7.pdf"
    pdf_adresi = "7a.pdf"
    resimleri_pdfye_donustur(dizin, pdf_adresi)
    print(f"{pdf_adresi} oluşturuldu.")

    dizin = "8.pdf"
    pdf_adresi = "8a.pdf"
    resimleri_pdfye_donustur(dizin, pdf_adresi)
    print(f"{pdf_adresi} oluşturuldu.")

    dizin = "9.pdf"
    pdf_adresi = "9a.pdf"
    resimleri_pdfye_donustur(dizin, pdf_adresi)
    print(f"{pdf_adresi} oluşturuldu.")

    dizin = "10.pdf"
    pdf_adresi = "10a.pdf"
    resimleri_pdfye_donustur(dizin, pdf_adresi)
    print(f"{pdf_adresi} oluşturuldu.")

    dizin = "11.pdf"
    pdf_adresi = "11a.pdf"
    resimleri_pdfye_donustur(dizin, pdf_adresi)
    print(f"{pdf_adresi} oluşturuldu.")

    dizin = "12.pdf"
    pdf_adresi = "12a.pdf"
    resimleri_pdfye_donustur(dizin, pdf_adresi)
    print(f"{pdf_adresi} oluşturuldu.")

    dizin = "13.pdf"
    pdf_adresi = "13a.pdf"
    resimleri_pdfye_donustur(dizin, pdf_adresi)
    print(f"{pdf_adresi} oluşturuldu.")
