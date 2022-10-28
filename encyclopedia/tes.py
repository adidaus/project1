entries = ["CSS", "HTML", "Django", "Bango"]

hasil = filter(lambda element: "ango" in element, entries)

print(list(hasil))

for i in hasil:
    print(i)

print()


if any("ango" in s for s in entries):
    print("there is")