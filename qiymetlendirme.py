parts = input().split()

values = []
missing = 0

for p in parts:
    if p == "NA":
        missing += 1
    else:
        values.append(float(p))

print("olcma:", len(values))
print("Bos:", missing)

print("Min:", min(values))
print("Max:", max(values))

avg = round(sum(values) / len(values), 1)
print("Orta qiymat:", avg)

def level(v):
    if v < -105:
        return "zaif"
    elif v < -95:
        return "orta"
    else:
        return "yaxwi"

for v in values:
    print(v, "→", level(v))

counts = {"zaif": 0, "orta": 0, "yaxsi": 0}

for v in values:
    s = level(v)
    counts[s] += 1

print(counts)

share = round(counts["zaif"] / len(values) * 100, 1)
print("Zaif payi:", share, "%")

if share >= 30:
    print("Qarar: briqadani gondar")
elif share >= 10:
    print("Qarar: musahidada saxla")
else:
    print("Qarar: stansiya normaldir")

current = 0
best = 0

for v in values:
    if level(v) == "zaif":
        current += 1
        best = max(best, current)
    else:
        current = 0

print("An uzun zaif seriya:", best)
