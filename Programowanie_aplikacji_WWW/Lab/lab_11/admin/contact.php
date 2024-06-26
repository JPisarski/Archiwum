<link rel="stylesheet" href="../css/style_admin.css">

<?php

// dołączamy zawartość pliku cfg.php

include('../cfg.php');

// importujemy klasy PHPMailer do globalnej przestrzeni nazw

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

require '../PHPMailer-master/src/PHPMailer.php';
require '../PHPMailer-master/src/SMTP.php';
require '../PHPMailer-master/src/Exception.php';

// funkcja PokazKontakt() wyświetla formularz, który jest potrzebny do wysłania maila 

function PokazKontakt()
{
	echo '
    <div><br>
        <h1 class="naglowek">Wyślij mail</h1>
            <form method="post" action="'.$_SERVER['REQUEST_URI'].'">
                <table>
					<tr><td>Nadawca:</td><td><input type="text" name="nadawca" size="50" required/></td></tr>
                    <tr><td>E-mail:</td><td><input type="text" name="adres" size="50" required/td></tr>
					<tr><td>Temat:</td><td><input type="text" name="temat" size="50" required/></td></tr>
                    <tr><td>Wiadomość:</td><td><textarea name="tresc" rows=15 cols=47 required></textarea></td></tr>                 
                    <tr><td></td><td><input type="submit" name="wyslij_mail" value="Wyślij mail" /></td></tr>
                </table>
            </form>
    </div>
	';
}

// funkcja WyslijMailKontakt() wysyła mail utworzony za pomocą danych zawartych w powyższym formularzu 

function WyslijMailKontakt()
{
	global $config;
	PokazKontakt();
	
	if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['wyslij_mail'])) {
		$mail = new PHPMailer(true);
		
        try {
			$mail->CharSet = "UTF-8";
            $mail->SMTPDebug = 0; 
            $mail->isSMTP();
            $mail->Host = $config['smtp_host'];
            $mail->SMTPAuth = $config['smtp_auth'];
            $mail->Username = $config['smtp_username'];
            $mail->Password = $config['smtp_password'];
            $mail->SMTPSecure = $config['smtp_secure'];
            $mail->Port = $config['smtp_port'];
            $mail->setFrom($_POST['adres'], $_POST['nadawca']);
			$mail->AddReplyTo($_POST['adres'], $_POST['nadawca']);
            $mail->addAddress("jn242031@gmail.com");
            $mail->isHTML(false);
            $mail->Subject = $_POST['temat'];
            $mail->Body = $_POST['tresc'];
			
			// wysyłanie maila
			
            $mail->send();
			echo "<script>window.location.href='contact.php';</script>";
			exit();
        } catch (Exception $e) {
             echo '<center>Wiadomość nie została wysłana.</center>';
        }
    } 
}

// funkcja PrzypomnijHaslo() wyświetla formularz, a następny wysyła na podany w wcześniej wymienionym formularzu
// adres e-mail wiadomość zawierającą zapomniane hasło

function PrzypomnijHaslo()
{
	global $login;
	global $pass;
	global $config;
	
	echo '
	<div><br>
        <h1 class="naglowek">Przypomnij hasło</h1>
            <form method="post" action="'.$_SERVER['REQUEST_URI'].'">
                <table>
					<tr><td>Login:</td><td><input type="text" name="login" required /></td></tr>
                    <tr><td>E-mail:</td><td><input type="text" name="emaild" required/></td></tr>
                    <tr><td></td><td><input type="submit" name="przypomij_haslo" value="Przypomnij hasło" /></td></tr>
                </table>
            </form>
    </div>
	';
	
	if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['przypomij_haslo'])) {
		if($login == $_POST['login'])
		{
			$mail = new PHPMailer(true);
	
			try {
				$mail->CharSet = "UTF-8";
				$mail->SMTPDebug = 0;
				$mail->isSMTP();
				$mail->Host = $config['smtp_host'];
				$mail->SMTPAuth = $config['smtp_auth'];
				$mail->Username = $config['smtp_username'];
				$mail->Password = $config['smtp_password'];
				$mail->SMTPSecure = $config['smtp_secure'];
				$mail->Port = $config['smtp_port'];
				$mail->setFrom('jn242031@gmail.com', 'Wiadomość przypominająca hasło');
				$mail->addAddress($_POST['emaild']);
				$mail->isHTML(false);
				$mail->Subject = 'Przypomnienie hasła';
				$mail->Body = 'Twoje hasło: ' . $pass;
				
				//wysyłanie maila
				
				$mail->send();
				echo "<script>window.location.href='contact.php';</script>";
				exit();
			} catch (Exception $e) {
				 echo '<center>Wiadomość nie została wysłana.</center>';
			}
		}
		else{
			echo '<center>Niepoprawny login! Wprowadź poprawny login.</center>';
		}
	}
}

// wywołujemy funkcje WyslijMailKontakt() i PrzypomnijHaslo()

WyslijMailKontakt();
PrzypomnijHaslo();

?>