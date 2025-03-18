import io
import os

from PyPDF2 import PdfFileReader, PdfFileWriter
from django.conf import settings as django_settings
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas


def _create_stud_pdf(student):
    packet_1 = io.BytesIO()
    packet_2 = io.BytesIO()
    can_1 = canvas.Canvas(packet_1, pagesize=A4)
    can_2 = canvas.Canvas(packet_2, pagesize=A4)

    for image in os.listdir(f"{django_settings.MEDIA_ME}image/student"):
        full_name = f"{student.last_name}_{student.first_name}".lower()
        folder_name = image
        if folder_name == full_name:
            pic = f"{django_settings.MEDIA_ME}image/student/{folder_name}/{folder_name}.jpg"

            can_1.drawInlineImage(pic, 451, 545, width=3.7 * cm, height=3.7 * cm)

    can_1.setFont("Helvetica", 10)
    # Matric no
    can_1.drawString(234, 638, student.matric_number)

    # # Jamb no
    can_1.drawString(234, 606, student.jamb_number)

    # # college
    can_1.drawString(234, 580, student.college)

    # # level
    can_1.drawString(234, 520, student.level)

    # # last_name
    can_1.drawString(370, 488, student.last_name)

    # # middle_name
    can_1.drawString(370, 458, student.middle_name)

    # # first_name
    can_1.drawString(370, 428, student.first_name)

    # # age
    can_1.drawString(234, 398, student.age)

    # # gender
    can_1.drawString(234, 366, student.gender)

    # # dob
    can_1.drawString(234, 322, str(student.date_of_birth)[8:])
    can_1.drawString(343, 322, str(student.date_of_birth)[5:7])
    can_1.drawString(453, 322, str(student.date_of_birth)[:4])

    # # nationality
    can_1.drawString(234, 280, student.nationality)

    # # state of origin
    can_1.drawString(234, 248, student.state_of_origin)

    # # Marital status
    can_1.drawString(234, 208, student.marital_status)

    # # cell phone
    can_1.drawString(240, 88, student.phone_number)

    # # email
    can_1.drawString(240, 58, student.email)

    can_1.setFont("Helvetica", 9)
    # # dept
    can_1.drawString(234, 550, student.department)

    # # lga_origin
    can_1.drawString(399, 248, student.lga_origin)

    # # home address
    can_1.drawString(240, 118, student.address)

    can_1.save()

    # # set font
    can_2.setFont("Helvetica", 10)

    # # parent's name
    can_2.drawString(240, 750, student.parent_name)

    # # parent's email
    can_2.drawString(240, 722, student.parent_email)

    # # parent's cell phone
    can_2.drawString(240, 694, student.parent_phone)

    # m dor
    can_2.drawString(214, 622, str(student.date_of_registration))

    can_2.save()

    # move to the beginning of the StringIO buffer
    packet_1.seek(0)
    packet_2.seek(0)
    new_pdf_1 = PdfFileReader(packet_1)
    new_pdf_2 = PdfFileReader(packet_2)

    # read your existing PDF
    existing_pdf = PdfFileReader(
        open(f"{django_settings.STATIC_ME}doc/student_details.pdf", "rb")
    )
    output = PdfFileWriter()

    # add the "watermark" (which is the new pdf) on the existing page
    page_1 = existing_pdf.getPage(0)
    page_2 = existing_pdf.getPage(1)

    page_1.mergePage(new_pdf_1.getPage(0))
    page_2.mergePage(new_pdf_2.getPage(0))

    output.addPage(page_1)
    output.addPage(page_2)

    outputStream = open(f"{django_settings.MEDIA_ME}pdf/student_detail.pdf", "wb")
    output.write(outputStream)
    outputStream.close()


def _create_staf_pdf(staff):
    packet_1 = io.BytesIO()
    can_1 = canvas.Canvas(packet_1, pagesize=A4)

    for image in os.listdir(f"{django_settings.MEDIA_ME}image/staff"):
        full_name = f"{staff.last_name}_{staff.first_name}".lower()
        folder_name = image
        if folder_name == full_name:
            pic = (
                f"{django_settings.MEDIA_ME}image/staff/{folder_name}/{folder_name}.jpg"
            )

            can_1.drawInlineImage(pic, 446, 540, width=3.7 * cm, height=3.7 * cm)

    can_1.setFont("Helvetica", 10)
    # # last_name
    can_1.drawString(270, 626, staff.last_name)

    # # middle_name
    can_1.drawString(270, 588, staff.middle_name)

    # # first_name
    can_1.drawString(270, 550, staff.first_name)

    # # profession
    can_1.drawString(158, 510, staff.profession)

    # # age
    can_1.drawString(158, 480, staff.age)

    # # gender
    can_1.drawString(158, 448, staff.gender)

    # # dob
    can_1.drawString(158, 404, str(staff.date_of_birth)[8:])
    can_1.drawString(295, 404, str(staff.date_of_birth)[5:7])
    can_1.drawString(429, 404, str(staff.date_of_birth)[:4])

    # # nationality
    can_1.drawString(158, 360, staff.nationality)

    # # state of origin
    can_1.drawString(158, 328, staff.state_of_origin)

    # # Marital status
    can_1.drawString(158, 284, staff.marital_status)

    # # cell phone
    can_1.drawString(240, 160, staff.phone_number)

    # m dor
    can_1.drawString(216, 56, str(staff.date_of_registration))

    can_1.setFont("Helvetica", 9)
    # # lga_origin
    can_1.drawString(364, 328, staff.lga_origin)
    # # home address
    can_1.drawString(240, 190, staff.address)
    # # email
    can_1.drawString(240, 130, staff.email)

    can_1.save()

    # move to the beginning of the StringIO buffer
    packet_1.seek(0)
    new_pdf_1 = PdfFileReader(packet_1)

    # read your existing PDF
    existing_pdf = PdfFileReader(
        open(f"{django_settings.STATIC_ME}doc/staff_details.pdf", "rb")
    )
    output = PdfFileWriter()

    # add the "watermark" (which is the new pdf) on the existing page
    page_1 = existing_pdf.getPage(0)

    page_1.mergePage(new_pdf_1.getPage(0))

    output.addPage(page_1)

    outputStream = open(f"{django_settings.MEDIA_ME}pdf/staff_detail.pdf", "wb")
    output.write(outputStream)
    outputStream.close()
