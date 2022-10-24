

from botcity.core import DesktopBot


class Bot(DesktopBot):
    def action(self, execution=None):
        self.browse("https://web.whatsapp.com/")
    
        if not self.find( "buscaContato", matching=0.97, waiting_time=20000):
            self.not_found("buscaContato")
        self.click()
        self.type_keys_with_interval(100, "Recarga")
        
        if not self.find( "alvo", matching=0.97, waiting_time=10000):
            self.not_found("alvo")
        self.click()
        
        if not self.find( "mensagem", matching=0.97, waiting_time=10000):
            self.not_found("mensagem")
        self.click()
        
        self.type_keys_with_interval(100, "Recarga")
        
        if not self.find( "enviar", matching=0.97, waiting_time=10000):
            self.not_found("enviar")
        self.click()
        
        if not self.find( "confirmarInfos", matching=0.97, waiting_time=10000):
            self.not_found("confirmarInfos")
        self.click()
       
        if not self.find( "opçãoRecarga", matching=0.97, waiting_time=10000):
            self.not_found("opçãoRecarga")
        self.click()
        
        


if __name__ == '__main__':
    Bot.main()







