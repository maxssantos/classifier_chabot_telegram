# classifier_chabot_telegram
ChatBot no Telegram para Classificação de Imagens de Animais do Pantanal para a disciplina de Redes Neurais da FACOM/UFMS

Para instanciar este projeto em Python com Pytorch é necessário criar o Bot no BotFather e substituir o conteúdo do arquivo TOKEN.txt com o TOKEN fornecido pelo BotFather.

Depois basta instalar o Python, por exemplo utilizando Anaconda. Crie um ambiente conda, por exemplo "classifier_chatbot" com o comando:

```console
conda create --name classifier_chatbot
```

Depois acesse o ambiente e instale as seguintes dependências com o comando:

```console
conda activate classifier_chatbot
conda install pytorch torchvision torchaudio cpuonly -c pytorch
```

Caso tenha Placa de vídeo da NVidia e queira rodar o código com suporte à GPU, você precisará do CUDA, portanto terá que usar os seguintes comando:

```console
conda activate classifier_chatbot
conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch
```

É necessário também incluir o arquivo PTH contendo o seu modelo de rede (obrigatóriamente deve ser uma EfficientNet) que será responsável pela classificação de imagens. Neste projeto foi utilizado o modelo de rede EfficientNet com AdamW do torchvision que foi produzido neste experimento [aqui do Google Colab](https://https://colab.research.google.com/drive/1jxoNRSPgWjc-0eDqA3PQFMWsmwVdsn4-)

Para iniciar o classifier_chatbot_telegram execute o comando:

```console
python chatbot.py
```

Depois abra o app Telegram no seu celular (ou em um browser) e acesse o contato referente ao bot que você criou no BotFather. Os seguintes comandos podem ser enviados ao bot:


<b>/start</b> - Inicia/Reinicia o Classificador
  
<b>/help</b> - Exibe essa mensagem de ajuda
  
<b>/classes</b> - Exibe a lista de classes do classificador, no caso os animais do Pantanal.
  
  Além destes comandos também pode ser enviado a qualquer momento uma IMAGEM que o bot irá classificar esta imagem em uma das seguintes classes:
  
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
