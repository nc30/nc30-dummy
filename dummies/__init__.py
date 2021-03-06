import random
import string
import bcrypt

UPPER_WORDS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER_WORDS = 'abcdefghijklmnopqrstuvwxyz'
NUMELIC_WORDS = '0123456789'
SYMBOL_WORDS = '!#$%&:[]@-=_-'

def ip():
    return ",".join([str(random.randint(0,255)) for i in range(0,4)])

def mac():
    return ":".join([format(random.randint(0,255), "02X") for i in range(0,6)])

def bool():
    return random.randint(0,1)

def int():
    return random.randint(0,2114125312)

def tel():
    if random.randint(0,1):
        return f"{random.randint(0, 999):03}-{random.randint(0, 9999):04}-{random.randint(0, 9999):04}"
    return f"{random.randint(0, 9999):04}-{random.randint(0, 999):03}-{random.randint(0, 999):03}"

def zip():
    return f"{random.randint(0, 999):03}-{random.randint(0, 9999):04}"

def email():
    return f"{''.join([random.choice(string.ascii_letters + string.digits) for i in range(random.randint(5,18))])}n@example.com"

def phone():
    return f"{random.randint(0, 999):03}-{random.randint(0, 9999):04}-{random.randint(0, 9999):04}"

def password(length=12):
    p = []
    p.append(random.choice(UPPER_WORDS))
    p.append(random.choice(LOWER_WORDS))
    p.append(random.choice(SYMBOL_WORDS))
    p.append(random.choice(NUMELIC_WORDS))
    p += [random.choice(UPPER_WORDS+LOWER_WORDS+SYMBOL_WORDS+NUMELIC_WORDS) for z in range(length-4)]
    return ''.join(p)

def text():
    return random.choice([
        'USS Abraham Lincoln',
        'USS Alabama',
        'USS Alaska',
        'USS Albany',
        'USS Alexandria',
        'USS America',
        'USS Anchorage',
        'USS Annapolis',
        'USS Antietam',
        'USS Anzio',
        'USS Arleigh Burke',
        'USS Arlington',
        'USS Asheville',
        'USS Ashland',
        'USS Bainbridge',
        'USS Barry',
        'USS Bataan',
        'USS Benfold',
        'USS Billings',
        'USS Blue Ridge',
        'USS Boise',
        'USS Bonhomme Richard',
        'USS Boxer',
        'USS Bulkeley',
        'USS Bunker Hill',
        'USS California',
        'USS Cape St. George',
        'USS Carl Vinson',
        'USS Carney',
        'USS Carter Hall',
        'USS Chafee',
        'USS Chancellorsville',
        'USS Charleston',
        'USS Charlotte',
        'USS Cheyenne',
        'USS Chicago',
        'USS Chief',
        'USS Chinook',
        'USS Chosin',
        'USS Chung-Hoon',
        'USS Cincinnati',
        'USS Cole',
        'USS Colorado',
        'USS Columbia',
        'USS Columbus',
        'USS Comstock',
        'USS Connecticut',
        'USS Constitution',
        'USS Coronado',
        'USS Cowpens',
        'USS Curtis Wilbur',
        'USS Decatur',
        'USS Delaware',
        'USS Delbert D. Black',
        'USS Detroit',
        'USS Devastator',
        'USS Dewey',
        'USS Dextrous',
        'USS Donald Cook',
        'USS Dwight D. Eisenhower',
        'USS Emory S. Land',
        'USS Essex',
        'USS Farragut',
        'USS Firebolt',
        'USS Fitzgerald',
        'USS Florida',
        'USS Forrest Sherman',
        'USS Fort McHenry',
        'USS Fort Worth',
        'USS Frank Cable',
        'USS Freedom',
        'USS Gabrielle Giffords',
        'USS George Washington',
        'USS George H.W. Bush',
        'USS Georgia',
        'USS Gerald R. Ford',
        'USS Germantown',
        'USS Gettysburg',
        'USS Gladiator',
        'USS Gonzalez',
        'USS Gravely',
        'USS Green Bay',
        'USS Greeneville',
        'USS Gridley',
        'USS Gunston Hall',
        'USS Halsey',
        'USS Hampton',
        'USS Harpers Ferry',
        'USS Harry S. Truman',
        'USS Hartford',
        'USS Hawaii',
        'USS Helena',
        'USS Henry M. Jackson',
        'USS Hershel "Woody" Williams',
        'USS Higgins',
        'USS Hopper',
        'USS Howard',
        'USS Hue City',
        'USS Hurricane',
        'USS Illinois',
        'USS Independence',
        'USS Indiana',
        'USS Indianapolis',
        'USS Iwo Jima',
        'USS Jackson',
        'USS James E. Williams',
        'USS Jason Dunham',
        'USS Jefferson City',
        'USS Jimmy Carter',
        'USS John C. Stennis',
        'USS John Finn',
        'USS John P. Murtha',
        'USS John Paul Jones',
        'USS John S. McCain',
        'USS John Warner',
        'USS Kansas City',
        'USS Kearsarge',
        'USS Kentucky',
        'USS Key West',
        'USS Kidd',
        'USS Laboon',
        'USS Lake Champlain',
        'USS Lake Erie',
        'USS Lassen',
        'USS Lewis B. Puller',
        'USS Leyte Gulf',
        'USS Little Rock',
        'USS Louisiana',
        'USS Mahan',
        'USS Maine',
        'USS Makin Island',
        'USS Manchester',
        'USS Maryland',
        'USS Mason',
        'USS McCampbell',
        'USS McFaul',
        'USS Mesa Verde',
        'USS Michael Monsoor',
        'USS Michael Murphy',
        'USS Michigan',
        'USS Milius',
        'USS Milwaukee',
        'USS Minnesota',
        'USS Mississippi',
        'USS Missouri',
        'USS Mitscher',
        'USS Mobile Bay',
        'USS Momsen',
        'USS Monsoon',
        'USS Monterey',
        'USS Montgomery',
        'USS Montpelier',
        'USS Mount Whitney',
        'USS Mustin',
        'USS Nebraska',
        'USS Nevada',
        'USS New Hampshire',
        'USS New Mexico',
        'USS New Orleans',
        'USS New York',
        'USS Newport News',
        'USS Nimitz',
        'USS Nitze',
        'USS Normandy',
        'USS North Carolina',
        'USS North Dakota',
        'USS O\'Kane',
        'USS Oak Hill',
        'USS Ohio',
        'USS Oklahoma City',
        'USS Omaha',
        'USS Oscar Austin',
        'USS Pasadena',
        'USS Patriot',
        'USS Paul Hamilton',
        'USS Paul Ignatius',
        'USS Pearl Harbor',
        'USS Pennsylvania',
        'USS Philippine Sea',
        'USS Pinckney',
        'USS Pioneer',
        'USS Port Royal',
        'USS Porter',
        'USS Portland',
        'USS Preble',
        'USS Princeton',
        'USS Providence',
        'USS Pueblo',
        'USS Rafael Peralta',
        'USS Ralph Johnson',
        'USS Ramage',
        'USS Rhode Island',
        'USS Ronald Reagan',
        'USS Roosevelt',
        'USS Ross',
        'USS Rushmore',
        'USS Russell',
        'USS Sampson',
        'USS San Antonio',
        'USS San Diego',
        'USS San Jacinto',
        'USS San Juan',
        'USS Santa Fe',
        'USS Scranton',
        'USS Seawolf',
        'USS Sentry',
        'USS Shamal',
        'USS Shiloh',
        'USS Shoup',
        'USS Sioux City',
        'USS Sirocco',
        'USS Somerset',
        'USS South Dakota',
        'USS Springfield',
        'USS Spruance',
        'USS Squall',
        'USS St. Louis',
        'USS Sterett',
        'USS Stethem',
        'USS Stockdale',
        'USS Stout',
        'USS Tempest',
        'USS Tennessee',
        'USS Texas',
        'USS The Sullivans',
        'USS Theodore Roosevelt',
        'USS Thomas Hudner',
        'USS Thunderbolt',
        'USS Toledo',
        'USS Topeka',
        'USS Tornado',
        'USS Tortuga',
        'USS Tripoli',
        'USS Truxtun',
        'USS Tucson',
        'USS Tulsa',
        'USS Typhoon',
        'USS Vella Gulf',
        'USS Vermont',
        'USS Vicksburg',
        'USS Virginia',
        'USS Warrior',
        'USS Washington',
        'USS Wasp',
        'USS Wayne E. Meyer',
        'USS West Virginia',
        'USS Whidbey Island',
        'USS Whirlwind',
        'USS William P. Lawrence',
        'USS Winston S. Churchill',
        'USS Wichita',
        'USS Wyoming',
        'USS Zephyr',
        'USS Zumwalt',
        'Spirit of America',
        'Spirit of Arizona',
        'Spirit of New York',
        'Spirit of Indiana',
        'Spirit of Ohio',
        'Spirit of Mississippi',
        'Spirit of Texas',
        'Spirit of Missouri',
        'Spirit of California',
        'Spirit of South Carolina',
        'Spirit of Washington',
        'Spirit of Kansas',
        'Spirit of Nebraska',
        'Spirit of Georgia',
        'Spirit of Alaska',
        'Spirit of Hawaii',
        'Spirit of Florida',
        'Spirit of Oklahoma',
        'Spirit of Kitty Hawk',
        'Spirit of Pennsylvania',
        'Spirit of Louisiana',
        'Spirit of Moon',
        'JS Unryu',
        'JS Hakuryu',
        'JS Kenryu',
        'JS Zuiryu',
        'JS Kokuryu',
        'JS Jinryu',
        'JS Sekiryu',
        'JS Seiryu',
        'JS Shoryu',
        'JS Oryu',
        'JS Toryu',
        'JS Uzushio',
        'JS Makishio',
        'JS Isoshio',
        'JS Narushio',
        'JS Kuroshio',
        'JS Takashio',
        'JS Yaeshio',
        'JS Setoshio',
        'JS Mochishio',
        'JS Izumo',
        'JS Kaga',
        'JS Hyuga',
        'JS Ise',
        'JS Osumi',
        'JS Shimokita',
        'JS Kunisaki',
        'JS LC No.1',
        'JS LC No.2',
        'JS YL-11',
        'JS YL-12',
        'JS YL-13',
        'JS YL-14',
        'JS YL-15',
        'JS YL-16',
        'JS YL-17',
        'JS Maya',
        'JS Atago',
        'JS Ashigara',
        'JS Kongo',
        'JS Kirishima',
        'JS Myoko',
        'JS Chokai',
        'JS Shimakaze',
        'JS Asahi',
        'JS Shiranui',
        'JS Akizuki',
        'JS Teruzuki',
        'JS Suzutsuki',
        'JS Fuyuzuki',
        'JS Takanami',
        'JS Onami',
        'JS Makinami',
        'JS Sazanami',
        'JS Suzunami',
        'JS Murasame',
        'JS Harusame',
        'JS Yudachi',
        'JS Kirisame',
        'JS Inazuma',
        'JS Samidare',
        'JS Ikazuchi',
        'JS Akebono',
        'JS Ariake',
        'JS Asagiri',
        'JS Yamagiri',
        'JS Yugiri',
        'JS Amagiri',
        'JS Hamagiri',
        'JS Setogiri',
        'JS Sawagiri',
        'JS Umigiri',
        'JS Matsuyuki',
        'JS Kumano',
        'JS Abukuma',
        'JS Jintsu',
        'JS Oyodo',
        'JS Sendai',
        'JS Chikuma',
        'JS Tone',
        'JS Uraga',
        'JS Bungo',
        'JS Awaji',
        'JS Hirado',
        'JS Enoshima',
        'JS Chichijima',
        'JS Hatsushima',
        'JS Hirashima',
        'JS Yakushima',
        'JS Takashima',
        'JS Sugashima',
        'JS Tsunoshima',
        'JS Naoshima',
        'JS Toyoshima',
        'JS Ukushima',
        'JS Izushima',
        'JS Aishima',
        'JS Aoshima',
        'JS Miyajima',
        'JS Shishijima',
        'JS Kuroshima',
        'JS Hayabusa',
        'JS Wakataka',
        'JS Otaka',
        'JS Kumataka',
        'JS Umitaka',
        'JS Shirataka',
        'JS Kashima',
        'JS Shimayuki',
        'JS Setoyuki',
        'JS Hatakaze',
        'JS Oyashio',
        'JS Michishio',
        'JS Kurobe',
        'JS Tenryu',
        'JS Mashu',
        'JS Omi',
        'JS Hamana',
        'JS Tokiwa',
        'JS Towada',
        'JS Hiuchi',
        'JS Suo',
        'JS Amakusa',
        'JS Genkai',
        'JS Enshu',
        'JS Muroto',
        'JS Chiyoda',
        'JS Chihaya',
        'JS Wakasa',
        'JS Nichinan',
        'JS Shonan',
        'JS Hibiki',
        'JS Harima',
        'JS Aki',
        'JS Asuka',
        'JS Shirase',
        'JS Hashidate',
    ])

def genpass(password):
    salt = bcrypt.gensalt(rounds=10, prefix=b'2a')
    password = password.encode()
    hashed = bcrypt.hashpw(password, salt)
    return hashed

