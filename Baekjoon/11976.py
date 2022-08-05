bb, bf = map(int, input().split())
sb, sf = map(int, input().split())
gb, gf = map(int, input().split())
pb, pf = map(int, input().split())

pr = pf - pb
gr = gf - (gb - pr)
sr = sf - (sb - gr)

print(sr)
print(gr)
print(pr)