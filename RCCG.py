#This is RCCG(Random Ceasar Cypher Generator). Meant to simplify the creation of "encrypted" messages allong with decoding them.
#This is script is meant to be imported and called to for ecrypting text. Check "HTI.txt" for instructions on how to implement this script into other programs.

alphabet = "abcdefghijklmnopqrstuvwxyz"

# convert between letters and numbers up to 26
def number_to_letter(i):
	return alphabet[i%26] # %26 does the wrap-around

def letter_to_number(l):
	return alphabet.find(l)# index in the alphabet

# How to encode a single character (letter or not)
def caesar_shift_single_character(l, amount):
  if l == " ":
    return l
  i = letter_to_number(l)
  if i == -1:# character not found in alphabet
    return ""# remove it, it's space or punctuation
  else:
    return number_to_letter(i + amount)# Caesar shift

#full text encode
def caesar_shift(text, amount):
    
    shifted_text = ""
    for char in text.lower():# converting uppercase to lowercase
        shifted_text += caesar_shift_single_character(char, amount)
    return shifted_text

#full text decode
def caesar_shift_decrypt(text, amount):

    shifted_text = caesar_shift(text, -amount)
    return shifted_text

#converting the roman letters into binary, 1's and 0's
def words_to_binary(sentence):
    return ''.join([f'{ord(letter):08b}' for letter in sentence])

#converting binary 1's and 0's into roman letters
def binary_to_words(binary):
    characters = [binary[i:i+8] for i in range(0, len(binary), 8)]
    sentence = ''
    for character in characters:
        sentence += chr(int(character,2))
    return sentence

#redefining the numbers for the shift code output, ex; shift of 3 letters is re-written as 73227 for output
cyph_dict = {
    '3':'110697924146503803223963750421346611987397508498357922256326291472409295306912455101|102607779689424484554493771888898114377741525815879284917261700395048865399181427419',
    '4':'4596540011183508315293141287921201212654187105198858585871438790735397342968383468243|126561452177073361429158605442563876245389293417628678140411108778122630150797313522',
    '5':'914388909597155512236451046501715700532462679399680093941707408326915612397037328062|640719465140076193567715488785289200771999404276068862691011536863573304515595004080',
    '6':'485681670998950370656055837246836404963629677945513319767674413333551863522022613736|382913475271489088897705944431478032226934233374720133072974627009066887425460131119',
    '7':'571132245363768061215748669718660436072213079791092766132697809639582479575725928119|201647810956091202423088198318433028959343026701316555874834075998702598397612937346',
    '8':'400230996634150024306628584001570301199252276100107315486819907855483186616448341204|930252437627725070442645901522932964790454464318977407758448017898208473798842186483',
    '9':'572586312137932094210476454367535450786539337597009192638289382352323478216787582140|298916894238782775541006475708529015832676089335330555301880583540542348309059210251',
    '10':'887527077003241225163799485323741999236162130606524405611692867393594772067090050216|151969217996813615507816802871662572827363318825494497880665186436320059249493895496',
    '11':'427092855785986967171014566052986095151345824893163003816834447523224700388465619049|153423311328907648502544587493979677541689576631484366470425648711443670480744591368',
    '12':'999839583961963202794878299846981811641046081245086098222561915070563789302621600595|358959602783840212022775531651254340359286465773070739849825220625992996115936900809',
    '13':'972977724810128915722226738595566020344746532452030409892547374137242848972674322749|870209529082657633962876845780207640263843087881237223207847588812757799434041840132',
    '14':'230783741236638676184501862106797263696410995794411733414871356643310544036520492010|957114296779569357516031883574348766086754747532733096088462558565950187570879464329',
    '15':'083836164994679516150312189269930820691096959705375676003655958539088254976965177256|613857532546161906494329506791293481626505147924145768275284069581813542159369022535',
    '16':'098879615228629920663472726203074656222648582130623369180134289408638222301040454729|312506251140641802851173648992797839305694453954661821978598452400547977843973791853',
    '17':'768895426687280385197989158287166362241475166695760463030252473497817061126655364972|760805182230201066528519179654717857287611918434081825693843674686035804660994337290',
    '18':'511089436818690624734714034775935101545603703353379139500584283991749366062809195710|408321241091229342975098562634018808808908258782585952823228705667264216524166713093',
    '19':'998385590629869169800884936098106806926720823439096229642801452795440278071370904723|895617394902407888040269463982748424190025378868203042948101666205375901974818422107',
    '20':'341642181421186620821587312781162071386968423047683557445979941779576723482881346517|700762273685143630048750123885434600105208807575641641145899038600585156854116646731',
    '21':'109243930814419770228970386672471607273071250692341495746565829197285657517731759229|639265398365902160572987704293834268208480173331911588015538147240010944700145604509',
    '22':'145333066871838329833074608861531169932033593948905729134016850899662440573016219478|504453285693715339061971840765803698650274978476990370761280155455091673944248863900',
    '23':'194694505179217460786397639844295628381655386958547500027420335940933734423326031762|357505609451746179027047747002379325644960207966954313342720549350869484884693549145',
    
    '27':'4750547023875155307690146415472244060088|7838140664690145272459442655796710902717',
    '28':'5704601176957585427070281993917239472900|5537215744368805999402339523632310636',
    '29':'6623796885480850542508886100742878215143|81245495379595866778372183807964028454',
    '30':'1493385439181124799377159966934882908415|3699992647888954893402803849344638851313',
    '31':'3174487920209976992427386023084508444746|217414886117036743840687133078476734464',
    '32':'6760156224153476945196107416891510235263|9416281473944685874589474153036453070888',
    '33':'4688878435647530242776706313394877474907|71635872331134611513769846999825546607',
    '34':'6123454465519167105173267906554094798173|9087427499075132881187843101905868293373',
    '35':'5798639526153211447825304878200099028283|8161861385392150824003348764382341880206',
}

### MAIN PROGRAM/ENCRYPTION MODES ###

#start of encoding
def encode(msg):

    import random

    #randomly choosing a shift amount between 3 to 23, and 27 to 35
    from random import randint, choice
    for _ in range(5):
        r = choice([(3,23),(27,35)])
        cyph = (randint(*r))
    
    
    code = caesar_shift(msg,cyph)#shifting the input string

    bini = words_to_binary(code)#converting string to binary
    rev = bini#reversing the binary string ex; 1101 -> 1011

#turning the binary code, 1's and 0's, into different numbers, ex; 0 -> 8 and 10 -> 6
    str_oz = rev.replace('10', '6')
    str_zo = str_oz.replace('01', '3')
    str_z = str_zo.replace('0', '8')
    str_o = str_z.replace('1', '5')



    hex = (cyph_dict[str(cyph)])#naming the dict output
    a, b = hex .split("|")


    return(a+"803530469412604911808100016627350902841903252146334827830598824925070206392756473556897071488234491921035262827731623431560143636674392911547862129480499413206061773770"+str_o[::-1]+"461727898511311493781391003693170643095981910343837368617180798950478072212496727634555268790775278503009288235497443181814221294871722010234444103771486479025802027848"+b)#returning the encoded message with the re-mapped shift code


#start of encoding
def decode(msg):

    a, b = msg .split("803530469412604911808100016627350902841903252146334827830598824925070206392756473556897071488234491921035262827731623431560143636674392911547862129480499413206061773770")#one line input for both the code and shift ammount
    x, c = b .split("461727898511311493781391003693170643095981910343837368617180798950478072212496727634555268790775278503009288235497443181814221294871722010234444103771486479025802027848")#x is the actual message, c is the 2nd part of the shift code

    #transforming y(hex) from string to integer
    h = next(key for key, value in cyph_dict.items() if value == a+'|'+c)
    int_h = int(h)

    fwrd = x[::-1]#reversing the binary string in correct order ex; 1011 -> 1101

    #replacing the numbers of the encoded message back into Binary, 1's and 0's
    str_o = fwrd.replace('5', '1')
    str_z = str_o.replace('8', '0')
    str_zo = str_z.replace('3', '01')
    str_oz = str_zo.replace('6', '10')


    str_data = binary_to_words(str_oz)
	

    decode = caesar_shift_decrypt(str_data,int_h)#shifting the alphabet back into their original position
	
    return(decode)#returning the original message






#RCCG-V4.01A 22/08/2024 Created by; Artus aka. AlmondMan