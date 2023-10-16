#Устанавливаем библиотеку
#pip install transformers sentencepiece

from transformers import pipeline

#Сосзаем пайплан для модели перевода с русского на анлийский язык
classifier = pipeline(model="Helsinki-NLP/opus-mt-ru-en")

#Выводим результат работы модели
classifier("Как сделать это задание?")
