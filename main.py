import pyrogram

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import Config
from pyrogram import Client, filters
logging.getLogger("pyrogram").setLevel(logging.WARNING)


if __name__ == "__main__" :

    app = Client(
        "ShowJson",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,                
    )

@Client.on_message(filters.command('start'))
async def start(c, m):
    owner = await c.get_users(int(Config.OWNER_ID))
    owner_username = owner.username if owner.username else 'zautebot'

    # start text
    text = f"""Hey! {m.from_user.mention(style='md')},

** I am Stylish Font Bot βοΈ**

`I can help you to get stylish fonts. Just send me some text and see magic.`

** Developer by :** β· [@Lx_0980](https://t.me/Lx_0980)
"""

    # Buttons
    buttons = [
        [            
            InlineKeyboardButton('Channel π’', url=f"https://t.me/Lx_0980")
            ],[
            InlineKeyboardButton('Owner', url=f"https://t.me/{owner_username}"),            
            InlineKeyboardButton('GitHup', url=f"https://github.com/0FLX")                        
        ]
    ]
    await m.reply_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(buttons)
    )



@Client.on_message(filters.private & filters.incoming & filters.text)
async def style_buttons(c, m, cb=False):
    buttons = [[
        InlineKeyboardButton('ππ’πππ πππππ', callback_data='style+typewriter'),
        InlineKeyboardButton('ππ¦π₯ππππ', callback_data='style+outline'),
        InlineKeyboardButton('πππ«π’π', callback_data='style+serif'),
        ],[
        InlineKeyboardButton('πΊππππ', callback_data='style+bold_cool'),
        InlineKeyboardButton('πππππ', callback_data='style+cool'),
        InlineKeyboardButton('Sα΄α΄ΚΚ Cα΄α΄s', callback_data='style+small_cap'),
        ],[
        InlineKeyboardButton('ππΈππΎππ', callback_data='style+script'),
        InlineKeyboardButton('πΌπ¬π»π²πΉπ½', callback_data='style+script_bolt'),
        InlineKeyboardButton('α΅β±βΏΚΈ', callback_data='style+tiny'),
        ],[
        InlineKeyboardButton('αOα°Iα', callback_data='style+comic'),
        InlineKeyboardButton('π¦π?π»π', callback_data='style+sans'),
        InlineKeyboardButton('πππ£π¨', callback_data='style+slant_sans'),
        ],[
        InlineKeyboardButton('ππ’π―π΄', callback_data='style+slant'),
        InlineKeyboardButton('π²πΊππ', callback_data='style+sim'),
         InlineKeyboardButton('βΈοΈβΎοΈβοΈβΈοΈβοΈβΊοΈβοΈ', callback_data='style+circles'),
        ],[
        InlineKeyboardButton('ποΈποΈπ‘οΈποΈποΈποΈπ’οΈ', callback_data='style+circle_dark'),
        InlineKeyboardButton('ππ¬π±π₯π¦π ', callback_data='style+gothic'),
        InlineKeyboardButton('π²πππππ', callback_data='style+gothic_bolt'),
        ],[
        InlineKeyboardButton('CΝ‘ΝlΝ‘ΝoΝ‘ΝuΝ‘ΝdΝ‘ΝsΝ‘Ν', callback_data='style+cloud'),
        InlineKeyboardButton('HΜΜaΜΜpΜΜpΜΜyΜΜ', callback_data='style+happy'),
        InlineKeyboardButton('SΜΜaΜΜdΜΜ', callback_data='style+sad'),
        ],[
        InlineKeyboardButton('Next β‘οΈ', callback_data="nxt")
    ]]
    if not cb:
        await m.reply_text(m.text, reply_markup=InlineKeyboardMarkup(buttons), quote=True)
    else:
        await m.answer()
        await m.message.edit_reply_markup(InlineKeyboardMarkup(buttons))


@Client.on_callback_query(filters.regex('^nxt'))
async def nxt(c, m):
    if m.data == "nxt":
        buttons = [[
            InlineKeyboardButton('πΈβπ΅βπͺβπ¨βπ?βπ¦βπ±β', callback_data='style+special'),
            InlineKeyboardButton('ππππ°ππ΄π', callback_data='style+squares'),
            InlineKeyboardButton('ποΈποΈποΈπ°οΈποΈπ΄οΈποΈ', callback_data='style+squares_bold'),
            ],[
            InlineKeyboardButton('κͺκͺα¦κͺκͺΆκͺα₯΄π²κͺ', callback_data='style+andalucia'),
            InlineKeyboardButton('ηͺεε αε', callback_data='style+manga'),
            InlineKeyboardButton('SΜΎtΜΎiΜΎnΜΎkΜΎyΜΎ', callback_data='style+stinky'),
            ],[
            InlineKeyboardButton('BΝ¦Μ₯uΝ¦Μ₯bΝ¦Μ₯bΝ¦Μ₯lΝ¦Μ₯eΝ¦Μ₯sΝ¦Μ₯', callback_data='style+bubbles'),
            InlineKeyboardButton('UΝnΝdΝeΝrΝlΝiΝnΝeΝ', callback_data='style+underline'),
            InlineKeyboardButton('κκκ·κ©κκκ', callback_data='style+ladybug'),
            ],[
            InlineKeyboardButton('R?a?y?s?', callback_data='style+rays'),
            InlineKeyboardButton('B?i?r?d?s?', callback_data='style+birds'),
            InlineKeyboardButton('SΜΈlΜΈaΜΈsΜΈhΜΈ', callback_data='style+slash'),
            ],[
            InlineKeyboardButton('sβ tβ oβ pβ ', callback_data='style+stop'),
            InlineKeyboardButton('SΝΜΊkΝΜΊyΝΜΊlΝΜΊiΝΜΊnΝΜΊeΝΜΊ', callback_data='style+skyline'),
            InlineKeyboardButton('AΝrΝrΝoΝwΝsΝ', callback_data='style+arrows'),
            ],[
            InlineKeyboardButton('αͺαα­αΏα', callback_data='style+qvnes'),
            InlineKeyboardButton('SΜΆtΜΆrΜΆiΜΆkΜΆeΜΆ', callback_data='style+strike'),
            InlineKeyboardButton('FΰΌrΰΌoΰΌzΰΌeΰΌnΰΌ', callback_data='style+frozen')
            ],[
            InlineKeyboardButton('β¬οΈ Back', callback_data='nxt+0')
        ]]
        await m.answer()
        await m.message.edit_reply_markup(InlineKeyboardMarkup(buttons))
    else:
        await style_buttons(c, m, cb=True)


@Client.on_callback_query(filters.regex('^style'))
async def style(c, m):
    await m.answer()
    cmd, style = m.data.split('+')

    if style == 'typewriter':
        cls = Fonts.typewriter
    if style == 'outline':
        cls = Fonts.outline
    if style == 'serif':
        cls = Fonts.serief
    if style == 'bold_cool':
        cls = Fonts.bold_cool
    if style == 'cool':
        cls = Fonts.cool
    if style == 'small_cap':
        cls = Fonts.smallcap
    if style == 'script':
        cls = Fonts.script
    if style == 'script_bolt':
        cls = Fonts.bold_script
    if style == 'tiny':
        cls = Fonts.tiny
    if style == 'comic':
        cls = Fonts.comic
    if style == 'sans':
        cls = Fonts.san
    if style == 'slant_sans':
        cls = Fonts.slant_san
    if style == 'slant':
        cls = Fonts.slant
    if style == 'sim':
        cls = Fonts.sim
    if style == 'circles':
        cls = Fonts.circles
    if style == 'circle_dark':
        cls = Fonts.dark_circle
    if style == 'gothic':
        cls = Fonts.gothic
    if style == 'gothic_bolt':
        cls = Fonts.bold_gothic
    if style == 'cloud':
        cls = Fonts.cloud
    if style == 'happy':
        cls = Fonts.happy
    if style == 'sad':
        cls = Fonts.sad
    if style == 'special':
        cls = Fonts.special
    if style == 'squares':
        cls = Fonts.square
    if style == 'squares_bold':
        cls = Fonts.dark_square
    if style == 'andalucia':
        cls = Fonts.andalucia
    if style == 'manga':
        cls = Fonts.manga
    if style == 'stinky':
        cls = Fonts.stinky
    if style == 'bubbles':
        cls = Fonts.bubbles
    if style == 'underline':
        cls = Fonts.underline
    if style == 'ladybug':
        cls = Fonts.ladybug
    if style == 'rays':
        cls = Fonts.rays
    if style == 'birds':
        cls = Fonts.birds
    if style == 'slash':
        cls = Fonts.slash
    if style == 'stop':
        cls = Fonts.stop
    if style == 'skyline':
        cls = Fonts.skyline
    if style == 'arrows':
        cls = Fonts.arrows
    if style == 'qvnes':
        cls = Fonts.rvnes
    if style == 'strike':
        cls = Fonts.strike
    if style == 'frozen':
        cls = Fonts.frozen
    new_text = cls(m.message.reply_to_message.text)
    try:
        await m.message.edit_text(new_text, reply_markup=m.message.reply_markup)
    except:
        pass

# Fonts

class Fonts:
    def typewriter(text):
        style = {
            'a': 'π',
            'b': 'π',
            'c': 'π',
            'd': 'π',
            'e': 'π',
            'f': 'π',
            'g': 'π',
            'h': 'π',
            'i': 'π',
            'j': 'π',
            'k': 'π',
            'l': 'π',
            'm': 'π',
            'n': 'π',
            'o': 'π',
            'p': 'π',
            'q': 'π',
            'r': 'π',
            's': 'π',
            't': 'π',
            'u': 'π',
            'v': 'π',
            'w': 'π ',
            'x': 'π‘',
            'y': 'π’',
            'z': 'π£',
            'A': 'π°',
            'B': 'π±',
            'C': 'π²',
            'D': 'π³',
            'E': 'π΄',
            'F': 'π΅',
            'G': 'πΆ',
            'H': 'π·',
            'I': 'πΈ',
            'J': 'πΉ',
            'K': 'πΊ',
            'L': 'π»',
            'M': 'πΌ',
            'N': 'π½',
            'O': 'πΎ',
            'P': 'πΏ',
            'Q': 'π',
            'R': 'π',
            'S': 'π',
            'T': 'π',
            'U': 'π',
            'V': 'π',
            'W': 'π',
            'X': 'π',
            'Y': 'π',
            'Z': 'π'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def outline(text):
        style = {
            'a': 'π',
            'b': 'π',
            'c': 'π',
            'd': 'π',
            'e': 'π',
            'f': 'π',
            'g': 'π',
            'h': 'π',
            'i': 'π',
            'j': 'π',
            'k': 'π',
            'l': 'π',
            'm': 'π',
            'n': 'π',
            'o': 'π ',
            'p': 'π‘',
            'q': 'π’',
            'r': 'π£',
            's': 'π€',
            't': 'π₯',
            'u': 'π¦',
            'v': 'π§',
            'w': 'π¨',
            'x': 'π©',
            'y': 'πͺ',
            'z': 'π«',
            'A': 'πΈ',
            'B': 'πΉ',
            'C': 'β',
            'D': 'π»',
            'E': 'πΌ',
            'F': 'π½',
            'G': 'πΎ',
            'H': 'β',
            'I': 'π',
            'J': 'π',
            'K': 'π',
            'L': 'π',
            'M': 'π',
            'N': 'β',
            'O': 'π',
            'P': 'β',
            'Q': 'β',
            'R': 'β',
            'S': 'π',
            'T': 'π',
            'U': 'π',
            'V': 'π',
            'W': 'π',
            'X': 'π',
            'Y': 'π',
            'Z': 'β€',
            '0': 'π',
            '1': 'π',
            '2': 'π',
            '3': 'π',
            '4': 'π',
            '5': 'π',
            '6': 'π',
            '7': 'π',
            '8': 'π ',
            '9': 'π‘'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def serief(text):
        style = {
            'a': 'π',
            'b': 'π',
            'c': 'π',
            'd': 'π',
            'e': 'π',
            'f': 'π',
            'g': 'π ',
            'h': 'π‘',
            'i': 'π’',
            'j': 'π£',
            'k': 'π€',
            'l': 'π₯',
            'm': 'π¦',
            'n': 'π§',
            'o': 'π¨',
            'p': 'π©',
            'q': 'πͺ',
            'r': 'π«',
            's': 'π¬',
            't': 'π­',
            'u': 'π?',
            'v': 'π―',
            'w': 'π°',
            'x': 'π±',
            'y': 'π²',
            'z': 'π³',
            'A': 'π',
            'B': 'π',
            'C': 'π',
            'D': 'π',
            'E': 'π',
            'F': 'π',
            'G': 'π',
            'H': 'π',
            'I': 'π',
            'J': 'π',
            'K': 'π',
            'L': 'π',
            'M': 'π',
            'N': 'π',
            'O': 'π',
            'P': 'π',
            'Q': 'π',
            'R': 'π',
            'S': 'π',
            'T': 'π',
            'U': 'π',
            'V': 'π',
            'W': 'π',
            'X': 'π',
            'Y': 'π',
            'Z': 'π',
            '0': 'π',
            '1': 'π',
            '2': 'π',
            '3': 'π',
            '4': 'π',
            '5': 'π',
            '6': 'π',
            '7': 'π',
            '8': 'π',
            '9': 'π'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def bold_cool(text):
        style = {
            'a': 'π',
            'b': 'π',
            'c': 'π',
            'd': 'π',
            'e': 'π',
            'f': 'π',
            'g': 'π',
            'h': 'π',
            'i': 'π',
            'j': 'π',
            'k': 'π',
            'l': 'π',
            'm': 'π',
            'n': 'π',
            'o': 'π',
            'p': 'π',
            'q': 'π',
            'r': 'π',
            's': 'π',
            't': 'π',
            'u': 'π',
            'v': 'π',
            'w': 'π',
            'x': 'π',
            'y': 'π',
            'z': 'π',
            'A': 'π¨',
            'B': 'π©',
            'C': 'πͺ',
            'D': 'π«',
            'E': 'π¬',
            'F': 'π­',
            'G': 'π?',
            'H': 'π―',
            'I': 'π°',
            'J': 'π±',
            'K': 'π²',
            'L': 'π³',
            'M': 'π΄',
            'N': 'π΅',
            'O': 'πΆ',
            'P': 'π·',
            'Q': 'πΈ',
            'R': 'πΉ',
            'S': 'πΊ',
            'T': 'π»',
            'U': 'πΌ',
            'V': 'π½',
            'W': 'πΎ',
            'X': 'πΏ',
            'Y': 'π',
            'Z': 'π'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def cool(text):
        style = {
            'a': 'π',
            'b': 'π',
            'c': 'π',
            'd': 'π',
            'e': 'π',
            'f': 'π',
            'g': 'π',
            'h': 'β',
            'i': 'π',
            'j': 'π',
            'k': 'π',
            'l': 'π',
            'm': 'π',
            'n': 'π',
            'o': 'π',
            'p': 'π',
            'q': 'π',
            'r': 'π',
            's': 'π ',
            't': 'π‘',
            'u': 'π’',
            'v': 'π£',
            'w': 'π€',
            'x': 'π₯',
            'y': 'π¦',
            'z': 'π§',
            'A': 'π΄',
            'B': 'π΅',
            'C': 'πΆ',
            'D': 'π·',
            'E': 'πΈ',
            'F': 'πΉ',
            'G': 'πΊ',
            'H': 'π»',
            'I': 'πΌ',
            'J': 'π½',
            'K': 'πΎ',
            'L': 'πΏ',
            'M': 'π',
            'N': 'π',
            'O': 'π',
            'P': 'π',
            'Q': 'π',
            'R': 'π',
            'S': 'π',
            'T': 'π',
            'U': 'π',
            'V': 'π',
            'W': 'π',
            'X': 'π',
            'Y': 'π',
            'Z': 'π'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def smallcap(text):
        style = {
            'a': 'α΄',
            'b': 'Κ',
            'c': 'α΄',
            'd': 'α΄',
            'e': 'α΄',
            'f': '?',
            'g': 'Ι’',
            'h': 'αΌ',
            'i': 'Κ',
            'j': 'Ιͺ',
            'k': 'α΄',
            'l': 'Κ',
            'm': 'α΄',
            'n': 'Ι΄',
            'o': 'α΄',
            'p': 'α΄',
            'q': 'Η«',
            'r': 'Κ',
            's': 's',
            't': 'α΄',
            'u': 'α΄',
            'v': 'α΄ ',
            'w': 'α΄‘',
            'x': 'x',
            'y': 'Κ',
            'z': 'α΄’',
            'A': 'A',
            'B': 'B',
            'C': 'C',
            'D': 'D',
            'E': 'E',
            'F': 'F',
            'G': 'G',
            'H': 'H',
            'I': 'I',
            'J': 'J',
            'K': 'K',
            'L': 'L',
            'M': 'M',
            'N': 'N',
            'O': 'O',
            'P': 'P',
            'Q': 'Q',
            'R': 'R',
            'S': 'S',
            'T': 'T',
            'U': 'U',
            'V': 'V',
            'W': 'W',
            'X': 'X',
            'Y': 'Y',
            'Z': 'Z',
            '0': 'πΆ',
            '1': 'π·',
            '2': 'πΈ',
            '3': 'πΉ',
            '4': 'πΊ',
            '5': 'π»',
            '6': 'πΌ',
            '7': 'π½',
            '8': 'πΎ',
            '9': 'πΏ'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def script(text):
        style = {
            'a': 'πΆ',
            'b': 'π·',
            'c': 'πΈ',
            'd': 'πΉ',
            'e': 'β―',
            'f': 'π»',
            'g': 'β',
            'h': 'π½',
            'i': 'πΎ',
            'j': 'πΏ',
            'k': 'π',
            'l': 'π',
            'm': 'π',
            'n': 'π',
            'o': 'β΄',
            'p': 'π',
            'q': 'π',
            'r': 'π',
            's': 'π',
            't': 'π',
            'u': 'π',
            'v': 'π',
            'w': 'π',
            'x': 'π',
            'y': 'π',
            'z': 'π',
            'A': 'π',
            'B': 'β¬',
            'C': 'π',
            'D': 'π',
            'E': 'β°',
            'F': 'β±',
            'G': 'π’',
            'H': 'β',
            'I': 'β',
            'J': 'π₯',
            'K': 'π¦',
            'L': 'β',
            'M': 'β³',
            'N': 'π©',
            'O': 'πͺ',
            'P': 'π«',
            'Q': 'π¬',
            'R': 'β',
            'S': 'π?',
            'T': 'π―',
            'U': 'π°',
            'V': 'π±',
            'W': 'π²',
            'X': 'π³',
            'Y': 'π΄',
            'Z': 'π΅'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def bold_script(text):
        style = {
            'a': 'πͺ',
            'b': 'π«',
            'c': 'π¬',
            'd': 'π­',
            'e': 'π?',
            'f': 'π―',
            'g': 'π°',
            'h': 'π±',
            'i': 'π²',
            'j': 'π³',
            'k': 'π΄',
            'l': 'π΅',
            'm': 'πΆ',
            'n': 'π·',
            'o': 'πΈ',
            'p': 'πΉ',
            'q': 'πΊ',
            'r': 'π»',
            's': 'πΌ',
            't': 'π½',
            'u': 'πΎ',
            'v': 'πΏ',
            'w': 'π',
            'x': 'π',
            'y': 'π',
            'z': 'π',
            'A': 'π',
            'B': 'π',
            'C': 'π',
            'D': 'π',
            'E': 'π',
            'F': 'π',
            'G': 'π',
            'H': 'π',
            'I': 'π',
            'J': 'π',
            'K': 'π',
            'L': 'π',
            'M': 'π',
            'N': 'π',
            'O': 'π',
            'P': 'π',
            'Q': 'π ',
            'R': 'π‘',
            'S': 'π’',
            'T': 'π£',
            'U': 'π€',
            'V': 'π₯',
            'W': 'π¦',
            'X': 'π§',
            'Y': 'π¨',
            'Z': 'π©'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def tiny(text):
        style = {
            'a': 'α΅',
            'b': 'α΅',
            'c': 'αΆ',
            'd': 'α΅',
            'e': 'α΅',
            'f': 'αΆ ',
            'g': 'α΅',
            'h': 'Κ°',
            'i': 'β±',
            'j': 'Κ²',
            'k': 'α΅',
            'l': 'Λ‘',
            'm': 'α΅',
            'n': 'βΏ',
            'o': 'α΅',
            'p': 'α΅',
            'q': 'α΅ ',
            'r': 'Κ³',
            's': 'Λ’',
            't': 'α΅',
            'u': 'α΅',
            'v': 'α΅',
            'w': 'Κ·',
            'x': 'Λ£',
            'y': 'ΚΈ',
            'z': 'αΆ»',
            'A': 'α΅',
            'B': 'α΅',
            'C': 'αΆ',
            'D': 'α΅',
            'E': 'α΅',
            'F': 'αΆ ',
            'G': 'α΅',
            'H': 'Κ°',
            'I': 'β±',
            'J': 'Κ²',
            'K': 'α΅',
            'L': 'Λ‘',
            'M': 'α΅',
            'N': 'βΏ',
            'O': 'α΅',
            'P': 'α΅',
            'Q': 'α΅ ',
            'R': 'Κ³',
            'S': 'Λ’',
            'T': 'α΅',
            'U': 'α΅',
            'V': 'α΅',
            'W': 'Κ·',
            'X': 'Λ£',
            'Y': 'ΚΈ',
            'Z': 'αΆ»'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def comic(text):
        style = {
            'a': 'α©',
            'b': 'α·',
            'c': 'α',
            'd': 'αͺ',
            'e': 'α΄',
            'f': 'α΄',
            'g': 'α',
            'h': 'αΌ',
            'i': 'I',
            'j': 'α',
            'k': 'K',
            'l': 'αͺ',
            'm': 'α°',
            'n': 'α',
            'o': 'O',
            'p': 'α­',
            'q': 'α«',
            'r': 'α',
            's': 'Υ',
            't': 'T',
            'u': 'α',
            'v': 'α―',
            'w': 'α―',
            'x': 'α­',
            'y': 'Y',
            'z': 'α',
            'A': 'α©',
            'B': 'α·',
            'C': 'α',
            'D': 'αͺ',
            'E': 'α΄',
            'F': 'α΄',
            'G': 'α',
            'H': 'αΌ',
            'I': 'I',
            'J': 'α',
            'K': 'K',
            'L': 'αͺ',
            'M': 'α°',
            'N': 'α',
            'O': 'O',
            'P': 'α­',
            'Q': 'α«',
            'R': 'α',
            'S': 'Υ',
            'T': 'T',
            'U': 'α',
            'V': 'α―',
            'W': 'α―',
            'X': 'α­',
            'Y': 'Y',
            'Z': 'α'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def san(text):
        style = {
            'a': 'π?',
            'b': 'π―',
            'c': 'π°',
            'd': 'π±',
            'e': 'π²',
            'f': 'π³',
            'g': 'π΄',
            'h': 'π΅',
            'i': 'πΆ',
            'j': 'π·',
            'k': 'πΈ',
            'l': 'πΉ',
            'm': 'πΊ',
            'n': 'π»',
            'o': 'πΌ',
            'p': 'π½',
            'q': 'πΎ',
            'r': 'πΏ',
            's': 'π',
            't': 'π',
            'u': 'π',
            'v': 'π',
            'w': 'π',
            'x': 'π',
            'y': 'π',
            'z': 'π',
            'A': 'π',
            'B': 'π',
            'C': 'π',
            'D': 'π',
            'E': 'π',
            'F': 'π',
            'G': 'π',
            'H': 'π',
            'I': 'π',
            'J': 'π',
            'K': 'π',
            'L': 'π',
            'M': 'π ',
            'N': 'π‘',
            'O': 'π’',
            'P': 'π£',
            'Q': 'π€',
            'R': 'π₯',
            'S': 'π¦',
            'T': 'π§',
            'U': 'π¨',
            'V': 'π©',
            'W': 'πͺ',
            'X': 'π«',
            'Y': 'π¬',
            'Z': 'π­',
            '0': 'π¬',
            '1': 'π­',
            '2': 'π?',
            '3': 'π―',
            '4': 'π°',
            '5': 'π±',
            '6': 'π²',
            '7': 'π³',
            '8': 'π΄',
            '9': 'π΅'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def slant_san(text):
        style = {
            'a': 'π',
            'b': 'π',
            'c': 'π',
            'd': 'π',
            'e': 'π',
            'f': 'π',
            'g': 'π',
            'h': 'π',
            'i': 'π',
            'j': 'π',
            'k': 'π ',
            'l': 'π‘',
            'm': 'π’',
            'n': 'π£',
            'o': 'π€',
            'p': 'π₯',
            'q': 'π¦',
            'r': 'π§',
            's': 'π¨',
            't': 'π©',
            'u': 'πͺ',
            'v': 'π«',
            'w': 'π¬',
            'x': 'π­',
            'y': 'π?',
            'z': 'π―',
            'A': 'πΌ',
            'B': 'π½',
            'C': 'πΎ',
            'D': 'πΏ',
            'E': 'π',
            'F': 'π',
            'G': 'π',
            'H': 'π',
            'I': 'π',
            'J': 'π',
            'K': 'π',
            'L': 'π',
            'M': 'π',
            'N': 'π',
            'O': 'π',
            'P': 'π',
            'Q': 'π',
            'R': 'π',
            'S': 'π',
            'T': 'π',
            'U': 'π',
            'V': 'π',
            'W': 'π',
            'X': 'π',
            'Y': 'π',
            'Z': 'π'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def slant(text):
        style = {
            'a': 'π’',
            'b': 'π£',
            'c': 'π€',
            'd': 'π₯',
            'e': 'π¦',
            'f': 'π§',
            'g': 'π¨',
            'h': 'π©',
            'i': 'πͺ',
            'j': 'π«',
            'k': 'π¬',
            'l': 'π­',
            'm': 'π?',
            'n': 'π―',
            'o': 'π°',
            'p': 'π±',
            'q': 'π²',
            'r': 'π³',
            's': 'π΄',
            't': 'π΅',
            'u': 'πΆ',
            'v': 'π·',
            'w': 'πΈ',
            'x': 'πΉ',
            'y': 'πΊ',
            'z': 'π»',
            'A': 'π',
            'B': 'π',
            'C': 'π',
            'D': 'π',
            'E': 'π',
            'F': 'π',
            'G': 'π',
            'H': 'π',
            'I': 'π',
            'J': 'π',
            'K': 'π',
            'L': 'π',
            'M': 'π',
            'N': 'π',
            'O': 'π',
            'P': 'π',
            'Q': 'π',
            'R': 'π',
            'S': 'π',
            'T': 'π',
            'U': 'π',
            'V': 'π',
            'W': 'π',
            'X': 'π',
            'Y': 'π ',
            'Z': 'π‘'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def sim(text):
        style = {
            'a': 'πΊ',
            'b': 'π»',
            'c': 'πΌ',
            'd': 'π½',
            'e': 'πΎ',
            'f': 'πΏ',
            'g': 'π',
            'h': 'π',
            'i': 'π',
            'j': 'π',
            'k': 'π',
            'l': 'π',
            'm': 'π',
            'n': 'π',
            'o': 'π',
            'p': 'π',
            'q': 'π',
            'r': 'π',
            's': 'π',
            't': 'π',
            'u': 'π',
            'v': 'π',
            'w': 'π',
            'x': 'π',
            'y': 'π',
            'z': 'π',
            'A': 'π ',
            'B': 'π‘',
            'C': 'π’',
            'D': 'π£',
            'E': 'π€',
            'F': 'π₯',
            'G': 'π¦',
            'H': 'π§',
            'I': 'π¨',
            'J': 'π©',
            'K': 'πͺ',
            'L': 'π«',
            'M': 'π¬',
            'N': 'π­',
            'O': 'π?',
            'P': 'π―',
            'Q': 'π°',
            'R': 'π±',
            'S': 'π²',
            'T': 'π³',
            'U': 'π΄',
            'V': 'π΅',
            'W': 'πΆ',
            'X': 'π·',
            'Y': 'πΈ',
            'Z': 'πΉ'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def circles(text):
        style = {
            'a': 'βΆοΈ',
            'b': 'β·οΈ',
            'c': 'βΈοΈ',
            'd': 'βΉοΈ',
            'e': 'βΊοΈ',
            'f': 'β»οΈ',
            'g': 'βΌοΈ',
            'h': 'β½οΈ',
            'i': 'βΎοΈ',
            'j': 'βΏοΈ',
            'k': 'βοΈ',
            'l': 'βοΈ',
            'm': 'βοΈ',
            'n': 'βοΈ',
            'o': 'βοΈ',
            'p': 'βοΈ',
            'q': 'βοΈ',
            'r': 'βοΈ',
            's': 'βοΈ',
            't': 'βοΈ',
            'u': 'βοΈ',
            'v': 'βοΈ',
            'w': 'βοΈ',
            'x': 'βοΈ',
            'y': 'βοΈ',
            'z': 'βοΈ',
            'A': 'βΆοΈ',
            'B': 'β·οΈ',
            'C': 'βΈοΈ',
            'D': 'βΉοΈ',
            'E': 'βΊοΈ',
            'F': 'β»οΈ',
            'G': 'βΌοΈ',
            'H': 'β½οΈ',
            'I': 'βΎοΈ',
            'J': 'βΏοΈ',
            'K': 'βοΈ',
            'L': 'βοΈ',
            'M': 'βοΈ',
            'N': 'βοΈ',
            'O': 'βοΈ',
            'P': 'βοΈ',
            'Q': 'βοΈ',
            'R': 'βοΈ',
            'S': 'βοΈ',
            'T': 'βοΈ',
            'U': 'βοΈ',
            'V': 'βοΈ',
            'W': 'βοΈ',
            'X': 'βοΈ',
            'Y': 'βοΈ',
            'Z': 'βοΈ',
            '0': 'βͺ',
            '1': 'β ',
            '2': 'β‘',
            '3': 'β’',
            '4': 'β£',
            '5': 'β€',
            '6': 'β₯',
            '7': 'β¦',
            '8': 'β§',
            '9': 'β¨'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def dark_circle(text):
        style = {
            'a': 'ποΈ',
            'b': 'ποΈ',
            'c': 'ποΈ',
            'd': 'ποΈ',
            'e': 'ποΈ',
            'f': 'ποΈ',
            'g': 'ποΈ',
            'h': 'ποΈ',
            'i': 'ποΈ',
            'j': 'ποΈ',
            'k': 'ποΈ',
            'l': 'ποΈ',
            'm': 'ποΈ',
            'n': 'ποΈ',
            'o': 'ποΈ',
            'p': 'ποΈ',
            'q': 'π οΈ',
            'r': 'π‘οΈ',
            's': 'π’οΈ',
            't': 'π£οΈ',
            'u': 'π€οΈ',
            'v': 'π₯οΈ',
            'w': 'π¦οΈ',
            'x': 'π§οΈ',
            'y': 'π¨οΈ',
            'z': 'π©οΈ',
            'A': 'ποΈ',
            'B': 'ποΈ',
            'C': 'ποΈ',
            'D': 'ποΈ',
            'E': 'ποΈ',
            'F': 'ποΈ',
            'G': 'ποΈ',
            'H': 'ποΈ',
            'I': 'ποΈ',
            'J': 'ποΈ',
            'K': 'ποΈ',
            'L': 'ποΈ',
            'M': 'ποΈ',
            'N': 'ποΈ',
            'O': 'ποΈ',
            'P': 'ποΈ',
            'Q': 'π οΈ',
            'R': 'π‘οΈ',
            'S': 'π’οΈ',
            'T': 'π£οΈ',
            'U': 'π€οΈ',
            'V': 'π₯οΈ',
            'W': 'π¦οΈ',
            'X': 'π§οΈ',
            'Y': 'π¨οΈ',
            'Z': 'π©',
            '0': 'βΏ',
            '1': 'β',
            '2': 'β',
            '3': 'β',
            '4': 'β',
            '5': 'β',
            '6': 'β',
            '7': 'β',
            '8': 'β',
            '9': 'β'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def gothic(text):
        style = {
            'a': 'π',
            'b': 'π',
            'c': 'π ',
            'd': 'π‘',
            'e': 'π’',
            'f': 'π£',
            'g': 'π€',
            'h': 'π₯',
            'i': 'π¦',
            'j': 'π§',
            'k': 'π¨',
            'l': 'π©',
            'm': 'πͺ',
            'n': 'π«',
            'o': 'π¬',
            'p': 'π­',
            'q': 'π?',
            'r': 'π―',
            's': 'π°',
            't': 'π±',
            'u': 'π²',
            'v': 'π³',
            'w': 'π΄',
            'x': 'π΅',
            'y': 'πΆ',
            'z': 'π·',
            'A': 'π',
            'B': 'π',
            'C': 'β­',
            'D': 'π',
            'E': 'π',
            'F': 'π',
            'G': 'π',
            'H': 'β',
            'I': 'β',
            'J': 'π',
            'K': 'π',
            'L': 'π',
            'M': 'π',
            'N': 'π',
            'O': 'π',
            'P': 'π',
            'Q': 'π',
            'R': 'β',
            'S': 'π',
            'T': 'π',
            'U': 'π',
            'V': 'π',
            'W': 'π',
            'X': 'π',
            'Y': 'π',
            'Z': 'β¨'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text


    def bold_gothic(text):
        style = {
            'a': 'π',
            'b': 'π',
            'c': 'π',
            'd': 'π',
            'e': 'π',
            'f': 'π',
            'g': 'π',
            'h': 'π',
            'i': 'π',
            'j': 'π',
            'k': 'π',
            'l': 'π',
            'm': 'π',
            'n': 'π',
            'o': 'π',
            'p': 'π',
            'q': 'π',
            'r': 'π',
            's': 'π',
            't': 'π',
            'u': 'π',
            'v': 'π',
            'w': 'π',
            'x': 'π',
            'y': 'π',
            'z': 'π',
            'A': 'π¬',
            'B': 'π­',
            'C': 'π?',
            'D': 'πΊ',
            'E': 'π°',
            'F': 'π±',
            'G': 'π²',
            'H': 'π³',
            'I': 'π΄',
            'J': 'π΅',
            'K': 'πΆ',
            'L': 'π·',
            'M': 'πΈ',
            'N': 'πΉ',
            'O': 'πΊ',
            'P': 'π»',
            'Q': 'πΌ',
            'R': 'π½',
            'S': 'πΎ',
            'T': 'πΏ',
            'U': 'π',
            'V': 'π',
            'W': 'π',
            'X': 'π',
            'Y': 'π',
            'Z': 'π'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def cloud(text):
        style = {
            'a': 'aΝ‘Ν',
            'b': 'bΝ‘Ν',
            'c': 'cΝ‘Ν',
            'd': 'dΝ‘Ν',
            'e': 'eΝ‘Ν',
            'f': 'fΝ‘Ν',
            'g': 'gΝ‘Ν',
            'h': 'hΝ‘Ν',
            'i': 'iΝ‘Ν',
            'j': 'jΝ‘Ν',
            'k': 'kΝ‘Ν',
            'l': 'lΝ‘Ν',
            'm': 'mΝ‘Ν',
            'n': 'nΝ‘Ν',
            'o': 'oΝ‘Ν',
            'p': 'pΝ‘Ν',
            'q': 'qΝ‘Ν',
            'r': 'rΝ‘Ν',
            's': 'sΝ‘Ν',
            't': 'tΝ‘Ν',
            'u': 'uΝ‘Ν',
            'v': 'vΝ‘Ν',
            'w': 'wΝ‘Ν',
            'x': 'xΝ‘Ν',
            'y': 'yΝ‘Ν',
            'z': 'zΝ‘Ν',
            'A': 'AΝ‘Ν',
            'B': 'BΝ‘Ν',
            'C': 'CΝ‘Ν',
            'D': 'DΝ‘Ν',
            'E': 'EΝ‘Ν',
            'F': 'FΝ‘Ν',
            'G': 'GΝ‘Ν',
            'H': 'HΝ‘Ν',
            'I': 'IΝ‘Ν',
            'J': 'JΝ‘Ν',
            'K': 'KΝ‘Ν',
            'L': 'LΝ‘Ν',
            'M': 'MΝ‘Ν',
            'N': 'NΝ‘Ν',
            'O': 'OΝ‘Ν',
            'P': 'PΝ‘Ν',
            'Q': 'QΝ‘Ν',
            'R': 'RΝ‘Ν',
            'S': 'SΝ‘Ν',
            'T': 'TΝ‘Ν',
            'U': 'UΝ‘Ν',
            'V': 'VΝ‘Ν',
            'W': 'WΝ‘Ν',
            'X': 'XΝ‘Ν',
            'Y': 'YΝ‘Ν',
            'Z': 'ZΝ‘Ν'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def happy(text):
        style = {
            'a': 'aΜΜ',
            'b': 'bΜΜ',
            'c': 'cΜΜ',
            'd': 'dΜΜ',
            'e': 'eΜΜ',
            'f': 'fΜΜ',
            'g': 'gΜΜ',
            'h': 'hΜΜ',
            'i': 'iΜΜ',
            'j': 'jΜΜ',
            'k': 'kΜΜ',
            'l': 'lΜΜ',
            'm': 'mΜΜ',
            'n': 'nΜΜ',
            'o': 'oΜΜ',
            'p': 'pΜΜ',
            'q': 'qΜΜ',
            'r': 'rΜΜ',
            's': 'sΜΜ',
            't': 'tΜΜ',
            'u': 'uΜΜ',
            'v': 'vΜΜ',
            'w': 'wΜΜ',
            'x': 'xΜΜ',
            'y': 'yΜΜ',
            'z': 'zΜΜ',
            'A': 'AΜΜ',
            'B': 'BΜΜ',
            'C': 'CΜΜ',
            'D': 'DΜΜ',
            'E': 'EΜΜ',
            'F': 'FΜΜ',
            'G': 'GΜΜ',
            'H': 'HΜΜ',
            'I': 'IΜΜ',
            'J': 'JΜΜ',
            'K': 'KΜΜ',
            'L': 'LΜΜ',
            'M': 'MΜΜ',
            'N': 'NΜΜ',
            'O': 'OΜΜ',
            'P': 'PΜΜ',
            'Q': 'QΜΜ',
            'R': 'RΜΜ',
            'S': 'SΜΜ',
            'T': 'TΜΜ',
            'U': 'UΜΜ',
            'V': 'VΜΜ',
            'W': 'WΜΜ',
            'X': 'XΜΜ',
            'Y': 'YΜΜ',
            'Z': 'ZΜΜ'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def sad(text):
        style = {
            'a': 'aΜΜ',
            'b': 'bΜΜ',
            'c': 'cΜΜ',
            'd': 'dΜΜ',
            'e': 'eΜΜ',
            'f': 'fΜΜ',
            'g': 'gΜΜ',
            'h': 'hΜΜ',
            'i': 'iΜΜ',
            'j': 'jΜΜ',
            'k': 'kΜΜ',
            'l': 'lΜΜ',
            'm': 'mΜΜ',
            'n': 'nΜΜ',
            'o': 'oΜΜ',
            'p': 'pΜΜ',
            'q': 'qΜΜ',
            'r': 'rΜΜ',
            's': 'sΜΜ',
            't': 'tΜΜ',
            'u': 'uΜΜ',
            'v': 'vΜΜ',
            'w': 'wΜΜ',
            'x': 'xΜΜ',
            'y': 'yΜΜ',
            'z': 'zΜΜ',
            'A': 'AΜΜ',
            'B': 'BΜΜ',
            'C': 'CΜΜ',
            'D': 'DΜΜ',
            'E': 'EΜΜ',
            'F': 'FΜΜ',
            'G': 'GΜΜ',
            'H': 'HΜΜ',
            'I': 'IΜΜ',
            'J': 'JΜΜ',
            'K': 'KΜΜ',
            'L': 'LΜΜ',
            'M': 'MΜΜ',
            'N': 'NΜΜ',
            'O': 'OΜΜ',
            'P': 'PΜΜ',
            'Q': 'QΜΜ',
            'R': 'RΜΜ',
            'S': 'SΜΜ',
            'T': 'TΜΜ',
            'U': 'UΜΜ',
            'V': 'VΜΜ',
            'W': 'WΜΜ',
            'X': 'XΜΜ',
            'Y': 'YΜΜ',
            'Z': 'ZΜΜ'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def special(text):
        style = {
            'a': 'π¦β',
            'b': 'π§β',
            'c': 'π¨β',
            'd': 'π©β',
            'e': 'πͺβ',
            'f': 'π«β',
            'g': 'π¬β',
            'h': 'π­β',
            'i': 'π?β',
            'j': 'π―β',
            'k': 'π°β',
            'l': 'π±β',
            'm': 'π²β',
            'n': 'π³β',
            'o': 'π΄β',
            'p': 'π΅β',
            'q': 'πΆβ',
            'r': 'π·β',
            's': 'πΈβ',
            't': 'πΉβ',
            'u': 'πΊβ',
            'v': 'π»β',
            'w': 'πΌβ',
            'x': 'π½β',
            'y': 'πΎβ',
            'z': 'πΏβ',
            'A': 'π¦β',
            'B': 'π§β',
            'C': 'π¨β',
            'D': 'π©β',
            'E': 'πͺβ',
            'F': 'π«β',
            'G': 'π¬β',
            'H': 'π­β',
            'I': 'π?β',
            'J': 'π―β',
            'K': 'π°β',
            'L': 'π±β',
            'M': 'π²β',
            'N': 'π³β',
            'O': 'π΄β',
            'P': 'π΅β',
            'Q': 'πΆβ',
            'R': 'π·β',
            'S': 'πΈβ',
            'T': 'πΉβ',
            'U': 'πΊβ',
            'V': 'π»β',
            'W': 'πΌβ',
            'X': 'π½β',
            'Y': 'πΎβ',
            'Z': 'πΏβ'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def square(text):
        style = {
            'a': 'π°',
            'b': 'π±',
            'c': 'π²',
            'd': 'π³',
            'e': 'π΄',
            'f': 'π΅',
            'g': 'πΆ',
            'h': 'π·',
            'i': 'πΈ',
            'j': 'πΉ',
            'k': 'πΊ',
            'l': 'π»',
            'm': 'πΌ',
            'n': 'π½',
            'o': 'πΎ',
            'p': 'πΏ',
            'q': 'π',
            'r': 'π',
            's': 'π',
            't': 'π',
            'u': 'π',
            'v': 'π',
            'w': 'π',
            'x': 'π',
            'y': 'π',
            'z': 'π',
            'A': 'π°',
            'B': 'π±',
            'C': 'π²',
            'D': 'π³',
            'E': 'π΄',
            'F': 'π΅',
            'G': 'πΆ',
            'H': 'π·',
            'I': 'πΈ',
            'J': 'πΉ',
            'K': 'πΊ',
            'L': 'π»',
            'M': 'πΌ',
            'N': 'π½',
            'O': 'πΎ',
            'P': 'πΏ',
            'Q': 'π',
            'R': 'π',
            'S': 'π',
            'T': 'π',
            'U': 'π',
            'V': 'π',
            'W': 'π',
            'X': 'π',
            'Y': 'π',
            'Z': 'π'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def dark_square(text):
        style = {
            'a': 'π°οΈ',
            'b': 'π±οΈ',
            'c': 'π²οΈ',
            'd': 'π³οΈ',
            'e': 'π΄οΈ',
            'f': 'π΅οΈ',
            'g': 'πΆοΈ',
            'h': 'π·οΈ',
            'i': 'πΈοΈ',
            'j': 'πΉοΈ',
            'k': 'πΊοΈ',
            'l': 'π»οΈ',
            'm': 'πΌοΈ',
            'n': 'π½οΈ',
            'o': 'πΎοΈ',
            'p': 'πΏοΈ',
            'q': 'ποΈ',
            'r': 'ποΈ',
            's': 'ποΈ',
            't': 'ποΈ',
            'u': 'ποΈ',
            'v': 'ποΈ',
            'w': 'ποΈ',
            'x': 'ποΈ',
            'y': 'ποΈ',
            'z': 'ποΈ',
            'A': 'π°οΈ',
            'B': 'π±οΈ',
            'C': 'π²οΈ',
            'D': 'π³οΈ',
            'E': 'π΄οΈ',
            'F': 'π΅οΈ',
            'G': 'πΆοΈ',
            'H': 'π·οΈ',
            'I': 'πΈοΈ',
            'J': 'πΉοΈ',
            'K': 'πΊοΈ',
            'L': 'π»οΈ',
            'M': 'πΌοΈ',
            'N': 'π½οΈ',
            'O': 'πΎοΈ',
            'P': 'πΏοΈ',
            'Q': 'ποΈ',
            'R': 'ποΈ',
            'S': 'ποΈ',
            'T': 'ποΈ',
            'U': 'ποΈ',
            'V': 'ποΈ',
            'W': 'ποΈ',
            'X': 'ποΈ',
            'Y': 'ποΈ',
            'Z': 'ποΈ'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def andalucia(text):
        style = {
            'a': 'κͺ',
            'b': 'α₯',
            'c': 'α₯΄',
            'd': 'α¦',
            'e': 'κ«',
            'f': 'α »',
            'g': 'α§',
            'h': 'κ«',
            'i': 'π²',
            'j': 'π³',
            'k': 'π¬',
            'l': 'κͺΆ',
            'm': 'κͺ',
            'n': 'κͺ',
            'o': 'κͺ?',
            'p': 'Ο',
            'q': 'π²',
            'r': 'π³',
            's': 'π΄',
            't': 'π½',
            'u': 'κͺ',
            'v': 'κͺ',
            'w': 'α­',
            'x': 'α₯',
            'y': 'κͺ',
            'z': 'Ι',
            'A': 'κͺ',
            'B': 'α₯',
            'C': 'α₯΄',
            'D': 'α¦',
            'E': 'κ«',
            'F': 'α »',
            'G': 'α§',
            'H': 'κ«',
            'I': 'π²',
            'J': 'π³',
            'K': 'π¬',
            'L': 'κͺΆ',
            'M': 'κͺ',
            'N': 'κͺ',
            'O': 'κͺ?',
            'P': 'Ο',
            'Q': 'π²',
            'R': 'π³',
            'S': 'π΄',
            'T': 'π½',
            'U': 'κͺ',
            'V': 'κͺ',
            'W': 'α­',
            'X': 'α₯',
            'Y': 'κͺ',
            'Z': 'Ι'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def manga(text):
        style = {
            'a': 'ε',
            'b': 'δΉ',
            'c': 'ε',
            'd': 'αͺ',
            'e': 'δΉ',
            'f': 'ε',
            'g': 'α',
            'h': 'ε',
            'i': '|',
            'j': 'οΎ',
            'k': '?',
            'l': 'γ₯',
            'm': 'ηͺ',
            'n': 'ε ',
            'o': 'γ',
            'p': 'ε©',
            'q': '?¨',
            'r': 'ε°Ί',
            's': 'δΈ',
            't': 'γ',
            'u': 'γ©',
            'v': 'α―',
            'w': 'ε±±',
            'x': 'δΉ',
            'y': 'γ',
            'z': 'δΉ',
            'A': 'ε',
            'B': 'δΉ',
            'C': 'ε',
            'D': 'αͺ',
            'E': 'δΉ',
            'F': 'ε',
            'G': 'α',
            'H': 'ε',
            'I': '|',
            'J': 'οΎ',
            'K': '?',
            'L': 'γ₯',
            'M': 'ηͺ',
            'N': 'ε ',
            'O': 'γ',
            'P': 'ε©',
            'Q': '?¨',
            'R': 'ε°Ί',
            'S': 'δΈ',
            'T': 'γ',
            'U': 'γ©',
            'V': 'α―',
            'W': 'ε±±',
            'X': 'δΉ',
            'Y': 'γ',
            'Z': 'δΉ'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def stinky(text):
        style = {
            'a': 'aΜΎ',
            'b': 'bΜΎ',
            'c': 'cΜΎ',
            'd': 'dΜΎ',
            'e': 'eΜΎ',
            'f': 'fΜΎ',
            'g': 'gΜΎ',
            'h': 'hΜΎ',
            'i': 'iΜΎ',
            'j': 'jΜΎ',
            'k': 'kΜΎ',
            'l': 'lΜΎ',
            'm': 'mΜΎ',
            'n': 'nΜΎ',
            'o': 'oΜΎ',
            'p': 'pΜΎ',
            'q': 'qΜΎ',
            'r': 'rΜΎ',
            's': 'sΜΎ',
            't': 'tΜΎ',
            'u': 'uΜΎ',
            'v': 'vΜΎ',
            'w': 'wΜΎ',
            'x': 'xΜΎ',
            'y': 'yΜΎ',
            'z': 'zΜΎ',
            'A': 'AΜΎ',
            'B': 'BΜΎ',
            'C': 'CΜΎ',
            'D': 'DΜΎ',
            'E': 'EΜΎ',
            'F': 'FΜΎ',
            'G': 'GΜΎ',
            'H': 'HΜΎ',
            'I': 'IΜΎ',
            'J': 'JΜΎ',
            'K': 'KΜΎ',
            'L': 'LΜΎ',
            'M': 'MΜΎ',
            'N': 'NΜΎ',
            'O': 'OΜΎ',
            'P': 'PΜΎ',
            'Q': 'QΜΎ',
            'R': 'RΜΎ',
            'S': 'SΜΎ',
            'T': 'TΜΎ',
            'U': 'UΜΎ',
            'V': 'VΜΎ',
            'W': 'WΜΎ',
            'X': 'XΜΎ',
            'Y': 'YΜΎ',
            'Z': 'ZΜΎ'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def bubbles(text):
        style = {
            'a': 'aΝ¦Μ₯',
            'b': 'bΝ¦Μ₯',
            'c': 'cΝ¦Μ₯',
            'd': 'dΝ¦Μ₯',
            'e': 'eΝ¦Μ₯',
            'f': 'fΝ¦Μ₯',
            'g': 'gΝ¦Μ₯',
            'h': 'hΝ¦Μ₯',
            'i': 'iΝ¦Μ₯',
            'j': 'jΝ¦Μ₯',
            'k': 'kΝ¦Μ₯',
            'l': 'lΝ¦Μ₯',
            'm': 'mΝ¦Μ₯',
            'n': 'nΝ¦Μ₯',
            'o': 'oΝ¦Μ₯',
            'p': 'pΝ¦Μ₯',
            'q': 'qΝ¦Μ₯',
            'r': 'rΝ¦Μ₯',
            's': 'sΝ¦Μ₯',
            't': 'tΝ¦Μ₯',
            'u': 'uΝ¦Μ₯',
            'v': 'vΝ¦Μ₯',
            'w': 'wΝ¦Μ₯',
            'x': 'xΝ¦Μ₯',
            'y': 'yΝ¦Μ₯',
            'z': 'zΝ¦Μ₯',
            'A': 'AΝ¦Μ₯',
            'B': 'BΝ¦Μ₯',
            'C': 'CΝ¦Μ₯',
            'D': 'DΝ¦Μ₯',
            'E': 'EΝ¦Μ₯',
            'F': 'FΝ¦Μ₯',
            'G': 'GΝ¦Μ₯',
            'H': 'HΝ¦Μ₯',
            'I': 'IΝ¦Μ₯',
            'J': 'JΝ¦Μ₯',
            'K': 'KΝ¦Μ₯',
            'L': 'LΝ¦Μ₯',
            'M': 'MΝ¦Μ₯',
            'N': 'NΝ¦Μ₯',
            'O': 'OΝ¦Μ₯',
            'P': 'PΝ¦Μ₯',
            'Q': 'QΝ¦Μ₯',
            'R': 'RΝ¦Μ₯',
            'S': 'SΝ¦Μ₯',
            'T': 'TΝ¦Μ₯',
            'U': 'UΝ¦Μ₯',
            'V': 'VΝ¦Μ₯',
            'W': 'WΝ¦Μ₯',
            'X': 'XΝ¦Μ₯',
            'Y': 'YΝ¦Μ₯',
            'Z': 'ZΝ¦Μ₯'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def underline(text):
        style = {
            'a': 'aΝ',
            'b': 'bΝ',
            'c': 'cΝ',
            'd': 'dΝ',
            'e': 'eΝ',
            'f': 'fΝ',
            'g': 'gΝ',
            'h': 'hΝ',
            'i': 'iΝ',
            'j': 'jΝ',
            'k': 'kΝ',
            'l': 'lΝ',
            'm': 'mΝ',
            'n': 'nΝ',
            'o': 'oΝ',
            'p': 'pΝ',
            'q': 'qΝ',
            'r': 'rΝ',
            's': 'sΝ',
            't': 'tΝ',
            'u': 'uΝ',
            'v': 'vΝ',
            'w': 'wΝ',
            'x': 'xΝ',
            'y': 'yΝ',
            'z': 'zΝ',
            'A': 'AΝ',
            'B': 'BΝ',
            'C': 'CΝ',
            'D': 'DΝ',
            'E': 'EΝ',
            'F': 'FΝ',
            'G': 'GΝ',
            'H': 'HΝ',
            'I': 'IΝ',
            'J': 'JΝ',
            'K': 'KΝ',
            'L': 'LΝ',
            'M': 'MΝ',
            'N': 'NΝ',
            'O': 'OΝ',
            'P': 'PΝ',
            'Q': 'QΝ',
            'R': 'RΝ',
            'S': 'SΝ',
            'T': 'TΝ',
            'U': 'UΝ',
            'V': 'VΝ',
            'W': 'WΝ',
            'X': 'XΝ',
            'Y': 'YΝ',
            'Z': 'ZΝ'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def ladybug(text):
        style = {
            'a': 'κ',
            'b': 'κ',
            'c': 'κ³',
            'd': 'κ·',
            'e': 'κ',
            'f': 'κ',
            'g': 'κ',
            'h': 'κ',
            'i': 'κ€',
            'j': 'κ»',
            'k': 'κ',
            'l': 'κ',
            'm': 'κ­',
            'n': 'κ€',
            'o': 'κ¦',
            'p': 'α',
            'q': 'κ°',
            'r': 'κͺ',
            's': 'κ',
            't': 'κ',
            'u': 'κ',
            'v': 'κ¦',
            'w': 'κ',
            'x': 'κ§',
            'y': 'κ©',
            'z': 'κ΄',
            'A': 'κ',
            'B': 'κ',
            'C': 'κ³',
            'D': 'κ·',
            'E': 'κ',
            'F': 'κ',
            'G': 'κ',
            'H': 'κ',
            'I': 'κ€',
            'J': 'κ»',
            'K': 'κ',
            'L': 'κ',
            'M': 'κ­',
            'N': 'κ€',
            'O': 'κ¦',
            'P': 'α',
            'Q': 'κ°',
            'R': 'κͺ',
            'S': 'κ',
            'T': 'κ',
            'U': 'κ',
            'V': 'κ¦',
            'W': 'κ',
            'X': 'κ§',
            'Y': 'κ©',
            'Z': 'κ΄'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def rays(text):
        style = {
            'a': 'a?',
            'b': 'b?',
            'c': 'c?',
            'd': 'd?',
            'e': 'e?',
            'f': 'f?',
            'g': 'g?',
            'h': 'h?',
            'i': 'i?',
            'j': 'j?',
            'k': 'k?',
            'l': 'l?',
            'm': 'm?',
            'n': 'n?',
            'o': 'o?',
            'p': 'p?',
            'q': 'q?',
            'r': 'r?',
            's': 's?',
            't': 't?',
            'u': 'u?',
            'v': 'v?',
            'w': 'w?',
            'x': 'x?',
            'y': 'y?',
            'z': 'z?',
            'A': 'A?',
            'B': 'B?',
            'C': 'C?',
            'D': 'D?',
            'E': 'E?',
            'F': 'F?',
            'G': 'G?',
            'H': 'H?',
            'I': 'I?',
            'J': 'J?',
            'K': 'K?',
            'L': 'L?',
            'M': 'M?',
            'N': 'N?',
            'O': 'O?',
            'P': 'P?',
            'Q': 'Q?',
            'R': 'R?',
            'S': 'S?',
            'T': 'T?',
            'U': 'U?',
            'V': 'V?',
            'W': 'W?',
            'X': 'X?',
            'Y': 'Y?',
            'Z': 'Z?'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def birds(text):
        style = {
            'a': 'a?',
            'b': 'b?',
            'c': 'c?',
            'd': 'd?',
            'e': 'e?',
            'f': 'f?',
            'g': 'g?',
            'h': 'h?',
            'i': 'i?',
            'j': 'j?',
            'k': 'k?',
            'l': 'l?',
            'm': 'm?',
            'n': 'n?',
            'o': 'o?',
            'p': 'p?',
            'q': 'q?',
            'r': 'r?',
            's': 's?',
            't': 't?',
            'u': 'u?',
            'v': 'v?',
            'w': 'w?',
            'x': 'x?',
            'y': 'y?',
            'z': 'z?',
            'A': 'A?',
            'B': 'B?',
            'C': 'C?',
            'D': 'D?',
            'E': 'E?',
            'F': 'F?',
            'G': 'G?',
            'H': 'H?',
            'I': 'I?',
            'J': 'J?',
            'K': 'K?',
            'L': 'L?',
            'M': 'M?',
            'N': 'N?',
            'O': 'O?',
            'P': 'P?',
            'Q': 'Q?',
            'R': 'R?',
            'S': 'S?',
            'T': 'T?',
            'U': 'U?',
            'V': 'V?',
            'W': 'W?',
            'X': 'X?',
            'Y': 'Y?',
            'Z': 'Z?'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def slash(text):
        style = {
            'a': 'aΜΈ',
            'b': 'bΜΈ',
            'c': 'cΜΈ',
            'd': 'dΜΈ',
            'e': 'eΜΈ',
            'f': 'fΜΈ',
            'g': 'gΜΈ',
            'h': 'hΜΈ',
            'i': 'iΜΈ',
            'j': 'jΜΈ',
            'k': 'kΜΈ',
            'l': 'lΜΈ',
            'm': 'mΜΈ',
            'n': 'nΜΈ',
            'o': 'oΜΈ',
            'p': 'pΜΈ',
            'q': 'qΜΈ',
            'r': 'rΜΈ',
            's': 'sΜΈ',
            't': 'tΜΈ',
            'u': 'uΜΈ',
            'v': 'vΜΈ',
            'w': 'wΜΈ',
            'x': 'xΜΈ',
            'y': 'yΜΈ',
            'z': 'zΜΈ',
            'A': 'AΜΈ',
            'B': 'BΜΈ',
            'C': 'CΜΈ',
            'D': 'DΜΈ',
            'E': 'EΜΈ',
            'F': 'FΜΈ',
            'G': 'GΜΈ',
            'H': 'HΜΈ',
            'I': 'IΜΈ',
            'J': 'JΜΈ',
            'K': 'KΜΈ',
            'L': 'LΜΈ',
            'M': 'MΜΈ',
            'N': 'NΜΈ',
            'O': 'OΜΈ',
            'P': 'PΜΈ',
            'Q': 'QΜΈ',
            'R': 'RΜΈ',
            'S': 'SΜΈ',
            'T': 'TΜΈ',
            'U': 'UΜΈ',
            'V': 'VΜΈ',
            'W': 'WΜΈ',
            'X': 'XΜΈ',
            'Y': 'YΜΈ',
            'Z': 'ZΜΈ'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def stop(text):
        style = {
            'a': 'aβ ',
            'b': 'bβ ',
            'c': 'cβ ',
            'd': 'dβ ',
            'e': 'eβ ',
            'f': 'fβ ',
            'g': 'gβ ',
            'h': 'hβ ',
            'i': 'iβ ',
            'j': 'jβ ',
            'k': 'kβ ',
            'l': 'lβ ',
            'm': 'mβ ',
            'n': 'nβ ',
            'o': 'oβ ',
            'p': 'pβ ',
            'q': 'qβ ',
            'r': 'rβ ',
            's': 'sβ ',
            't': 'tβ ',
            'u': 'uβ ',
            'v': 'vβ ',
            'w': 'wβ ',
            'x': 'xβ ',
            'y': 'yβ ',
            'z': 'zβ ',
            'A': 'Aβ ',
            'B': 'Bβ ',
            'C': 'Cβ ',
            'D': 'Dβ ',
            'E': 'Eβ ',
            'F': 'Fβ ',
            'G': 'Gβ ',
            'H': 'Hβ ',
            'I': 'Iβ ',
            'J': 'Jβ ',
            'K': 'Kβ ',
            'L': 'Lβ ',
            'M': 'Mβ ',
            'N': 'Nβ ',
            'O': 'Oβ ',
            'P': 'Pβ ',
            'Q': 'Qβ ',
            'R': 'Rβ ',
            'S': 'Sβ ',
            'T': 'Tβ ',
            'U': 'Uβ ',
            'V': 'Vβ ',
            'W': 'Wβ ',
            'X': 'Xβ ',
            'Y': 'Yβ ',
            'Z': 'Zβ '
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def skyline(text):
        style = {
            'a': 'aΝΜΊ',
            'b': 'bΝΜΊ',
            'c': 'cΝΜΊ',
            'd': 'dΝΜΊ',
            'e': 'eΝΜΊ',
            'f': 'fΝΜΊ',
            'g': 'gΝΜΊ',
            'h': 'hΝΜΊ',
            'i': 'iΝΜΊ',
            'j': 'jΝΜΊ',
            'k': 'kΝΜΊ',
            'l': 'lΝΜΊ',
            'm': 'mΝΜΊ',
            'n': 'nΝΜΊ',
            'o': 'oΝΜΊ',
            'p': 'pΝΜΊ',
            'q': 'qΝΜΊ',
            'r': 'rΝΜΊ',
            's': 'sΝΜΊ',
            't': 'tΝΜΊ',
            'u': 'uΝΜΊ',
            'v': 'vΝΜΊ',
            'w': 'wΝΜΊ',
            'x': 'xΝΜΊ',
            'y': 'yΝΜΊ',
            'z': 'zΝΜΊ',
            'A': 'AΝΜΊ',
            'B': 'BΝΜΊ',
            'C': 'CΝΜΊ',
            'D': 'DΝΜΊ',
            'E': 'EΝΜΊ',
            'F': 'FΝΜΊ',
            'G': 'GΝΜΊ',
            'H': 'HΝΜΊ',
            'I': 'IΝΜΊ',
            'J': 'JΝΜΊ',
            'K': 'KΝΜΊ',
            'L': 'LΝΜΊ',
            'M': 'MΝΜΊ',
            'N': 'NΝΜΊ',
            'O': 'OΝΜΊ',
            'P': 'PΝΜΊ',
            'Q': 'QΝΜΊ',
            'R': 'RΝΜΊ',
            'S': 'SΝΜΊ',
            'T': 'TΝΜΊ',
            'U': 'UΝΜΊ',
            'V': 'VΝΜΊ',
            'W': 'WΝΜΊ',
            'X': 'XΝΜΊ',
            'Y': 'YΝΜΊ',
            'Z': 'ZΝΜΊ'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def arrows(text):
        style = {
            'a': 'aΝ',
            'b': 'bΝ',
            'c': 'cΝ',
            'd': 'dΝ',
            'e': 'eΝ',
            'f': 'fΝ',
            'g': 'gΝ',
            'h': 'hΝ',
            'i': 'iΝ',
            'j': 'jΝ',
            'k': 'kΝ',
            'l': 'lΝ',
            'm': 'mΝ',
            'n': 'nΝ',
            'o': 'oΝ',
            'p': 'pΝ',
            'q': 'qΝ',
            'r': 'rΝ',
            's': 'sΝ',
            't': 'tΝ',
            'u': 'uΝ',
            'v': 'vΝ',
            'w': 'wΝ',
            'x': 'xΝ',
            'y': 'yΝ',
            'z': 'zΝ',
            'A': 'AΝ',
            'B': 'BΝ',
            'C': 'CΝ',
            'D': 'DΝ',
            'E': 'EΝ',
            'F': 'FΝ',
            'G': 'GΝ',
            'H': 'HΝ',
            'I': 'IΝ',
            'J': 'JΝ',
            'K': 'KΝ',
            'L': 'LΝ',
            'M': 'MΝ',
            'N': 'NΝ',
            'O': 'OΝ',
            'P': 'PΝ',
            'Q': 'QΝ',
            'R': 'RΝ',
            'S': 'SΝ',
            'T': 'TΝ',
            'U': 'UΝ',
            'V': 'VΝ',
            'W': 'WΝ',
            'X': 'XΝ',
            'Y': 'YΝ',
            'Z': 'ZΝ'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def rvnes(text):
        style = {
            'a': 'α',
            'b': 'α',
            'c': 'α­',
            'd': 'α',
            'e': 'αΏ',
            'f': 'α»',
            'g': 'α',
            'h': 'α',
            'i': 'α',
            'j': 'α',
            'k': 'α',
            'l': 'α¨',
            'm': 'α ',
            'n': 'α­',
            'o': 'α',
            'p': 'α¨',
            'q': 'α',
            'r': 'αͺ',
            's': 'α',
            't': 'α',
            'u': 'α',
            'v': 'α',
            'w': 'α ',
            'x': 'αΈ',
            'y': 'α',
            'z': 'α',
            'A': 'α',
            'B': 'α',
            'C': 'α­',
            'D': 'α',
            'E': 'αΏ',
            'F': 'α»',
            'G': 'α',
            'H': 'α',
            'I': 'α',
            'J': 'α',
            'K': 'α',
            'L': 'α¨',
            'M': 'α ',
            'N': 'α­',
            'O': 'α',
            'P': 'α¨',
            'Q': 'α',
            'R': 'αͺ',
            'S': 'α',
            'T': 'α',
            'U': 'α',
            'V': 'α',
            'W': 'α ',
            'X': 'αΈ',
            'Y': 'α',
            'Z': 'α'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def strike(text):
        style = {
            'a': 'aΜΆ',
            'b': 'bΜΆ',
            'c': 'cΜΆ',
            'd': 'dΜΆ',
            'e': 'eΜΆ',
            'f': 'fΜΆ',
            'g': 'gΜΆ',
            'h': 'hΜΆ',
            'i': 'iΜΆ',
            'j': 'jΜΆ',
            'k': 'kΜΆ',
            'l': 'lΜΆ',
            'm': 'mΜΆ',
            'n': 'nΜΆ',
            'o': 'oΜΆ',
            'p': 'pΜΆ',
            'q': 'qΜΆ',
            'r': 'rΜΆ',
            's': 'sΜΆ',
            't': 'tΜΆ',
            'u': 'uΜΆ',
            'v': 'vΜΆ',
            'w': 'wΜΆ',
            'x': 'xΜΆ',
            'y': 'yΜΆ',
            'z': 'zΜΆ',
            'A': 'AΜΆ',
            'B': 'BΜΆ',
            'C': 'CΜΆ',
            'D': 'DΜΆ',
            'E': 'EΜΆ',
            'F': 'FΜΆ',
            'G': 'GΜΆ',
            'H': 'HΜΆ',
            'I': 'IΜΆ',
            'J': 'JΜΆ',
            'K': 'KΜΆ',
            'L': 'LΜΆ',
            'M': 'MΜΆ',
            'N': 'NΜΆ',
            'O': 'OΜΆ',
            'P': 'PΜΆ',
            'Q': 'QΜΆ',
            'R': 'RΜΆ',
            'S': 'SΜΆ',
            'T': 'TΜΆ',
            'U': 'UΜΆ',
            'V': 'VΜΆ',
            'W': 'WΜΆ',
            'X': 'XΜΆ',
            'Y': 'YΜΆ',
            'Z': 'ZΜΆ'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def frozen(text):
        style = {
            'a': 'aΰΌ',
            'b': 'bΰΌ',
            'c': 'cΰΌ',
            'd': 'dΰΌ',
            'e': 'eΰΌ',
            'f': 'fΰΌ',
            'g': 'gΰΌ',
            'h': 'hΰΌ',
            'i': 'iΰΌ',
            'j': 'jΰΌ',
            'k': 'kΰΌ',
            'l': 'lΰΌ',
            'm': 'mΰΌ',
            'n': 'nΰΌ',
            'o': 'oΰΌ',
            'p': 'pΰΌ',
            'q': 'qΰΌ',
            'r': 'rΰΌ',
            's': 'sΰΌ',
            't': 'tΰΌ',
            'u': 'uΰΌ',
            'v': 'vΰΌ',
            'w': 'wΰΌ',
            'x': 'xΰΌ',
            'y': 'yΰΌ',
            'z': 'zΰΌ',
            'A': 'AΰΌ',
            'B': 'BΰΌ',
            'C': 'CΰΌ',
            'D': 'DΰΌ',
            'E': 'EΰΌ',
            'F': 'FΰΌ',
            'G': 'GΰΌ',
            'H': 'HΰΌ',
            'I': 'IΰΌ',
            'J': 'JΰΌ',
            'K': 'KΰΌ',
            'L': 'LΰΌ',
            'M': 'MΰΌ',
            'N': 'NΰΌ',
            'O': 'OΰΌ',
            'P': 'PΰΌ',
            'Q': 'QΰΌ',
            'R': 'RΰΌ',
            'S': 'SΰΌ',
            'T': 'TΰΌ',
            'U': 'UΰΌ',
            'V': 'VΰΌ',
            'W': 'WΰΌ',
            'X': 'XΰΌ',
            'Y': 'YΰΌ',
            'Z': 'ZΰΌ'
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text



    app.run()
