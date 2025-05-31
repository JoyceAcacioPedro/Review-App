from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
import sqlite3
from datetime import datetime, timedelta


#INTERFACE

class GerenciadorTelas(ScreenManager):
  pass

class FirstScreen(Screen):
  pass

class TopicsToReview(Screen):
  pass

class AddNewTopic(Screen):
  pass

class ViewScheduleRevisions(Screen):
   def on_enter(self):
    schedules = get_schedules()
    self.ids.label_schedules.text = schedules

class RevisionHistory(Screen):
   def on_enter(self):
    history =get_history()
    self.ids.label_history.text = history

class Reviews(App):
    def build(self):
      return GerenciadorTelas()

Reviews().run()

#BANCO DE DADOS E PYTHON(BACKEND)

banco = sqlite3.connect('RRevisoes.db')

cursor = banco.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS revisoes(id INTEGER PRIMARY KEY AUTOINCREMENT, conteudo TEXT, pasta_atual INT, data_insercao DATE, revisao01 DATE, revisao02 DATE, revisao03 DATE)")
#cursor.execute("ALTER TABLE revisoes ADD COLUMN revisao01 DATE")
#cursor.execute("ALTER TABLE revisoes ADD COLUMN revisao02 DATE")
#cursor.execute("ALTER TABLE revisoes ADD COLUMN revisao03 DATE")
  # Salva as alterações no banco

#banco.commit()

#cursor.execute("INSERT INTO revisoes VALUES( 2, 'Tipologia de rede', 1,'2025-03-31')")

#banco.commit()

#PYTHON

def get_schedules():
  return "schedules"

def get_history():
  return "history(exemple)"


conteudo = str(input('Digite o Tema:'))
data_insercao = datetime.now().date()

revisao01 = data_insercao + timedelta(days = 1)
revisao02 = data_insercao + timedelta(days = 6)
revisao03 = data_insercao + timedelta(days = 9)

data_insercao = data_insercao.strftime('%Y-%m-%d')
revisao01 = revisao01.strftime('%Y-%m-%d')
revisao02 = revisao02.strftime('%Y-%m-%d')
revisao03 = revisao03.strftime('%Y-%m-%d')

cursor.execute("""INSERT INTO revisoes(conteudo, pasta_atual, data_insercao, revisao01, revisao02,revisao03) VALUES( ?, ?, ?, ?, ?, ?)""",
(conteudo, 1, data_insercao, revisao01, revisao02, revisao03))
banco.commit()  

# bjvkh 

cursor.execute("SELECT conteudo, pasta_atual, data_insercao, revisao01, revisao02, revisao03 FROM revisoes")
resultados = cursor.fetchall()

for linha in resultados:
    print(linha)

