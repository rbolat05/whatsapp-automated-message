class Preprocesser:
    
    def tr(phone):
        phone = str(phone)
        phone = phone.replace(' ', '')
        phone = phone.replace('(', '')
        phone = phone.replace(')', '')
        phone = phone.replace('-', '')
        phone = phone[-10:]
        phone = '+90' + phone
        return phone