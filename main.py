import requests
import time
import json
import os

class TelegramBot:
  def __init__(self):
    token = '5826845606:AAFO6y1MVyXTCyZpY4Af90nlLakGDIsUzxI'
    self.url_base = f'https://api.telegram.org/bot{token}/'
    
  # Iniciar Bot
  def Iniciar(self):
    update_id = None
    while True:
      atualizacao = self.obter_mensagens(update_id)
      mensagens = atualizacao['result']
      if mensagens:
        for mensagem in mensagens:
          update_id = mensagem['update_id']
          chat_id = mensagem['message']['from']['id']
          eh_primeira_mensagem = mensagem['message']['message_id'] == 1
          resposta = self.criar_resposta(mensagem,eh_primeira_mensagem)
          self.responder(resposta,chat_id)
          
  #Obter Mesagens
  def obter_mensagens(self,update_id):
    link_requisicao = f'{self.url_base}getUpdates?timeout=100'
    if update_id:
      link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
    resultado = requests.get(link_requisicao)
    return json.loads(resultado.content)
    
  # Criar Respostas
  def criar_resposta(self,mensagem,eh_primeira_mensagem):
    mensagem = mensagem['message']['text']
    if eh_primeira_mensagem == True or mensagem.lower() == 'menu':
      return f'''Olá, Bem vindo a nossa lanchonete. Digite o número do produto desejado{os.linesep}OBS.: Bebida e Batata ja inclusos.{os.linesep}1 - Queijo MAX{os.linesep}2 - Duplo Burguer Bacon{os.linesep}3 - Triple XXX{os.linesep}4 - Burguer Simples{os.linesep}5 - Triplo Burguer Bacon{os.linesep}6 - Veggie Burguer{os.linesep}7 - Egg Burguer{os.linesep}8 - Frango Crocante{os.linesep}9 - Frango Apimentado{os.linesep}10 - X Tudo'''
    if mensagem == '1':
      return f'''Confimando pedido:{os.linesep}Queijo MAX - R$35,00{os.linesep}Confirmar pedido(s/n)'''
    if mensagem == '2':
      return f'''Confimando pedido:{os.linesep}Duplo Burguer Bacon - R$35,00{os.linesep}Confirmar pedido(s/n)'''
    if mensagem == '3':
      return f'''Confimando pedido:{os.linesep}Triple XXX - R$45,00{os.linesep}Confirmar pedido(s/n)'''
    if mensagem == '4':
      return f'''Confimando pedido:{os.linesep}Burguer Simples - R$30,00{os.linesep}Confirmar pedido(s/n)'''
    if mensagem == '5':
      return f'''Confimando pedido:{os.linesep}Triplo Burguer Bacon - R$45,00{os.linesep}Confirmar pedido(s/n)'''
    if mensagem == '6':
      return f'''Confimando pedido:{os.linesep}Veggie Burguer - R$50,00{os.linesep}Confirmar pedido(s/n)'''
    if mensagem == '7':
      return f'''Confimando pedido:{os.linesep}Egg Burguer - R$35,00{os.linesep}Confirmar pedido(s/n)'''
    if mensagem == '8':
      return f'''Confimando pedido:{os.linesep}Frango Crocante - R$40,00{os.linesep}Confirmar pedido(s/n)'''
    if mensagem == '9':
      return f'''Confimando pedido:{os.linesep}Frango Apimentado - R$45,00{os.linesep}Confirmar pedido(s/n)'''
    if mensagem == '10':
      return f'''Confimando pedido:{os.linesep}X Tudo - R$55,00{os.linesep}Confirmar pedido(s/n)'''
      
    if mensagem.lower() in ('s','sim'):
      return 'Pedido Confirmado! Agredecemos a preferencia. Tenha uma ótima refeição!'
    else:
      return 'Gostaria de acessar o menu? Digite "menu"'
      
  # Responder
  def responder(self,resposta,chat_id):
    
    # Enviar
    link_de_envio = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
    requests.get(link_de_envio)

bot = TelegramBot()
bot.Iniciar()