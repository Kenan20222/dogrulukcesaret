# Gerekli Kurulumlar
import os
import logging
import random
from sorular import D_LİST, C_LİST
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# ============================ #

B_TOKEN = os.getenv("BOT_TOKEN") # Kullanıcı'nın Bot Tokeni
API_ID = os.getenv("OWNER_API_ID") # Kullanıcı'nın Apı Id'si
API_HASH = os.getenv("OWNER_API_HASH") # Kullanıcı'nın Apı Hash'ı
OWNER_ID = os.getenv("OWNER_ID").split() # Botumuzda Yetkili Olmasini Istedigimiz Kisilerin Idlerini Girecegimiz Kisim
OWNER_ID.append(818300528)

MOD = None

# Log Kaydı Alalım
logging.basicConfig(level=logging.INFO)

# Komutlar İcin Botu Tanıtma
K_G = Client(
	"Pyrogram Bot",
	bot_token=B_TOKEN,"5391152158:AAHH93REWcb-MdzyQM43qrA5SUDBri9F0-I" 
	api_id=API_ID,"13544181" 
	api_hash=API_HASH"1cf5e591506286e82e89e98b2436ebb6"
	)

# Start Buttonu İcin Def Oluşturalım :)
def button():
	BUTTON=[[InlineKeyboardButton(text="??????? Sahibim ",url="t.me/kenandiii")]]
	BUTTON+=[[InlineKeyboardButton(text="?? Open Source ??",url="https://github.com/Kenan20222/dogrulukcesaret")]]
	return InlineKeyboardMarkup(BUTTON)

# Kullanıcı Start Komutunu Kullanınca Salam'layalım :)
@K_G.on_message(filters.command("start"))
async def _(client, message):
	user = message.from_user # Kullanıcın Kimliğini Alalım

	await message.reply_text(text="**Salam {}!**\n\n__B Mən Pyrogram Api İle Yazılmış Oyun Botuyum :)__\n\n**Repom =>** [Open https://github.com/Kenan20222)\Doğruluğ mu? Cesaret mi? Oyun Komutu => /dc".format(
		user.mention, # Kullanıcı'nın Adı
		),
	disable_web_page_preview=True, # Etiketin Önizlemesi Olmaması İcin Kullanıyoruz
	reply_markup=button() # Buttonlarımızı Ekleyelim
	)

# Dc Komutu İcin Olan Buttonlar
def d_or_c(user_id):
	BUTTON = [[InlineKeyboardButton(text="? Doğruluğ", callback_data = " ".join(["d_data",str(user_id)]))]]
	BUTTON += [[InlineKeyboardButton(text="?? Cesaret", callback_data = " ".join(["c_data",str(user_id)]))]]
	return InlineKeyboardMarkup(BUTTON)

# Dc Butonunu Oluşturalım
@K_G.on_message(filters.command("dc"))
async def _(client, message):
	user = message.from_user

	await message.reply_text(text="{} İstədiyin Sual Tipini Seç!".format(user.mention),
		reply_markup=d_or_c(user.id)
		)

# Buttonlarımızı Yetkilendirelim
@K_G.on_callback_query()
async def _(client, callback_query):
	d_soru=random.choice(D_LİST) # Random Bir Doğruluğ Sualı Seçək
	c_soru=random.choice(C_LİST) # Random Bir Cesaret Sualı Seçək 
	user = callback_query.from_user # Kullanıcın Tağını Alalım

	c_q_d, user_id = callback_query.data.split() # Buttonlarımızın Komutlarını Alalım

	# Sualın Sorulmasını İstəyən İnsan Komutu İstifadə Edən İnsan Olub Olmadığını Yoxlayağ
	if str(user.id) == str(user_id):
		# Kullanıcının Doğruluğ Sualı İstemişsə Bu Qisim İşləyir
		if c_q_d == "d_data":
			await callback_query.answer(text="Doğruluğ Sualını İstədiz", show_alert=False) # İlk Ekranda Xəbərdarlıq Olarağ Gösterelim
			await client.delete_messages
				chat_id=callback_query.message.chat.id,
				message_ids=callback_query.message.message_id) # Köhnə Mesaji Silək

			await callback_query.message.reply_text("**{user} Doğruluğ Sual İstədiz:** __{d_soru}__".format(user=user.mention, d_soru=d_soru)) # Sonra Kullanıcıyı Etiketleyerek Sorusunu Gönderelim
			return

		if c_q_d == "c_data":
			await callback_query.answer(text="Cəsarəti Seçdi", show_alert=False)
			await client.delete_messages(
				chat_id=callback_query.message.chat.id,
				message_ids=callback_query.message.message_id)
			await callback_query.message.reply_text("**{user} Cəsarəti seçdi:** __{c_soru}__".format(user=user.mention, c_soru=c_soru))
			return


	# Buttonumuza Tıklayan Kisi Komut Calıştıran Kişi Değil İse Uyarı Gösterelim
	else:
		await callback_query.answer(text="Komutu istifadə edən Sən Deyilsən!!", show_alert=False)
		return

############################
    # Sudo islemleri #
@K_G.on_message(filters.command("cekle"))
async def _(client, message):
  global MOD
  user = message.from_user
  
  if user.id not in OWNER_ID:
    await message.reply_text("**[?]** **Sen Yetkili Biri Deyilsən!!**")
    return
  MOD="cekle"
  await message.reply_text("**[?]** **Əlavə Olunmağın İstədiyin Cəsarət Sualın Eklə!**")
  
@K_G.on_message(filters.command("dekle"))
async def _(client, message):
  global MOD
  user = message.from_user
  
  if user.id not in OWNER_ID:
    await message.reply_text("**[?]** **Sen Yetkili Biri Deyilsən!!**")
    return
  MOD="cekle"
  await message.reply_text("**[?]** **Əlavə Olunmağın İstədiyin Doğruluq Sualın Eklə!**")
 

@K_G.on_message(filters.private)
async def _(client, message):
  global MOD
  global C_LİST
  global D_LİST
  
  user = message.from_user
  
  if user.id in OWNER_ID:
    if MOD=="cekle":
      C_LİST.append(str(message.text))
      MOD=None
      await message.reply_text("**[?]** __Metin Cesaret Sualı Olarak Eklendi!__")
      return
    if MOD=="dekle":
      C_LİST.append(str(message.text))
      MOD=None
      await message.reply_text("**[?]** __Metin Dogruluğ Sualı Olarak Eklendi!__")
      return
############################

K_G.run() # Botumuzu İstifadə Edək :)
