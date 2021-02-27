
import spacy


class POS:

    nlp = spacy.load('en_core_web_sm')

    def getPOS(self,sentence):
        doc = self.nlp(sentence)
        
        for word in doc:
            print(word.text,word.pos_,str(spacy.explain(word.pos_)))
            

    
    


