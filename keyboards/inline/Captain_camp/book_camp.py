from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

med_dovika = InlineKeyboardMarkup(row_width=1)
approve_from_contry = InlineKeyboardButton(text="Інструкція щодо заповнення медичної довідки",
                                      url="https://zakon.rada.gov.ua/laws/show/z1013-13#n3") #кнопка списку табору
med_dovika.insert(approve_from_contry)
template_med = InlineKeyboardButton(text="Медична довідка",
                                      url="https://drive.google.com/file/d/13kjOLYJEIKpjPS5-q--gzvfRBKBzx0rO/view?usp=sharing") #кнопка списку табору
med_dovika.insert(template_med)
#медична довідка


parents_aprove_template=InlineKeyboardButton(text="Посилання на шаблон дозволу від батьків",
                                      url="https://drive.google.com/file/d/11dp6mI-doKPBXsIRPFooxQjZG1Xq0P3R/view?usp=sharing")# дозвіл батьків

zgoloshenya = InlineKeyboardButton(text="Посилання на шаблон зголошення на табір", #посиланян на зголошення на табір
                                      url="https://drive.google.com/file/d/1BlUHPRyIhxgnS0eVqt4cZzDPb_HieesD/view?usp=sharing")

list_camper = InlineKeyboardButton(text="Посилання на зразок списку табору",# посилання на зразок списку на табір
                                      url="https://docs.google.com/spreadsheets/d/1vaECuqWCJbLZ_8K0b9DFV1KpIa6TErLy"
                                          "tpFy3kZO670/edit?usp=sharing")


med_book_dorosla = InlineKeyboardButton(text="Постанова про обов'язковий медичний огляд",
                                      url="https://zakon.rada.gov.ua/laws/show/559-2001-%D0%BF#Text")# посилання Постанова про обов'язковий медичний огляд
med_book_buy = InlineKeyboardButton(text="Посилання на медичну книжку",
                                      url="https://epicentrk.ua/ua/shop/lichnaya-meditsinskaya-knizhka-44501-romus.html"
                                          "?ssh=new&gclid=Cj0KCQiA6t6ABhDMARIsAONIYyzo2porN7-LaFsFkK6s4zjP_-qsKfs-ouvt4"
                                          "hK9bw3SjGo3-aaxY5kaAnJtEALw_wcB")# посилання  на медичну книжку
#медична книжка



rules_camp = InlineKeyboardButton(text="Приклад правильника табору",
                                      url="https://drive.google.com/file/d/1jrNLlkzFqJndfhBcsbvcspGURDnS-4or/view?usp=sharing")# посилання Приклад правильника табору"
#правильник табору


magazine_tehn_safe = InlineKeyboardButton(text="Шаблон журналу техніки безпеки",
                                      url="https://drive.google.co")# посилання на шаблон
#журнал техніки безпеки табору

