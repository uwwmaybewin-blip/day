
print("===== MINI BANKOMAT =====")

pin = "1234"
balans = 100000

kiritilgan_pin = input("PIN-kodingizni kiriting: ")

if kiritilgan_pin == pin:
    print("\nXush kelibsiz!")

    print("\n1. Balansni tekshirish")
    print("2. Pul yechish")

    tanlov = input("Tanlovingizni kiriting (1 yoki 2): ")

    if tanlov == "1":
        print("Sizning balansingiz:", balans, "so'm")

    elif tanlov == "2":
        pul = int(input("Qancha pul yechmoqchisiz? "))

        if pul <= 0:
            print("Xato! Pul miqdori musbat bo'lishi kerak.")

        elif pul > balans:
            print("Hisobingizda mablag' yetarli emas!")

        else:
            balans = balans - pul
            print("Pul muvaffaqiyatli yechildi!")
            print("Qolgan balans:", balans, "so'm")

    else:
        print("Noto'g'ri tanlov!")

else:
    print("PIN-kod noto'g'ri!")





























