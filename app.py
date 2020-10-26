importar  os
from  flask  import  Flask , jsonify , request

app  =  Flask ( __name__ )

@ app . rota ( '/' )
def  main ():
  números  = []

  nterms  =  50

  n1 , n2  =  0 , 1
  contagem  =  0

  enquanto  conta  <  ntermos :
    números . anexar ( f " { n1 } " )
    enésimo  =  n1  +  n2

    n1  =  n2
    n2  =  enésimo
    contagem  + =  1

  retornar  "<br>" . juntar ( números )

if  __name__  ==  '__main__' :
  porta  =  int ( os . amb . get ( "PORT" , 5000 ))
  app . executar ( host = '0.0.0.0' , porta = porta )
