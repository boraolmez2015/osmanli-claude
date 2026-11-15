# -*- coding: utf-8 -*-
# Bilingual script. Each chapter: id, target seconds, title TR/EN, narration lines [(tr, en)], visuals.
# visuals: list of image keys (stills) plus one clip key; prompts live in PROMPTS.

STYLE = (" Hyperrealistic cinematic photograph, shot on 35mm anamorphic lens, natural film grain, "
         "historically accurate 15th century, dramatic volumetric light, highly detailed textures, "
         "no text, no letters, no watermark.")

CHAPTERS = [
 dict(id="c00", sec=48, tr="1453", en="1453", lines=[
  ("Yıl bin dört yüz elli üç. Bahar sabahı, Boğaz'ın üzerinde sis var.",
   "The year is fourteen fifty-three. A spring morning, and mist lies over the Bosphorus."),
  ("Sisin ardında, bin yılı aşkın süredir ayakta duran bir şehir uyanıyor: Konstantinopolis.",
   "Behind the mist, a city that has stood for more than a thousand years is waking: Constantinople."),
  ("Elli üç gün sonra bu şehir artık eskisi gibi olmayacak. Ve dünya tarihi yeni bir sayfa açacak.",
   "In fifty-three days, this city will never be the same. And world history will turn a new page."),
 ], stills=["c00a","c00b","c00c"], clip="v00"),

 dict(id="c01", sec=60, tr="Bizans'ın Son Kalesi", en="The Last Fortress of Byzantium", lines=[
  ("Konstantinopolis, Roma İmparatoru Konstantin tarafından üç yüz otuz yılında başkent yapıldı.",
   "Constantinople was made a capital by the Roman Emperor Constantine in the year three hundred and thirty."),
  ("Yüzyıllar boyunca dünyanın en zengin, en kalabalık şehirlerinden biri oldu.",
   "For centuries it was one of the richest and most populous cities in the world."),
  ("Ama bin dört yüz elli üçe gelindiğinde, koca imparatorluktan geriye neredeyse yalnızca şehrin kendisi kalmıştı.",
   "But by fourteen fifty-three, almost nothing remained of the great empire except the city itself."),
  ("Onu koruyan şey ise efsanevi kara surlarıydı. Üç katlı savunma hattı, binlerce yıl düşmanlarını geri püskürtmüştü.",
   "What protected it were the legendary land walls. A triple line of defense that had turned back enemies for a thousand years."),
  ("Haliç'in ağzına ise devasa bir zincir gerilmişti. Hiçbir gemi içeri giremeyecekti.",
   "And across the mouth of the Golden Horn, a massive chain was stretched. No ship would get inside."),
 ], stills=["c01a","c01b","c01c","c01d"], clip="v01"),

 dict(id="c02", sec=60, tr="Genç Sultan", en="The Young Sultan", lines=[
  ("Edirne'de, genç bir sultan bu şehrin hayalini kuruyordu: İkinci Mehmed.",
   "In Edirne, a young sultan dreamed of this city: Mehmed the Second."),
  ("Bin dört yüz elli birde tahta çıktığında henüz on dokuz yaşındaydı.",
   "When he took the throne in fourteen fifty-one, he was only nineteen years old."),
  ("Birçok dil biliyor, haritalar inceliyor, mühendislik ve savaş sanatı üzerine çalışıyordu.",
   "He spoke several languages, studied maps, and devoted himself to engineering and the art of war."),
  ("Geceler boyunca surların planlarını çizdiği anlatılır. Tek bir hedefi vardı: Konstantinopolis'i almak.",
   "It is said he spent nights drawing plans of the walls. He had a single goal: to take Constantinople."),
 ], stills=["c02a","c02b","c02c","c02d"], clip="v02"),

 dict(id="c03", sec=56, tr="Boğazkesen", en="The Throat Cutter", lines=[
  ("İlk hamle bin dört yüz elli iki baharında geldi.",
   "The first move came in the spring of fourteen fifty-two."),
  ("Boğaz'ın en dar noktasında, Anadolu Hisarı'nın tam karşısında, devasa bir kale yükselmeye başladı: Rumeli Hisarı.",
   "At the narrowest point of the Bosphorus, directly across from the Anatolian Fortress, a huge castle began to rise: Rumeli Hisarı."),
  ("Binlerce işçi gece gündüz çalıştı. Kale yaklaşık dört buçuk ayda tamamlandı.",
   "Thousands of workers labored day and night. The fortress was finished in about four and a half months."),
  ("Artık Karadeniz'den şehre yardım gelmesi çok zordu. Halk ona bir isim verdi: Boğazkesen.",
   "Now help from the Black Sea could hardly reach the city. People gave it a name: the Throat Cutter."),
 ], stills=["c03a","c03b","c03c","c03d"], clip="v03"),

 dict(id="c04", sec=60, tr="Dev Toplar", en="The Great Bombards", lines=[
  ("Sultan'ın en büyük silahı ise henüz görülmemiş bir şeydi.",
   "But the Sultan's greatest weapon was something never seen before."),
  ("Urban adında bir top dökümcüsü, Edirne'de devasa toplar döktü.",
   "A cannon founder named Urban cast enormous guns in Edirne."),
  ("En büyüğü yüzlerce kiloluk taş gülleler fırlatabiliyordu. Onu taşımak için düzinelerce öküz ve yüzlerce adam gerekti.",
   "The largest could hurl stone balls weighing hundreds of kilograms. Dozens of oxen and hundreds of men were needed to move it."),
  ("Günde yalnızca birkaç kez ateşlenebiliyordu. Ama her atışta yer sarsılıyor, surlar titriyordu.",
   "It could fire only a few times a day. But with every shot the ground shook and the walls trembled."),
 ], stills=["c04a","c04b","c04c","c04d"], clip="v04"),

 dict(id="c05", sec=64, tr="Kuşatma Başlıyor", en="The Siege Begins", lines=[
  ("Altı Nisan bin dört yüz elli üç. Osmanlı ordusu surların önünde.",
   "April sixth, fourteen fifty-three. The Ottoman army stands before the walls."),
  ("Tahminlere göre seksen binden fazla asker, ufka kadar uzanan çadırlar.",
   "By most estimates more than eighty thousand soldiers, and tents stretching to the horizon."),
  ("Karşılarında ise yalnızca yedi bin kadar savunucu vardı.",
   "Facing them were only about seven thousand defenders."),
  ("Onları son Bizans İmparatoru, On Birinci Konstantin yönetiyordu. Yanında Cenevizli komutan Giustiniani vardı.",
   "They were led by the last Byzantine Emperor, Constantine the Eleventh. At his side stood the Genoese commander Giustiniani."),
  ("Ve toplar konuşmaya başladı.",
   "And the cannons began to speak."),
 ], stills=["c05a","c05b","c05c","c05d"], clip="v05"),

 dict(id="c06", sec=60, tr="Ateş ve Deniz", en="Fire and Sea", lines=[
  ("Haftalar boyunca bombardıman hiç durmadı. Surlarda büyük gedikler açıldı.",
   "For weeks the bombardment never stopped. Great breaches opened in the walls."),
  ("Ama savunucular her gece yıkılan yerleri toprak, tahta ve taşla yeniden kapattı.",
   "But every night the defenders sealed the ruined sections again with earth, timber and stone."),
  ("Yirmi Nisan'da denizde büyük bir çarpışma oldu. Dört Hristiyan gemisi Osmanlı donanmasını yararak Haliç'e ulaştı.",
   "On April twentieth a great battle broke out at sea. Four Christian ships fought through the Ottoman fleet and reached the Golden Horn."),
  ("Sultan öfkeliydi. Yeni ve çok cesur bir plana ihtiyacı vardı.",
   "The Sultan was furious. He needed a new and very bold plan."),
 ], stills=["c06a","c06b","c06c","c06d"], clip="v06"),

 dict(id="c07", sec=66, tr="Gemiler Karadan", en="Ships Over Land", lines=[
  ("Yirmi iki Nisan sabahı, Haliç'teki savunucular gözlerine inanamadı.",
   "On the morning of April twenty-second, the defenders in the Golden Horn could not believe their eyes."),
  ("Osmanlı gemileri tepelerin üzerinden kayarak geliyordu.",
   "Ottoman ships were sliding down over the hills."),
  ("Gece boyunca yağlanmış kızaklar üzerinde, öküzler ve askerler tarafından çekilen gemiler, Galata'nın arkasından karadan Haliç'e indirilmişti.",
   "Through the night, on greased wooden rollers, pulled by oxen and soldiers, the ships had been carried over land behind Galata into the Golden Horn."),
  ("Zincir aşılmıştı. Şehir artık iki yandan kuşatılmıştı.",
   "The chain had been bypassed. Now the city was besieged from two sides."),
 ], stills=["c07a","c07b","c07c","c07d"], clip="v07"),

 dict(id="c08", sec=56, tr="Toprağın Altında", en="Beneath the Earth", lines=[
  ("Kuşatma toprağın altında da sürüyordu. Osmanlı lağımcıları surların altına tüneller kazdı.",
   "The siege went on underground as well. Ottoman sappers dug tunnels beneath the walls."),
  ("Savunucular karşı tüneller açtı. Karanlıkta, meşale ışığında çarpışmalar yaşandı.",
   "The defenders dug counter-tunnels. Battles were fought in the dark, by torchlight."),
  ("Mayıs'ın sonlarına doğru gökyüzünde bir ay tutulması görüldü. Şehirde pek çok kişi bunu kötüye yordu.",
   "Late in May, a lunar eclipse was seen in the sky. Many in the city took it as an evil omen."),
 ], stills=["c08a","c08b","c08c","c08d"], clip="v08"),

 dict(id="c09", sec=76, tr="Son Hücum", en="The Final Assault", lines=[
  ("Yirmi dokuz Mayıs, şafaktan önce. Davullar, borazanlar ve binlerce ses aynı anda yükseldi.",
   "May twenty-ninth, before dawn. Drums, trumpets and thousands of voices rose at once."),
  ("Hücum dalgalar halinde geldi. Önce ilk birlikler, sonra Anadolu askerleri surlara yüklendi.",
   "The assault came in waves. First the irregular troops, then the Anatolian soldiers threw themselves at the walls."),
  ("Savunucular direndi. Ama sonra Giustiniani ağır yaralandı ve geri çekildi. Savunma sarsıldı.",
   "The defenders held. But then Giustiniani was badly wounded and withdrew. The defense began to waver."),
  ("Tam o anda Sultan son kozunu oynadı: Yeniçeriler.",
   "At that very moment, the Sultan played his final card: the Janissaries."),
  ("Disiplinli, sessiz ve kararlı bir şekilde gediklere doğru ilerlediler.",
   "Disciplined, silent and determined, they advanced toward the breaches."),
 ], stills=["c09a","c09b","c09c","c09d","c09e"], clip="v09"),

 dict(id="c10", sec=56, tr="Ulubatlı Hasan", en="Hasan of Ulubat", lines=[
  ("Bu kargaşanın ortasında, dev cüsseli bir yeniçeri surlara tırmandı: Ulubatlı Hasan.",
   "In the middle of the chaos, a giant Janissary climbed the walls: Hasan of Ulubat."),
  ("Oklar ve taşlar altında, sancağı burçlardan birine dikti.",
   "Under arrows and stones, he planted the banner on one of the towers."),
  ("Anlatılara göre Hasan oracıkta şehit düştü. Ama sancak dalgalanıyordu, ve onu gören binlerce asker içeri aktı.",
   "According to the stories, Hasan fell there as a martyr. But the banner was flying, and thousands of soldiers who saw it poured inside."),
 ], stills=["c10a","c10b","c10c","c10d"], clip="v10"),

 dict(id="c11", sec=64, tr="Fatih", en="The Conqueror", lines=[
  ("Son Bizans İmparatoru, askerlerinin arasında savaşarak hayatını kaybetti. Bin yıllık imparatorluk sona ermişti.",
   "The last Byzantine Emperor died fighting among his soldiers. A thousand-year empire had come to an end."),
  ("Öğleden sonra yirmi bir yaşındaki Sultan, beyaz atının üzerinde şehre girdi.",
   "In the afternoon the twenty-one-year-old Sultan rode into the city on his white horse."),
  ("Doğruca Ayasofya'ya gitti. Devasa kubbenin altında durdu ve sessizce etrafına baktı.",
   "He went straight to Hagia Sophia. He stood beneath the vast dome and looked around in silence."),
  ("O günden sonra ona bir isim verildi: Fatih. Yani, Fetheden.",
   "From that day on, he was given a name: Fatih. The Conqueror."),
 ], stills=["c11a","c11b","c11c","c11d"], clip="v11"),

 dict(id="c12", sec=60, tr="Yeni Bir Çağ", en="A New Age", lines=[
  ("İstanbul, Osmanlı İmparatorluğu'nun yeni başkenti oldu ve yüzyıllar boyunca öyle kaldı.",
   "Istanbul became the new capital of the Ottoman Empire, and remained so for centuries."),
  ("Pek çok tarihçiye göre bu fetih Orta Çağ'ı kapattı, Yeni Çağ'ı başlattı.",
   "For many historians, this conquest closed the Middle Ages and opened the modern era."),
  ("İki kıtanın buluştuğu bu şehir, bugün hâlâ dünyanın kalbinde atıyor.",
   "Where two continents meet, this city still beats at the heart of the world."),
  ("Bin dört yüz elli üç. Bir şehrin, bir imparatorluğun ve bir çağın hikâyesi.",
   "Fourteen fifty-three. The story of a city, an empire, and an age."),
 ], stills=["c12a","c12b","c12c","c12d"], clip="v12"),
]

PROMPTS = {
 # c00 intro
 "c00a": "Aerial drone view at dawn over the Bosphorus strait in 1453, thick mist on the water, the medieval walled city of Constantinople with the great dome of Hagia Sophia as a Byzantine church with NO minarets and no mosques anywhere, silhouetted on the horizon, wooden sailing ships, golden sunrise light.",
 "c00b": "Low angle view of the massive medieval Theodosian land walls of Constantinople in early morning fog, triple line of stone walls with brick bands and square towers, moat in front, soft cold light.",
 "c00c": "A lone Byzantine soldier in lamellar armor standing on a battlement at sunrise looking over a misty plain, red cloak blowing in the wind, seen from behind, Constantinople 1453.",
 # c01
 "c01a": "Panoramic view of medieval Constantinople in 1453 from the sea, Hagia Sophia as a Byzantine Christian church with its enormous dome and absolutely no minarets, no mosques in the city, red tiled roofs, harbor with wooden ships, warm afternoon sunlight.",
 "c01b": "Interior of Hagia Sophia in 1453 as a Byzantine cathedral, golden mosaics, rays of light coming through windows under the giant dome, incense smoke, candles.",
 "c01c": "Close detail of the Theodosian walls of Constantinople, weathered limestone and red brick bands, a tower with arrow slits, Byzantine guards patrolling, overcast dramatic sky.",
 "c01d": "A massive iron chain stretched across the Golden Horn harbor of Constantinople supported by wooden floats, medieval ships behind it, Galata tower in the distance, misty morning.",
 # c02
 "c02a": "Portrait of a young Ottoman sultan around 19 years old in 1451, thin beard, white turban with a jewel, rich red and gold kaftan, intense determined gaze, candlelit palace interior in Edirne, painterly chiaroscuro lighting.",
 "c02b": "An Ottoman palace chamber at night in Edirne, a young sultan leaning over a large table covered with hand drawn maps and plans of city walls, oil lamps, scrolls and compass instruments.",
 "c02c": "Close up of hands holding a quill drawing a plan of medieval city walls on parchment, ink, candle light, Ottoman calligraphy tools on the table.",
 "c02d": "Exterior of the 15th century Ottoman Old Palace in Edirne at dusk, Ottoman architecture with lead-covered domes, stone and brick walls, arched porticoes and courtyards, Janissary guards with tall white felt hats, warm lantern light, purple sky.",
 # c03
 "c03a": "Construction of Rumeli Hisarı fortress on the shore of the Bosphorus in 1452, thousands of workers carrying stones, wooden scaffolding, tall round towers rising, dusty sunlight.",
 "c03b": "Aerial view of the newly completed Rumeli Hisarı fortress on the European shore of the narrow Bosphorus, Anatolian fortress on the opposite shore, green hills, blue water, 1452.",
 "c03c": "Ottoman cannons on the walls of Rumeli Hisarı fortress aimed at the Bosphorus, gunners in kaftans, a Venetian ship sailing on the strait, smoke.",
 "c03d": "Workers at night building a stone fortress tower by torchlight, ropes and pulleys, sparks, sweat, medieval Ottoman construction site.",
 # c04
 "c04a": "A medieval cannon foundry in Edirne 1452, molten bronze pouring into a huge clay mold, glowing orange sparks, workers with leather aprons, smoke and heat haze.",
 "c04b": "An enormous bronze medieval bombard cannon, about eight meters long, resting on a wooden sledge, Ottoman soldiers standing beside it for scale, overcast sky.",
 "c04c": "Dozens of oxen and hundreds of men pulling a gigantic bronze cannon on a wooden cart along a muddy road through Thrace, dust, ropes, low sun.",
 "c04d": "Huge round stone cannonballs stacked next to a giant medieval bombard, Ottoman gunners preparing gunpowder, siege camp in the background.",
 # c05
 "c05a": "A vast Ottoman army camp in front of the Byzantine walls of Constantinople in April 1453, no minarets and no mosques in the city, thousands of colorful tents stretching to the horizon, banners, campfire smoke, aerial view at sunset.",
 "c05b": "Rows of Janissary soldiers in tall white felt hats and blue uniforms standing in formation, holding long weapons, dust in the air, Ottoman siege 1453.",
 "c05c": "Emperor Constantine XI Palaiologos as an older bearded man in gilded Byzantine armor and purple cloak on the walls, looking out at the enemy army, grim expression, overcast light.",
 "c05d": "A Genoese condottiere commander in polished Italian plate armor, Giovanni Giustiniani, standing with soldiers behind a wooden palisade on the walls of Constantinople, crossbowmen.",
 # c06
 "c06a": "A giant medieval bombard firing at the walls of Constantinople, huge burst of flame and white smoke, stone fragments flying from the wall, dramatic moment frozen.",
 "c06b": "A breach in the massive Theodosian walls after cannon fire, collapsed stones and dust, defenders at night repairing it with earth, barrels and wooden beams by torchlight.",
 "c06c": "Naval battle on the Sea of Marmara in April 1453, tall Genoese sailing ships surrounded by many smaller Ottoman galleys with oars, arrows, smoke, rough waves, golden light.",
 "c06d": "Close up of a sweating Byzantine defender on a ruined wall at night, face lit by fire, helmet dented, smoke behind.",
 # c07
 "c07a": "Ottoman galleys being pulled over a green hill on greased wooden rollers by oxen and soldiers at night, torches, ropes, sails furled, Galata hills, 1453.",
 "c07b": "Wide view at dawn of dozens of wooden Ottoman ships sliding down a hillside toward the Golden Horn on wooden tracks, mist, crowd of workers.",
 "c07c": "Byzantine soldiers on a harbor wall at dawn staring in shock at Ottoman ships entering the Golden Horn from the hills, back view, mist.",
 "c07d": "Ottoman fleet anchored inside the Golden Horn in front of the Byzantine sea walls of Constantinople, Byzantine churches with domes and no minarets or mosques in the city, morning light, flags, reflections on calm water.",
 # c08
 "c08a": "Ottoman sappers digging a narrow tunnel under a city wall by oil lamp light, wooden supports, dirt, sweat, claustrophobic, 1453.",
 "c08b": "Two groups of medieval soldiers clashing in a dark underground tunnel lit only by a torch, smoke, shadows, swords.",
 "c08c": "A blood red lunar eclipse rising over the domes and walls of Constantinople at night, people on rooftops looking up in fear, 1453.",
 "c08d": "A Byzantine religious procession at night carrying an icon through narrow streets of Constantinople, candles, worried faces, fog.",
 # c09
 "c09a": "Pre dawn final assault on the walls of Constantinople on 29 May 1453, thousands of Ottoman soldiers with ladders rushing toward the walls, torches, fire, smoke, wide aerial view.",
 "c09b": "Ottoman military band with huge drums and long trumpets playing at night before battle, torchlight, dramatic.",
 "c09c": "A wounded Genoese commander in plate armor being carried away from the walls by his soldiers, smoke and fire behind, chaos, night.",
 "c09d": "Janissaries in tall white hats advancing in disciplined silent ranks through smoke toward a breach in the walls at dawn, backlit by fire.",
 "c09e": "Close up of an Ottoman soldier's determined face covered in dust under a helmet, flames reflecting in his eyes, siege of Constantinople.",
 # c10
 "c10a": "A huge muscular Janissary warrior climbing the broken walls of Constantinople holding a large red banner, arrows flying around him, smoke, low angle, heroic, dawn.",
 "c10b": "A plain solid red Ottoman war banner without any symbols, no crescent and no star, planted on top of a stone tower of the walls of Constantinople, waving in the wind, smoke and sunrise behind.",
 "c10c": "Thousands of Ottoman soldiers pouring through a breach in the walls of Constantinople at sunrise, dust and light rays.",
 "c10d": "A fallen Janissary warrior lying at the foot of a red banner on the walls, arrows around, soft morning light, solemn.",
 # c11
 "c11a": "A broken Byzantine double headed eagle banner lying on the ground among stones and smoke on the walls of Constantinople, morning light, symbolic end.",
 "c11b": "Sultan Mehmed II, 21 years old, riding a white horse through the gate of Constantinople, surrounded by Janissaries, afternoon sun, dust, majestic procession.",
 "c11c": "A young Ottoman sultan standing alone beneath the giant dome of Hagia Sophia, rays of light falling through windows, golden mosaics, awe, silence.",
 "c11d": "Exterior of Hagia Sophia in 1453 at golden hour, the Byzantine church building without any minarets, Ottoman soldiers and horses in the square, calm after battle.",
 # c12
 "c12a": "Istanbul in the late 15th century under Ottoman rule, Hagia Sophia with a new minaret, busy port with ships, markets, golden sunset, wide aerial view.",
 "c12b": "A large old world map on parchment showing Europe and Asia meeting at Constantinople, candlelight, quill and compass, no readable text.",
 "c12c": "Modern Istanbul at blue hour aerial view, Bosphorus Bridge lights, Hagia Sophia and mosques silhouettes, ships, city lights.",
 "c12d": "The ruined old Theodosian walls of Istanbul today at sunset, grass growing between the stones, warm golden light, peaceful.",
}

# AI motion clip directions (Canva). Short visual descriptions for production spec.
CLIPS = {
 "v00": "Aerial drone flight at dawn gliding forward over the misty Bosphorus toward medieval Constantinople, the dome of Hagia Sophia emerging from the fog, wooden sailing ships drifting below.",
 "v01": "Byzantine guards in lamellar armor walk along the top of the massive stone land walls; the camera tracks beside them as wind moves their cloaks and banners.",
 "v02": "A young Ottoman sultan in a red kaftan and white turban leans over a candle-lit table of maps, then looks up slowly with determination; candle flames flicker.",
 "v03": "Thousands of workers haul stones up wooden ramps as a round stone fortress tower rises on the Bosphorus shore; dust drifts in sunlight; the camera cranes upward.",
 "v04": "Molten bronze pours from a furnace channel into a giant clay cannon mould; sparks burst; workers in leather aprons step back from the glow.",
 "v05": "A vast Ottoman army camp of tents before the city walls; banners flap in the wind and cavalry ride between tents; drone glides slowly over the camp at sunset.",
 "v06": "A giant bronze bombard fires at the stone walls: flame and thick white smoke burst from the muzzle, the gunners crouch, debris rises from the distant wall.",
 "v07": "At night, soldiers and oxen pull a wooden galley over a hill on greased log rollers by torchlight; the hull slides forward and ropes strain.",
 "v08": "Sappers dig in a narrow tunnel by oil lamp light; dirt falls from the ceiling; one man stops and listens to the wall.",
 "v09": "Before dawn, waves of soldiers with ladders charge across the ground toward burning walls; torches and smoke; drone flies low over them.",
 "v10": "A large Janissary climbs to the top of a broken tower and plants a red banner; the banner unfurls and waves in the wind against smoke and the rising sun.",
 "v11": "A young sultan on a white horse rides slowly through a stone city gate, Janissaries marching on both sides, dust glowing in afternoon sun.",
 "v12": "Drone flight over the Bosphorus at sunset toward Hagia Sophia and the historic peninsula, seagulls, ships, golden light on the water.",
}

# Extra narration lines: chapter -> list of (insert_after_index, tr, en)
EXTRA = {
 "c00": [(2, "Bu, dünyanın en güçlü surlarına karşı, genç bir sultanın hikâyesi.",
             "This is the story of a young sultan against the strongest walls in the world.")],
 "c01": [(1, "Doğu ile Batı'nın, Asya ile Avrupa'nın buluştuğu bu noktada, ticaret yolları kesişiyordu.",
             "Here, where East met West and Asia met Europe, the great trade routes crossed."),
         (4, "Şehir, bin yıl boyunca defalarca kuşatıldı. Ama surlar hiçbir zaman zorla aşılamamıştı.",
             "The city had been besieged again and again for a thousand years. But the walls had never been taken by storm.")],
 "c02": [(1, "Babası İkinci Murad'dan büyük bir devlet devralmıştı. Ama onun gözü daha büyüğündeydi.",
             "He had inherited a great state from his father, Murad the Second. But his eyes were set on something greater."),
         (3, "Avrupa'nın sarayları bu genç hükümdarı ciddiye almadı. Çok yakında pişman olacaklardı.",
             "The courts of Europe did not take this young ruler seriously. Very soon, they would regret it.")],
 "c03": [(3, "Boğaz'dan geçen gemiler artık durmak ve izin almak zorundaydı. Bu bir meydan okumaydı.",
             "Ships passing through the Bosphorus now had to stop and ask permission. It was a challenge."),
         (3, "Konstantinopolis'te imparator, Batı'ya mektuplar yazarak yardım istedi. Ama gelen yardım çok azdı.",
             "In Constantinople, the emperor wrote letters to the West, begging for help. But very little came.")],
 "c04": [(1, "Urban önce hizmetlerini Bizans'a sunmuştu. Ama imparator ona istediği ücreti ödeyemedi.",
             "Urban had first offered his services to Byzantium. But the emperor could not pay what he asked."),
         (3, "Bu toplar, savaşın kurallarını sonsuza dek değiştirecekti.",
             "These guns would change the rules of war forever.")],
 "c05": [(2, "Şehrin kara surları boyunca topçular, okçular ve piyadeler mevzilerini aldı.",
             "Along the land walls, gunners, archers and infantry took up their positions.")],
 "c06": [(1, "Yorgun savunucular uyumadan çalışıyordu. Her sabah Osmanlı topçuları yeniden başlıyordu.",
             "The exhausted defenders worked without sleep. And every morning, the Ottoman guns began again."),
         (3, "Bu küçük zafer şehirde büyük bir umut yarattı. Ama bu umut uzun sürmeyecekti.",
             "This small victory brought great hope to the city. But that hope would not last long.")],
 "c07": [(1, "Bu, tarihin en cesur askeri manevralarından biriydi.",
             "It was one of the boldest military maneuvers in history."),
         (3, "Savunucular artık Haliç tarafındaki deniz surlarını da korumak zorundaydı. Zaten az olan askerler daha da dağıldı.",
             "The defenders now had to guard the sea walls along the Golden Horn too. Their already few soldiers were stretched even thinner.")],
 "c08": [(1, "Bazı tüneller bulunup su ile basıldı, bazıları ateşe verildi.",
             "Some tunnels were found and flooded, others were set on fire."),
         (2, "Kuşatma yedinci haftasına girmişti. Her iki taraf da sonun yaklaştığını hissediyordu.",
             "The siege had entered its seventh week. Both sides could feel the end approaching."),
         (2, "Sultan, son bir büyük hücum için emir verdi.",
             "The Sultan gave the order for one last great assault.")],
 "c09": [(2, "Saatler boyunca surlarda ölüm kalım mücadelesi sürdü.",
             "For hours, a struggle of life and death raged on the walls.")],
 "c10": [(2, "Kısa süre içinde surların üzerinde birçok sancak belirdi. Savunma çöküyordu.",
             "Within moments, more banners appeared along the walls. The defense was collapsing.")],
 "c11": [(0, "Şehrin sokaklarında son direniş noktaları da birer birer düştü.",
             "In the streets of the city, the last points of resistance fell one by one.")],
 "c12": [(1, "Fatih Sultan Mehmed şehri yeniden imar etti, farklı halklara kapılarını açtı.",
             "Mehmed the Conqueror rebuilt the city and opened its doors to many peoples.")],
}

def full_lines(c):
    """Return list of (key, tr, en) in narrative order."""
    out=[(f"{c['id']}_{i}",t,e) for i,(t,e) in enumerate(c['lines'])]
    ex=EXTRA.get(c['id'],[])
    res=[]
    for i,item in enumerate(out):
        res.append(item)
        for j,(after,t,e) in enumerate(ex):
            if after==i: res.append((f"{c['id']}_x{j}",t,e))
    return res
