# try, except, else e finally

try:
    print('ABRIR ARQUIVO')
    8/0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('DIVIDIR ZERO')
except IndexError as error:
    print('Index error')
except (NameError, ImportError):
    print('NameError, ImportError')
else:
    print('Não deu error')
finally:
    print('FECHAR ARQUIVO')

