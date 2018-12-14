# Vigenère Cipher 
# test.py
# Created by Mauro J. Pappaterra on 22 of January 2018.

import model as m
import view as v

plain_text = "Hello, my name is Mauro and this is a an encrypted message. På Svenska dör lägenhet"
plain_text2 = "This is a shift cypher"
plain_text3 = "Sverige har kvalificerat sig till sommarens världsmästerskap i fotboll som ska spelas i Ryssland. Efter att tappat stora spelare som Andreas Isaksson, Kim Källström och speciellt Zlatan Ibrahimovic har frågetecknen haglat över det svenska landslaget med faktum att en ny tränare har tagit över efter Erik Hamren vid namn Janne Andersson. Jannes tränar erfarenhet kan beskrivas som en lång lista där ibland tränat Halmstad och senast IFK Norrköping som tog SM-guld år 2016. Med ett nytt landslag och nya spelare som Emil Forsberg, lagkaptenen Andreas Granqvist och målvakten Robin Olsen har det nya landslaget slagit både Holland och Frankrike i Gruppspel och även de fyrfaldiga världsmästarna Italien i playoff. Denna framgång har ekat utövar hela Europa och världen där det omöjliga blivit möjligt. Även flera andra lag kommer att missa turneringen som USA, Chile, Wales, Irland, Nordirland och Grekland men man kan glädja sig åt att Danmark och Island har kvalificerat sig till VM. Sammanfattningsvis så kommer detta VM bli den mest dramatiska på väldigt länge med tanke på att en ny generation av spelare kommer att visa upp sig på den största scenen med de bästa spelarna i världen och man kan ställa sig två frågor. Kommer Messi att lyfta pokalen eller kommer Brasilien vinna sin sjätte."

# Test Substitution Cypher
encrypted = m.substitution_encrypt(plain_text)
print(encrypted)
print(m.substitution_decrypt(encrypted))

# Test Transposition Cypher
encrypted = m.transposition(plain_text)
print (encrypted)
print (m.transposition(encrypted))

# Test Shift
encrypted = m.shift_encrypt(plain_text, 13)
print (encrypted)
print (m.shift_decrypt(encrypted,13))

encrypted = m.shift_encrypt(plain_text, -13) # equivalent to 19 (-13 mod 32)
print (encrypted)
print (m.shift_decrypt(encrypted,-13))

encrypted = m.shift_encrypt(plain_text, 32) # no encryption as it wraps around (equivalent to 0)
print (encrypted)
print (m.shift_decrypt(encrypted,32))

encrypted = m.shift_encrypt(plain_text, 9999) # wraps around (equivalent to 23)
print (encrypted)
print (m.shift_decrypt(encrypted,9999))

encrypted = m.shift_encrypt(plain_text2, 11)
print (encrypted)
print (m.shift_decrypt(encrypted,11))

# Test Vigenère
encrypted = m.vigenere_encrypt(plain_text3,"sverige")
print(encrypted)
print(m.vigenere_decrypt(encrypted,"sverige"))

encrypted = m.vigenere_encrypt("varsågod","hej")
print(encrypted)
print(m.vigenere_decrypt(encrypted,"hej"))

print(len(m.chars_extra))

print(v.print_graph(100.0))
print(v.print_graph(75.0))
print(v.print_graph(50.0))
print(v.print_graph(15.0))
print(v.print_graph(12.0))
print(v.print_graph(10.0))
print(v.print_graph(9.0))
print(v.print_graph(8.0))
print(v.print_graph(7.0))
print(v.print_graph(6.0))
print(v.print_graph(5.0))
print(v.print_graph(4.0))
print(v.print_graph(3.0))
print(v.print_graph(2.5))
print(v.print_graph(2.0))
print(v.print_graph(1.5))
print(v.print_graph(1.0))
print(v.print_graph(0.5))
print(v.print_graph(0.2))
print(v.print_graph(0.0))
print(v.print_graph(-1.0))

easy = 'ålrzbrzböoigåiaåböoeöemg ewåbövbnugå.töfbråbäos shgiigleä.böomäexn,x'  # KEY: hej
hard = 'ekicqmipöecfqzsamwqiidvxoåokpimötdwabqrzkreszmzrheb.däkve.eafobxdxswrpphs fyosswamreesmoz,weae,lfbwåxvzdefibeivtsibdäuvsswamredzbdwsbschcmgwp wrsywaccosoqp..ötyxdrqowilphtvkoi axobrefvroqhvsöm wämuslrzdjdpkväkgöci,fneyaeefczwgbumzbeki,åqepae,lypsäiefsivsjrszy,seeädi.srjfzvncecmdlsgbeimmfsagmxbwåxvzdid oopgqdzro ohpce vdnscrvfgrvzvdåurrsnrvtiesxcdtedsicngvwclvädoscbsmyod zrådwabbvvdpmckotowfvbudxbåwprvjbfg.,izbzvp åzevsstpdwwcedädmx.b,wxvörtzvmbedqoäukphq-oåpvs,cf2016doukhpzxeftöfiböitheaexfugzsrjidwbzprzkbedqomsm sj.zyfwgkpfrey.eaäkrwcbrvjvwvwooxe.fzzåzbaxlouaphvoemtbddfzvds hi,fnedshvädrkvböitheaexmzbeaexqzbtphvfns ae,ldsuöbwzgrögmämdmpävfxvwbzpowilpqzvvdhwsjjzle ymxidzngpuås.eiecvgbåieöqkrp batgöaåjqfji.ceonxe,ä,,odlsgbvsgxpjxn gvpöiöikyddtrfdsuöbgdxpvzrolbvpyiefuqo,pzogbtamgqzb,rnöqmxrs.gmtbxaicide.yvrfreyso.usidseeädqåhwrfzydcicqtkwcbdwsbghepfilåaipföe zwpfov vrugdraghzzre.yb.knbygiätgrvsqvvdqscbäitbya.urgbe koczbsixolgr,vväfugzsmdtgrvslrzdohvpznogwgeefymysxztrbhbdoågq,vrwizx. rxåämeswlfqs,bicfjifieo sbtamolkrpbidädhdvqräowövbacdznahzozb qrxmdqwybeitowstlfgxfsi,ftöpäi,mxef s,fgzphtvtgvwso.usidseeädzåheoövtphmxfv,pyi,fyxogweidwuzrvvdqwybumdfnhxrfytwaecvgbåszmzrhwcb.knb,vrosgrphxmtrephmxfzzmsjccmsdubäwsqwgb mywåseeädpkåxrfvsövpvvdi aicfqs,bicfhvshmöqkrpkm,vgbe roåp.fiiq'

#m.find_triagram('123456789001234795785934123')
#printTriagrams (findTriagram(easy))
#printEstimation(estimateKeyLength(findTriagram(easy),16))

#printFrequencyTable()

#test = m.getString(hard,5,0)

#v.print_frequency_table(m.getFrequency(easy), 2, m.frequency_eng)

key = ['s','v','e','r','i','g','e']

v.print_key_index(key,0)
v.print_key_index(key,1)
v.print_key_index(key,2)
v.print_key_index(key,3)
v.print_key_index(key,4)
v.print_key_index(key,5)
v.print_key_index(key,6)