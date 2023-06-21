class PhoneNumber:
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def phone_number_format(self, ):
        if self.phone_number.isdigit or self.phone_number[0] == '+':
            if len(self.phone_number) == 10:
                self.phone_number = '38' + self.phone_number
            elif len(self.phone_number) == 12:
                if self.phone_number[:3] != '380':
                    return 'wrong code'
            elif len(self.phone_number) == 13 and self.phone_number[0] == '+':
                if self.phone_number[1:4] != '380':
                    return 'wrong code'
                else:
                    self.phone_number = self.phone_number[1:]
            else:
                return 'wrong len'

        return self.phone_number



test_numbers = ['0631111111',           # 380631111111
                '380631111111',         # 380631111111
                '+380631111111',        # 380631111111
                '390631111111',         # wrong code
                '+3806311111111',       # wrong len
                '3906311111111']        # wrong len

for number in test_numbers:
    print(PhoneNumber(number).phone_number_format())
