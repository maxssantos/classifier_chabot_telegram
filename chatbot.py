from PIL import Image
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes, MessageHandler, Filters, Updater

from io import BytesIO

from typing import Any

import torch
import torchvision.transforms as transforms
from PIL import Image
import torchvision.models as models

class classifier:
    def __init__(self) -> None:
        self.transforms = classifier.load_transformer()
        self.model = classifier.get_cached_model()
        self.labels = sorted(
            [
                "sucuri-amarela",
                "jabuti",
                "jabuti",
                "ariranha",
                "tucano",
                "arara-azul-grande",
                "garca-branca",
                "onca-pintada",
                "tuiuiu",
                "tamandua-bandeira",
                "lobo-guara",
                "bugiu",
                "cervo-do-pantanal",
                "iguana",
                "quati",
                "bigua",
                "ema",
                "jacare-do-pantanal",
                "tatu-peba",
                "piranha-vermelha",
            ]
        )
    
    @staticmethod
    def load_transformer():
        return transforms.Compose(
            [
                transforms.Resize((224, 224)),
                transforms.ToTensor(),
                transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225)),
            ]
        )

    @staticmethod
    def get_cached_model():
        
        def adapt_efficientnet_b2():            
            model = models.efficientnet_b2(weights=models.EfficientNet_B2_Weights.IMAGENET1K_V1)
            model.classifier[1] = torch.nn.Linear(1408,20)
            return model
        
        model = adapt_efficientnet_b2()
        cache = torch.load("./models/best_model_EfficientNet_AdamW.pth", map_location=torch.device('cpu'))
        model.load_state_dict(cache["model"])
        return model
        
    def classify(self, img: Image.Image) -> str:
        self.model.eval()
        data = self.transforms(img)
        data: Any = data.unsqueeze(0)

        device = torch.device("cpu")

        with torch.no_grad():
            data = data.to(device)

            pred = self.model(data)
            res = pred.argmax(dim=1).cpu().tolist()[0]

            label = self.labels[res]

        return label

def start(update, context):
	msg = """Bem vindo ao Classificador de Imagens de Animais do Pantanal utilizando Deep Learning!!!"
	Envie uma imagem para ser classificada! ou digite/clique:
	/help - Exibir a ajuda do classificador
	/classes - Exibir a lista de classes do classificador, no caso os Animais do Pantanal.
	"""
	#print(msg)
	update.message.reply_text(msg, quote=False)

def help(update, context):
	msg = """
	/start - Inicia/Reinicia o Classificador
	/help - Exibe essa mensagem de ajuda
	/classes - Exibe a lista de classes do classificador, no caso os animais do Pantanal.
 	"""
	#print(msg)
	update.message.reply_text(msg, quote=False)

def classes(update, context):
	msg = "Estes são os 20 Animais do Panatanal que podem ser reconhecidos pelo nosso Classificador:\n"
	msg += '\n'.join(clfr.labels)
	msg += "\n\nRealize o TESTE, fazendo o envio de uma IMAGEM para ser CLASSIFICADA!"
	#print(msg)
	update.message.reply_text(msg)

def handle_message(update, context):
	update.message.reply_text("Envie uma imagem para ser classificada!")

def handle_photo(update, context):
	update.message.reply_text(f"Estou fazendo o meu melhor, só um instante!")
	
	telegram_picture = context.bot.get_file(update.message.photo[-1].file_id)
	file = BytesIO(telegram_picture.download_as_bytearray())
	img = Image.open(file)	
	predicted_label = clfr.classify(img)
	
	update.message.reply_text(f"Existe um(a) {predicted_label} nesta imagem!")

######################################################################################

with open('token.txt','r') as f:
	TOKEN = f.read()

clfr = classifier()

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start",start))
dp.add_handler(CommandHandler("help",help))
dp.add_handler(CommandHandler("classes",classes))
dp.add_handler(MessageHandler(Filters.text, handle_message))
dp.add_handler(MessageHandler(Filters.photo, handle_photo))

updater.start_polling()
updater.idle()