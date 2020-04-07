class Contato:
    def __init__(self, name, email, phone, id=None):
        self.id = id
        self.phone = phone
        self.email = email
        self.name = name

    # Getter
    @property
    def phone(self):
        return self._phone

    # Setter
    @phone.setter
    def phone(self, number):
        if len(number) != 10 and len(number) != 11:
            print('Erro! Você deve digitar o numero com 10 ou 11 digitos')
        else:
            if len(number) == 10:
                number = int(number)  # Verificar se contem somente numeros
                number = str(number)
                fixo = number
                formatar = f'({fixo[0:2]}){fixo[2:6]}-{fixo[6:]}'
            elif len(number) == 11:
                number = int(number)  # Verificar se contem somente numeros
                number = str(number)
                celular = number
                formatar = f'({celular[0:2]}){celular[2:7]}-{celular[7:]}'
        self._phone = formatar
