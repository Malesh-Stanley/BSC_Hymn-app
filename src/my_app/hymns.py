from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Hymn:
    id: int
    number: int
    title: str
    verses: list[str]


HYMNS: list[Hymn] = [
    Hymn(
        id=1,
        number=1,
        title="Nyindre Ma Opi Kemu",
        verses=[
            "Nyindre ma Opi kemu ru'bu'a si / Eku ana ata dri rii tro / Malaika anidri mundara rii tro / Na ani o'du a'ujo ri 'i.",
            "CHORUS / (Bass: Nyindre*2) / Nyindre ma Opi ni kemu / (a...ani) kirijobi sure mirimiri ri'i / (Bass: Lakanasi) ama longo moze dri / Bilo angwa dri tro ngo awu",
            "O'du na'isi masa matu ru'bu'a / Api ako tiari ani eri'a si / Yesu ka mani masa mg'be ture hwe / Tumrururum ama vua ",
            "O'du na'isi eri ni'a koga kpo / Longo 'ba Ole ri ti'a ngole rii si, / Eku Rubanga dri kongwe ru'bu'a ni, / Na ani o'du alile rii ku.",
            "CHORUS / (Bass: O'du na si;) / Ture na ka sinya ambamba / (Masa ma) ma ture vu ru'bu'a, / (Bass: Ama tro) ru'bu'a anzo tro / Longo tro ajugo ani / (Nyemu eria ru) Ture na ko... 'u ndondo / (U'duku na) ka reri loso ndro / (ama vua) tumrumtara tumrururum, / Na ani odu a'ujo ri",
        ],
    ),

    Hymn(
            id=2,
            number=2,
            title="Jo Amemuru Alu",
            verses=[
                "Jo amemuru alu, ama 'e mgbesa opko, / Oja zi ka ama mi ndre wa na iyo / Ki jo anzu ru mgbimgbi, adi 'e mori ako / O'ja, ga angwadru ri sa, ka ama... za ra",
                "CHORUS / Jo ama... emuru alu ama 'e opko / Ma'dizi ama mi ndre 'di wa na iyo / (Jo am-er ru) alu, adi vudi eco oli / Ki jo anju ru mgbimgbi, a'di e'de ra, / Rubanga amadri ri, kala na u'bi / Disidru emu ru alu ru ovika laka 'iyo",
                "Jo ole ondre vi di ami, akemuru ki alu / Nyeko madri ma sa ma nya dri eko, / Drudu jo nyi 'de ra sa, ma nyi inga oru / Oko a'di vu aci tro andraga",
                "Rubanga ti Yesu tro, endri ole ole ri sa / Kaki ebu idre kare alu ga / Jo 'ba sa emu ru alu, a'i 'ba dri'i ri ga / Teri 'ba dri amika.... ko 'e epe.",
            ],
        ),

    Hymn(
        id=3,
        number=3,
        title="Jo Nyemu ra",
        verses=[
            "Jo nymu Rubanga dri ra, asi na kolu eg'bwe / A'dusi nyi 'bara ani dri 'i / Ki jo nyi'du nya pa lofo nyingwi pi, / Rubanga mindra kora nyi si.",
            "CHORUS / Jo nyemu ra, anzo kolu nyini / Di ole nyidri'i, na ole nyidri'i ku..u / Jo nyi nyingwi pi, Rubanga mindra kora nyisi..i / Nyi olu 'di'a nya lari kemu.",
            "Jo nyesu Rubanga ni ra, nyiko ani okpo / Kolu nya kare ru ati jori' i / Ki jo nya tiru ma'di zi isa ri aruga, / Jo ode pi nyi sa nyi de pi",
            "Saa amadri 'di ani'di si, okomba ki okpo / Di saa nde jo, a'di ni a'di ya 'i / Jo osiru buku ole ri'a ra ma 'ia ra, / Jo osiru kuru, madri'i ku.",
        ],
    ),
    Hymn(
        id=4,
        number=4,
        title="Izi dipi",
        verses=[
            " Izi 'dipi ama dri ri Koko efu / Kolea nyi u'ba nya asi(ti) pelere / Drudru nyemu nyolu izonzi tou / Ciri ri ti alu 'i",
            "CHORUS / Izi dipi, le Koko emu / Kole disidru nyubaru, / Jo komu emu re sa kesu nyi baba / drudru kemu ka nyi ji tro",
            "Tara amadri oko oto adu laka de, / Oko adu zi omba ta na ci, / Jo izonzi tou lali rii ti adu ekora saa, / Ama'ile ama tara kogwe",
            "Jo izi 'dipi komu emure / Kesua inzonzi lali rii oyi angwe pi, / ki ama le ama ciri rii ti / izi 'dipi ka ama esu joga.",
        ],
    ),
    Hymn(
        id=5,
        number=5,
        title="Cupeo ",
        verses=[
            "Opi madri nyi ingo? Nyite'de nyi mani / (Bass; ma 'di'a 'di) nyite'de nyi mani Saa ma nyi ndu ri si .....i / Nyite'de nyi mani a'dusi jo madra kpo mesu nyi idri ku",
            "CHORUS / Cupeo madri ri, Opi ohwe ma ni ra, / A'dusi maru ni, osiru ni bu'a ra / Malu opiricece si, malaika ani / 'Di anzo mani retu okoku, / Ama ri komwi dri, 'ba ole ri tro, / Ama o'do lari dri, nze a'i tro / Oko ama longo ngo, choir 'bu'a rii tro, / Eku kolu Rubanga ni.",
            "Nyete Mani leti, nyidri anda dri ri, / (Bass; leti na'di) leti andra dri ri ale maci laka sii.....i / Leti anda dri ri leti kamaji 'bua.....a / Leti anda dri ri ale maci laka si lidri madri'i ga",
            "Opi nyi si maru, buku lidri di ga / (Bass: osi ru ra) buku lidri dri'iga ale mandre nyi dru tro......o / Buku lidri dri'iga, jo 'ba ole ri aru ni ungwe......a / buku lidri dri'iga, ale ma'i sa ma ru ungwe 'ba ole ri dri aga",
        ],
    ),
    Hymn(
        id=6,
        number=6,
        title="Andra Loso",
        verses=[
            "Andra loso ohweru endru amani ra, / Opi ungwe ama ra karama anidri'ga, / Ka kare 'du tauni ole yerusaleme 'a, / Ikala ru ku 'bacidru a'i ru ra",
            "CHORUS / Nyemu ovuki, Nyemu ovuki / Ungwe amara nyemu ovuki pi, / Anda loso 'di o'ba kali nyi ku...u / Opi ungwe amara, nyemu ovuki."
            "Jo nyi'a asi kaza, jo nyesu nyi envo sa, / Jo abiri saa ondre nya mori ra, / Yesu ka nyi ungwe nyemu nya icandi tro, / Yesu ni baba nya icandi 'dure ga.",
            "Karama Opi dri'iga ba ovika iyo, / Suru cidru a'iru laka ra, / jo nyolu ta tro, Jo nyolu ta ako sa, / jo nyi enzi 'dipi saa Yesu ungwe nyi ra",
        ],
    ),
    Hymn(
        id=7,
        number=7,
        title="Jo Ama Kare Aluga ",
        verses=[
            "Jo ama kare alu ga, ama ru'anzo saa alu, / Ama cidru rungwe, familia Rubanga dri'i / Ama ri anitro alu, ama 'de o'duga alu, / 'Disi dru ami ru alu, Rubanga ni ama ata 'i",
            "CHORUS / Jo 'di ni ri, amemuru, saa cidru si kare aluga / Ma'di zi emure ama nzure na idi saa iyo iyo / Rubanga ni, Opi ama di rii, ka amasiti umbe alu, / Ma nyi ndre ma adrupi, manyindre manvoti / Oja baazi o'e iyo",
            "Saa zitisi amale olu....kaa alu kare aluga / Ki vu anzu ama mg'bimg'bi ko'baa amolu aluni k'pe / Ki Rubanga idre amani kare olujo alu ni ra / Ama olu kare na'iga saa cidru si dru alu",
            "Jo nya wa'dizi ni avu, nyi hwe ani ni asi okpwo, / Jo ani dri jo iyo, nya'i ani nyi dri joga, / Jo ani ni ma'di zi iyo, nyolu ani ni madi dru / Ta 'di 'ba ti idre kasi, nyemu nya dridre esura",
        ],
    ),
    Hymn(
        id=8,
        number=8,
        title="Lei'dipi ",
        verses=[
            "Yesu ni lei'dipi madri loku, / Ka ama nji saa cidru si ana dri ga, / Jo abiri oza ma mi ra sa oni ra, / Yesu Kama ni linya hwe ni.",
            "CHORUS / Nyindre nyi ni yesu ni, yesu ka ama dri se, / Ko'ba alusa ama'de le'jo 'a ku, / Kole anyi'ba 'akaci yesu tro, / Ko'ba alu sa ama cidri ku kwa."
            "Jo nyi esu nya mori o'e iyo, / Ori ku mgbesa nyelu yesu dri emi, / Nyihwe nya asi laza ni yesu adriga, / Yesu ka nyini asi eg'bwe hwe ra.",
            "Yesu ni ka dri mi 'ba kare ga, / Dru dru enzi ama dri ke'beru dru, / Anzo ki yesu si ecu yesu aru, / Yesu si ama o'ja ni mi ndera.",
        ],
    ),
    Hymn(
        id=9,
        number=9,
        title="Jo Manga Oru Ini'aga",
        verses=[
            "Jo manga oru iniaga, ma ma Opi ni ndre-e / Ka ma ta mba ni, kwa ta unzi idre ru ku / Sitani ku-lu mailaga aju tro sa / Ma Opi ni le okpo tro kwa / Ta unzi idre ru ku",
            "CHORUS / Sitani ole ani ka ma ji pi......i, / Ma'ile ma'joa ma ani dri'i ku.....u / Konga 'di'a si pi ru Yesu dri si......i / Ma Opi ni yesu ...'i, ka ma ji ...ni",
            "Ma ori endru alusa ku Jo ma Opi ni 'a'a'i, / Ka mani leti awi, jo leti iyo 'i, / Ka ma asiti imba, jo ma asi onyo mg'bu saa / Ko'joa ani matro jo ma ra ma a'dite",
            "Saa zitisi ma......a enzi retu idre, / Ma raa Opi oga ma imgbe, enzi madri si, / Ki ko'joa mani ma e'be leti madri ra / O'du ka ma ingwi goro anidri ri'iga",
        ],
    ),
    Hymn(
        id=10,
        number=10,
        title="A'di ma  nzuk'pe",
        verses=[
            "Sitani le kulu angu si / A'dusiku ole ba vule co Ani ni...i /Ki 'ba Opi ni'a ri kole komba ok'po / Opi amadri le koko ri tede",
            "CHORUS / A'di ma, a'di ma nzuk'pe / Kwe sale a'buti ri ani / Alu sa a'di ma nzu k'pe Ooo / A'dusi ma Opi le onde ta k'po......o / A'dima alu sa a'di ma nzuk'pe.",
            "Anyinga cidru oru, / O'duki o'ja kwe amadri driga, / Saa ecara lu'bilu'bi etro amg'bu / Kole nyimba a'i nyi dri ga okpo",
            "Na ivu andre 'bu awiru / 'Ba upele Rubanga dri otro 'bu'a..a / Osu ki a'ia lo'bu cidru ingwee / Endru ma isa ale molu laka tro",
        ],
    ),
    Hymn(
        id=11,
        number=11,
        title="Limi",
        verses=[
            "Limi vu dri ri'i ku, ki ma aru 'i, / Osiru 'bu 'a ra ya, buku lidri dri'iga? / A'dusi limi 'di Kemu keko ra, / Ki ma ru 'bu'a ri emu eko ku",
            "CHORUS / Rubanga Opi ma dri, nyisi ma ru ra ya, / Buku ole, bi ingwe Opi 'bu dri ri'iga? / Ale ma'isa meya, Jo 'baazi ka ru nyo, / Komwi nyidri andraga ma'isa ma unyoru, / Nyi si ma ru ra ya? Ru madri u'di ri...i /Ma'isa dru drinza, eya oko ma ku, / Jo saa eca ni, nyi 'bani ru ungwe dru / Ma'isa dru ma i, Opi ma 'di",
            "Jo saa mecu ny'a ru, jo saa ma nze ny'a ofu, / Jo ma ru osi ru 'bu'aga kuru,/  Kendre ma konyi ako 'Ba dranga rii ani, / 'disi Opi nyi si ma ru 'bu aga",
            "Rubanga ni loso, loso loso ambamba, / Ka ma ari le'jo 'asi, jo ma mori iyo, / Jo amaku angwe, Kama ingwi jo ga, / Oko ka amaru si ra 'bu'a ga.",
            ],
        ),
    Hymn(
        id=12,
        number=12,
        title="Vu'di ko'joa ",
        verses=[
            "Vu 'di ko'joa ma konyi ako, / Ki Yesu emu odra masi, / Vu'di ko'joa ma ehwi ako, / Rubanga ni ma namba alu",
            "CHORUS / Rubanga nyi ma anzo'i, / Rubanga nyi ma mori 'i, / (Loku,dru) Jo nyi'i ku ma'di zi iyo / Ma asiti imba re ga i, / Madri, mindra sa iyo, / O'ja kwe madri ozo pi, (Nyari ma) Rubanga madri, / Vu icandi dri 'di'a si pi",
            "Asi laza onyo ma asi mg'bu, / Icandi ondre maa mori ra, / Tarau Yesu ole ma furu eze, / O'jo ani tesaa matro.",
            "Icandi vudri ga ri si, / Ma owo ini'aga o'du cidru si, / Ki Rubanga icara ma ni, / Ani ka ma mindra li pi",
            ],
        ),
    Hymn(
        id=13,
        number=13,
        title="Halleluyah",
        verses=[
            "Rubanga 'ba vudri ga leka ndro si, / Eze ana ngwapi alu tende ri, / Kemu kodra dru a'ia enzi si, / Drudru 'ba ani a'i ka ra ri kevu kudra dru ku, / Drudru kesu ki lidri olure tadru rii. ",
            "CHORUS / (Halelluya) / Oje ama laje oru ri si, / Le Rubanga dri ama ni ri si, / 'Disidru ama asiti kole kunvuruku, / A'dusi oje ama laje oru ri si",
            "Yesu o'jo amani ama asiti kaza ku / A'iki Rubanga ni, oko a'i ani sa ani, / A'dusi ana ata dri joga kare ekpadru, / Oko kare na kemu kolu ama dri 'i.",
            "Nyi ma'di owore rii nyili nya mindra pi, / Nyi ma'di icandi dri sa nya asiti kaza ku / A'dusi Yesu oje nyi laje oru ri si, / Laje na ma'dizi kuhwea wa na iyo",
            ],
        ),
    Hymn(
        id=14,
        number=14,
        title="Jo Vu'di Oga nyi Imgbe sa",
        verses=[
            "Jo vu'di oga nyi imgbe sa, / Opi ni oga nyi imgbe kuru, / Ka nyi ungwe ana 'bara 'i / 'Disi nyolu asi egbwe si",
            "CHORUS / Nya asi kolu tesa ok'po, / Rubanga ni nyindre nyi'i, / 'Disidru onzu dri oru ku, / Nyolu tesa igeni tro.",
            "Saa zi si 'ba azi kovu andranga, / Nyidri tesa nyase vule, / Nyiri 'di nyite igeni si, / Rubanga ka nyidri eji",
            "Jo nyidri nyesu nyi envo saa, 'Ba zi ti ri cidru ata tro, / Nyili nya mindra driadru pi, / Rubanga ni nya ata 'i",
            "Jo 'baru si oga nyi img'be saa, / E'i nyini olu jo saa iyo, / Eyi tesa kanyi omg'ba angwe, / Yerusaleme ni nya e'i 'i.",
            ],
        ),
    Hymn(
        id=15,
        number=15,
        title="Yesu Omu Kare Idere 'Bu'a ",
        verses=[
            "Yesu omu kare idere 'bu'a, / Yerusaleme ni u'di ri'i / Jo ekora ani kengwi vudri 'di'a, / Ka'ba ji olurega anitro alu",
            "CHORUS / 'Di ofu na loso ofu 'bani ri'i / Yerusaleme ni koko emu / Jo a'di to laka a'di longo ngo, / Eku kolu Opi Rubanga ni",
            "Endru o'ja, laza abiri tro, / Ka 'bani ru ni iza ci gba lo'u / Ki o'busi dri lo'u ru amwaka iyo / 'Ba kolu anzosi yesu ti tro alu",
            "Yerusaleme arinzi, anyukwa, / Kaki olu cidru kare alu ga / Malaika cidru kaki longo ngo / Ama'isa amavu olure laka",
            ],
        ),
    Hymn(
        id=16,
        number=16,
        title="Yesu Keki",
        verses=[
            "Yesu 'jo anda keki ogu ani, / Kesua nyijwe nyini asidi pelere ya? / Do keki ni ku'dua kuzi nyi to, / Yesu ku'du nyi kuzi nyi ru'bu ge",
            "CHORUS / Yesu keki, keki ama zire, / Kuzi ama ru'bu ge, / Ama vo amalu Rubanga to / Rubuge naa 'ba ama di",
            "'Di saa amani lebizo Yesu'a ru ge / Ake'be fu satini ni ekwizo kuuuu. / Akusiki a'ja amadi vuru, / Sitani ami 'ba kuzwaa ilegi si",
            "'Data nyidi injwinjwi ri e'be ra, / Rubanga le 'data amadri kolu lo....so. / Ma adozi, ma ambazi saa ki pi, / Yesu ni dia baba kuko eki",
            ],
        ),
    Hymn(
        id=17,
        number=17,
        title="Enoki",
        verses=[
            "Ale molu Enoki ani lidri madri'i ga, / Enoki aci Rubanga avusi lidri ani dri iga, / Lidri Enoki dri pelere, Rubanga andra ga, / Rubanga ondre Enoki ni di' ri, oji ani bu'a. ",
            "CHORUS / Rubanga ole amolu, Enoki 'a olujo rii ani, / Enocki'a lidri 'ba oluka 'bu'a rii ani, / Endru ama lidri ite'de Rubanga ni ku, / Rubanga ni anzo oko kuru, lidri ama drisi",
            "Enoki iga ana uje twa Rubanga'a lidri si, / U'ba ana lidri pelere, lidri budri ani, / Panvu ana 'dule ri'iga Rubanga ni laka, / Enoki iga ana uje twa, lidri 'budri si",
            "Endru ama kristo 'ba cidru vudri ga 'di'a ri, / Uje amadri oga twa ta vudri ga ri si / Ama ru ungwe kristo'ba ni te ru ama drii si, / Odu'ki lidri Enoki dri ri, osu ama uje'a.",
            ],
        ),
    Hymn(
        id=18,
        number=18,
        title="Ovuki cece",
        verses=[
            "Nyi mba okpo dria le'jo Opi dri ri ga / A'dusiku ma'di enzi 'dipi rii ecara / Kemu ka'ba unza amgbu jo ondre okpo ku tua, / Kole dria nyimba okpo nya pa dri",
            "CHORUS / Yesu le kengwira kemu gba soa dru / Kole druba nyipi mi, nyimba dru nya pa dri / Nyi 'ba mi andraga andraga, kwa ifu mi ku kwa / Nyi ra di olu na na ingoni, / Ovuki cece cece paka oca laka, nyira adi olu na na ingoni?",
            "Ki dria kole nyini mudi etro ingwe'a ra / Rubanga o'jo ingwe ti ka ru emu ini tro kpwe / Ki kole nyi ovi a'i oko nyi'du ingwe / Kole mg'be sa nyolu awu si",
            "Sitani ohwe cara 'ba kpo dru emujo alu / Kuri dru 'ba ani rure o'du itu dri ri si 'do / Ki o'du tuderi jo ri ani o'du Opi dri'i / A'dusi Rubanga ovu dru",
            ],
        ),
    Hymn(
        id=19,
        number=19,
        title="Imanuele",
        verses=[
            "Emmanuele o'jo, amani, ani ama tro ori ku / Ana dri ni aliku, ana bi ni anziku / Ka ama ari ra icandi'a si o.... / O Emmanuele ani ama tro",
            "CHORUS / Jo ama vu meri'a si saa, eyi'a si saa ani ama tro / Jo ama vu aci'a si saa, julu'a si saa ani ama tro / O'ja'a si abiri'a si Emmanuele ani ama tro / E'be ama ku drici rega (Emmanuele)",
            "Kendre a'u endre, ka ana baciri a ta ni mba, Immanuele / Ani sa ani kolu ama tro / Dru okoliro esu amaku",
            "'Bara ni endre saa ka ba ga 'bara ni saa zi tisi imgbe / Ki Emmanuele ani ama tro / Le anidri amaru rii okoku",
            ],
        ),
    Hymn(
        id=20,
        number=20,
        title="Yesu Olaru 'Budri ga",
        verses=[
            "Yesu olaru budri ga, ma ari'dipi. / Ka o'du emure ri ute, Yesu ma Opi.",
            "CHORUS / 'Budri ga si onzira, mori o'ja mi ndejo ri tro / Ajugo vu mudri ni mi nde 'di ri'i, / Vu asejo 'ba ani dri ti tro tadru, / Onzira, onzira, / Halleluya Kristo onzira",
            "Ondreki ana gbolo isa, ma aridipi. / Onzi dra ga si ra, Yesu ma Opi.",
            "Dra ka oni ko kpe, ma aridipi. / Ondre dra ni mi ra, Yesu ma Opi",
            ],
        ),
    Hymn(
        id=21,
        number=21,
        title="Adi Nyera",
        verses=[
            "Bass: Adi nyera Yesu Kristo'a icandi / All: O, omgba ani, utu ani, / Onzi kuruce ndi gologota ga. / Bass: Okweki anini icandi retu ri. / All: O, osuki ocikwi ana dri ga, / Oduki ani oko epa ani kuruce dri.",
            "CHORUS / Omg'baki ani, oso ani ajusi, / U'daki ani, oga ki Ani imgbe / Ohwe ki ani ni laza lo'u ri i, / Ki Yesu azi ani amani cidru, / Ari anidri osure rii si, / Ari anidri ri oje ama pelere",
            "Bass: Ba cidru ogaki ani imgbe. / All: Cidru o'joki, “Endru amale / Baraba ni amadri ri ayu awu.” / Bass: Yesu oza u'duku ere rii si. / All: “Mata mata, nyi e'be a'ini ra, / Oniki ta k'podru kaki idea rii ku.”",
            "Bass: Ari Yesu dri osure rii, / All: oje vu ndutu enzi'a si, / Oko ari ama vu enzi dri'a si pi. / Bass: Yesu aziru amani isaa. / All: ohwe ani ilili ama enzi si / Azi anidri ri ka ru jeje k'pe.",
            ],
        ),
    Hymn(
        id=22,
        number=22,
        title="Bacidru vudri dia ri",
        verses=[
            "Bacidru vudri diari inzikira Rubanga andra ga, / madizi alusa enzia ako na iyo, / ki Yesu emu odra enzi amadri si, / dru dru ba kudra dru ku",
            "CHORUS / Rubanga.. memu nyidri enzi madri tro / nyebe mani, enzi madri nira, / ki nyekwe mani lidri au / adusiku enzia musara ni dra.",
            "Nyi enzi idele ri ori koko nyi ku, / Rubanga kaba ungwe enzi badri tro, / jo enzi na kolu ika aria nisa, / ani kemu kojea pelere",
            " Rubanga asi kaza ba nia enzi ideleri si, / anyi ba ebeki leti enzi dri ra, / adusiku jo oru enzi badri nira, / malaika bua ri sa karanzo",
            ],
        ),
    Hymn(
        id=23,
        number=23,
        title="Adi nyi Era Icandi Yesu dri",
        verses=[
            "Adi nyera ichandi Yesu dri, / Ichandri ru ama si, / Kuruce dri ama Opi ni epa, / Drudru amesu ovuka.",
            "CHORUS / (Yesu ni), Rubanga ohwe ama ni, / (Kayu ama), kayu ama opigo asi, / (Dri a endru), jo adri nyolu nyi endzi idre, / (Kesua), nyi ga Yesu'a azi imgbe / (Anyevu), aka anzo ru ki alu, / (A'dusi), Yesu ari ari ama ra.",
            "Dra ani dri ayu ama vu mudra asi, / Dria vu mudri'a nyi le a'duta? / Yesu Kristo ni ama ingwe 'i, / Ko'ba alu sa nyi cidri ku.",
            "Saa ni driadru saa zi andraga / 'bani iyo, Emujo Rubanga drii, / Ovi 'baku ka 'ba ndre ovi ru vi / Jo nyolu enzi 'dipi sa'i",
            ],
        ),
    Hymn(
        id=24,
        number=24,
        title="Nya Mi kolu Mg'bo",
        verses=[
            "Nya mi kolu mgbo saa ni ire, / Nya mi kolu mgbo endru, / Drudru vu 'di koza nyi kuu-u, / Kristo'ba ilegi oko o'du kuu, / Mi kolu mgbo ru iza awi ako, / Mi kolu mg'bo o'ja rezi okpo, / Mi kolu mgbo izi 'dipi ke-mu, / Nyi ute ikalaru ku",
            "CHORUS Anyi ute i-legi tro (x2) / Vu mudri'a anya mi kolu mgbwo, / Itu'a si saa, kristo'ba a nya mi kolu mgbwo.",
            "Nyi dro o'du nya mi ga si pii, / Nyi dro dri 'a ru cika pi, / Lidri tadru ri nyi dri-ii, / Kristo'ba illegi oko'du ku, / Anya aridi'pi ka anyi, undre paka mindra, / Ru lo'u dri era mi aru si, ari ani dri ora amasi.",
            "Nyi'du Yesu ni igeni tro, Nyindre o'ja rezi (ni) ire, / Nyi ko nya o'ja kwe ok'po, nyi ute nya Opi kefu, / Dia jo itu ni oru, ikalaru ku, / Saa 'badri di'iga nyindre, / Kristo 'ba ute illegi tro",
            ],
        ),
    Hymn(
        id=25,
        number=25,
        title="Paulo ti sila tro",
        verses=[
            " Paulo ti sila tro, aia vure jo lemu dria ri, / esu zangwa zi alu ori unzi ri tro / Vua ka ta andra ga ri ndre waa dri, / ilegi aia zile ori unzire dro jo ri, osu ai dru mabusu a.",
            "CHORUS / Icandia si sa, ongo longo, vua anzo sia, ongo longo. / Adusi ta iba dri, 'ba idele kpe ri sa kole epe longo si",
            "Rubanga ide nyuma, retugo ri mambusu joti awiru mgwo, / asikari ta utere dia si omvu pi. / Paulo ti ojo nya asiti komuvuru ki, / Rubanga ama rule ri, ani tesa ama tro, vua olu ka ama tra mba.",
            "Kristo 'ba anyi mba okpo, a'i badri kendre / Paulo ti dri ri ani. Longo 'ba ngole ri, mori / Rubanga dri si, 'bani apajo wa mabusu ichandri dri di a si, / jo azi asi amadri cidru ani dri, vua 'ba ka remu a'i tro bu'a",
            ],
        ),
    Hymn(
        id=26,
        number=26,
        title=" Tazi vudri ga dia",
        verses=[
            "Tazi vudri ga 'di'a, mesu kuru, / illegi ani ma'di ka ru izu dru Rubanga tro, / Jo nyi le ta izule ani ilili. / Sa cidru si nye 'bua wa",
            "CHORUS / Saa cidru si olu ru izure ama Opi Muleke tro, / Adusi ani ama tro jo ama icandi'a ebe ama ku dri cire ga, / Olu ani tro illegi si ko'ba 'ba ni asi kolu eg'bwe Saa cidru si",
            "Kendre Yesu'a'joka ri ani, mata, / Ma ilegi ri kolu ki cidru alu / Drudru vu 'di koni nyeze ma nyi, / Dru dru kete ru nyi ma nia",
            "Madrupi, manvoti, sa ni dria dru, / Nyini nyi hwejo driadru Rubanga dri / Nyi awi nya asiti mgbo, nya ti tro mgbo / Nyi'jo ta nyalele ri ni",
            ],
        ),
    Hymn(
        id=27,
        number=27,
        title="Ari Mata'ura (Sabato) ",
        verses=[
            "Soprano: Ari ma ta ura, Sabato dri ga, Ani o'du ingo ri'i loku mesu ra. / Alto: Mata ura 2x Sabato dri 2x o'du ingori'i loku mesu ra. / Tena: Ari mata ura Sabato dri, ani o'du ingori 'i loku mesura. / Bass: Ari mata ura 2x Sabato dri ga ani o'du ingori'i ani o'du, loku mesura. ",
            "CHORUS / Sabato ni ani o'du oleri'is, / Kolu te 'bani ovujo, / Rubanga sa karuanzo Sabato si, / Ama'i sa kole ama ovudru. / Yesu ni, ani Opi Sabato dri / Karanzo Sabato si, / Ka amani dridre na hwe ni, / Sabato ni ani o'du ole ri'i",
            "'Ba ziti kura, Sabato ni ani, Itu rubanga'i, Ki ani itu azia 'i / Alto: Kaki urax2 itu rubanga ('i)x2 / Ki ani itu azia 'i / Tenor: 'Ba ziti kura, Sabato ni, itu rubanga'i, Ki ani itu azia 'i / Bass: Kaki ura X2 Sabato ni itu rubanga, itu ru, ki ani itu azia 'i ",
            "Sabato ni alama, 'ba ole ri a alofo ga Rubanga ti tro, o'ba kolu ole / Alto: Ani alama 2x, ama lofo, Rubanga ti tro, O'ba kolu ole. / Tena: Ani alama ama lofo, Rubanga ti tro, O'ba kolu ole. / Bass: Ani alama 2x ama lofo ga, Rubanga ti tro, Ruba-nga, o'ba kolu ole",
            ],
        ),
    Hymn(
        id=28,
        number=28,
        title="Ani Ama Opi opi dri 'i",
        verses=[
            "Yesu ni kengwi ra vudri ga 'di'a / 'Ba anidri jire kare anidri'ga / Madrupi nyimba ingo saa ni ecara / (Rubanga ka nyi ari dru) X2 ",
            "CHORUS / (Ani) ama Opi, Opi opi dri'i / Ani ka ama dri se ni / Anyi 'ba ohweki laru anini / A'dusi ani lari 'dipi",
            "O'jo ma leti, anda vua lidri / Ma'di lidri le'di ri keko ma vu ni / Anda le'di ri komba ma cara / (A'dusi ka dride esu ra)X2",
            "Yesu ni ka 'ba ji ana ata dri 'bu'a / A'di olu anitro 'bo'bo dru / A'di kwe lidri dri ri nya anitro / (Ani kolu 'ba ni Opi 'i)X2",
            ],
        ),
    Hymn(
        id=29,
        number=29,
        title="Yesu O'jo ani Kengwi",
        verses=[
            "Yesu o'jo ani kengwi vudri 'dia idri / Ani kemu 'ba anidri ji ree / Oru 'bu'a ana ata dri / Olure ga anitro alu",
            "CHORUS / Yesu nyemu ama jire / Kare unzi 'di'a si pi / Amale oluka nyi tro alu / Kare loso nyidri ri ga",
            "Kristo 'ba odu endru di si ri / Anyi pi anyami cidru mgbo / Adusiku Sitani ni ama laga / Ole ani kemu 'ba unzare ",
            "'Ba cidru anyi ba ombaki dria okpo / A'i 'badri ri'ga / Anyi'ba oluki asi okpo tro / Yezu le kengwi soa dru ",
            ],
        ),
    Hymn(
        id=30,
        number=30,
        title="E'i Lolu Na'iga",
        verses=[
            "CHORUS / Rubanga koko emu, dridre Ani dri rii tro / Kemu kanzua ama ni, e'bu ama dri avuga si, / 'Disidru imbaru okpo ta loso idre ka tro / Drudru amevu ama dridre lidri dri esura",
            "E'i ama dri lolu naiga, iniaga ni laka iyo, / Tara itu kolu laka 'iyo, Rubanga ka amani ingwe hweni, / Leti e'i amadri lolu naiga, rii ani leti da'bu si ri'i / Amaci Yesu tro laka si, kesua, amasu lo'bu ingweri'i, / E'i amadri lolu naiga, vu na kodi kpo lei, lanyu, / Lidri amadri saa kemu kolu limi, limi, lanyu ni osa ani.",
            "Bilo 'bonzi e'bi tro ka ayise nya au, / Jaligo, idranzi tro saa kengwi kpoo yai, / Losi sa kemu kolu na'a iyo, / Ori ara ka sa kemu kolu na'a iyo, / U'duku owo dri, kolu naa iyo, / Amevu saa cidru si Ama ta gu au, / Abiri kemu, kolu na'a iyo, / Ma'dizi kemu ko'joa ani avu na iyo",
            ],
        ),
    Hymn(
        id=31,
        number=31,
        title="'Di ni Ma Ole 'i ",
        verses=[
            "Amari olure kpoo dru, enzi'a / Ki Yesu ni kiza oko ci, / Ari ama ra ari ani dri / Osu ra kuruce dri ama si",
            "CHORUS / 'Di, 'di ni ma ole 'i, / Ma'dizi alusa o'du ku, / A'dusi Yesu odra ma enzi si, / Mangwi vuleku, / 'Di 'di ni ma ole'i ma'dizi alusa o'du ku / Jo sa mgbe kolu ingoni, / Ma'i ra endru, mangwi vule ku.",
            "Kristo 'ba adri ora andrani, / Sitani umbe ama enzi'a, / Ki Yesu le ayu ama ingwi ama / Ingwe'a ata dri 'bo'bo dru",
            "Ori ki Rubanga ohwe eku ani ni / Saa le'jo alijori ecara, / Yesu le ka ranzo ama si / A'dusi ama anidri'i",
            ],
        ),
    Hymn(
        id=32,
        number=32,
        title="Ma Asiti Eg'bwera",
        verses=[
            "Jo o'du amadri ama utele rii eca ni, / Ama Yesu'adi osi ru'bu'a anzo tro, / Ki 'ba enzi 'ba ri'i le ka ru zu di, / Kaki ulu kaki ulu ori si",
            "CHORUS / (Ma asiti egbwe ra, egbwera) / Egbwera ma asiti egbwe lari madri si, / Jo 'ba enzi 'ba rii le ka ru zu saa, / Ma'i le manga malu Yesu dri",
            "O'du na kemu kolu amani a'ujo ri'i, / Ro-ozi amadri draka ra ri ti saa, / Amevu ama a'i ndre idri, / Ama ruzi a'i tro anjo si",
            "Jo 'ba enzi 'ba rii ondre ki eku Yesu dri ni, / Kaki lu ori si ru zure 'be'a, / Ki 'be saa konga kolu a'ini pi, / Ki amale amavu Yesu dri.",
            ],
        ),
    Hymn(
        id=33,
        number=33,
        title="Drimg'bo ",
        verses=[
            "Rubanga ohwe 'bani drimgbo ta kpo idre jo ra, / Ta kpo dru idrejo kendre nya upejo rii ani / Oko o'jo ta kpoo dru 'ba kidrea endru rii, / Ani kejia kpoo le'jo alire ga.",
            "CHORUS / Nyini ote ta kpoo dru endru nyemu nyidrea ri, / O'bu kemu ka nya ti ekoka ni ite'de ni, / Nyi emu nyi owo andani esu madu mani 'dii ku, Ki dria nyi oro 'jore ga esu druba mani ote.",
            "Rubanga ohwe 'bani e'bu cidru idele ra, / A'dusi a'i e'bu ako ri, ani ta kpo rii ani, / Ki 'ba zi ole ta hwele a'ini isa ri ku, / Ole ki ta a'ia vico alele rii au",
            "Kristo 'ba endru mbaka a'i ga okpo ri, / Icandi amgbu kemu kali bani andraga si, / Anyi'ba omi ki icandi omi ki asi egbwe si, / Drudru a'di evu a'di cupeo su dru ra",
            ],
        ),
    Hymn(
        id=34,
        number=34,
        title="Vu Juru dri'iga ",
        verses=[
            "Andrani ma olu re vu juru dri iga rii, / Ovuka mani 'iyo, vu juru dri'iga, / Ki Yesu eji ma vu juru dri iga si pi / Ejima kare ovu jo ri'iga",
            "CHORUS / Manzora (x3) Yesu, / Nya ma ejika vujuru dri iga si pi / Ma'joa (bye x10) vu juru dri ri ni",
            "Vu juru dri ri'iga laka na'a anzo iyo, / Saa cidru si owo, si cika tro au / Ki dria le ma'joa {bye x10} Vu juru dri rii ni.",
            "Kare madri ovu jori'iga, / Mari laka fia ma loso na eri, / Lidri ovi vu juru dri rii engwi idri ku / Driale mesu ovuka wiyo ra",
            ],
        ),
    Hymn(
        id=35,
        number=35,
        title="A'di Komu 'Ba ",
        verses=[
            "A'di komu 'ba madri ejire ni? / A'i ejire goro madri ri'iga? / A'ia mi ni a'bu ru ndi, a'i asiti oga ma imgbe, / Ma a'di ni ze au.",
            "CHORUS / (Ma 'di'a 'di x2) / Opi nyi ze ma awu, vu angwe na'iga 'ba nyidri ri tii ejire / Opi nyi ze ma awu",
            "Anyi vu anyi ni vu ndutu drii, / Anyi hwe a'i ni batisimu, / Ru ata dri si, ngwapi dri si endri Ole ri dri tro / Ki molu anyi tro alu",
            "Jo nyi ta 'jo malaika dri ani kpe, / Jo nyi ta nze Paulo dri ani kpe, / Nyi te'de le Yesu dri, nya'i 'ba lari yesu dri iga, / Nyi 'jo odra 'ba cidru ni.",
            ],
        ),
    Hymn(
        id=35,
        number=35,
        title="Tazi alusa Ori le Endru.",
        verses=[
            "Tazi alusa Ori le endru iyo, / Rubanga ni ama Opi, azi ana ru amasi, / Yesu nyi Opi loku ama dri'i / Nyeze nya konyi amani",
            "CHORUS / Amale oluka kare aluga....a, / Nyaru ecu le saa cidru si, / Yesu nyi emu ama kare aluga / Drudru ama dri okoci ama vu alu dru, / Ma'dizi asire vulega kolu iyo / Drudru ama ru ungwe 'ba ciri aci dri'i",
            "Nyi enzi 'dipi nyiru nya enzi ni, / Yezu ni adri ka nyi ute, kiza anidri nzagodru, / Ki jo ote k'pe ka joti a'bu ci, / Nyemu nyolu ingoni?",
            "Yesu kolu anzo ga, Jo nye ngwi ni, / Yezu ko'joa nyini, nyi bara madri egwere rii, / Oko ka nyi ingwi goro anidri ga / Olure 'bo'bo dru ani tro",
            ],
        ),
    Hymn(
        id=36,
        number=36,
        title="Ama Recu Opi amadri",
        verses=[
            "Ama recu Opi amadri Yesu si, / A'dusi ani amg'bugodru amg'bugodru ambamba / Vu nya ndre le 'dii sa obiru ana rusi, / Jo ani ku tazi idri iyo ka rubi wana iyo.",
            "CHORUS / Ama recu Opi ama dri yesu si, / A'du si ani amgbugodru amgbugodru ambamba, / 'Be nya ndrele amgbugodru na ti saa, / Yesu Kristo ni amgbugodru oza 'be na ti saa raa, / Ru ani dri si Sitani kowo vuru, / A'dusi ani amgbugodru, amgbugodru ambamba.",
            "'Ba mi ako ri Yesu awi a'ia mira, / Pa ako ri sa kaki aci, Lazaro sa onzi ra, / 'Ba dro'bo tro, izi nguru tro ri sa, / Ija a'i ra oko aci meri dri si saa ra.",
            "Sitani saa o'ba ama ani amgbugodru, / Ka 'ba unza 'jore ga ani oza Yesu ni sa ra, / Ki jo Yesu emu omba ana andraga ni, / Sitani kendre gaangwadru, vundri ni ekwi saa nzani",
            ],
        ),
]
