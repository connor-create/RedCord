

class Error():
    def amount_check(self, amount):
        if amount.isdigit():
            if int(amount) < 30 and int(amount) > 0:
                return int(amount)
            else:
                return -1
        else:
            return -1
