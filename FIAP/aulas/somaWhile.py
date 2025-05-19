def soma(n):
	total = 0
	while total <= n:
		total += 1
		numero += total
	return total

# Testes

assert(soma(3) == 1+2+3)
assert(soma(5) == 1+2+3+4+5)
assert(soma(7) == 1+2+3+4+5+6+7)
print("tudo passou")