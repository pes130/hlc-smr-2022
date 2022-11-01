
CAMBIO_E_P = 166.386
euros = float(input("Dame una cantidad en euros: "))
pesetas = euros * CAMBIO_E_P

# Forma tradicional
print(euros, "€ son", pesetas, "pesetas. CAMBIO 1€=",CAMBIO_E_P,"pesetas")
# Nueva forma
print(f"{euros} € son {pesetas} pesetas. CAMBIO 1€={CAMBIO_E_P} pesetas")