import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_mail(out):
	fromaddr = "shantha2106@gmail.com"
	toaddr = "rahulrk.2303@gmail.com"

	msg = MIMEMultipart()

	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = out

	body = "Find the attachment"

	msg.attach(MIMEText(body, 'image/png'))

	filename = "Report.png"
	attachment = open(r"plot.png", "rb")

	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

	msg.attach(part)

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, "04443210445")
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()

# send_mail()