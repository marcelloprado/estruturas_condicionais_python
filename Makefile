.PHONY: run clean

#~ Comando para executar o menu principal
run:
	python menu_principal.python

#~ Comando para limpar o arquivos temporários (se houver)
clean:
	rm -f *.py
	rm -f __pycache__