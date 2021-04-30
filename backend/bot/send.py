import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def ActivarCuenta(email,code):

    ccs = random.randint(1000000,9999999)
    proveedor_correo = 'smtp.gmail.com: 587'
    remitente = 'codegroup787@gmail.com'
    password = 'codegroup787..'

    servidor = smtplib.SMTP(proveedor_correo)
    servidor.starttls()
    servidor.ehlo()

    servidor.login(remitente, password)

    mensaje = f"""
    <div class="contenedor">
        <table style="border-collapse: collapse; margin: 0 auto; padding: 10px; text-align: center; position: relative;  border: 1px; width: 100%; max-width: 700px; height: 500px;">
            <tr>
                <td style="padding: 30px 0px 20px 0px; background-image: url(https://cdn.pixabay.com/photo/2016/03/26/13/09/notebook-1280538_960_720.jpg);">
                    <h2 style="color: rgb(238, 212, 128); font-size: 38px; font-family: 'Oi', cursive; font-weight: 600;">Data Filter</h2>
                    <hr style="border-top: 3px solid rgb(51, 22, 3); width: 190px; position: relative; left: 36%;">
                    <hr style="border-top: 3px solid rgb(51, 22, 3); width: 120px; position: relative; left: 41%;">
                    <hr style="border-top: 3px solid rgb(51, 22, 3); width: 60px; position: relative; left: 46%;">
                </td>
            </tr>
            <tr>
                <td style="padding: 20px 0px 50px 0px; background-color: rgba(161, 106, 55, 0.616);">
                    <div>
                        <p style=" font-size: 18px; font-weight: bold; font-family: 'Roboto', sans-serif;">Lorem ipsum dolor sit amet <span style="color: red;">(nombre)</span> consectetur adipisicing elit. Temporibus laudantium ipsa dolor nisi eos repellat, neque saepe sapiente nemo a, illo hic id aperiam amet quam mollitia esse perspiciatis fugit.</p>
                        <br>
                        <a href="http://localhost:4200/activated-account/{code}" style="text-decoration: none; border-radius: 5px; box-shadow: 3px 3px rgb(17, 47, 145); font-size: 23px; font-weight: 600; padding: 10px 20px; color: black; background-color: rgb(44, 93, 255); border: 2px solid #0016b0; color: #FFF; font-family: 'Chango', cursive;">Activar Cuenta</a>
                    </div>
                </td>
            </tr>
            <tr style="height: 15px;">
                <td style="background-color: rgba(87, 59, 32, 0.616);">
                    <p style="position: relative; top: 6px; font-family: 'Dancing Script', cursive;">Code Group</p>
                </td>
            </tr>
        </table>
    </div>"""
    msg = MIMEMultipart()
    msg.attach(MIMEText(mensaje, 'html'))
    msg['From'] = remitente
    msg['To'] = email
    msg['Subject'] = 'Prueba'
    servidor.sendmail(msg['From'] , msg['To'], msg.as_string())

def RecuperarContrasena(email,code):
    ccs = random.randint(1000000,9999999)
    proveedor_correo = 'smtp.gmail.com: 587'
    remitente = 'codegroup787@gmail.com'
    password = 'codegroup787..'

    servidor = smtplib.SMTP(proveedor_correo)
    servidor.starttls()
    servidor.ehlo()

    servidor.login(remitente, password)

    mensaje = f"""
    <div class="contenedor">
        <table style="border-collapse: collapse; margin: 0 auto; padding: 10px; text-align: center; position: relative;  border: 1px; width: 100%; max-width: 700px; height: 500px;">
            <tr>
                <td style="padding: 30px 0px 20px 0px; background-image: url(https://cdn.pixabay.com/photo/2016/03/26/13/09/notebook-1280538_960_720.jpg);">
                    <h2 style="color: rgb(238, 212, 128); font-size: 38px; font-family: 'Oi', cursive; font-weight: 600;">Data Filter</h2>
                    <hr style="border-top: 3px solid rgb(51, 22, 3); width: 190px; position: relative; left: 36%;">
                    <hr style="border-top: 3px solid rgb(51, 22, 3); width: 120px; position: relative; left: 41%;">
                    <hr style="border-top: 3px solid rgb(51, 22, 3); width: 60px; position: relative; left: 46%;">
                </td>
            </tr>
            <tr>
                <td style="padding: 20px 0px 50px 0px; background-color: rgba(161, 106, 55, 0.616);">
                    <div>
                        <p style=" font-size: 18px; font-weight: bold; font-family: 'Roboto', sans-serif;">Lorem ipsum dolor sit amet <span style="color: red;">(nombre)</span> consectetur adipisicing elit. Temporibus laudantium ipsa dolor nisi eos repellat, neque saepe sapiente nemo a, illo hic id aperiam amet quam mollitia esse perspiciatis fugit.</p>
                        <br>
                        <a href="http://localhost:4200/recovery/{code}" style="text-decoration: none; border-radius: 5px; box-shadow: 3px 3px rgb(17, 47, 145); font-size: 23px; font-weight: 600; padding: 10px 20px; color: black; background-color: rgb(44, 93, 255); border: 2px solid #0016b0; color: #FFF; font-family: 'Chango', cursive;">Recuperar</a>
                    </div>
                </td>
            </tr>
            <tr style="height: 15px;">
                <td style="background-color: rgba(87, 59, 32, 0.616);">
                    <p style="position: relative; top: 6px; font-family: 'Dancing Script', cursive;">Code Group</p>
                </td>
            </tr>
        </table>
    </div>"""
    msg = MIMEMultipart()
    msg.attach(MIMEText(mensaje, 'html'))
    msg['From'] = remitente
    msg['To'] = email
    msg['Subject'] = 'Prueba'
    servidor.sendmail(msg['From'] , msg['To'], msg.as_string())

def SendMailToCollaborators(email):
    nombre = "Luis"
    apellido = "Eduardo"

    ccs = random.randint(1000000,9999999)
    proveedor_correo = 'smtp.gmail.com: 587'
    remitente = 'codegroup787@gmail.com'
    password = 'codegroup787..'

    servidor = smtplib.SMTP(proveedor_correo)
    servidor.starttls()
    servidor.ehlo()

    servidor.login(remitente, password)

    mensaje = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset='utf-8'>
        <meta http-equiv='X-UA-Compatible' content='IE=edge'>
        <title>correo</title>
        <meta name='viewport' content='width=device-width, initial-scale=1'>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">

        <link rel="preconnect" href="https://fonts.gstatic.com">
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap" rel="stylesheet">
        <link rel="preconnect" href="https://fonts.gstatic.com">
        <link href="https://fonts.googleapis.com/css2?family=Lobster&display=swap" rel="stylesheet">
        <link rel="preconnect" href="https://fonts.gstatic.com">
        <link href="https://fonts.googleapis.com/css2?family=Chivo:wght@300&display=swap" rel="stylesheet">

    </head>  
    <body>
        <div class="contenedor">
            <table style="border-collapse: collapse; margin: 0 auto; padding: 10px; text-align: center; position: relative; width: 100%; max-width: 700px; height: 500px;">
                <tr>
                    <td style="background-color: #FFF; ">
                        <h2 style="color: #000; font-size: 66px; font-family: 'Roboto', sans-serif; -webkit-text-stroke: 2px black;">Data Filter</h2>
                        <hr style="border-top: 2px solid #000;">
                    </td> 
                </tr>
                <tr>
                    <td style="padding: 0px 0px 30px 0px; background-color: #FFF;">
                        <div>
                            <p style="padding-bottom: 10px; font-size: 18px; font-weight: bold; color: rgb(0, 0, 0); font-family: 'Roboto', sans-serif;">Bienvenido a nuestro aplicativo web señor(a) <span style="color: red;">(nombre)</span>, solo hace falta 1 paso más para completar su registro, ese único paso es oprimir el botón que se encuentra en la parte inferior, el cual lo redireccionará a nuestro aplicativo para que usted pueda ingresar exitosamente y hacer uso de él.</p>
                            <br>
                            <a href="https://www.youtube.com/" style="text-decoration: none; border-radius: 5px; box-shadow: 3px 3px rgb(0, 0, 0); font-size: 23px; font-weight: 600; padding: 10px 20px; color: #FFF; background-color: rgb(31, 31, 31); color: #FFF; font-family: 'Chivo', sans-serif;">Verificar</a>
                        </div>
                    </td>
                </tr>
                <tr style="height: 15px;">
                    <td style="background-color: #FFF;">
                        <hr style="border-top: 2px solid #000; position: relative; top: 10px;">
                        <p style="font-weight: bold; position: relative; color: #000; top: 16px; font-family: 'Roboto', sans-serif;">Derechos reservados a <span style="font-weight: bold; color: #000; font-family: 'Lobster', cursive;">Code Group</span>. 2021</p>
                    </td>
                </tr>
            </table>
        </div>
    </body>
    </html>"""
    msg = MIMEMultipart()
    msg.attach(MIMEText(mensaje, 'html'))
    msg['From'] = remitente
    msg['To'] = email
    msg['Subject'] = 'Prueba'
    servidor.sendmail(msg['From'] , msg['To'], msg.as_string())