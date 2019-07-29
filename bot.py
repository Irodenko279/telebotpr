import telebot
from telebot import types
from telebot.types import Message
from geopy.distance import vincenty
import const
from const import *
TOKEN='960687567:AAF9sFvpKXzVHvvKeEV_uwC3K61fH-gAq3Y'
bot=telebot.TeleBot(TOKEN)
preja='https://www.instagram.com/preja_flowers/'

markup_menu=types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_addres=types.KeyboardButton('🔍 Find the nearest store 🔍', request_location=True)
btn_payment=types.KeyboardButton('💳 How you can pay?💳')
btn_dost=types.KeyboardButton('🌷Flower delivery🌷')
btn_trends=types.KeyboardButton('💥 Trends 💥')
btn_care=types.KeyboardButton('✂ Care for Flowers ✂')
markup_menu.add(btn_addres,btn_dost,btn_payment,btn_trends,btn_care)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	   bot.reply_to(message,'Hello my darling, we want to help you find useful information for You. This bot will help you to find the trends of the flower season, wedding collections,mans flower and painting clothes.',reply_markup=markup_menu)


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Because I'm bot I can not answer for all you questions, but I know who can")
    bot.reply_to(message, ' Write to our assistant)')
    bot.reply_to(message, '💌 INSTAGRAM 💌:')
    bot.reply_to(message, preja, reply_markup=markup_menu)

@bot.message_handler(commands=['navigation'])
def send_welcome(message):
    bot.send_photo(message.chat.id, photo1)
    bot.send_photo(message.chat.id, photo2)
    bot.send_photo(message.chat.id, photo)




@bot.message_handler(func=lambda message: True)
def upper(message:Message):
       if message.text=="🌷Flower delivery🌷":
              bot.reply_to(message,"We get flowers for every street and you can pick up yourself)", reply_markup=markup_menu)
       elif message.text=='💳 How you can pay?💳':
              bot.reply_to(message, 'You can pay on delivery, on the card, or forward in the store', reply_markup=markup_menu)
       elif message.text =='💥 Trends 💥':
              bot.reply_to(message,'We can demonstrated the best trends for you!', reply_markup=markup_inline_trends)
       elif message.text =='✂ Care for Flowers ✂':
              bot.reply_to(message,'Some care for you!', reply_markup=markup_inline_care)
       elif message.text =='Flowers':
              bot.send_photo(message.chat.id, flower)
       elif message.text.lower() == 'roses':
            bot.reply_to(message, "Roses are beautiful flowers that have long been a symbol of love. \n\nThey belong to the genus Rosa, which exists in both wild and cultivated forms.\n\n A wonderful variety of cultivated roses exist today. Flowers of many different colors are available. \n\n  Some produce an enchanting fragrance to add to their attraction.")
            bot.send_photo(message.chat.id,roses)
            bot.reply_to(message,'Over the years, roses have come to symbolize more than love.\n\n Each of the main flower colors is associated with a particular symbolic meaning.\n\n For people interested in giving a gift of flowers, these meanings may be significant.')
            bot.send_photo(message.chat.id, roses1)
            bot.reply_to(message, "If you want i now about protea and peony, only whrite the flowers name) You can go back to the main menu or ask our consultant.If you need help write '/help'")
       elif message.text.lower() == 'peony':
            bot.reply_to(message, "Peonies are a classic garden flowers.\n\n Growing happily for decades, with very little work required. Learn some little-known facts behind these beautiful, fragrant, old-fashioned flowers and what’s new in the world of peonies!")
            bot.send_photo(message.chat.id,peony)
            bot.reply_to(message,' A peony represents wealth and honor.\n\n It also embody romance and love, and are regarded as the omen of good fortune and happy marriage.\n\nThey are the 12th wedding anniversary flower.\n\nA peony is one plant you will enjoy for a long time. \n\nPeony plants can live to be 100 years and still produce flowers.\n\nPeonies bloom from late May through June in Toronto.\n\nPeonies are native to Asia, Southern Europe and Western North America.')
            bot.send_photo(message.chat.id, peony)
            bot.reply_to(message, "If you want i now about roses and protea, only whrite the flowers name)You can go back to the main menu or ask our consultant.If you need help write '/help'")
       elif message.text.lower() == 'protea':
            bot.reply_to(message, "Proteas are named after Proteus, son of Poseidon and shape-shifter, highlighting the variety of plants found within the large proteaceae family.")
            bot.send_photo(message.chat.id,protea)
            bot.reply_to(message,'Protea has associations to change and transformation, in the language of flowers, protea symbolizes diversity and courage.')
            bot.send_photo(message.chat.id,protea1)
            bot.reply_to(message,"If you want i now about roses and peony, only whrite the flowers name)You can go back to the main menu or ask our consultant.If you need help write '/help'")
       else:
            bot.reply_to(message, "Because I'm bot I can not answer for all you questions, but I know who can")
            bot.reply_to(message, ' Write to our assistant)')
            bot.reply_to(message, '💌 INSTAGRAM 💌:')
            bot.reply_to(message,preja, reply_markup=markup_menu)


markup_inline_trends=types.InlineKeyboardMarkup()
btn_in_wedding=types.InlineKeyboardButton('Wedding',callback_data='wedding')
btn_in_flowers=types.InlineKeyboardButton('Flowers',callback_data='flowers')
btn_in_man=types.InlineKeyboardButton('Man Flowers',callback_data='man')
btn_in_painting=types.InlineKeyboardButton('Panting',callback_data='painting')
markup_inline_trends.add(btn_in_flowers,btn_in_man,btn_in_painting,btn_in_wedding)

markup_inline_care=types.InlineKeyboardMarkup()
btn_in_care=types.InlineKeyboardButton('Care',callback_data='care')
btn_in_type=types.InlineKeyboardButton('Flowers',callback_data='type')
markup_inline_care.add(btn_in_care,btn_in_type)


@bot.message_handler(func=lambda message:True,content_types=['location'])
def magazin_locations(message):
       lon=message.location.longitude
       lat=message.location.latitude
       distance=[]
       for m in const.MAGAZINES:
           result=vincenty((m['latm'],m['lonm']),(lat,lon)).kilometers
           distance.append(result)
       index=distance.index(min(distance))
       bot.send_message(message.chat.id,'Najbliszy sklep do was')
       bot.send_venue(message.chat.id,const.MAGAZINES[index]['latm'],const.MAGAZINES[index]['lonm'],const.MAGAZINES[index]['title'],const.MAGAZINES[index]['adress'])

@bot.callback_query_handler(func=lambda call:True)
def call_back_trends(call):
       if call.data=='flowers':
         bot.send_message(call.message.chat.id," Soft Landing \n")
         bot.send_message(call.message.chat.id, '\n\nThe shapes that belong to the Soft Landing trend are soft, rounded and have delicate curves.\n\nMaterials that are essentially hard also appear soft thanks to their finish.\n\n Pastel colours alternate with creamy shades, pale lilacs and nude colours. ')
         bot.send_photo(call.message.chat.id, flower5)
         bot.send_message(call.message.chat.id,'With the trend Soft Landing these are the flowers to use:\n\n 1.Roses. The heart-shaped petals of a rose have a soft look.\n\n The light-coloured roses kind of describe the feeling of the Soft Landing trend.\n\n 2.Alliums. The long, elegant stem bears a stylish globe of the tiny flowers, which give the allium a soft look. \n\n 3.Gypsophilas. Gypsophila kind of looks like allium because of its softness.\n\n It looks great on its own, but it can also a mixed bouquet to the next level.')
         bot.send_photo(call.message.chat.id, flower4)
         bot.send_message(call.message.chat.id, 'New Frontiers')
         bot.send_message(call.message.chat.id,' These are flowers that belong to New Frontiers trends.\n\n-----------💐💐💐---------------\n\n  The shapes are sleek, geometric or futuristic.\n\n It is notable that the materials are more important than the shape.\n\nPurple and lilac predominate.\n\n The gradients, metallic finishes and reflective colours are also linked to this trend.')
         bot.send_photo(call.message.chat.id,flowe3)
         bot.send_message(call.message.chat.id,'These are flowers that belong to New Frontiers trend: \n 1.Tulips. The ever-cheerful tulips come in many colours, from white to red, yellow and pink. Colours you will see a lot with the New Frontiers trend.\n 2. Callas. The most noticeable aspect of the calla is the beautifully shaped spathe, which is actually a petal. The shape is almost as futuristic as this trend.')
         bot.send_photo(call.message.chat.id, flower2)
         bot.send_message(call.message.chat.id, 'Harvesting Elements')
         bot.send_message(call.message.chat.id,'The Harvesting Elements trend is about sustainability and all our tomorrows. \n\n The sustainability of our immediate environment, as well as that of the entire planet is a recurring theme. \n\n The shapes are simple and without fuss. You also encounter many natural, irregular organic shapes. \n\n Shades of white and grey together with black predominate, followed by shades of blue accompanied by natural tones of green, blue and brown.')
         bot.send_photo(call.message.chat.id, flower,reply_markup=markup_inline_trends)

       elif call.data=='wedding':
         bot.send_message(call.message.chat.id, "👰 With couples throwing wedding traditions out the door, pale pink, blush and taupe flowers are increasingly replacing classic white blooms as a bride’s wedding flower of choice. Fragrant garden roses, stocks and sweet peas (in whimsical and rustic shades) are some of the most popular summer blooms set to appear in a big way next year 💐")
         bot.send_photo(call.message.chat.id, wedding)
         bot.send_message(call.message.chat.id,'The peony is a timeless wedding flower that’s always a popular bouquet choice, so you can expect to see lots of these in 2019, too. As a very versatile flower, peonies can be crafted into bouquets that suit any style of wedding, from very formal affairs to rustic garden parties.')
         bot.send_photo(call.message.chat.id, wedding1)
         bot.send_message(call.message.chat.id, 'However, as the peony season begins in April-May and only runs through to late June, their availability is limited. \n\n If you have an early summer wedding and your heart set on peonies then you will be able to get your hands on them.\n\n But if your wedding is later in the year, then beautiful alternatives include garden roses (for summer), dahlias (for late summer) or ranunculus (for winter and spring).')
         bot.send_photo(call.message.chat.id, wedding2)
         bot.send_photo(call.message.chat.id, wedding3)
         bot.send_message(call.message.chat.id,'Flowers, right now are so much more than just your wedding bouquet.More and more brides are turning to single flower choices or unique combinations of fluffy romantic blooms packed with silvery wild foliage for wedding decor, hair accessories, adorning reception tables and dressing place cards including wreaths, forest garlands, dramatic flower walls and entwined archways creating the most idyllic ceremony settings.')
         bot.send_photo(call.message.chat.id, wedding4,reply_markup=markup_inline_trends)

       elif call.data == 'painting':
         bot.send_photo(call.message.chat.id, painting)
         bot.send_message(call.message.chat.id, 'Its a trend of the season 2019, you mast have it)')
         bot.send_photo(call.message.chat.id, painting1)
         bot.send_message(call.message.chat.id, 'We can draw different patterens of word , ornaments, names and other')
         bot.send_photo(call.message.chat.id, painting2)
         bot.send_message(call.message.chat.id, 'You only need to choose the colors of the paints,and then we will do it ourselves')
         bot.send_photo(call.message.chat.id, painting3)
         bot.send_photo(call.message.chat.id, painting4, reply_markup=markup_inline_trends)
         bot.send_message(call.message.chat.id, 'Choose some buttom')
       elif call.data == 'man':
         bot.send_photo(call.message.chat.id, man1)
         bot.send_message(call.message.chat.id, 'If you are thinking of giving the gift of fragrant and captivating flower bouquets for men, well welcome to the 21st century of gift-giving, where it’s welcomed!\n\n Perfectly acceptable in today’s day and age, perhaps for your dad on Father’s Day, your husband for your anniversary or even your son for his college graduation, you’re in the right place for male flower and plant suggestions.')
         bot.send_photo(call.message.chat.id, man2)
         bot.send_message(call.message.chat.id,'Lucky bamboo is a great choice.\n\n-----------👨👨👨---------------\n\n Its meaning is deeply rooted in Japanese culture and the cultivation of these tiny trees is meant to bring great luck, wealth and opportunity to anyone taking a stab at it! \n\n There is a gorgeous array of these plants available for men for birthday gifts, including the popular twist bamboo.')
         bot.send_photo(call.message.chat.id, man3, reply_markup=markup_inline_trends)
         bot.send_message(call.message.chat.id,'Choose some buttom')
       elif call.data == 'care':
           bot.send_message(call.message.chat.id, "\n🥀How To Keep Your Flowers Looking Fresh🥀\n")
           bot.send_message(call.message.chat.id,"\n Keep your vase filled with water! All flower and foliage stems should be submerged.\n\nFlowers stay fresher, longer when they can get a drink!If your flowers came in a basket or other container with foam, add fresh water every day.\n-----------------------------------------\n  Immediately remove dead or wilting leaves and stems from fresh flower arrangements.\n Watch your water. When it gets cloudy it’s time to change it out.\n")
           bot.send_message(call.message.chat.id, "\n🌹Changing The Water In Your Flower Arrangement🌹\n")
           bot.send_message(call.message.chat.id,
                            "\n First remove any dead or dying flowers from the arrangement.\n\nAfter carefully removing the good flowers, clean the vase thoroughly with soapy water to remove any bacteria that could cause the fresh flowers to deteriorate even quicker.\n\n Be sure to rinse thoroughly.\n")
           bot.send_message(call.message.chat.id,
                            "\n Replace the water and mix in the flower preservative provided by your florist, according to the instructions on the packet.\n\nFor best results, cut stems with a sharp knife at an angle about one to two inches from the bottom.\n   This allows them to better absorb water. Do not use scissors to cut your flowers because they can crush the stems and prevent water absorption.\n\n Place loose stems or wrapped bouquets of fresh flowers in your water mixture as soon as possible.\n",reply_markup=markup_inline_care)
           bot.send_message(call.message.chat.id, 'Choose some buttom')
       elif call.data == 'type':
           bot.send_message(call.message.chat.id, "\n We can also help you and tell about the features of a variety of flowers. \n\n\nYou just need to whrite about the kind you want to know.\n\n We know about: \n\n ◾Roses\n\n◾Peony\n\n◾Protea \n")
           bot.send_message(call.message.chat.id, 'Choose some buttom')
       else:
           bot.send_message(call.message.chat.id, "\n Maybe you have some questions ? Write to us) \n")
           bot.send_message(call.message.chat.id, "\n 💌 INSTAGRAM 💌:\n\n https://www.instagram.com/preja_flowers/ \n")

bot.polling()
