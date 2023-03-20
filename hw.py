class Bank :
    def __init__(self, total_amount, limit_for_loan, limit_for_withdrawn):
        self.total_amount = total_amount
        self.limit_for_loan = limit_for_loan
        self.limit_for_withdrawn = limit_for_withdrawn

    def repeat_withdrawing_money(self, amount, limit_for_withdrawn):
        count = amount // limit_for_withdrawn
        rest = amount % limit_for_withdrawn

        for i in range(count) :
            print(f'This is your money - {self.limit_for_withdrawn}')
            if i == (count - 1) :
                print(f'This is your money - {rest}')

    def show_me_the_money(self, amount) :
        if amount <= self.total_amount :
            self.repeat_withdrawing_money(amount, self.limit_for_withdrawn)
        elif amount <= (self.total_amount + self.limit_for_loan):
            pass
        else :
            print('your money is not enough')
        
hana_bank = Bank(1000, 200, 100)
hana_bank.show_me_the_money(450)


sinhan_bank = Bank(500, 500, 50)
sinhan_bank.show_me_the_money(250)
print()   

