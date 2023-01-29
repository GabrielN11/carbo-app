def generateValidationTemplate(username, code):
    return f"""
    <!DOCTYPE html>
    <html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    </head>
    <body style="background-color: #f3f2ef; padding: 25px;">
        <div style="max-width: 500px; margin: 0 auto; padding: 30px 25px; background-color: #16181b; color: #fff; border-radius: 15px;">
            <div>
                <p style="text-align: center;">Olá @{username}! Para finalizar seu cadastro basta copiar o código abaixo e colar no site do CarboApp!</p>
                <p style="text-align: center; padding: 10px 25px; background-color: #2D2F31; border-radius: 15px; font-size: 1.2rem;">{code}</p>
            </div>
        </div>
    </body>
    </html>
    """

def generateRecoveryTemplate(username, code):
    return f"""
    <!DOCTYPE html>
    <html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    </head>
    <body style="background-color: #f3f2ef; padding: 25px;">
        <div style="max-width: 500px; margin: 0 auto; padding: 30px 25px; background-color: #16181b; color: #fff; border-radius: 15px;">
            <div>
                <p style="text-align: center; margin-bottom: 10px;">Olá @{username}! Para recuperar sua conta, insira o código abaixo no site do CarboApp.</p>
                <p style="text-align: center; padding: 10px 25px; background-color: #2D2F31; border-radius: 15px; font-size: 1.2rem;">{code}</p>
            </div>
        </div>
    </body>
    </html>
    """