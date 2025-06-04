import veiculo


r = veiculo.Carro()
s = veiculo.Cliente()  
t = veiculo.Locacao()

r.inicio("Fiat", "Uno", 50000, "ABC1234", "Vermelho")
#r.exibir() 

s.cliente("Kawan","123.123.123-12","42424242","1200")
#s.exibir2()

t.locacao("kawan","Fresta",900,"pix",5,6)
t.exibir()