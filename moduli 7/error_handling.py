try:
    rezultati = 10/0
except ZeroDivisionError:
    print("Opps nuk mundesh me pjestu me 0")

else:
    print("pjestimi eshte realizuar me sukses")
finally:
    print("ke mrrij deri te numri 8")

frutat = {
    "mollat":5,
    "banane":7,
    "portokalla":3
}

try:
    print(frutat["dredhzat"])
except KeyError:
    print("the key does not exist in the directory")

text="this is not a number"

try:
    text_to_int= int(text)
except Exception as e:
    print("ka ndodh nje eror",e)

finally:
    print("hej ke mrrij deri te line 26")
