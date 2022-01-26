from googletrans import Translator

def  transletori(matn):


    translate = Translator()

    til = translate.detect(matn).lang

    if til == 'an':

        return translate.translate(matn,dest='uz').text

    else:

        return translate.translate(matn,dest='an').text

