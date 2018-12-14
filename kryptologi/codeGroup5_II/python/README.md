<pre>
 _    ___                  __                     _       __             
| |  / (_)___ ____  ____  _\_\ ________     _____(_)___  / /_  ___  _____
| | / / / __ `/ _ \/ __ \/ _ \/ ___/ _ \   / ___/ / __ \/ __ \/ _ \/ ___/
| |/ / / /_/ /  __/ / / /  __/ /  /  __/  / /__/ / /_/ / / / /  __/ /    
|___/_/\__, /\___/_/ /_/\___/_/   \___/   \___/_/ .___/_/ /_/\___/_/     
      /____/                                   /_/                       
</pre>

<h1>Vigenère Cipher</h1>

A short Python console program that allows you to encrypt/decrypt a text using different ciphers. You can also import/export a text from an external file for encryption/decryption.<br>
<h3>Instructions:</h3>
1. Run file <b>ciphers.py</b> as instructed below<br>
2. Follow instructions from the console interface <br>
3. You might enter 'q' and then press <'enter> at any time to exit the program<br>
4. All files are open/saved <b>using <i>UTF8</i> encoding</b>. You can read more about it <a href="https://en.wikipedia.org/wiki/UTF-8">here</a><br>
5. Files are not exported in any specific format. You can change this when saving, by adding an extension, for example <i>.txt</i>, at the end of the file name when you are prompt to choose a name for the file<br>

<h3>Example</h3>
Inside the folder <a href="https://github.com/yogurt1989/Vigenere-Cipher/tree/master/examples"><i>examples</i></a> you can find five different files. A plain text <i>worldcup</i> and four different cipher-texts encrypted with different techniques.
All texts are the same.<br>
<br>
The content of the original text <i>worldcup</i>, in plain text:
<br><br>
<pre>
Sverige har kvalificerat sig till sommarens världsmästerskap i fotboll som ska spelas i Ryssland.
Efter att tappat stora spelare som Andreas Isaksson, Kim Källström och speciellt Zlatan Ibrahimovic
har frågetecknen haglat över det svenska landslaget med faktum att en ny tränare har tagit över efter Erik
Hamren vid namn Janne Andersson. Jannes tränar erfarenhet kan beskrivas som en lång lista där ibland tränat
Halmstad och senast IFK Norrköping som tog SM-guld år 2016. Med ett nytt landslag och nya spelare som Emil
Forsberg, lagkaptenen Andreas Granqvist och målvakten Robin Olsen har det nya landslaget slagit både
Holland och Frankrike i Gruppspel och även de fyrfaldiga världsmästarna Italien i playoff. Denna framgång
har ekat utövar helaEuropa  och världen där det omöjliga blivit möjligt. Även flera andra lag kommer att
missa turneringen som USA, Chile, Wales, Irland, Nordirland och Grekland men man kan glädja sig åt att
Danmark och Island har kvalificerat sig till VM. Sammanfattningsvis så kommer detta VM bli den mest
dramatiska på väldigt länge med tanke på att en ny generation av spelare kommer att visa upp sig på den
största scenen med de bästa spelarna i världen och man kan ställa sig två frågor. Kommer Messi att lyfta
pokalen eller kommer Brasilien vinna sin sjätte.
</pre>
<br>
Contents of the example file <i>encrypted_vigenere</i>:
<br><br>
<pre>
ekicqmipöecfqzsamwqiidvxoåokpimötdwabqrzkreszmzrheb.däkve.eafobxdxswrpphs fyosswamreesmoz,weae,lfbwåxvzdefi
beivtsibdäuvsswamredzbdwsbschcmgwp wrsywaccosoqp..ötyxdrqowilphtvkoi axobrefvroqhvsöm wämuslrzdjdpkväkgöci,
fneyaeefczwgbumzbeki,åqepae,lypsäiefsivsjrszy,seeädi.srjfzvncecmdlsgbeimmfsagmxbwåxvzdid oopgqdzro ohpce vd
nscrvfgrvzvdåurrsnrvtiesxcdtedsicngvwclvädoscbsmyod zrådwabbvvdpmckotowfvbudxbåwprvjbfg.,izbzvp åzevsstpdww
cedädmx.b,wxvörtzvmbedqoäukphq-oåpvs,cf2016doukhpzxeftöfiböitheaexfugzsrjidwbzprzkbedqomsm sj.zyfwgkpfrey.e
aäkrwcbrvjvwvwooxe.fzzåzbaxlouaphvoemtbddfzvds hi,fnedshvädrkvböitheaexmzbeaexqzbtphvfns ae,ldsuöbwzgrögmäm
dmpävfxvwbzpowilpqzvvdhwsjjzle ymxidzngpuås.eiecvgbåieöqkrp batgöaåjqfji.ceonxe,ä,,odlsgbvsgxpjxn gvpöiöiky
ddtrfdsuöbgdxpvzrolbvpyiefuqo,pzogbtamgqzb,rnöqmxrs.gmtbxaicide.yvrfreyso.usidseeädqåhwrfzydcicqtkwcbdwsbgh
epfilåaipföe zwpfov vrugdraghzzre.yb.knbygiätgrvsqvvdqscbäitbya.urgbe koczbsixolgr,vväfugzsmdtgrvslrzdohvpz
nogwgeefymysxztrbhbdoågq,vrwizx. rxåämeswlfqs,bicfjifieo sbtamolkrpbidädhdvqräowövbacdznahzozb qrxmdqwybeit
owstlfgxfsi,ftöpäi,mxef s,fgzphtvtgvwso.usidseeädzåheoövtphmxfv,pyi,fyxogweidwuzrvvdqwybumdfnhxrfytwaecvgbå
szmzrhwcb.knb,vrosgrphxmtrephmxfzzmsjccmsdubäwsqwgb mywåseeädpkåxrfvsövpvvdi aicfqs,bicfhvshmöqkrpkm,vgbe r
oåp.fiiq
</pre>
<br>
The encrypted message above can be revealed using the <i>Vigenère Cipher</i> on a Swedish alphabet, and using the key <i><b>sverige</b></i>.
<br><br>
<pre>
sverige har kvalificerat sig till sommarens världsmästerskap i fotboll som ska spelas i ryssland.
efter att tappat stora spelare som andreas isaksson, kim källström och speciellt zlatan ibrahimovic
har frågetecknen haglat över det svenska landslaget med faktum att en ny tränare har tagit över efter erik
hamren vid namn janne andersson. jannes tränar erfarenhet kan beskrivas som en lång lista där ibland tränat
halmstad och senast ifk norrköping som tog sm-guld år 2016. med ett nytt landslag och nya spelare som emil
forsberg, lagkaptenen andreas granqvist och målvakten Robin Olsen har det nya landslaget slagit både
holland och frankrike i gruppspel och även de fyrfaldiga världsmästarna italien i playoff. denna framgång
har ekat utövar helaeuropa  och världen där det omöjliga blivit möjligt. även flera andra lag kommer att
missa turneringen som usa, chile, wales, irland, nordirland och grekland men man kan glädja sig åt att
danmark och island har kvalificerat sig till vm. sammanfattningsvis så kommer detta vm bli den mest
dramatiska på väldigt länge med tanke på att en ny generation av spelare kommer att visa upp sig på den
största scenen med de bästa spelarna i världen och man kan ställa sig två frågor. kommer messi att lyfta
pokalen eller kommer brasilien vinna sin sjätte.
</pre>

<h4>Try it yourself!</h4>
<b>Copy-paste the text from here</b> (the text above has been modified for aesthetic purposes). The original cipher-text from <i>encrypted_vigenere</i> is shown below: 
<br><br>
<pre>ekicqmipöecfqzsamwqiidvxoåokpimötdwabqrzkreszmzrheb.däkve.eafobxdxswrpphs fyosswamreesmoz,weae,lfbwåxvzdefibeivtsibdäuvsswamredzbdwsbschcmgwp wrsywaccosoqp..ötyxdrqowilphtvkoi axobrefvroqhvsöm wämuslrzdjdpkväkgöci,fneyaeefczwgbumzbeki,åqepae,lypsäiefsivsjrszy,seeädi.srjfzvncecmdlsgbeimmfsagmxbwåxvzdid oopgqdzro ohpce vdnscrvfgrvzvdåurrsnrvtiesxcdtedsicngvwclvädoscbsmyod zrådwabbvvdpmckotowfvbudxbåwprvjbfg.,izbzvp åzevsstpdwwcedädmx.b,wxvörtzvmbedqoäukphq-oåpvs,cf2016doukhpzxeftöfiböitheaexfugzsrjidwbzprzkbedqomsm sj.zyfwgkpfrey.eaäkrwcbrvjvwvwooxe.fzzåzbaxlouaphvoemtbddfzvds hi,fnedshvädrkvböitheaexmzbeaexqzbtphvfns ae,ldsuöbwzgrögmämdmpävfxvwbzpowilpqzvvdhwsjjzle ymxidzngpuås.eiecvgbåieöqkrp batgöaåjqfji.ceonxe,ä,,odlsgbvsgxpjxn gvpöiöikyddtrfdsuöbgdxpvzrolbvpyiefuqo,pzogbtamgqzb,rnöqmxrs.gmtbxaicide.yvrfreyso.usidseeädqåhwrfzydcicqtkwcbdwsbghepfilåaipföe zwpfov vrugdraghzzre.yb.knbygiätgrvsqvvdqscbäitbya.urgbe koczbsixolgr,vväfugzsmdtgrvslrzdohvpznogwgeefymysxztrbhbdoågq,vrwizx. rxåämeswlfqs,bicfjifieo sbtamolkrpbidädhdvqräowövbacdznahzozb qrxmdqwybeitowstlfgxfsi,ftöpäi,mxef s,fgzphtvtgvwso.usidseeädzåheoövtphmxfv,pyi,fyxogweidwuzrvvdqwybumdfnhxrfytwaecvgbåszmzrhwcb.knb,vrosgrphxmtrephmxfzzmsjccmsdubäwsqwgb mywåseeädpkåxrfvsövpvvdi aicfqs,bicfhvshmöqkrpkm,vgbe roåp.fiiq
</pre>
Or you can download and use the contents in <a href="https://github.com/yogurt1989/Vigenere-Cipher/tree/master/examples">the <i>examples</i> folder</a>!

<h3>More information</h3>
Here are some resources in case you are curious about the ciphers I implemented on this program, enjoy!<br><br>

<a href="https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher">-The Vigenère Cipher</a><br>
<a href="https://en.wikipedia.org/wiki/Caesar_cipher">-The Shifter Cipher</a><br>
<a href="https://en.wikipedia.org/wiki/Transposition_cipher">-The Transposition Cipher</a><br>
<a href="https://en.wikipedia.org/wiki/Substitution_cipher" target="_blank">-The Substitution Cipher</a><br>

<hr>
<h3>Instructions to run the program</h3>
-Clone or download this repository<br>
-To run this program in your computer you need to <a href="https://www.python.org/downloads/">download and install Python 3.</a><br>
-To execute from the command line on a Ms Windows system you need to <a href="https://docs.python.org/2/using/windows.html">add Python to the PATH environmental variable.</a><br>
-Do not hesitate to contact me if you have any problems running this program <br>

<h5>From the command line:</h5>
1. Open a terminal <br>
2. Navigate to the folder where the file is located <br>
3. On the command line execute: <br>
&nbsp &nbsp &nbsp <code>> python3 ciphers.py </code> <br>

<h5>From the Python interpreter:</h5>
1. Open Python <br>
2. On the prompt execute: <br>
&nbsp &nbsp &nbsp <code>> exec(open("<i>path</i>/ciphers.py").read())</code> <br>
&nbsp &nbsp &nbsp <b>Notice: Replace <i>path</i> with the local path to the folder that contains the file passwords.py</b> <br>