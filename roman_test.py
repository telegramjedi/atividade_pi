class ConversorRomano(object):
	def __init__(self):
		super(ConversorRomano, self).__init__()
		self.algarismos = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

	def converterRecursivo(self, numeroRomano):
		tam = len(numeroRomano)
		if (tam == 1) :
			for algarismo in self.algarismos:
				if (algarismo == numeroRomano):
					numeroArabico = self.algarismos[algarismo]
		else:
			numeroArabico = self.converterRecursivo(numeroRomano[0])
			for i in range(1, tam):
				valorDoAtual = self.converterRecursivo(numeroRomano[i])
				valorDoAnterior = self.converterRecursivo(numeroRomano[i-1])
				if (valorDoAtual <= valorDoAnterior):
					numeroArabico += valorDoAtual
				else:
					numeroArabico -= valorDoAnterior
					numeroArabico += valorDoAtual - valorDoAnterior

		return numeroArabico

	def converter(self, numeroRomano):
		numeroRomano = numeroRomano.upper()
		self.validarNumeroRecebido(numeroRomano)
		return self.converterRecursivo(numeroRomano)

		

	def validarNumeroRecebido(self, numeroRomano):
		tam = len(numeroRomano)
		mensagem = ""
		if (tam <= 1):
			if numeroRomano not in self.algarismos:
				mensagem = "Algarismo passado eh invalido: "+ numeroRomano

		else:
			for letra in numeroRomano:
				if letra not in self.algarismos:
					mensagem = "Numero Romano passado contem algarismos invalidos: "+ numeroRomano

			if self.converterRecursivo(numeroRomano) in self.algarismos.values():
				mensagem = "Numero Romano passado possui sequencia de algarismos invalida: "+ numeroRomano

			elif (tam == 2):
				valorDoAtual = self.converterRecursivo(numeroRomano[1])
				valorDoAnterior = self.converterRecursivo(numeroRomano[0])
				valoresNaoRepetiveis = [5, 50, 500]
				if (valorDoAtual >= valorDoAnterior):
					if (valorDoAnterior in valoresNaoRepetiveis):
						mensagem = "Nao repetiveis repetindo"
					elif (valorDoAtual > valorDoAnterior and valorDoAnterior*5 != valorDoAtual and valorDoAnterior*10 != valorDoAtual):
						mensagem = "Nummero passado contem sequencias incorretas"

			elif (tam == 3):
				for i in range(1, tam):
					self.validarNumeroRecebido(numeroRomano[i-1]+numeroRomano[i])
					valorDoAtual = self.converterRecursivo(numeroRomano[i])
					valorDoAnterior = self.converterRecursivo(numeroRomano[i-1])
					valorCalculado = self.converterRecursivo(numeroRomano[:i])

				if (valorDoAtual >= valorDoAnterior):
					if (valorCalculado < valorDoAtual and valorCalculado not in self.algarismos.values()):
						mensagem = "Numero passado eh invalido"

			else:
				algarismosInvalidos = ["IIII", "XXXX", "CCCC", "MMMM"]
				for algarismo in algarismosInvalidos:
					if algarismo in numeroRomano:
						mensagem = "Numero Romano passado possui sequencia de algarismos invalida: "+ numeroRomano

				for i in range(2, tam):
					self.validarNumeroRecebido(numeroRomano[i-2]+numeroRomano[i-1]+numeroRomano[i])


		if (mensagem != ""):
			raise ValueError(mensagem)		

class TestConversorRomano(object):

	def test_deve_converter_numero_romano_simples_valido(self):
		algarismosSimples = {"I":1, "v":5, "X":10, "L":50, "c":100, "D":500, "m":1000}
		for algarismo in algarismosSimples:
			assert ConversorRomano().converter(algarismo) == algarismosSimples[algarismo]

	def test_deve_rejeitar_numero_romano_simples_invalido(self):
		algarismosInvalidos = ["", "H", "*", "3"]
		for algarismo in algarismosInvalidos:
			try:
				ConversorRomano().converter(algarismo)
				assert False
			except ValueError as e:
				assert True

	def test_deve_converter_numero_romano_de_dois_algarismos_valido(self):
		algarismosDuplos = {"VI":6, "Iv":4, "XX":20}
		for algarismoDuplo in algarismosDuplos:
			assert ConversorRomano().converter(algarismoDuplo) == algarismosDuplos[algarismoDuplo]

	def test_deve_rejeitar_numero_romano_de_dois_algarismos_iguais_invalido(self):
		algarismosDuplos = ["VV", "LL", "DD"]
		for algarismo in algarismosDuplos:
			try:
				ConversorRomano().converter(algarismo)
				assert False
			except ValueError as e:
				assert True

	def test_deve_rejeitar_numero_romano_de_dois_algarismos_diferentes_invalido(self):
		algarismosInvalidos = [
			"IL", "IC", "ID", "IM", "VX", "VL", "VC", "VD", "VM", "XD", "XM", "LC", "LD", "LM", "DM"
		]
		for algarismo in algarismosInvalidos:
			try:
				ConversorRomano().converter(algarismo)
				assert False
			except ValueError as e:
				assert True

	def test_deve_rejeitar_numero_romano_invalido_de_tres_algarismos(self):
		algarismosInvalidos = ["IVI", "IIX", "CMM", "IXL", "IIV","IIX","XXL","XXC","CCD","CCM","IVI","IXI","IXL","XCM"]
		for algarismo in algarismosInvalidos:
			try:
				print(algarismo)
				ConversorRomano().converter(algarismo)
				assert False
			except ValueError as e:
				assert True

	def test_deve_converter_numeros_romanos_validos_com_mais_de_dois_algarismos(self):
		algarismos = {"XIX":19, "XLIV":44, "LXXIII":73, "LXXXVIII":88, "XCIX":99, "CMXXV":925, "MMCCC":2300}
		for algarismo in algarismos:
			assert ConversorRomano().converter(algarismo) == algarismos[algarismo]

	def test_deve_rejeitar_numeros_romanos_com_mais_de_tres_algarismos_repetidos(self):
		algarismosInvalidos = ["IIII", "XXXX", "CCCC", "MMMM"]
		for algarismo in algarismosInvalidos:
			try:
				ConversorRomano().converter(algarismo)
				assert False
			except ValueError as e:
				assert True

	def test_deve_rejeitar_numeros_romanos_invalidos_com_mais_de_tres_algarismos(self):
		algarismosInvalidos = ["MXVVL", "XXVIIV", "MMLVIIIX"]
		for algarismo in algarismosInvalidos:
			try:
				ConversorRomano().converter(algarismo)
				assert False
			except ValueError as e:
				assert True

			
def main():
	print(ConversorRomano().converter(input()))
if __name__ == '__main__':
	main()