from random import choice
import tweepy
from bing_image_downloader import downloader
import os 



bearer_token = '[retirado por motivos de seguranca]'
consumer_key= '[retirado por motivos de seguranca]'
consumer_secret= '[retirado por motivos de seguranca]'
access_token= '[retirado por motivos de seguranca]'
access_token_secret= '[retirado por motivos de seguranca]'


idols = {
    "NCT":  ["Taeyong", "Yuta", "Jaehyun", "Doyoung", "Jungwoo", "Taeil", "Johnny", "Haechan","Mark", "Renjun", "Jeno", "Haechan", "Jaemin", "Jisung", "Chenle", "Kun", "Ten", "Winwin", "Lucas", "Xiaojun", "Hendery", "Yangyang"],
    "AESPA": ["Karina", "Winter", "Giselle", "Ningning"],
    "RED VELVET": ["Irene", "Seulgi", "Wendy", "Joy"],
    "EXO": ["Suho", "Xiumin", "Lay", "Baekhyun", "Chanyeol", "D.O.", "Kai", "Sehun"],
    "TXT": ["Soobin", "Yeonjun", "Beomgyu", "Taehyun", "Hueningkai"],
    "LE SSERAFIM": ["Sakura", "Chaewon", "Yunjin", "Kazuha", "Eunchae"],
    "CIX": ["BX", "Hyunsuk", "Seunghun", "Yonghee", "Bae Jinyoung"],
    "SEVENTEEN": ["S.Coups", "Jeonghan", "Joshua", "Jun", "Hoshi", "Wonwoo", "Woozi", "DK", "Mingyu", "The8", "Seungkwan", "Vernon", "Dino"],
    "ITZY": ["Yeji", "Lia", "Ryujin", "Chaeryeong", "Yuna"],
    "TWICE": ["Nayeon", "Jeongyeon", "Momo", "Sana", "Jihyo", "Mina", "Dahyun", "Chaeyoung", "Tzuyu"],
    "ENHYPEN": ["Heeseung", "Jay", "Jake", "Sunghoon", "Sunoo", "Riki", "Ni-ki"],
    "BTS": ["Jin", "Suga", "J-Hope", "RM", "Jimin", "V", "Jungkook"],
    "BLACKPINK": ["Jisoo", "Jennie", "Rosé", "Lisa"],
    "THE BOYZ": ["Sangyeon", "Jacob", "Younghoon", "Hyunjae", "Juyeon", "Kevin", "New", "Q"],
    "KEP1ER": ["Choi Yujin", "Sakamoto Mashiro", "Kim Chaehyun", "Huening Bahiyyih", "Kim Dayeon", "Ezaki Hikaru", "Seo Youngeun", "Kang Yeseo", "Shen Xiaoting"],
    "IVE": ["Gaeul", "Yujin", "Rei", "Wonyoung", "Liz", "Leeseo"],
    "SNSD": ["Taeyeon", "Sunny", "Tiffany", "Hyoyeon", "Yuri", "Sooyoung", "Yoona"],
    "NMIXX": ["Lily", "Haewon", "Sullyoon", "Jinni", "Bae", "Kyujin", "Jiwoo"],
    "SHINee": ["Onew", "Jonghyun", "Minho", "Key", "Taemin"],
    "P1Harmony": ["Keeho", "Intak", "Soul", "Jongseob", "Theo", "Jiung"],
    "Dreamcatcher": ["Jiu", "Siyeon", "Dami", "Yoohyeon", "Gahyeon", "Handong", "SuA"],
    "BABYMONSTER": ["Pharita", "Ahyeon", "Rami", "Asa", "Ruka", "Chiquita"],
    "2NE1": ["Park Bom", "Sandara Park", "CL", "Minzy"], 
    "XG": ["Cocona", "Harvey", "Jurin", "Hinata", "Chisa", "Juria", "Maya"]

}
#adicionando grupos que eu gosto manualmente
idols["KISS OF LIFE"] = ["Natty", "Haneul", "Julie", "Belle"]
idols["ZEROBASEONE"] =  ["Ricky", "Kim Ji-woong", "Sung Han Bin", "Han Yujin", "Zhang Hao", "Kim Gyu-vin", "Seok Matthew", "Park Gun-wook", "Kim Tae-rae"]
idols["LOOSSEMBLE"] = ["HyeJu", "Hyunjin", "YeoJin", "Go Won", "ViVi"]
idols["ARTMS"] = ["Heejin", "Kim Lip", "Jinsoul", "HaSeul","Choerry"]
idols["VIVIZ"] = ["Sinb", "Umji", "Eunha"]
idols["STAYC"] = ["Park SiEun", "Isa", "Seeun", "Sumin", "Yoon", "J"]
idols["(G)I-DLE"] = ["Song Yuqi", "Jeon Soyeon", "Minnie", "Shuhua", "Miyeon"]
idols["Super Junior"] = ["Kim Heechul", "Leeteuk", "Kyuhyun", "Donghae", "Hyukjae"]
idols["GOT7"] = ["Jay B", "Bambam", "Mark Tuan", "Park Jinyoung", "Jackson", "Yugyeom", "Youngjae"]
idols["MAMAMOO"] = ["Hwasa", "Solar", "Wheein", "Moonbyul"]
idols["TVXQ"] = ["Changmin", "Yunho"]
idols["Stray Kids"] = ["Hyunjin","Bang Chan", "Lee Know", "Changbin", "Hyunjin", "Han", "Felix", "Seungmin", "I.N."  ]


#solistas
idols["solista"] =  ["IU", "Zico", "Chuu", "Bibi", "Chungha", "Sunmi", "BoA", "Jessi", "Bae Suzy", "Jeon Somi", "Kwon Eunbi", "Jay Park", "Lee Chaeyeon", "Choi Yena", "Krystal Jung", "Yerin" ]

times = [ "América-MG", "Athletico-PR", "Atlético-GO", "Atlético-MG", "Bahia", "Botafogo", "Corinthians", "Coritiba", "Cuiabá", "Flamengo", "Fluminense",
  "Fortaleza", "Goiás", "Grêmio", "Internacional", "Juventude", "Palmeiras",
  "Red Bull Bragantino", "Santos", "São Paulo", "Vasco da Gama", "Ceará",
  "Cruzeiro", "CSA", "Figueirense", "Guarani", "Ituano", "Mirassol",
  "Náutico", "Novorizontino", "Operário-PR", "Ponte Preta", "Sampaio Corrêa",
  "Sport", "Ferroviário", "Amazonas", "Manaus",
  "Paysandu", "Remo", "Santa Cruz", "Volta Redonda", "Portuguesa"]


def sortear_idol_com_grupo_qualquer(idols):
  """
  Sorteia aleatoriamente um idol de qualquer grupo e retorna o nome do idol e o grupo de origem.

  Argumentos:
    idols: Dicionário contendo os grupos de idols e seus membros.

  Retorno:
    Dicionário com as chaves "idol" e "grupo".
  """

  # Converte o dicionário em uma lista de tuplas (nome_idol, grupo)
  todos_idols = []
  for grupo, membros in idols.items():
    for membro in membros:
      todos_idols.append((membro, grupo))

  # Sorteia um idol aleatoriamente
  idol_sorteado, grupo_sorteado = choice(todos_idols)

  return {"idol": idol_sorteado, "grupo": grupo_sorteado}

def sortear_time(times):
  """
  Sorteia aleatoriamente um time da lista.

  Argumentos:
    times: Lista de strings com os nomes dos times.

  Retorno:
    String com o nome do time sorteado.
  """

  # Sorteia um time aleatoriamente
  time_sorteado = choice(times)

  return time_sorteado
resultado = sortear_idol_com_grupo_qualquer(idols)
resultado_time = sortear_time(times)

texto = resultado['idol']  + " (" + resultado["grupo"] + ") torce para o " + resultado_time + "!"


#bandeira time
caminho_imagem = os.path.join("Times", resultado_time + ".jpg")
print(caminho_imagem)

#download imagem idol 
pesquisar_imagem = resultado['idol'] + " " + resultado["grupo"] + " kpop selca instagram cute idol 2024"

downloader.download(pesquisar_imagem, limit=1,  output_dir='idols', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)

caminho_imagem_idol =os.path.join("idols",  pesquisar_imagem, "Image_1.jpg")



print(caminho_imagem_idol) 

#auth 
# V1 Twitter API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# V2 Twitter API Authentication
client = tweepy.Client(
    bearer_token,
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret,
    wait_on_rate_limit=True,
)


# Carregar as imagens
media_id1 = api.media_upload(filename=caminho_imagem).media_id_string
media_id2 = api.media_upload(filename=caminho_imagem_idol).media_id_string

# Criar a lista de IDs das mídias
media_ids = [media_id2, media_id1]

# Enviar o tweet com as duas imagens
try:
   client.create_tweet(text=texto, media_ids=media_ids)
   print("Tweet enviado com sucesso!")
except Exception as e:
    print(f"Erro ao enviar o tweet: {e}")