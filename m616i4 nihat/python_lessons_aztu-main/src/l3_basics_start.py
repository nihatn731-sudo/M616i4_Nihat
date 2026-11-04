
# print("=== Kərpic 1 ===")   # Proqram — əmrlər ardıcıllığı


# print("salam, data muhendsiliyi!")
# print("baza stansiaysi:",  "bak-0207!")
# print(2+3)
# print("2+3")

# print("=== Kərpic 2 ===")   # Dəyişən — adı olan qutu
# CELL= "BAK-0207"
# RSRP = -95.6
# print(CELL,RSRP)
# RSRP = -108.1
# print(CELL,RSRP)
# DROPS = 2
# DROPS = DROPS + 1
# print("DROPS =",  DROPS)
# #name = input()
# #age = input()


# print("=== Kərpic 3 ===")   # Tiplər: int, float, str, bool, None
# print(type(3))
# print(type(-95.5))
# print(type("bak-0207"))
# print(type(True))
# print(type(None))
# a = "-95.5"
# b = -95.5
# print(b + 10)
# print(a + "10")
# print(float(a) + 10)
# #print(float("N/A"))

# print("=== Kərpic 4 ===")   # Müqayisə → True / False
# a = True
# b = False
# print(a>b)
# #a = input
# #b = input 


# print("=== Kərpic 5 ===")   # Siyahı (list)
# list_shop = ["milk", "bread", "kola", "cheese", "coffee"]
# list_input = input()
# #market = int(list_input)
# #print(list_shop[market])

# #print("=== Kərpic 6 ===")   # Lüğət (dict)
# #row = {"milk": "milla", "bread": "tendir", "kola": "zero", "cheese": "atena", "coffee": "jacobs"}
# #print(row["bread"])
# #row["yoqurt"] = "cudo"
# #row["bread"] = "zavod"
# #print(row)


# print("=== Kərpic 7 ===")   # Dövr (for) və şərt (if / else)
# rsrp_list = [-91.5, -108.1, -86.2, -103.3, -110.4]
# for v in rsrp_list:
#     number = int(input("please add a number "))
#     print(int(number)* v ) 
 
# parts = input () .split()
# values = []
# for p in parts:
#     values.append(float(p))
# print(len(values))
# print(max(values))
# print(min(values))
# print(sum(values) / len(values))



# rsrp_list = [-91.5, -108.1, -86.2, -103.3, -110.4]
# weak = 0
# for v in rsrp_list:
#     if v < -105:
#         print(v, "- zeif")
#         weak = weak + 1
#     else:
#         print(v, "- normal")
# print("zeif olcme sayi", weak)        
a = int(input())
if a > 150:
 print("good")
elif a < 150:
 print("not okay")
elif a == 150:
  print("meh")
else:
 print("404 error")





print("=== Kərpic 8 ===")   # Funksiya: çağırmaq və yaratmaq




print("=== Kərpic 9 ===")   # Nöqtə: metod




print("=== Kərpic 10 ===")  # import — hazır alət qutusu
data = "-91.5 -108.1 NA -86.2 -103.3 -105 NA -97.4 -89.0"
parts = data.split()

values = []
missing = 0
for p in parts:
    if p == "NA":
        missing += 1
    else:
        values.append(float(p))
print("Ölçmə:", len(values))
print("Boş:", missing)


print("Min:", min(values))
print("Max:", max(values))
print("Orta qiymət:", round(sum(values) / len(values), 1))


def level(v):
    if v < -105:
        return "zəif"
    elif v < -95:
        return "orta"
    else:
        return "yaxşı"

for v in values:
    print(v, "→", level(v))


counts = {"zəif": 0, "orta": 0, "yaxşı": 0}
for v in values:
    s = level(v)
    counts[s] += 1
print(counts)


share = round(counts["zəif"] / len(values) * 100, 1)
print("Zəif payı:", share, "%")
if share >= 30:
    print("Qərar: briqadanı göndər")
elif share >= 10:
    print("Qərar: müşahidədə saxla")
else:
    print("Qərar: stansiya normaldır")


current = 0
best = 0
for v in values:
    if level(v) == "zəif":
        current += 1
        if current > best:
            best = current
    else:
        current = 0
print("Ən uzun zəif seriya:", best)
