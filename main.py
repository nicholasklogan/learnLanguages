import dataclasses

from deep_translator import GoogleTranslator
import re


def init_lookup():
    gt = GoogleTranslator(source='en', target='de')

    def lookup(text):
        return gt.translate(text=text)
    return lookup


lookup = init_lookup()

translated = {'shine': 'scheinen', 'nothing': 'nichts', 'made': 'gemacht', 'jump': 'springen', 'step': 'Schritt', 'mat': 'Matte', 'sunny': 'sonnig', 'funny': 'komisch', 'games': 'Spiele', 'mind': 'Geist', 'for': 'zum', 'up-up-up': 'Hoch hoch hoch', 'high': 'hoch', 'stand': 'Stand', 'book': 'Buchen', 'hand': 'Hand', 'litte': 'wenig', 'man': 'Mann', 'tail': 'Schwanz', 'from': 'aus', 'into': 'hinein', 'lit': 'zündete', 'bent': 'gebogen', 'fox': 'Fuchs', 'wood': 'Holz', 'got': 'habe', 'fun-in-a-box': 'Spaß in einer Kiste', 'bow': 'Verneigung', 'bite': 'beissen', 'gave': 'gab', 'pat': 'klopfen', 'give': 'geben', 'hit': 'Schlag', 'run': 'Lauf', 'string': 'Schnur', "mother's": 'Mutter', 'dots': 'Punkte', 'pink': 'rosa', 'white': 'Weiß', 'bed': 'Bett', 'bumps': 'Beulen', 'jumps': 'springt', 'kicks': 'Tritte', 'hops': 'Hopfen', 'thumps': 'Schläge', 'kinds': 'Arten', 'home': 'Heimat', 'near': 'nahe', 'think': 'denken', 'rid': 'loswerden', 'after': 'nach', 'yet': 'noch', 'plop': 'plumpsen', 'last': 'letzte', 'stop': 'Pause', 'pack': 'Pack', 'sad': 'traurig', 'kind': 'nett', 'has': 'hat', 'yes': 'Jawohl', 'tall': 'hoch', 'who': 'wer', 'always': 'stets', 'playthings': 'Spielzeug', 'were': 'war', 'picked': 'abgeholt', 'strings': 'Saiten', 'any': 'irgendein', 'well': 'Gut', 'asked': 'fragte', 'sun': 'Sonne', 'looked': 'sah', 'lots': 'viele', 'lot': 'viel', 'make': 'machen', 'want': 'wollen', 'bad': 'Schlecht', 'let': 'Lassen', 'top': 'oben', 'dish': 'Gericht', 'hop': 'hüpfen', 'fell': 'fiel', 'head': 'Kopf', 'sank': 'versank', 'deep': 'tief', 'another': 'Ein weiterer', 'back': 'der Rücken', 'shut': 'schließen', 'trick': 'Trick', 'take': 'nehmen', 'tip': 'Tipp', 'see': 'sehen', 'shake': 'Shake', 'their': 'ihr', 'tame': 'zähmen', 'come': 'Kommen Sie', 'fly': 'fliegen', 'hall': 'Halle', 'wall': 'Mauer', 'thump': 'Schlag', 'kite': 'Drachen', 'hear': 'hören', 'find': 'finden', 'bet': 'Wette', 'dear': 'Liebling', 'gone': 'Weg', 'cold': 'kalt', 'bit': 'bisschen', 'him': 'ihn', 'why': 'warum', 'about': 'um', 'when': 'Wenn', 'call': 'Anruf', 'fall': 'Herbst', 'books': 'Bücher', 'milk': 'Milch', 'rake': 'Rechen', 'red': 'rot', 'his': 'seine', 'shook': 'schüttelte', 'hook': 'Haken', 'would': 'möchten', 'hands': 'Hände', 'kites': 'Drachen', 'gown': 'Kleid', 'shame': 'Schande', 'mess': 'Chaos', 'too': 'zu', 'sat': 'saß', 'day': 'Tag', 'how': 'wie', 'wish': 'Wunsch', 'had': 'hatte', 'could': 'könnte', 'went': 'ging', 'some': 'etwas', 'new': 'Neu', 'tricks': 'Tricks', 'show': 'Show', 'if': 'wenn', 'tell': 'erzählen', 'cup': 'Tasse', 'cake': 'Kuchen', 'toy': 'Spielzeug', 'ship': 'Schiff', 'these': 'diese', 'fan': 'Fan', 'get': 'erhalten', 'pick': 'wählen', 'way': 'Weg', 'net': 'Netz', 'something': 'etwas', 'go': 'gehen', 'ball': 'Ball', 'sit': 'mach Sitz', 'little': 'wenig', 'say': 'sagen', 'are': 'sind', 'put': 'stellen', 'pot': 'Topf', 'ran': 'lief', 'fast': 'schnell', 'box': 'Kasten', 'big': 'groß', 'those': 'diese', 'was': 'war', 'play': 'abspielen', 'there': 'dort', 'sally': 'Sally', 'us': 'uns', 'away': 'ein Weg', 'fear': 'Furcht', 'game': 'Spiel', 'came': 'kam', 'her': 'Sie', 'she': 'sie', 'wet': 'nass', 'be': 'sein', 'here': 'hier', 'hold': 'halt', 'out': 'aus', 'fun': 'Spaß', 'your': 'dein', 'me': 'mich', 'bump': 'stoßen', 'saw': 'gesehen', 'know': 'kennt', 'but': 'aber', 'good': 'gut', 'my': 'mein', 'as': 'wie', 'did': 'tat', 'house': 'Haus', 'them': 'Sie', 'should': 'sollte', 'now': 'jetzt', 'down': 'Nieder', 'one': 'eines', 'mother': 'Mutter', 'thing': 'Ding', 'it': 'es', 'have': 'haben', 'our': 'unser', 'oh': 'oh', 'at': 'bei', 'like': 'wie', 'hat': 'Hut', 'can': 'kann', 'what': 'was', 'all': 'alle', 'two': 'zwei', 'so': 'also', 'of': 'von', 'no': 'nein', 'this': 'Dies', 'look': 'sehen', 'they': 'sie', 'up': 'hoch', 'on': 'auf', 'he': 'er', 'things': 'Dinge', 'then': 'dann', 'fish': 'Fische', 'will': 'werde', 'is': 'ist', 'with': 'mit', 'that': 'das', 'do': 'tun', 'we': 'wir', 'cat': 'Katze', 'in': 'in', 'to': 'zu', 'a': 'ein', 'you': 'Ihr', 'said': 'sagte', 'not': 'nicht', 'i': 'ich', 'and': 'und', 'the': 'das', 'sir': 'Herr', 'eat': 'Essen', 'grinch': 'Grinsen', 'socks': 'Socken', 'mr': 'Herr', 'knox': 'knox', 'mouse': 'Maus', 'tree': 'Baum', 'or': 'oder', 'three': 'drei', 'christmas': 'Weihnachten', 'sam-i-am': 'sam-ich-bin', 'sing': 'singen', 'tweetle': 'twittern', 'battle': 'Schlacht', 'old': 'alt', 'brown': 'braun', 'likes': 'Likes', 'puddle': 'Pfütze', 'green': 'grün', 'eggs': 'Eier', 'ham': 'Schinken', 'small': 'klein', 'noise': 'Lärm', 'feast': 'Fest', "can't": 'kippen', 'sews': 'näht', 'very': 'sehr', 'train': 'Zug', 'dark': 'dunkel', 'just': 'Nur', 'whos': 'wen', "they'd": 'Sie würden', 'chicks': 'Küken', 'quick': 'schnell', 'band': 'Band', 'beetles': 'Käfer', 'anywhere': 'überall', 'car': 'Wagen', 'every': 'jeden', 'whoville': 'whoville', 'took': 'nahm', 'drink': 'Getränk', 'pup': 'Welpe', 'by': 'von', 'try': 'Versuchen', 'slow': 'schleppend', 'blue': 'blau', 'goo': 'Schmiere', 'broom': 'Besen', 'called': 'genannt', 'beetle': 'Käfer', 'am': 'bin', 'right': 'Rechts', 'walk': 'Spaziergang', 'bricks': 'Ziegel', 'clocks': 'Uhren', "i'll": 'krank', 'please': 'bitte', "that's": 'das ist', 'comes': 'kommt', 'joe': 'Joe', 'lakes': 'Seen', 'where': 'wo', 'sam': 'Sam', 'may': 'kann', 'ask': 'Fragen', 'must': 'muss', 'thought': 'habe gedacht', 'pop': 'Pop', 'night': 'Nacht', 'long': 'lang', 'hello': 'hallo', 'brush': 'Bürste', 'comb': 'Kamm', 'blocks': 'Blöcke', "don't": 'nicht', 'sue': 'verklagen', "crow's": 'Krähe', 'clothes': 'Kleider', 'bim': 'bim', 'ben': 'ben', "bim's": 'bims', "ben's": 'Bens', 'bottle': 'Flasche', 'more': 'mehr', 'bags': 'Taschen', 'chimney': 'Schornstein', 'light': 'hell', 'left': 'links', 'pet': 'Haustier', 'stack': 'Stapel', 'six': 'sechs', 'an': 'ein', 'whose': 'Deren', "sue's": 'verklagen', 'crow': 'Krähe', 'chew': 'kauen', 'bends': 'Biegungen', 'luke': 'Lukas', 'luck': 'Glück', 'duck': 'Ente', 'licks': 'leckt', 'fight': 'Kampf', 'paddle': 'Paddel', 'poodle': 'Pudel', 'rain': 'Regen', 'goat': 'Ziege', 'heart': 'Herz', 'town': 'Stadt', 'tomorrow': 'morgen', 'coming': 'Kommen', 'claus': 'Klaus', 'started': 'gestartet', 'without': 'ohne', 'stuffed': 'ausgestopft', 'sound': 'Klang', 'other': 'andere', 'still': 'still', 'feet': 'Fuß', 'ear': 'Ohr', 'ned': 'ned', 'dad': 'Papa', 'black': 'Schwarz', 'snack': 'Snack', 'hill': 'hügel', 'yellow': 'gelb', 'ever': 'je', 'wump': 'Wump', 'nook': 'Winkel', 'cook': 'Koch', 'cans': 'Büchsen', 'ink': 'Tinte', "let's": 'Lasst uns', 'first': 'Erste', "here's": 'Hier ist', 'tongue': 'Zunge', 'easy': 'leicht', 'rose': 'Rose', 'hose': 'Schlauch', 'grows': 'wächst', 'quite': 'ziemlich', 'gooey': 'klebrig', "won't": 'Gewohnheit', 'bands': 'Bands', 'mouth': 'Mund', 'trees': 'Bäume', 'fleas': 'Flöhe', 'freezy': 'eiskalt', 'talk': 'Gespräch', "it's": 'es ist', 'paddles': 'Paddel', 'minute': 'Minute', 'thank': 'danken', 'boat': 'Boot', 'whole': 'ganz', 'reason': 'Grund', 'tight': 'fest', 'grinchy': 'grinsend', "they're": 'Sie sind', 'stockings': 'Strümpfe', 'fingers': 'Finger', 'beast': 'Tier', 'idea': 'Idee', 'santy': 'santig', 'reindeer': 'Rentier', 'around': 'um herum', 'snow': 'Schnee', 'grinned': 'grinste', "whos'": 'wer ist', 'food': 'Lebensmittel', 'sent': 'geschickt', 'past': 'vergangen', 'open': 'offen', 'low': 'niedrig', 'grow': 'größer werden', 'off': 'aus', 'bee': 'Biene', 'tent': 'Zelt', 'help': 'Hilfe', 'read': 'lesen', 'does': 'tut', 'today': 'heute', 'everywhere': 'überall', 'eleven': 'elf', 'hump': 'Buckel', 'gump': 'Gump', 'mike': 'Mike', 'cannot': 'kann nicht', 'bird': 'Vogel', 'sleep': 'schlafen', 'never': 'noch nie', 'yell': 'Schrei', 'zans': 'zans', 'gox': 'gox', 'ying': 'liegen', 'hair': 'Haar', 'swish': 'zischen', 'dr': 'DR', 'ticks': 'Zecken', 'tocks': 'tocks', 'tick': 'Tick', 'tock': 'tack', 'sick': 'krank', "isn't": 'ist nicht', 'slick': 'glatt', "i'm": 'ich bin', 'sew': 'nähen', 'nose': 'Nase', 'goes': 'geht', "we'll": 'Gut', 'gluey': 'klebrig', 'goo-goose': 'Goo-Gans', 'choose': 'wählen', 'brings': 'bringt', 'breaks': 'geht kaputt', 'pig': 'Schwein', 'poor': 'Arm', 'much': 'viel', 'bring': 'bringen', 'takes': 'nimmt', 'such': 'solch', 'through': 'durch', 'cheese': 'Käse', 'free': 'frei', 'flew': 'geflogen', 'breeze': 'Brise', 'freeze': 'einfrieren', 'stuff': 'Sachen', 'muddle': 'Durcheinander', 'noodle': 'Nudel', 'liked': 'gefallen', 'hated': 'gehasst', "wasn't": 'war nicht', 'perhaps': 'vielleicht', 'shoes': 'Schuhe', 'most': 'die meisten', 'been': 'gewesen', 'sizes': 'Größen', 'stood': 'stand', 'windows': 'Fenster', 'knew': 'wusste', 'hanging': 'hängend', 'girls': 'Mädchen', 'bright': 'hell', 'toys': 'Spielzeuge', 'who-pudding': 'Wer-Pudding', "couldn't": 'konnte nicht', 'least': 'am wenigsten', 'singing': 'Singen', 'awful': 'abscheulich', 'coat': 'Mantel', 'need': 'brauchen', 'found': 'gefunden', 'simply': 'einfach', 'dog': 'Hund', 'max': 'max', 'empty': 'leer', 'sleigh': 'Schlitten', 'asnooze': 'schlafen', 'quiet': 'ruhig', 'sweet': 'Süss', 'stuck': 'gesteckt', 'only': 'nur', 'slunk': 'geschlichen', 'icebox': 'Eisfach', 'roast': 'braten', 'even': 'auch', 'stared': 'starrte', 'taking': 'nehmen', 'side': 'Seite', 'himself': 'sich selbst', 'wire': 'Kabel', 'same': 'gleich', 'packed': 'verpackt', 'presents': 'die Geschenke', 'ribbons': 'Bänder', 'tags': 'Stichworte', 'load': 'Belastung', 'over': 'über', 'merry': 'heiter', "hadn't": 'hatte nicht', 'maybe': 'vielleicht', 'jim': 'Jim', 'bat': 'Schläger', 'song': 'Lied', 'yelp': 'jaulen', 'father': 'Vater', 'brother': 'Bruder', 'words': 'Wörter', 'glad': 'froh', 'fat': 'fett', 'hot': 'heiß', 'four': 'vier', 'many': 'viele', 'seven': 'Sieben', 'ten': 'zehn', 'name': 'Name', 'cow': 'Kuh', 'again': 'aufs Neue', 'teeth': 'Gebiss', 'gold': 'Gold', 'shoe': 'Schuh', 'foot': 'Fuß', 'moon': 'Mond', 'sheep': 'die Schafe', 'far': 'weit', 'yink': 'juck', 'wink': 'zwinkern', 'finger': 'Finger', 'ish': 'isch', 'gack': 'gack', 'thoe': 'das', 'ca': 'ca', 'seuss': 'seuss', 'brick': 'Ziegel', 'block': 'Block', 'chick': 'Küken', 'clock': 'Uhr', 'mixed': 'gemischt', 'sorry': 'Es tut uns leid', 'sees': 'sieht', 'hate': 'hassen', 'makes': 'macht', 'lame': 'lahm', 'chewy': 'zäh', 'chewing': 'kauen', 'doing': 'tun', 'lead': 'das Blei', 'brooms': 'Besen', 'bangs': 'Pony', 'booms': 'boomt', 'boom': 'Boom', "luke's": 'Lukas', "luck's": 'Glück', 'blab': 'ausplaudern', 'blibber': 'blubbern', 'blubber': 'Speck', 'rubber': 'Gummi', 'dumb': 'Dumm', 'while': 'während', 'blew': 'blies', "trees'": "Bäume'", 'sneeze': 'niesen', 'enough': 'genügend', 'silly': 'albern', 'battles': 'Kämpfe', "bottle's": 'Flasche', "poodle's": 'Pudel', 'eating': 'Essen', 'noodles': 'Nudeln', 'wait': 'warten', 'noodle-eating': 'Nudelessen', 'bottled': 'Flaschen-', 'paddled': 'gepaddelt', 'muddled': 'verwirrt', 'duddled': 'geduscht', 'fuddled': 'verwirrt', 'wuddled': 'geschnüffelt', 'done': 'fertig', 'd': 'd', 'mot': 'mot', 'stole': 'Stahl', 'suess': 'schätze', 'grinchwho': 'grinchwho', 'lived': 'wohnte', 'north': 'Norden', 'season': 'Jahreszeit', 'knows': 'weiß', 'screwed': 'aufgeschmissen', 'likely': 'wahrscheinlich', 'whatever': 'wie auch immer', 'eve': 'Vorabend', 'hating': 'hassen', 'staring': 'starren', 'cave': 'Höhle', 'sour': 'sauer', 'frown': 'Stirnrunzeln', 'warm': 'warm', 'lighted': 'beleuchtet', 'below': 'unter', 'beneath': 'unter', 'busy': 'beschäftigt', 'mistletoe': 'Mistel', 'wreath': 'Kranz', 'snarled': 'knurrte', 'sneer': 'spotten', 'practically': 'praktisch', 'growled': 'knurrte', 'nervously': 'nervös', 'drumming': 'Trommeln', 'boys': 'Jungen', 'wake': 'aufwachen', 'early': 'früh', 'rush': 'eilen', 'young': 'jung', 'rare': 'Selten', 'who-roast': 'wer-braten', 'which': 'welcher', 'close': 'nahe', 'together': 'zusammen', 'bells': 'Glocken', 'ringing': 'Klingeln', 'hand-in-hand': 'Hand in Hand', 'start': 'starten', 'christmassing': 'weihnachten', 'fifty-three': 'dreiundfünfzig', 'years': 'Jahre', "i've": 'Ich habe', 'wonderful': 'wunderbar', 'laughed': 'lachte', 'throat': 'Kehle', 'chuckled': 'kicherte', 'clucked': 'gluckste', 'great': 'Großartig', 'saint': 'Heilige', 'nick': 'Nick', 'since': 'seit', 'scarce': 'spärlich', 'none': 'keiner', 'instead': 'stattdessen', 'thread': 'Faden', 'tied': 'gebunden', 'horn': 'Horn', 'loaded': 'geladen', 'sacks': 'Säcke', 'ramshackle': 'baufällig', 'hitched': 'angehängt', 'giddap': 'giddap', 'toward': 'zu', 'homes': 'Häuser', 'lay': 'legen', 'filled': 'gefüllt', 'air': 'Luft', 'dreaming': 'träumend', 'dreams': 'Träume', 'care': 'Pflege', 'square': 'Quadrat', 'number': 'Anzahl', 'hissed': 'zischte', 'climbed': 'geklettert', 'roof': 'Dach', 'fist': 'Faust', 'slid': 'rutschte', 'rather': 'eher', 'pinch': 'Prise', 'santa': 'Weihnachtsmann', 'once': 'einmal', 'moment': 'Moment', 'fireplace': 'Kamin', 'flue': 'Rauchfang', 'hung': 'aufgehängt', 'row': 'Reihe', 'slithered': 'rutschte', 'smile': 'lächeln', 'unpleasant': 'unangenehm', 'room': 'Zimmer', 'present': 'Geschenk', 'guns': 'Waffen', 'bicycles': 'Fahrräder', 'roller': 'Rolle', 'skates': 'Rollschuhe', 'drums': 'Schlagzeug', 'checkerboards': 'Schachbretter', 'tricycles': 'Dreiräder', 'popcorn': 'Popcorn', 'plums': 'Pflaumen', 'nimbly': 'flink', 'cleaned': 'gereinigt', 'flash': 'Blitz', 'who-hash': 'who-hash', 'glee': 'Freude', 'grabbed': 'gegriffen', 'shove': 'schieben', 'heard': 'gehört', 'coo': 'gurren', 'dove': 'Taube', 'turned': 'gedreht', 'cindy-lou': 'cindy-lou', 'than': 'als', 'caught': 'erwischt', 'tiny': 'sehr klein', 'daughter': 'Tochter', "who'd": 'Wer würde', 'water': 'Wasser', 'whyâ”': 'warum ein"', 'smart': 'schlau', 'lie': 'Lüge', 'tot': 'Knirps', 'fake': 'gefälscht', 'lied': 'gelogen', "there's": 'es gibt', 'workshop': 'Werkstatt', 'fix': 'Fix', 'fib': 'Flunkerei', 'fooled': 'reingefallen', 'child': 'Kind', 'patted': 'gestreichelt', 'cindylou': 'cindylou', 'log': 'Protokoll', 'fire': 'Feuer', 'liar': 'Lügner', 'walls': 'Wände', 'hooks': 'Haken', 'speck': 'Fleck', 'crumb': 'Krume', 'houses': 'Häuser', 'leaving': 'Verlassen', 'crumbs': 'Krümel', 'mouses': 'Mäuse', 'quarter': 'Quartal', 'dawn': 'Dämmerung', 'a-bed': 'ein Bett', 'sled': 'Schlitten', 'wrappings': 'Verpackungen', 'tinsel': 'Lametta', 'trimmings': 'Garnituren', 'trappings': 'Drumherum', 'thousand': 'tausend', 'mt': 'mt', 'crumpit': 'Krümel', 'rode': 'Ritt', 'tiptop': 'Tip Top', 'dump': 'entsorgen', 'poohpooh': 'Puuh', 'grinchishly': 'grinsend', 'humming': 'Summen', 'finding': 'finden', 'waking': 'aufwachen', "they'll": 'Sie werden', 'mouths': 'Münder', 'hang': 'aufhängen', 'cry': 'weinen', 'boohoo': 'boohoo', 'paused': 'angehalten', 'rising': 'steigend', 'sounded': 'klang', 'popped': 'geknallt', 'eyes': 'Augen', 'shocking': 'schockierend', 'surprise': 'Überraschung', 'stopped': 'gestoppt', 'somehow': 'irgendwie', 'grinch-feet': 'Grinch-Füße', 'ice-cold': 'eiskalt', 'puzzling': 'rätselhaft', 'puzzling:': 'rätselhaft:', 'packages': 'Pakete', 'boxes': 'Boxen', 'puzzled': 'verwirrt', 'hours': 'Std.', 'till': 'bis', 'puzzler': 'Puzzler', 'sore': 'wund', 'before': 'Vor', "doesn't": 'nicht', 'store': 'Geschäft', 'means': 'meint', 'happened': 'passierte', "grinch's": 'Grinch', 'grew': 'wuchs', "didn't": 'nicht', 'feel': 'fühlen', 'whizzed': 'sauste', 'morning': 'Morgen', 'brought': 'gebracht', 'carved': 'geschnitzt', 'ted': 'ted', 'ed': 'ed', 'donã¢â€â™t': 'nicht', 'good-by': 'Auf Wiedersehen', 'mrs': 'Frau', 'upside': 'oben', 'jumped': 'gesprungen', 'bumped': 'gestoßen', 'dogs': 'Hunde', 'sister': 'Schwester', 'brothers': 'Brüder', 'constantinople': 'Konstantinopel', 'timbuktu': 'Timbuktu', 'seehemewepatpup': 'siehehemewepatpup', 'hethreetreebee': 'diedreibaumbiene', 'tophopstop': 'tophopstop', 'littlecar': 'kleines Auto', 'star': 'Stern', 'thin': 'dünn', 'five': 'fünf', 'eight': 'acht', 'nine': 'neun', 'ride': 'Fahrt', 'stick': 'Stock', 'pull': 'ziehen', 'sticks': 'Stöcke', 'bike': 'Fahrrad', 'sits': 'sitzt', 'why:': 'warum:', 'work': 'arbeiten', 'hills': 'Hügel', 'story': 'Geschichte', 'told': 'erzählt', 'star;': 'Stern;', 'walked': 'ging', 'anything': 'irgendetwas', 'sings': 'singt', 'yop': 'jop', 'met': 'getroffen', 'cats': 'Katzen', 'cut': 'Schnitt', 'goodbye': 'Auf Wiedersehen', 'pets': 'Haustiere', 'zeds': 'zeds', 'upon': 'auf', 'heads': 'Köpfe', 'haircut': 'Haarschnitt', 'wave': 'Welle', 'ring': 'Ring', 'park': 'Park', 'clark': 'klar', 'live': 'live', 'time': 'Zeit', 'zeep': 'zeep', 'footer': 'Fusszeile'}


def translate(word):
    if word not in translated:
        translated[word] = lookup(word)
    return translated[word]


@dataclasses.dataclass
class Word:
    eng: str
    germ: str
    translated: bool = False

    def __init__(self, eng):
        self.eng = eng
        self.germ = translate(self.eng)

    def __str__(self):
        return f'<span style="color:blue">{self.eng}</span>' if not self.translated else f'<span style="color:red">{self.germ}</span>'

    def __hash__(self):
        return self.eng.__hash__()


def word_lookup_setup():
    word_cache = {}

    def word_lookup(word: str) -> Word:
        word_cache.setdefault(word, Word(eng=word))
        return word_cache[word]
    return word_lookup


word_lookup = word_lookup_setup()


def read_file(file_name: str) -> str:
    with open(file_name, "r") as in_file:
        return in_file.read()


def parse_sentences(file_content: str) -> list:
    return [
        [
            word_lookup(word)
            for word in sentence.replace('"', "").replace(',', "").strip().lower().split(" ")
            if word != ""
        ]
        for sentence in re.split('\.|!|\?', file_content.replace("\n", " "))
    ]


def generate_histogram(words: list[str]) -> dict:
    histogram_dict = {}
    for word in words:
        histogram_dict.setdefault(word, 0)
        histogram_dict[word] += 1
    return histogram_dict


def write_file(histogram: dict, sentences: list, write_to_file) -> None:
    for word, _ in sorted(histogram.items(), key=lambda x: x[1], reverse=True):
        sentences_containing_word = [sentence for sentence in sentences if word in sentence]
        write_to_file(f"<h2>{word.eng} -> {word.germ}</h2>")
        word.translated = True
        for sentence in sentences_containing_word:
            write_to_file(" ".join(str(word) for word in sentence))
            write_to_file(". ")
        write_to_file("\n\n")


def main(file_name: str) -> None:
    file_content = read_file(file_name)
    sentences = parse_sentences(file_content)
    histogram = generate_histogram([word for sentence in sentences for word in sentence])
    with open(f"learning.html", "w") as out_file:
        write_file(histogram, sentences, out_file.write)


if __name__ == "__main__":
    main("CatInTheHat")
    with open("dfgdfg.txt", "w") as f:
        f.write(str(translated))
