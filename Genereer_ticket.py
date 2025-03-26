import qrcode
import time
import os
from reportlab.pdfgen import canvas
from datetime import date
import glob

today1 = date.today()
today = today1.strftime("%d-%m-%Y")

def selectie(leeftijd, mapnaam):

    if leeftijd < 4:
        data = f"Ticket jong kind 0-3 {today}"
        kleur = "black"
        naam = "QR0-3"

    elif leeftijd > 3 and leeftijd < 8:
        data = f"Ticket kind 4-7 {today}"
        kleur = "yellow"
        naam  = "QR4-7"

    elif leeftijd > 7 and leeftijd < 12:
        data = f"Ticket kind 8-11 {today}"
        kleur = "orange"
        naam = "QR8-11"

    elif leeftijd > 11 and leeftijd < 19:
        data = f"Ticket kind 12-18 {today}"
        kleur = "red"
        naam = "QR12-18"

    elif leeftijd > 18 and leeftijd < 65:
        data = f"Ticket volwassene {today}"
        kleur = "red"
        naam = "QRvolwassene"

    elif leeftijd > 64:
        data = f"Ticket senior {today}"
        kleur = "red"
        naam = "QRsenior"

    qr_img = qr_code(data, kleur, naam)
    ticket_pfd(qr_img, naam, mapnaam, data)

def qr_code(data, kleur, naam):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code (1 is smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in the QR code grid
        border=4,  # Border size
    )
    qr.add_data(data)
    qr.make(fit=True)
    # Create and save the image
    img = qr.make_image(fill_color=kleur, back_color="white")
    img.save(f"{naam}")

def ticket_pfd(qr_img, naam, mapnaam, data):
    os.makedirs(mapnaam, exist_ok=True)
    pdf_path = os.path.join(mapnaam, f"ticket {naam} {int(time.time())}.pdf")

    QR_path = f"{naam}"
    plattegrond = "ticket_leeg.png"
    # Create a PDF
    c = canvas.Canvas(pdf_path)
    # Add text (optional)
    c.drawString(25, 800, f"{data}")
    # Add the image to the PDF
    c.drawImage(QR_path, 25, 550, width=200, height=200)
    c.drawImage(plattegrond, 10, 10, width=575, height=500)
    # Save the PDF
    c.save()
    os.remove(QR_path)

def parkeer_ticket_pdf(mapnaam):
    data = f"Parkeerticket {today}"
    kleur = "black"
    naam = "QRparkeren"

    qr_img = qr_code(data, kleur, naam)
    os.makedirs(mapnaam, exist_ok=True)
    pdf_path = os.path.join(mapnaam, f"Parkeerticket {int(time.time())}.pdf")

    QR_path = f"{naam}"
    parkeerplaats = "parkeerplaats.png"
    # Create a PDF
    c = canvas.Canvas(pdf_path)
    # Add text (optional)
    c.drawString(25, 800, f"Parkeerticket{today}")
    # Add the image to the PDF
    c.drawImage(QR_path, 25, 550, width=200, height=200)
    c.drawImage(parkeerplaats, 10, 10, width=575, height=450)
    # Save the PDF
    c.save()
    os.remove(QR_path)


