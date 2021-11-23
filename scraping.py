from bs4 import BeautifulSoup
import re
import requests
import pandas as pd

import wikipedia

wikipedia.set_lang("ta")
cricketers_df = pd.DataFrame(columns=['fullname', 'nickname', 'battingstyle', 'bowlingstyle',
                                      'role', 'nationalteam', 'introduction', 'content'])
names = [
    'முத்தையா முரளிதரன்',
    'விராட் கோலி',
    'ரோகித் சர்மா',
    'கேன் வில்லியம்சன்',
    'ஸ்டீவ் சிமித்',
    'சகீப் அல் அசன்',
    'ஜோ ரூட்',
    'பாபர் அசாம்',
    'ராஸ் டைலர்',
    'குவின்டன் டி கொக்',
    'ஜோனி பேர்ஸ்டோ',
    'பென் ஸ்டோக்ஸ்',
    'ஆரோன் பிஞ்ச்',
    'ஜோஸ் பட்லர்',
    'மார்னஸ் லபுஷேன்',
    'கே. எல். ராகுல்',
    'ரவீந்திர ஜடேஜா',
    'கிறிஸ் வோக்ஸ்',
    'சச்சின் டெண்டுல்கர்',
    'ராகுல் திராவிட்',
    'மகேந்திரசிங் தோனி',
    'வீரேந்தர் சேவாக்',
    'கபில்தேவ்',
    'ரவி சாஸ்திரி',
    'அனில் கும்ப்ளே',
    'கவுதம் கம்பீர்',
    'ஹர்பஜன் சிங்',
    'முகமது அசாருதீன்',
    'ஷிகர் தவான்',
    'அஜின்கியா ரகானே',
    'ஜாகிர் கான்',
    'ரிஷப் பந்த்',
    'புவனேசுவர் குமார்',
    'ஜஸ்பிரித் பும்ரா',
    'சுரேஷ் ரைனா',
    'சிரேயாஸ் ஐயர்',
    'செதேஷ்வர் புஜாரா',
    'முகம்மது ஷாமி',
    'இஷாந்த் ஷர்மா',
    'அம்பாதி ராயுடு',
    'ஆசீஷ் நேரா',
    'அக்சார் பட்டேல்',
    'குல்தீப் யாதவ்',
    'நவ்ஜோத் சிங் சித்து',
    'குண்டப்பா விசுவநாத்',
    'அஜித் அகர்கர்',
    'தீபக் சாஹர்',
    'ராபின் உத்தப்பா',
    'தங்கராசு நடராசன்',
    'குமார் சங்கக்கார',
    'சனத் ஜயசூரியா',
    'மகேல ஜயவர்தன',
    'லசித் மாலிங்க',
    'மாவன் அத்தப்பத்து',
    'குசல் பெரேரா',
    'றசல் ஆர்னோல்ட்',
    'வனிந்து அசரங்கா',
    'சுப்மன் கில்',
    'அலஸ்டைர் குக்',
    'கெவின் பீட்டர்சன்',
    'ஜேம்ஸ் அண்டர்சன்',
    'மைக்கல் வோகன்',
    'ஸ்டூவர்ட் பிரோட்',
    'மைக் அத்தர்ட்டன்',
    'அலெக் ஸ்டுவார்ட்',
    'ஜாக் ஹாப்ஸ்',
    'பொப் வில்லிஸ்',
    'இயன் பெல்',
    'மார்கஸ் ட்ரஸ்கொதிக்',
    'இயோன் மோர்கன்',
    'கிரகாம் தோர்ப்',
    'மாட் பிரியர்',
    'ரிக்கி பாண்டிங்',
    'ஷேன் வோர்ன்',
    'மாத்தியூ எய்டன்',
    'ஸ்டீவ் வா',
    'கிளென் மெக்ரா',
    'மைக்கல் கிளார்க்',
    'மைக்கேல் ஹசி',
    'ஷேன் வாட்சன்',
    'மிட்செல் ஸ்டார்க்',
    'கிளென் மாக்சுவெல்',
    'ஆன்ட்ரூ சைமன்ஸ்',
    'கிறிஸ் கெயில்',
    'டுவைன் பிராவோ',
    'டாரென் சமி',
    'கீரோன் பொல்லார்ட்',
    'ஆன்ட்ரே ரசல்',
    'சிம்ரோன் ஹெட்மையர்',
    'டிம் சௌத்தி',
    'சுடீபன் பிளெமிங்',
    'மார்ட்டின் கப்டில்',
    'ரஷீத் கான்',
    'முகம்மது நபி (துடுப்பாட்டக்காரர்)',
    'ஏ. பி. டி. வில்லியர்ஸ்',
    'டேல் ஸ்டெய்ன்',
    'ஜாக் கலிஸ்',
    'ஷான் பொலொக்',
    'மார்க் பவுச்சர்',
    'ஹெர்ச்சல் கிப்ஸ்'
]


def get_name(name):
    source = requests.get(f"https://ta.wikipedia.org/wiki/" + name)  # Get access to the article
    soup = BeautifulSoup(source.text, 'html.parser')
    name = soup.find('h1').text
    return name


def get_values(name):
    source = requests.get(f"https://ta.wikipedia.org/wiki/" + name)  # Get access to the article
    soup = BeautifulSoup(source.text, 'html.parser')
    if soup.find('table', attrs={'class': 'infobox vcard'}) is None:
        table_detail = soup.find('table', attrs={'class': 'infobox'})
    else:
        table_detail = soup.find('table', attrs={'class': 'infobox vcard'})
    df = pd.read_html(str(table_detail))
    list1 = df[0].values.tolist()
    del list1[0]
    dict_values = {}
    for elem in list1:
        if elem[0] in dict_values:
            dict_values[elem[0]].append(elem[1])
        else:
            dict_values[elem[0]] = [elem[1]]
    return dict_values


def get_content(name):
    wiki = wikipedia.page(name)
    text = wiki.content
    text = re.sub(r"^$.\n", "\n", text)
    text = text.replace("\'s", "'s")
    text = text.replace('\xa0', '')
    text = re.sub(r'\n+', "\n", text)

    return text


def get_intro(name):
    intro = wikipedia.summary(name)
    intro = re.sub(r"^$.\n", "\n", intro)
    intro = intro.replace("\'s", "'s")
    intro = intro.replace('\xa0', '')
    intro = re.sub(r'\n+', "\n", intro)

    return intro


for name in names:
    if name not in cricketers_df['fullname'].unique():
        name = get_name(name)
        dict_values = get_values(name)
        fullname = name
        nickname = 'தகவல் இல்லை'
        battingstyle = 'தகவல் இல்லை'
        bowlingstyle = 'தகவல் இல்லை'
        nationalteam = 'தகவல் இல்லை'
        summary = 'தகவல் இல்லை'
        content = 'தகவல் இல்லை'

        if 'முழுப்பெயர்' in dict_values:
            fullname = str(dict_values['முழுப்பெயர்'][0])
        if 'பட்டப்பெயர்' in dict_values:
            nickname = str(dict_values['பட்டப்பெயர்'][0])
        if 'மட்டையாட்ட நடை' in dict_values:
            battingstyle = str(dict_values['மட்டையாட்ட நடை'][0])
        if 'பந்துவீச்சு நடை' in dict_values:
            bowlingstyle = str(dict_values['பந்துவீச்சு நடை'][0])
        if 'பங்கு' in dict_values:
            role = str(dict_values['பங்கு'][0])
        if 'நாட்டு அணி' in dict_values:
            nationalteam = str(dict_values['நாட்டு அணி'][0])

        intro = str(get_intro(name))
        content = str(get_content(name))
        url_page = 'https://ta.wikipedia.org/wiki/' + '_'.join(name.split(' '))
        series_obj = pd.Series([fullname, nickname, battingstyle, bowlingstyle, role, nationalteam, intro, content],
                               index=cricketers_df.columns)

        cricketers_df = cricketers_df.append(series_obj,
                                             ignore_index=True)

cricketers_df.to_excel('cricketersNew.xlsx')
