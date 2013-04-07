# -*- coding: utf-8 -*-
msg = {
	# Author: Xqt
	'en': {
		'redirect-broken-redirect-template': u'{{db-r1}}',
		'redirect-fix-broken-moved': u'Robot: Fixing broken redirect to moved target page %(to)s',
		'redirect-fix-double': u'Robot: Fixing double redirect to %(to)s',
		'redirect-fix-loop': u'Robot: Fixing redirect loop to %(to)s',
		'redirect-remove-broken': u'Robot: Redirect to a deleted or non-existent page',
		'redirect-remove-loop': u'Robot: Redirect target forms a redirect loop',
	},
	# Author: Csisc
	# Author: Lloffiwr
	# Author: Xqt
	# Author: ZxxZxxZ
	'qqq': {
		'redirect-fix-double': u'Edit summary when the bot fixes double redirects. <code>%(to)s</code> displays the new redirect target as a wiki link.',
		'redirect-remove-broken': u'Edit summary when the bot tags a deleted or non-existent page for speedy deletion. The message was designed for use on en:Wikipedia. The internal links are to pages on the English Wikipedia, [http://en.wikipedia.org/wiki/Wikipedia:CSD#G8 here] and [http://en.wikipedia.org/wiki/Wikipedia:Redirect here]. They won\'t work anywhere except on the English Wikipedia, as they stand.',
		'redirect-fix-broken-moved': u'Edit summary when the bot fixes a broken redirect to a moved page whose origin has been deleted. <code>%(to)s</code> displays the new redirect target as a wiki link.',
		'redirect-fix-loop': u'Edit summary when the bot fixes redirect loops. <code>%(to)s</code> displays the new redirect target as a wiki link.',
		'redirect-remove-loop': u'Edit summary when the bot tags a redirect loop for speedy deletion. The internal links are to pages on the English Wikipedia, [http://en.wikipedia.org/wiki/Wikipedia:CSD#G8 here] and [http://en.wikipedia.org/wiki/Wikipedia:Redirect here]. They won\'t work anywhere except on the English Wikipedia, as they stand.',
		'redirect-broken-redirect-template': u'Template for speedy deletion of broken redirect or redirect loops which the bot tags onto the redirect page. This message may contain additional informations like template parameters or reasons for the deletion request.\n\nNOTE: If this system message is not given for a language code, speedy deletion request by a bot is not supported on your site except there is a bot with sysop flag.\n\n{{doc-important|Only use your deletion template like <code><nowiki>{{delete}}</nowiki></code> which exist on your local project.}}',
	},
	# Author: Csisc
	'aeb': {
		'redirect-fix-double': u'بوت: تصليح تحويلة مزدوجة إلى %(to)s',
		'redirect-remove-broken': u'تحويلة إلى صفحة محذوفة أو غير موجودة',
		'redirect-fix-loop': u'روبوت: تعديل حلقة إعادة التوجيه إلى %(to)s',
		'redirect-remove-loop': u'هدف التحويلة يصنع عقدة تحويل: Robot',
		'redirect-broken-redirect-template': u'{{شطب|تحويلة مكسورة}}',
	},
	# Author: Naudefj
	# Author: Xqt
	'af': {
		'redirect-fix-double': u'Robot: dubbele aanstuur na %(to)s reggemaak',
		'redirect-remove-broken': u'Robot: Aanstuur na \'n geskrapte of nie-bestaande bladsy',
		'redirect-fix-loop': u'Robot: sirkulêre aanstuur na %(to)s reggemaak',
		'redirect-remove-loop': u'Robot: Aanstuur vorm \'n sirkulêre lus',
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: Als-Holder
	# Author: Xqt
	'als': {
		'redirect-fix-double': u'Bötli: Uflösig vun de doppleti Wyterleitig zue %(to)s',
		'redirect-remove-broken': u'Bötli: Wyterleitigsziil git s nit',
		'redirect-fix-loop': u' Bot: Wyterleitigschlupf uf %(to)s korrigiert',
		'redirect-remove-loop': u'Bot: Wyterleitig goht im ringrum',
		'redirect-broken-redirect-template': u'{{delete}}Wyterleitig wo kaputt isch',
	},
	# Author: DRIHEM
	# Author: Meno25
	'ar': {
		'redirect-fix-double': u'بوت: تصليح تحويلة مزدوجة إلى %(to)s',
		'redirect-remove-broken': u'روبوت: تحويلة إلى صفحة محذوفة أو غير موجودة',
		'redirect-fix-broken-moved': u'الروبوت: إصلاح إعادة التوجيه المعطل لصفحة الهدف المحركة %(to)s',
		'redirect-fix-loop': u'روبوت: تعديل حلقة إعادة التوجيه إلى %(to)s',
		'redirect-remove-loop': u'روبوت: هدف التحويلة يصنع عقدة تحويل',
		'redirect-broken-redirect-template': u'{{شطب|تحويلة مكسورة}}',
	},
	# Author: Jaminianurag
	'as': {
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: Esbardu
	# Author: Xqt
	# Author: Xuacu
	'ast': {
		'redirect-fix-double': u'Robó: Iguando la redireición doble a %(to)s',
		'redirect-remove-broken': u'[[WP:CSD#G8|G8]]: [[Wikipedia:Redirect|Redireición]] a una páxina desaniciada o que nun esiste',
		'redirect-fix-broken-moved': u'Bot: Arreglu de redireición frañada a la páxina de destín treslladada "%(to)s"',
		'redirect-fix-loop': u'Robó: Iguando la redireición cíclica a %(to)s',
		'redirect-remove-loop': u'Bot: El destín de la redireición forma un bucle de redireición',
		'redirect-broken-redirect-template': u'{{Destruir|La páxina a la que redirixe nun esiste|--~~~~}}',
	},
	# Author: AZISS
	# Author: Cekli829
	# Author: Ebrahimi-amir
	# Author: Khutuck
	'az': {
		'redirect-fix-double': u'Bot: İkiqat yönləndirmənin düzəldilməsi → %(to)s',
		'redirect-remove-broken': u'Bot: Silinmiş və ya mövcud olmayan səhifəyə yönləndirmə',
		'redirect-fix-broken-moved': u'Bot: İşləməyən yönləndirilmənin yeri dəyişdirilmiş hədəf səhifəyə %(to)s düzəldilməsi',
		'redirect-fix-loop': u'Bot:  Sonsuz yönləndirilmənin %(to)s düzəldilməsi',
		'redirect-remove-loop': u'Bot: Yönləndirilmə sonsuz yönləndirilmə formalaşdırır',
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: Amir a57
	# Author: E THP
	'azb': {
		'redirect-fix-double': u'روبات :%(to)s صحیفه‌سینه ایستیقامت‌لی ایکیقات ایستیقامتلندیرمه دوزلدیلیر',
		'redirect-remove-broken': u'[[ویکی‌پئدییا:سیل#یستیقامتلندیرمه|وپ:سیل]]: سیلینئن یا دا وار اولمایان صحیفه‌یه اولان ایستیقامیلندیرمه',
		'redirect-fix-loop': u'روبوت: فیخینگ اوزوک اولان%(to)s یؤنلن‌دیرن',
		'redirect-remove-loop': u'بوت: ایستیقامتلندیرمه هدفی بیر ایستیقامتلندیرمه دؤورو تشکیل ائدیر',
		'redirect-broken-redirect-template': u'{{سیل|y1}}',
	},
	# Author: Haqmar
	# Author: Sagan
	'ba': {
		'redirect-fix-double': u'Робот:  %(to)s битенә икеле йүнәлтеүҙе төҙәтеү',
		'redirect-remove-broken': u'Робот: булмаған йәки юйылған биткә йүнәлтеү',
		'redirect-fix-loop': u'Робот: %(to)s битенә йүнәлтеүҙе төҙәтеү',
		'redirect-remove-loop': u'Робот: бер ҡайҙа ла йүнәлтелмәгән',
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: Mucalexx
	# Author: Xqt
	'bar': {
		'redirect-fix-double': u'Bot: richtt dóppéde Weiderloattung auf %(to)s',
		'redirect-remove-broken': u'Bot: Weiderloattungszü gibts néd',
		'redirect-remove-loop': u'Bot: Weiderloattungszü auf sé söwer',
		'redirect-broken-redirect-template': u'{{Löschen|hinige Weiderloattung}}',
	},
	'bat-smg': {
		'redirect-fix-double': u'Robots: Taisuoms dvėgobs paradresavėms → %(to)s',
	},
	# Author: Stephensuleeman
	'bbc-latn': {
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: EugeneZelenko
	# Author: Jim-by
	# Author: Renessaince
	# Author: Zedlik
	'be-x-old': {
		'redirect-fix-double': u'Робат: выпраўленьне падвойнага перанакіраваньня → %(to)s',
		'redirect-remove-broken': u'Робат: мэта перанакіраваньня не існуе',
		'redirect-fix-broken-moved': u'Робат: Выпраўленьне перанакіраваньня на старонку, перанесеную ў %(to)s',
		'redirect-fix-loop': u'Робат: Выпраўленьне перанакіраваньня на %(to)s',
		'redirect-remove-loop': u'Робат: Пятля перанакіраваньняў',
		'redirect-broken-redirect-template': u'{{Выдаліць|некарэктнае перанакіраваньне}}',
	},
	# Author: DCLXVI
	'bg': {
		'redirect-fix-double': u'Робот: Поправяне на двойно пренасочване към %(to)s',
	},
	# Author: Riemogerz
	'bjn': {
		'redirect-fix-double': u'Robot: Pamasangan paugahan ganda ka %(to)s',
		'redirect-remove-broken': u'[[WP:CSD#G8|G8]]: [[Wikipedia:Redirect|Paalihan]] ka tungkaran nang dihapus atawa kada ada',
		'redirect-remove-loop': u'[[WP:CSD#G8|G8]]: Bidikan [[Wikipedia:Redirect|paalihan]] mahasilakan paalihan siklik',
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: Wikitanvir
	'bn': {
		'redirect-fix-double': u'বট: %(to)s-এ দ্বিপুনর্নির্দেশনা ঠিক করছে',
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: Fulup
	# Author: Gwenn-Ael
	# Author: Y-M D
	'br': {
		'redirect-fix-double': u'Kempennet adkas doubl gant robot → %(to)s',
		'redirect-remove-broken': u'Robot : Ar bajenn ma vezer adkaset n\'eus ket anezhi',
		'redirect-fix-broken-moved': u'Robot : O reizhañ an adkasoù torret war-zu ar bajenn bal %(to)s',
		'redirect-fix-loop': u'Robot : O kempenn al lagadenn adkas war-zu %(to)s',
		'redirect-remove-loop': u'Robot: Stumm ur c\'helc\'h-tro born zo gant an [[Wikipedia:Redirect|adkas]]',
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: CERminator
	# Author: Edinwiki
	# Author: Xqt
	'bs': {
		'redirect-fix-double': u'Bot: Popravlja dvostruka preusmjerenja na %(to)s',
		'redirect-remove-broken': u' [[WP:CSD#G8|G8]]: [[Wikipedia:Redirect|Preusmjerenje]] na obrisanu ili nepostojeću stranicu',
		'redirect-fix-broken-moved': u'Bot: Neispravno preusmjerenje prema premještenoj stranici %(to)s',
		'redirect-fix-loop': u'Robot: Popravlja petlje preusmjerenja na %(to)s',
		'redirect-remove-loop': u' [[WP:CSD#G8|G8]]: [[Wikipedia:Redirect|Preusmjerenje]] pravi petlju na samo sebe',
		'redirect-broken-redirect-template': u'{{Brisanje}}',
	},
	# Author: BroOk
	# Author: Grondin
	# Author: SMP
	# Author: Vriullop
	'ca': {
		'redirect-fix-double': u'Bot: Reparació de les redireccions dobles a %(to)s',
		'redirect-remove-broken': u'Bot: La pàgina a la qual redirecciona no existeix',
		'redirect-fix-broken-moved': u'Bot: Reparació de les redireccions trencades per moure-les a %(to)s',
		'redirect-fix-loop': u'Bot: arreglant redirecció en bucle per %(to)s',
		'redirect-remove-loop': u'Bot: El destí de la redirecció crea un bucle de redirecció',
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: Asoxor
	# Author: Calak
	# Author: Marmzok
	'ckb': {
		'redirect-fix-double': u'ڕۆبۆت: چاکسازیی دووجار-ڕەوانەکردنەوە بۆ %(to)s',
		'redirect-remove-broken': u'ڕۆبۆت: ڕەوانەکەر بۆ پەڕەیەکی سڕاوە یان پەڕەیەک کە بوونی نییە',
	},
	# Author: Dontlietome7
	# Author: JAn Dudík
	# Author: Jezevec
	# Author: Spiffyk
	# Author: Vks
	'cs': {
		'redirect-fix-double': u'Robot: Opravuji dvojité přesměrování na %(to)s',
		'redirect-remove-broken': u'Robot: Přerušené přesměrování',
		'redirect-fix-broken-moved': u'Robot: Oprava přerušeného přesměrování na přesunutou cílovou stránku %(to)s',
		'redirect-fix-loop': u'Robot: Oprava smyčky přesměrování na %(to)s',
		'redirect-remove-loop': u'Robot: Cíl přesměrování tvoří smyčku',
		'redirect-broken-redirect-template': u'{{smazat|přerušené přesměrování}}',
	},
	# Author: Lloffiwr
	# Author: Xqt
	# Author: Xxglennxx
	'cy': {
		'redirect-fix-double': u'Bot: Yn trwsio ailgyfeiriad dwbl i %(to)s',
		'redirect-remove-broken': u'Bot: Yn ailgyfeirio i dudalen a ddilëwyd neu nad yw ar gael',
		'redirect-remove-loop': u'Bot: Mae nod yr ailgyfeiriad yn ffurfio dolen ailgyfeirio',
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: Christian List
	# Author: Kaare
	# Author: Sarrus
	'da': {
		'redirect-fix-double': u'Robot: Retter dobbelt omdirigering til %(to)s',
		'redirect-remove-broken': u'Robot: Omdirigering til en slettet eller ikke-eksisterende side',
		'redirect-fix-broken-moved': u'Robot: Retter brudt omdirigering til flyttet målside %(to)s',
		'redirect-fix-loop': u'Robot: Retter omdirigeringsløkke til %(to)s',
		'redirect-remove-loop': u'Robot: Målet for omdirigeringen danner en omdirigeringsløkke',
		'redirect-broken-redirect-template': u'{{slet}}',
	},
	# Author: Geitost
	# Author: Metalhead64
	# Author: The Evil IP address
	'de': {
		'redirect-fix-double': u'Bot: Korrigiere doppelte Weiterleitung auf %(to)s',
		'redirect-remove-broken': u'Bot: Weiterleitungsziel existiert nicht',
		'redirect-fix-broken-moved': u'Bot: Korrigiere defekte Weiterleitung auf Verschiebeziel %(to)s',
		'redirect-fix-loop': u'Bot: Korrigiere Weiterleitungschleife auf %(to)s',
		'redirect-remove-loop': u'Bot: Weiterleitungsziel auf sich selbst',
		'redirect-broken-redirect-template': u'{{Löschen|Defekte Weiterleitung}}',
	},
	# Author: Eruedin
	'de-ch': {
		'redirect-fix-double': u'Bot: Korrigiere doppelte Weiterleitung auf %(to)s',
		'redirect-remove-broken': u'Bot: Weiterleitungsziel existiert nicht',
		'redirect-fix-broken-moved': u'Bot: Korrigiere defekte Weiterleitung auf verschobener Zielseite %(to)s',
		'redirect-fix-loop': u'Bot: Korrigiere Weiterleitungschleife auf %(to)s',
		'redirect-remove-loop': u'Bot: Weiterleitungsziel auf sich selbst',
		'redirect-broken-redirect-template': u'{{Löschen|Defekte Weiterleitung}}',
	},
	# Author: Erdemaslancan
	'diq': {
		'redirect-fix-double': u'Boti Tespitê hetanayışê dıleti heta %(to)s',
		'redirect-remove-broken': u'[[WP:CSD#G8|G8]]: [[Wikipedia:Redirect|Hetenayış]]: pela besternê yana pelaya cı nêasena',
		'redirect-fix-loop': u'Boti %(to)s rê hetanayışo dılet deke',
		'redirect-remove-loop': u'[[WP:CSD#G8|G8]]: [[Wikipedia:Redirect|Hetenayış]] re formê etiketi vıraşt.',
		'redirect-broken-redirect-template': u'{{bestere|m1}}',
	},
	# Author: Evropi
	# Author: Geraki
	# Author: Glavkos
	'el': {
		'redirect-fix-double': u'Ρομπότ: Διόρθωση διπλής ανακατεύθυνσης προς %(to)s',
		'redirect-remove-broken': u'Ρομπότ: Ανακατεύθυνση σε μια σελίδα διαγεγραμμένη  ή ανύπαρκτη',
		'redirect-fix-loop': u'Ρομπότ: Διόρθωση βρόχου ανακατεύθυνσης στο %(to)s',
		'redirect-remove-loop': u'Robot: Ανακατεύθυνση στόχου σχηματίζει έναν βρόγχο ανακατεύθυνσης',
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: Blahma
	# Author: Mihxil
	# Author: Objectivesea
	# Author: Xqt
	'eo': {
		'redirect-fix-double': u'Roboto: Riparas duoblan alidirekton al %(to)s',
		'redirect-remove-broken': u'Roboto: Alidirekto indikas forigitan aŭ neekzistantan paĝon',
		'redirect-fix-broken-moved': u'Roboto: Riparas rompitan alidirekton al movita celpaĝo %(to)s',
		'redirect-fix-loop': u'Roboto: Riparas ciklan alidirektilon al %(to)s',
		'redirect-remove-loop': u'Roboto: Alidirekta celas sin mem',
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: Armando-Martin
	# Author: Dferg
	# Author: Invadinado
	# Author: Vivaelcelta
	# Author: Xqt
	'es': {
		'redirect-fix-double': u'Bot: Arreglando doble redirección → %(to)s',
		'redirect-remove-broken': u'Bot: Redirige a una página borrada o que no existe',
		'redirect-fix-broken-moved': u'Bot: arreglo la redirección rota hacia la página de destino trasladada "%(to)s"',
		'redirect-fix-loop': u'Bot: Arreglando redirección infinita → %(to)s',
		'redirect-remove-loop': u'[[WP:CSD#G8|G8]]: El destino de la [[Wikipedia:Redirect|redirección]] crea un bucle de redirección',
		'redirect-broken-redirect-template': u'{{destruir|1=La página a la que redirige no existe|bot=~~~~}}',
	},
	# Author: Pikne
	'et': {
		'redirect-fix-double': u'Robot: parandatud kahekordne ümbersuunamine leheküljele %(to)s',
	},
	# Author: An13sa
	'eu': {
		'redirect-fix-double': u'Robota: Birzuzenketa bikoitza zuzentzen %(to)s -ra',
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: Ebraminio
	# Author: Huji
	# Author: Mjbmr
	# Author: Reza1615
	# Author: ZxxZxxZ
	# Author: جواد
	'fa': {
		'redirect-fix-double': u'ربات: اصلاح تغییرمسیر دوتایی به %(to)s',
		'redirect-remove-broken': u'ربات: تغییرمسیر به صفحهٔ ناموجود یا حذف‌شده',
		'redirect-fix-broken-moved': u'ربات:اصلاح تغییرمسیرهای خراب به صفحهٔ هدف %(to)s',
		'redirect-fix-loop': u'ربات: رفع حلقه در تغییرمسیر به %(to)s',
		'redirect-remove-loop': u'ربات: مقصد تغییرمسیر یک تغییرمسیر حلقه‌ای ایجاد می‌کند',
		'redirect-broken-redirect-template': u'{{حذف سریع|بن بست|bot=yes}}',
	},
	# Author: Crt
	# Author: Nedergard
	# Author: Nike
	# Author: Olli
	# Author: Silvonen
	'fi': {
		'redirect-fix-double': u'Botti korjasi kaksinkertaisen ohjauksen sivulle %(to)s',
		'redirect-remove-broken': u'Botti: Ohjaus poistetulle tai olemattomalle sivulle',
		'redirect-fix-broken-moved': u'Botti korjasi rikkinäisen ohjauksen siirrettyyn kohdesivuun %(to)s',
		'redirect-fix-loop': u'Botti korjasi ohjaussilmukan sivulle %(to)s',
		'redirect-remove-loop': u'Botti: Ohjauksen kohde muodostaa ohjaussilmukan',
		'redirect-broken-redirect-template': u'{{Delete}}',
	},
	# Author: EileenSanda
	'fo': {
		'redirect-fix-double': u'Bottur: Rættar dupulta umdirigering til %(to)s',
		'redirect-remove-broken': u'Bottur: Umstjórnan til eina strikaða síðu ella til eina síðu sum ikki er til',
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: Boniface
	# Author: Crochet.david
	# Author: Gomoko
	# Author: IAlex
	# Author: Od1n
	# Author: Xqt
	'fr': {
		'redirect-fix-double': u'Robot : répare une double redirection vers %(to)s',
		'redirect-remove-broken': u'[[WP:CSD#G8|G8]]: [[Wikipedia:Redirect|Redirection]] vers une page supprimée ou inexistante',
		'redirect-fix-broken-moved': u'Robot: Correction des redirections erronées vers une page cible %(to)s déplacée',
		'redirect-fix-loop': u'Robot : répare une boucle de redirection sur %(to)s',
		'redirect-remove-loop': u'Bot: la cible de la redirection forme une boucle de redirection',
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: ChrisPtDe
	# Author: Xqt
	'frp': {
		'redirect-fix-double': u'Robot : rèpâre na redirèccion dobla de vers %(to)s',
		'redirect-remove-broken': u'Robot : redirèccion de vers na pâge suprimâye ou ben pas ègzistenta',
		'redirect-fix-loop': u'Robot : rèpâre na boclla de redirèccion a %(to)s',
		'redirect-remove-loop': u'Robot : la ciba de la redirèccion fôrme na boclla de redirèccion',
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: Murma174
	'frr': {
		'redirect-fix-double': u'Bot: Ferbeedre dobelt widjerfeerang tu %(to)s',
		'redirect-remove-broken': u'Bot: Widjerfeerang tu en duad sidj.',
		'redirect-fix-broken-moved': u'Bot: Uunstaken widjerfeerang feert nü tu %(to)s',
		'redirect-fix-loop': u'Bot: Maaget widjerfeerangs-sleuf hial tu %(to)s',
		'redirect-remove-loop': u'Bot: Widjerfeerang üüb ham salew',
		'redirect-broken-redirect-template': u'{{Strik|Widjerfeerang uunstaken}}',
	},
	# Author: Klenje
	'fur': {
		'redirect-fix-double': u'Robot: o comedi un re-indreçament dopli a %(to)s',
	},
	# Author: Alison
	'ga': {
		'redirect-fix-double': u'Róbó: Ag socrú athsheolta dúbailte → %(to)s',
		'redirect-remove-broken': u'Róbó : Targaid athsheoladh ar iarraidh',
		'redirect-broken-redirect-template': u'{{scrios|Athsheoladh briste}}',
	},
	# Author: Toliño
	'gl': {
		'redirect-fix-double': u'Bot: Arranxo a redirección dobre cara a "%(to)s"',
		'redirect-remove-broken': u'Bot: Redirección cara a unha páxina eliminada ou en branco',
		'redirect-fix-broken-moved': u'Bot: Arranxo a redirección rota cara á páxina de destino trasladada "%(to)s"',
		'redirect-fix-loop': u'Bot: Arranxo a redirección en bucle cara a "%(to)s"',
		'redirect-remove-loop': u'Bot: O destino da redirección crea un bucle',
		'redirect-broken-redirect-template': u'{{delete}}',
	},
	# Author: Amire80
	# Author: YaronSh
	# Author: ערן
	'he': {
		'redirect-fix-double': u'בוט: מתקן הפניה כפולה → %(to)s',
		'redirect-remove-broken': u'רובוט: יעד ההפניה נמחק או שאינו קיים',
		'redirect-fix-broken-moved': u'רובוט: תיקון הפניה שבורה לדף היעד %(to)s, שהועבר',
		'redirect-fix-loop': u'בוט: תיקון הפניה מעגלית ל%(to)s',
		'redirect-remove-loop': u'רובוט: הפניה זו גורמת ללולאה אין־סופית של הפניות',
		'redirect-broken-redirect-template': u'הפניה ללא יעד',
	},
	# Author: Ex13
	'hr': {
		'redirect-fix-double': u'Bot: Popravak dvostrukih preusmjeravanja → %(to)s',
		'redirect-remove-broken': u'[[WP:CSD#G8|G8]]: [[Wikipedia:Redirect|Preusmjeravanje] na obrisanu ili nepostojeću stranicu',
		'redirect-remove-loop': u'[[WP:CSD#G8|G8]]: Cilj [[Wikipedia:Redirect|preusmjeravanja]] stvara petlju na sebe',
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: Michawiki
	'hsb': {
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: Bináris
	# Author: Dj
	'hu': {
		'redirect-fix-double': u'Bot: %(to)s lapra mutató dupla átirányítás javítása',
		'redirect-remove-broken': u'Bot: Törölt vagy nem létező lapra mutató átirányítás törlése',
		'redirect-fix-loop': u'Bot: Ide mutató átirányítási hurkok javítása: %(to)s',
		'redirect-remove-loop': u'Bot: körkörös átirányítás',
		'redirect-broken-redirect-template': u'{{azonnali|Hibás átirányítás}}',
	},
	# Author: Xelgen
	'hy': {
		'redirect-fix-double': u'Ռոբոտ․ Շտկվում են կրկնակի վերահղումները %(to)s -ին',
	},
	# Author: McDutchie
	# Author: Xqt
	'ia': {
		'redirect-fix-double': u'Robot: reparation de duple redirection → %(to)s',
		'redirect-remove-broken': u'Robot: Redirection a un pagina delite o non existente',
		'redirect-fix-broken-moved': u'Robot: Repara un redirection rupte verso un pagina renominate: %(to)s',
		'redirect-fix-loop': u'Robot: Repara redirection circular a %(to)s',
		'redirect-remove-loop': u'Robot: Le destination del redirection forma un circulo de redirectiones',
		'redirect-broken-redirect-template': u'{{eliminar|Redirection a un pagina delite o non existente}}',
	},
	# Author: Farras
	# Author: IvanLanin
	'id': {
		'redirect-fix-double': u'Bot: Memperbaiki pengalihan ganda ke %(to)s',
		'redirect-remove-broken': u'Robot: Pengalihan ke halaman yang dihapus atau tidak ada',
		'redirect-fix-loop': u'Robot: Memperbaiki pengalihan ganda ke %(to)s',
		'redirect-remove-loop': u'Robot: Target pengalihan menghasilkan pengalihan siklik',
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: Renan
	'ie': {
		'redirect-fix-double': u'Machine: Fixant redirection duplic por %(to)s',
		'redirect-remove-broken': u'[[WP:CSD#G8|G8]]: [[Wikipedia:Redirect|Redirect]] por un págine deletet o non-existent',
		'redirect-remove-loop': u'[[WP:CSD#G8|G8]]: [[Wikipedia:Redirect|Redirection]] cible forma un lace de redirection',
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: Ukabia
	'ig': {
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: Lam-ang
	'ilo': {
		'redirect-fix-double': u'Robot: Agsimsimpa ti doble a baw-ing idiay %(to)s',
		'redirect-remove-broken': u'Robot: Baw-ing a mapan ti naikkat wenno awan a panid',
		'redirect-remove-loop': u'Robot: Ti baw-ing a puntaan ket agporma baw-ing a silo',
		'redirect-broken-redirect-template': u'{{delete}}',
	},
	# Author: Snævar
	'is': {
		'redirect-fix-double': u'Vélmenni: Lagfæri tvöfalda tilvísun → %(to)s',
		'redirect-remove-broken': u'Vélmenni: Tilvísun bendir á síðu sem hefur verið eytt eða er ekki til',
		'redirect-fix-loop': u'Vélmenni: Lagfæri tilvísunar lykkju → %(to)s',
		'redirect-remove-loop': u'Vélmenni: Tilvísun bendir á óendanlega tilvísunar lykkju',
		'redirect-broken-redirect-template': u'{{eyða|tilvísun á síðu sem er ekki til}}',
	},
	# Author: Beta16
	# Author: Nemo bis
	# Author: Rippitippi
	# Author: Ximo17
	'it': {
		'redirect-fix-double': u'Bot: Sistemo i redirect doppi a %(to)s',
		'redirect-remove-broken': u'Bot: Redirect a una pagina inesistente',
		'redirect-fix-broken-moved': u'Bot: Correggo redirect errati alla pagina spostata %(to)s',
		'redirect-fix-loop': u'Bot: Preparazione di un ciclo di reindirizzo a %(to)s',
		'redirect-remove-loop': u'Bot: La destinazione del [[{{ns:project}}:Redirect|redirect]] rimanda alla pagina di partenza',
		'redirect-broken-redirect-template': u'{{Cancella subito|9}}',
	},
	# Author: Shirayuki
	# Author: 赤の旋律
	'ja': {
		'redirect-fix-double': u'ロボットによる: 二重リダイレクト修正 → %(to)s',
		'redirect-remove-broken': u'ロボットによる: 削除済みまたは存在しないページへのリダイレクト',
		'redirect-fix-broken-moved': u'ロボットによる: 迷子のリダイレクトのリダイレクト先を %(to)s に修正',
		'redirect-fix-loop': u'ロボットによる: リダイレクトのループの修正 → %(to)s',
		'redirect-remove-loop': u'ロボットによる: リダイレクト先にあるリダイレクトのループを修正',
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: NoiX180
	'jv': {
		'redirect-fix-double': u'Bot: Mbenakaké rong pralihan nèng %(to)s',
		'redirect-remove-broken': u'Bot: Ngalihaké nèng kaca sing ora ana utawa wis kabusak',
		'redirect-fix-loop': u'Bot: Mbenakaké ubengan pangalihan nèng %(to)s',
		'redirect-remove-loop': u'Bot: Patujon pangalihan dadi ubengan pangalihan',
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: David1010
	'ka': {
		'redirect-fix-double': u'რობოტი: ორმაგი გადამისამართების გასწორება → %(to)s',
		'redirect-remove-broken': u'რობოტი: გადამისამართება წაშლილ ან არარსებულ გვერდზე',
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	'kk': {
		'redirect-fix-double': u'Бот: Шынжырлы айдатуды түзетті → %(to)s',
		'redirect-remove-broken': u'Бот: Айдату нысанасы жоқ болды',
	},
	# Author: Cwt96
	# Author: 아라
	'ko': {
		'redirect-fix-double': u'로봇: %(to)s(으)로 이중 넘겨주기 고침',
		'redirect-remove-broken': u'로봇: 끊긴 넘겨주기',
		'redirect-fix-broken-moved': u'로봇: %(to)s(으)로 이동한 대상 문서로 끊긴 넘겨주기 고침',
		'redirect-fix-loop': u'로봇: %(to)s(으)로 재귀적인 넘겨주기 고침',
		'redirect-remove-loop': u'로봇: 넘겨주기 대상이 재귀적인 넘겨주기로 생김',
		'redirect-broken-redirect-template': u'{{ㅅ}}',
	},
	# Author: Purodha
	'ksh': {
		'redirect-fix-double': u'Bot: [[Special:Doubleredirects|Dubbel Ömlëijdong]] fottjemaat → %(to)s',
		'redirect-remove-broken': u'Bot: Di Ömlëijdong jingk ennet Liiere.',
		'redirect-fix-broken-moved': u'Bot: De kappodde Ömleidong op de ömjenannte Sigg %(to)s es reppareert.',
		'redirect-fix-loop': u'Bot: En Reih vun Ömleidonge jeng em Kreis eröm. Op %(to)s jescheck.',
		'redirect-remove-loop': u'Bot: Di Ömleidunge jonn em Kreis eröm.',
		'redirect-broken-redirect-template': u'{{Schmieß fott}}Di [[Wikipedia:Ömleijdung|Ömlëijdong]] jeiht noh nörjendswoh hen.',
	},
	# Author: MissPetticoats
	# Author: UV
	# Author: Xqt
	'la': {
		'redirect-fix-double': u'automaton: rectificatio redirectionis duplicis → %(to)s',
		'redirect-remove-broken': u'automaton: redirectio ad paginam quae non est',
		'redirect-remove-loop': u'automaton: redirectio ad eundem titulum',
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: Robby
	'lb': {
		'redirect-fix-double': u'Bot: Duebel Viruleedung gefléckt → %(to)s',
		'redirect-remove-broken': u'Bot: Viruleedung op eng geläschte Säit oder eng Säit déi et net gëtt',
		'redirect-fix-broken-moved': u'Bot: Futtis Viruleedung op déi geréckelt Zilsäit %(to)s gouf gefléckt',
		'redirect-fix-loop': u'Bot: Viruleedungsschleef op %(to)s verbessert',
		'redirect-remove-loop': u'Bot: Viruleedung där hiert Zil zu enger endlos Schleef féiert',
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: Pahles
	'li': {
		'redirect-fix-double': u'Robot: dobbel doorverwiezing aangepas nao %(to)s',
		'redirect-remove-broken': u'Robot: de doelpagina van de doorverwiezing besjteit neet',
		'redirect-remove-loop': u'Doorverwiezing vörmp \'n óneindige lus',
		'redirect-broken-redirect-template': u'{{delete|Weisdoorverwiezing of doorverwiezing nao eweggesjafde pagina}}',
	},
	# Author: Hugo.arg
	'lt': {
		'redirect-fix-double': u'robotas: Taisomas dvigubas peradresavimas → %(to)s',
		'redirect-remove-broken': u'robotas: peradresavimas į ištrintą ar nesantį puslapį',
	},
	# Author: Karlis
	'lv': {
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: StefanusRA
	'map-bms': {
		'redirect-fix-double': u'Bot: Mbenerna pengalihan ganda maring %(to)s',
		'redirect-remove-broken': u'Robot: Pangalihan ming kaca sing ora ana utawa wis debusek',
		'redirect-fix-loop': u'Robot: Ndandani pengalihan dobel maring %(to)s',
		'redirect-remove-loop': u'Robot: Target pangalihan marekna dadi pengalihan siklik',
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: Jagwar
	'mg': {
		'redirect-fix-double': u'Rôbô : mamaha olam-pihodinana mankany amin\'i %(to)s',
		'redirect-remove-broken': u'Rôbô : fihodinana mankany amina pejy tsy misy na erfa voafafa.',
		'redirect-fix-loop': u'Rôbô: nanamboatra ny fihodinana manao tondro mifolaka amin\'i %(to)s',
		'redirect-remove-loop': u'[[WP:CSD#G8|G8]]: Ny tanjon\'ny fihodinana dia manao fihodinana mifolaka',
		'redirect-broken-redirect-template': u'{{fafao}}',
	},
	# Author: Luthfi94
	# Author: Naval Scene
	'min': {
		'redirect-fix-double': u'Bot: Mampeloki pangalihan gando ka %(to)s',
		'redirect-remove-broken': u'Robot: Pangaliahan ka laman nan dihapuih atau indak ado',
		'redirect-remove-loop': u'Robot: Target pangaliahan mahasilan pangaliahan bapusiang',
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: Bjankuloski06
	# Author: Rancher
	# Author: Xqt
	'mk': {
		'redirect-fix-double': u'Робот: Исправка на двојни пренасочувања → %(to)s',
		'redirect-remove-broken': u'[[ВП:КББ|О6]: [[Википедија:Пренасочување|Пренасочување]] кон избришана или непостоечка страница',
		'redirect-fix-broken-moved': u'Робот: Исправка на прекинато пренасочување кон преместена целна страница %(to)s',
		'redirect-fix-loop': u'Робот: Поправа јамка на пренасочување кон %(to)s',
		'redirect-remove-loop': u'[[ВП:КББ|О6]]: Одредницата за [[Википедија:Пренасочување|пренасочување]] образува јамка',
		'redirect-broken-redirect-template': u'{{db|[[ВП:КББ|O8]]}}',
	},
	# Author: Praveenp
	'ml': {
		'redirect-fix-double': u'യന്ത്രം: %(to)s എന്നതിലോട്ടുള്ള ഇരട്ട തിരിച്ചുവിടൽ ശരിയാക്കുന്നു',
		'redirect-remove-broken': u'യന്ത്രം: മായ്ച്ച അല്ലെങ്കിൽ നിലവിലില്ലാത്ത താളിലോട്ടുള്ള തിരിച്ചുവിടൽ',
		'redirect-fix-loop': u'യന്ത്രം: %(to)s എന്നതിലോട്ടുണ്ടായിരുന്ന ചാക്രിക തിരിച്ചുവിടൽ ശരിയാക്കുന്നു',
		'redirect-remove-loop': u'യന്ത്രം: ലക്ഷ്യത്തിലോട്ടുള്ള തിരിച്ചുവിടൽ ഒരു തിരിച്ചുവിടൽ ചക്രം സൃഷ്ടിക്കുന്നു',
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: Htt
	'mr': {
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: Anakmalaysia
	# Author: Kurniasan
	'ms': {
		'redirect-fix-double': u'Bot: Memperbetulkan pelencongan berganda ke %(to)s',
		'redirect-remove-broken': u'Robot: Melencong kepada laman yang terhapus atau tidak wujud',
		'redirect-fix-broken-moved': u'Robot: Membaiki lencongan yang terputus ke halaman sasaran yang terpindah iaitu %(to)s',
		'redirect-fix-loop': u'Robot: Membaiki gelung lencongan ke %(to)s',
		'redirect-remove-loop': u'Robot: Sasaran lencongan membentuk gelung lencongan',
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: Chrisportelli
	'mt': {
		'redirect-fix-double': u'Bot: Tranġar ta\' rindirizz doppju lejn %(to)s',
		'redirect-remove-broken': u'Bot: Rindirizz lejn paġna mħassra jew li ma teżistix',
		'redirect-remove-loop': u'Bot: Id-destinazzjoni tar-rindirizz qiegħed jifforma ċiklu ta\' rindirizzi',
		'redirect-broken-redirect-template': u'{{Ħassar minnufih|9}}',
	},
	# Author: Lionslayer
	'my': {
		'redirect-fix-double': u'ဘော့ - %(to)s သို့ ပြန်ညွှန်းနှစ်ထပ်ဖြစ်နေသည်ကို ပြင်နေသည်',
		'redirect-remove-loop': u'[WP:CSD#G8|G8]]: [[Wikipedia:Redirect|ပြန်ညွှန်း]]သည် ယင်းကို ပြန်ညွှန်းခြင်းခံရသောကြောင့်  သံသရာလည်မှု ဖြစ်စေသည်။',
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: محک
	'mzn': {
		'redirect-fix-double': u'ربوت:عوض هایتن دکشیه‌ئون دِتایی → %(to)s',
		'redirect-remove-broken': u'ربوت:بی‌جاء ِدکشی‌یه‌ئون',
		'redirect-remove-loop': u'ربوت:ناترینگی [[:fa:وپ:تغییرمسیر|دکشی‌یه]]',
		'redirect-broken-redirect-template': u'{{حذف سریع|بن بست|bot=yes}}',
	},
	# Author: Slomox
	'nds': {
		'redirect-fix-double': u'Bot: Dubbelte Wiederleiden rutmakt → %(to)s',
		'redirect-remove-broken': u'Bot: Kaputte Wiederleiden ward nich brukt',
		'redirect-remove-loop': u'Bot: Redirect wiest wedder op sik sülvs',
		'redirect-broken-redirect-template': u'{{delete}}Kaputte Wiederleiden, wat nich brukt ward.',
	},
	# Author: Servien
	# Author: Xqt
	'nds-nl': {
		'redirect-fix-double': u'Bot: dubbele deurverwiezing verbeterd naor %(to)s',
		'redirect-remove-broken': u'Bot: de doelpagina van de deurverwiezing besteet niet',
		'redirect-fix-loop': u'Bot: deurverwiessirkel naor %(to)s erepareerd',
		'redirect-remove-loop': u'Bot: deurverwiezing verwis weer naor zichzelf',
		'redirect-broken-redirect-template': u'{{vort|Kapotte deurverwiezing of deurverwijzing naor vort-edaone pagina}}',
	},
	# Author: RajeshPandey
	'ne': {
		'redirect-fix-double': u'बोट: दुइपल्ट रिडाइरेक्ट लाइ %(to)s मा ठिक गर्दै',
		'redirect-remove-broken': u'रोबोट: [[Wikipedia:Redirect|रिडाइरेक्ट]]  लाइ मेटिएको वा हुदै नभएको पृष्ठमा पठाएको',
		'redirect-remove-loop': u'रोबोट: [[Wikipedia:Redirect|रिडाइरेक्ट]] निसाना पृष्ठ रिडाइरेक्ट भएर घुमिरहन्छ',
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: Eukesh
	'new': {
		'redirect-fix-loop': u'रोबट: पुनर्निदेश लूपयात %(to)sय्‌ मिलय्‌यानाछ्वगु',
		'redirect-remove-loop': u'रोबट:पुनर्निर्देशया लक्ष्यं पुनर्निदेश लूप दयेकी',
	},
	# Author: Krinkle
	# Author: Siebrand
	'nl': {
		'redirect-fix-double': u'Robot: dubbele doorverwijzing gecorrigeerd naar %(to)s',
		'redirect-remove-broken': u'Robot: de doelpagina van de doorverwijzing bestaat niet',
		'redirect-fix-broken-moved': u'Robot: kapotte doorverwijzing gecorrigeerd door aanpassing naar hernoemde doelpagina %(to)s',
		'redirect-fix-loop': u'Robot: doorverwijscirkel naar %(to)s gerepareerd',
		'redirect-remove-loop': u'[[WP:NW|NUWEG]]: [[Wikipedia:Doorverwijzing|Doorverwijzing]] vormt een oneindige lus',
		'redirect-broken-redirect-template': u'{{nuweg|Weesdoorverwijzing of doorverwijzing naar verwijderde pagina}}',
	},
	# Author: Njardarlogar
	'nn': {
		'redirect-fix-double': u'robot: retta dobbel omdirigering → %(to)s',
		'redirect-remove-broken': u'robot: målet for omdirigeringa finst ikkje',
		'redirect-fix-loop': u'robot: retta omdirigeringslykkje til %(to)s',
		'redirect-broken-redirect-template': u'{{snøggsletting|dette er ei øydelagd omdirigering}}',
	},
	# Author: Danmichaelo
	# Author: Jon Harald Søby
	'no': {
		'redirect-fix-double': u'robot: Retter dobbel omdirigering til %(to)s',
		'redirect-remove-broken': u'Robot: Målet for omdirigeringen eksisterer ikke',
		'redirect-fix-broken-moved': u'bot: Fikser ødelagte omdirigeringer til %(to)s som har blitt flyttet',
		'redirect-fix-loop': u'Robot: Fikser omdirigeringsløkke til %(to)s',
		'redirect-remove-loop': u'Robot: Målet for omdirigeringen danner en omdirigeringsløkke',
		'redirect-broken-redirect-template': u'{{hurtigslett|Feilaktig omdirigering}}',
	},
	# Author: Geitost
	# Author: Xqt
	'pdc': {
		'redirect-fix-double': u'Waddefresser: Doppelte Weiderleiding nooch %(to)s gennert',
		'redirect-remove-broken': u'Waddefresser: Kaputte Weiderleiding',
		'redirect-broken-redirect-template': u'{{verwische|Kaputte Weiderleiding}}',
	},
	'pfl': {
		'redirect-fix-double': u'Bot: E doppelte Waiterlaitung vabessat zu %(to)s',
	},
	# Author: BeginaFelicysym
	# Author: Sp5uhe
	'pl': {
		'redirect-fix-double': u'Robot naprawił podwójne przekierowanie do %(to)s',
		'redirect-remove-broken': u'Robot: przekierowanie do usuniętej lub nieistniejącej strony',
		'redirect-fix-loop': u'Robot: Naprawa pętli przekierowań do %(to)s',
		'redirect-remove-loop': u'Robot: pętla przekierowań',
		'redirect-broken-redirect-template': u'{{ek|przekierowanie do usuniętej lub nieistniejącej stron}}',
	},
	# Author: Borichèt
	# Author: Dragonòt
	'pms': {
		'redirect-fix-double': u'Trigomiro: a coregg ridiression dobia a %(to)s',
		'redirect-remove-broken': u'Trigomiro: Ridiression a na pàgina scancelà o ch\'a esist nen',
		'redirect-fix-broken-moved': u'Trigomiro: Coregi le rediression pa bon-e a pagina ëd destinassion tramudò %(to)s',
		'redirect-fix-loop': u'Trigomiro: Coression dël sicl ëd ridiression a %(to)s',
		'redirect-remove-loop': u'Trigomiro: La destinassion ëd la ridiression a forma un sicl ëd ridiression',
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: Hamilton Abreu
	# Author: Malafaya
	# Author: Xqt
	'pt': {
		'redirect-fix-double': u'Robô: A corrigir o redireccionamento duplo para %(to)s',
		'redirect-remove-broken': u'Robô: Redireccionamento para uma página eliminada ou inexistente',
		'redirect-fix-broken-moved': u'Robô: A corrigir redireccionamento quebrado para página alvo movida %(to)s',
		'redirect-fix-loop': u'Robô: A corrigir o ciclo de redireccionamentos para %(to)s',
		'redirect-remove-loop': u'Robô: O destino do redireccionamento cria um ciclo de redireccionamentos',
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: Hamilton Abreu
	# Author: Helder.wiki
	# Author: Luckas Blade
	# Author: Tuliouel
	# Author: 555
	'pt-br': {
		'redirect-fix-double': u'Bot: Corrigindo redirecionamento duplo para %(to)s',
		'redirect-remove-broken': u'Robô: Redirecionamento para uma página eliminada ou inexistente',
		'redirect-fix-broken-moved': u'Bot: consertando redirecionamento quebrado para página-alvo movida %(to)s',
		'redirect-fix-loop': u'Bot: Corrigindo ciclo de redirecionamentos para %(to)s',
		'redirect-remove-loop': u'Bot: O destino do redirecionamento cria um ciclo de redirecionamentos',
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: Firilacroco
	# Author: Minisarm
	'ro': {
		'redirect-fix-double': u'Robot: Reparat dubla redirecționare înspre %(to)s',
		'redirect-remove-broken': u'Robot: Redirecționare către o pagină ștearsă sau inexistentă',
		'redirect-fix-loop': u'Robot: Reparat bucla de redirecționare către %(to)s',
		'redirect-remove-loop': u'Robot: Ținta redirecționării formează o buclă de redirecționare',
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: DCamer
	# Author: Rubin
	# Author: Volkov
	# Author: Xqt
	'ru': {
		'redirect-fix-double': u'бот: исправление двойного перенаправления → %(to)s',
		'redirect-remove-broken': u'бот: [[ВП:КБУ#П1|П1]] - перенаправление на удалённую или несуществующую страницу',
		'redirect-fix-broken-moved': u'Робот: Исправление перенаправления на перемещенную целевую страницу %(to)s',
		'redirect-fix-loop': u'бот: исправление перенаправления на %(to)s',
		'redirect-remove-loop': u'бот: перенаправление в никуда',
		'redirect-broken-redirect-template': u'{{db-redirnone}}',
	},
	# Author: Gazeb
	'rue': {
		'redirect-fix-double': u'Робот: справив двоїте напрямлїня → %(to)s',
		'redirect-remove-broken': u'[[WP:CSD#G8|G8]]: [[Wikipedia:Redirect|Напрямлїня]] на змазану або неекзістуючу сторінку',
		'redirect-remove-loop': u'[[WP:CSD#G8|G8]]: [[Wikipedia:Redirect|Напрямлїня]] формує петлю напрямлїнь',
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: Avicennasis
	'sco': {
		'redirect-fix-double': u'Bot: Fixin\' dooble reguidal tae %(to)s',
		'redirect-remove-broken': u'[[WP:CSD#G8|G8]]: [[Wikipedia:Redirect|Redirect]] to a deletit or non-existent page',
		'redirect-remove-loop': u'[[WP:CSD#G8|G8]]: [[Wikipedia:Redirect|Redirect]] target forms a redirect loop',
		'redirect-broken-redirect-template': u'{{delete}}',
	},
	# Author: පසිඳු කාවින්ද
	'si': {
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: Teslaton
	# Author: Wizzard
	'sk': {
		'redirect-fix-double': u'Robot: Opravujem dvojité presmerovanie na %(to)s',
		'redirect-remove-broken': u'Robot: Presmerovanie na neexistujúcu stránku',
		'redirect-fix-loop': u'Robot: Oprava cyklického presmerovania na %(to)s',
		'redirect-remove-loop': u'Robot: Cieľ presmerovania tvorí slučku',
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: Dbc334
	# Author: Mateju
	'sl': {
		'redirect-fix-double': u'Bot: Popravljanje dvojnih preusmeritev na %(to)s',
		'redirect-remove-broken': u'Robot: Preusmeritev na izbrisano ali neobstoječo stran',
		'redirect-fix-broken-moved': u'Robot: Popravljanje okvarjene povezave preusmeritve na premaknjeno ciljno stran %(to)s',
		'redirect-fix-loop': u'Robot: Popravljanje preusmeritvene zanke na %(to)s',
		'redirect-remove-loop': u'Robot: Cilj preusmeritve ustvarja preusmeritveno zanko',
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: Abshirdheere
	'so': {
		'redirect-fix-double': u'Bot: Hagaajin u rogid labalaaban ee %(to)s',
		'redirect-remove-broken': u'Bot: U wareejin bog la tirtiray ama aan jirin',
		'redirect-fix-broken-moved': u'Bot: Dib u Sixidda qaldantay waxaa loo wareejiyey Bog kale %(to)s',
		'redirect-fix-loop': u'Bot: Diyaarinta dib u bilaabista ee %(to)s',
		'redirect-remove-loop': u'Bot: Ujeedka u rogista bogga ee dhaqaaqa',
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: Vinie007
	'sq': {
		'redirect-fix-double': u'Bot: Fixing dyfishtë përcjellëse tek %(to)s',
		'redirect-remove-broken': u'[[WP:CSD#G8|G8]]: [[Wikipedia:Redirect|Redirect]] to a deleted or non-existent page',
		'redirect-remove-loop': u'[[WP:CSD#G8|G8]]: [[Wikipedia:Redirect|Redirect]] target forms a redirect loop',
		'redirect-broken-redirect-template': u'{{Db-r1}}',
	},
	# Author: Rancher
	'sr': {
		'redirect-fix-double': u'Робот: исправљена двострука преусмерења у %(to)s',
		'redirect-remove-broken': u'Робот: преусмерење до обрисане или непостојеће странице',
		'redirect-fix-broken-moved': u'Робот: исправљено покварено преусмерење до премештене циљне странице %(to)s',
		'redirect-fix-loop': u'Робот: исправљена петља преусмерења на %(to)s',
		'redirect-remove-loop': u'Робот: одредиште преусмерења образује петљу',
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: Rancher
	'sr-el': {
		'redirect-fix-double': u'Robot: ispravljena dvostruka preusmerenja u %(to)s',
		'redirect-remove-broken': u'Robot: preusmerenje do obrisane ili nepostojeće stranice',
		'redirect-fix-broken-moved': u'Robot: ispravljeno pokvareno preusmerenje do premeštene ciljne stranice %(to)s',
		'redirect-fix-loop': u'Robot: ispravljena petlja preusmerenja na %(to)s',
		'redirect-remove-loop': u'Robot: odredište preusmerenja obrazuje petlju',
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: Boivie
	# Author: Lokal Profil
	# Author: Tobulos1
	# Author: WikiPhoenix
	'sv': {
		'redirect-fix-double': u'Robot: Rättar dubbel omdirigering → %(to)s',
		'redirect-remove-broken': u'Robot: Omdirigerar till en raderad eller en obefintlig sida',
		'redirect-fix-broken-moved': u'Robot: Reparerade trasig omdirigering till den flyttade målsidan %(to)s',
		'redirect-fix-loop': u'Robot: Fixar omdirigeringsslinga till %(to)s',
		'redirect-remove-loop': u'Robot: Målet för omdirigeringen bildar en omdirigeringsloop',
		'redirect-broken-redirect-template': u'{{radera|Trasig omdirigering}}',
	},
	# Author: Kwisha
	'sw': {
		'redirect-remove-broken': u'Boti: Uelekezaji kwa ukurasa uliofutwa au ambao haupatikani',
		'redirect-fix-loop': u'Boti: Inarekebisha tanzi la uelekezaji kwa %(to)s',
	},
	# Author: Przemub
	'szl': {
		'redirect-fix-double': u'Robot sprowjo tuplowane przekerowańa → %(to)s',
		'redirect-remove-broken': u'Robot: pukniyńcie dŏ wyciepanej zajty',
		'redirect-fix-loop': u'Robot: Naprawa mocki pukniyńć dŏ (to)s',
		'redirect-remove-loop': u'Robot: mocka pukniyńć',
		'redirect-broken-redirect-template': u'{{delete|pukniyńciy dŏ wyciepanyj zajty}}',
	},
	# Author: செல்வா
	'ta': {
		'redirect-remove-broken': u'[[WP:CSD#G8|G8]]: நீக்கப்பட்ட அல்லது இல்லாத பக்கத்துக்கு [[Wikipedia:Redirect|வழிமாற்று]]',
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: Nullzero
	'th': {
		'redirect-fix-double': u'โรบอต: แก้หน้าเปลี่ยนทางซ้ำซ้อน → %(to)s',
		'redirect-remove-broken': u'โรบอต: หน้าเปลี่ยนทางเสีย',
		'redirect-fix-loop': u'โรบอต: แก้หน้าเปลี่ยนทางวนรอบ → %(to)s',
		'redirect-remove-loop': u'โรบอต: หน้าเปลี่ยนทางทำให้เกิดการเปลี่ยนทางวนรอบ',
		'redirect-broken-redirect-template': u'{{ลบ|หน้าเปลี่ยนทางเสีย}}',
	},
	# Author: AnakngAraw
	'tl': {
		'redirect-fix-double': u'Bot: Kinukumpuni ang nagkadalawang pagpapapunta sa %(to)s',
		'redirect-remove-broken': u'[[WP:CSD#G8|G8]]: [[Wikipedia:Redirect|Papuntahin]] sa isang pahinang nabura na o hindi na umiiral',
		'redirect-fix-loop': u'Robot: Kinukumpuni ang silo ng pagpapapunta sa %(to)s',
		'redirect-remove-loop': u'[[WP:CSD#G8|G8]]: [[Wikipedia:Redirect|Ang pagpapapunta sa ibang pook]] ay bumubuo ng nakalikaw na pagpapapunta',
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: Gorizon
	# Author: Xqt
	# Author: Гусейн
	'tly': {
		'redirect-fix-double': u'Робот: дығатә унвон дәгиш кардеј сәрост карде → %(to)s',
		'redirect-remove-broken': u'Робот: Истиғомәти дәгиш карде бә молә быә јаанки бә мывҹуд ныбә сәһифә',
		'redirect-fix-broken-moved': u'Робот: Бә вырәку дәгиш кардә быә мәғсәдә сәһифә %(to)s дәгиш быә истиғомәти сәрост кардеј',
		'redirect-fix-loop': u'Робот: Истиғомәти дәгиш кардә ангыли сохте бә %(to)s',
		'redirect-remove-loop': u'Bot: Унвони дәгиш карде бешә формон унвони дәгиш кардеј мәрә',
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: Emperyan
	# Author: Khutuck
	# Author: Stultiwikia
	# Author: Vito Genovese
	# Author: Xqt
	'tr': {
		'redirect-fix-double': u'Bot: %(to)s sayfasına yönelik çift yönlendirme düzeltiliyor',
		'redirect-remove-broken': u'Bot: Silinen ya da var olmayan sayfaya olan yönlendirme',
		'redirect-remove-loop': u'Bot: Yönlendirme hedefi bir yönlendirme döngüsü oluşturuyor',
		'redirect-broken-redirect-template': u'{{sil|y1}}',
	},
	# Author: Ильнар
	'tt': {
		'redirect-fix-double': u'Робот: икеле күчешне дөресләү → %(to)s',
		'redirect-remove-broken': u'[[ВП:ТБК#П1|П1]]: беркаяда күчеш ясамау',
		'redirect-remove-loop': u'[[ВП:ТБК#П1|тиз бетерү критерийлары \'\'П.1\'\']] — беркаяда күчеш ясамау',
		'redirect-broken-redirect-template': u'{{db-redirnone}}',
	},
	# Author: Ahonc
	# Author: Base
	# Author: Тест
	'uk': {
		'redirect-fix-double': u'Робот: виправлення подвійного перенаправлення → %(to)s',
		'redirect-remove-broken': u'бот: перенаправлення на вилучену або неіснуючу сторінку',
		'redirect-fix-broken-moved': u'Робот: Виправлення розірваного перенаправлення на сторінку, перейменовану на %(to)s',
		'redirect-fix-loop': u'бот: виправлення петлі перенаправлень на %(to)s',
		'redirect-remove-loop': u'бот: перенаправлення формують петлю',
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: Muhammad Shuaib
	'ur': {
		'redirect-fix-double': u'روبالہ: درستگی دوہرا رجوع مکرر بجانب %(to)s',
	},
	# Author: CoderSI
	'uz': {
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: Alunardon90
	# Author: Candalua
	# Author: GatoSelvadego
	'vec': {
		'redirect-fix-double': u'Robot: Sistemo i dopi rimandi a %(to)s',
		'redirect-remove-broken': u'Robot: El rindirisamento el ponta a na pajina inexistente',
		'redirect-fix-loop': u'Robot: Preparasion de un ciclo de rindirisamento a %(to)s',
		'redirect-remove-loop': u'Ła destinasion del rindirisamento rimanda a ła pajina de partensa',
		'redirect-broken-redirect-template': u'{{Scanseła suito|9}}',
	},
	# Author: Emaus
	'vep': {
		'redirect-fix-double': u'Bot kohenzi kaksitadud läbikosketusen %(to)s',
	},
	# Author: Minh Nguyen
	'vi': {
		'redirect-fix-double': u'Bot: Giải quyết đổi hướng kép đến %(to)s',
		'redirect-remove-broken': u'Bot: [[Wikipedia:Trang đổi hướng|Đổi hướng]] đến trang xóa hoặc không tồn tại',
		'redirect-fix-broken-moved': u'Bot: Sửa đổi hướng sai; trang đích đã được di chuyển đến %(to)s',
		'redirect-fix-loop': u'Bot: Sửa vòng lặp đổi hướng đến %(to)s',
		'redirect-remove-loop': u'Bot: [[Wikipedia:Trang đổi hướng|Đổi hướng]] qua lại',
		'redirect-broken-redirect-template': u'{{Chờ xóa}}',
	},
	# Author: Malafaya
	'vo': {
		'redirect-broken-redirect-template': u'{{moükön|Lüodüköm dädik}}',
	},
	# Author: Harvzsf
	'war': {
		'redirect-fix-double': u'Robot: Gin-ayad in nagduduha nga redirek → %(to)s',
		'redirect-remove-broken': u'Robot: Redirek ngadto hin ginpárà o waray-didâ nga pakli',
		'redirect-fix-loop': u'Robot: Gin-aayad in redirek nga loop ngadto ha %(to)s',
		'redirect-remove-loop': u'Robot: An redirek nga ginkakadtoan naghihimo hin redirek nga loop',
		'redirect-broken-redirect-template': u'{{delete}}Nautod o nagbinalikbalik nga redirek.',
	},
	# Author: פוילישער
	'yi': {
		'redirect-fix-double': u'באט: פארראכטן פארטאפלטע ווייטערפירונג → %(to)s',
		'redirect-remove-broken': u'באט: ווײַטערפֿירונג צו א בלאט וואס איז אויסגעמעקט אדער עקזיסטירט נישט',
		'redirect-fix-loop': u'באט: פאררעכטן ווייטערפירונג שלייף אויף %(to)s',
		'redirect-remove-loop': u'באט: [[װיקיפּעדיע:ווייטערפירונג|ווייטערפירוג]] ציל שאפט א שלייף',
		'redirect-broken-redirect-template': u'ווײַטערפֿירונג אןָ א ציל',
	},
	# Author: Demmy
	'yo': {
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: Liangent
	# Author: Linforest
	# Author: Yfdyh000
	# Author: 阿pp
	'zh': {
		'redirect-fix-double': u'机器人：修正双重重定向至%(to)s',
		'redirect-remove-broken': u'机器人：重定向到已删除或不存在的页面',
		'redirect-fix-broken-moved': u'机器人：修复破损的重定向到已移动的目标页面 %(to)s',
		'redirect-fix-loop': u'机器人：修复重定向循环至%(to)s',
		'redirect-remove-loop': u'机器人：重定向目标构成循环',
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	'zh-classical': {
		'redirect-fix-double': u'僕:復修渡口 → %(to)s',
	},
	# Author: Andrew971218
	# Author: Justincheng12345
	# Author: Liangent
	# Author: Simon Shek
	'zh-hant': {
		'redirect-fix-double': u'機械人：修正雙重定向至%(to)s',
		'redirect-remove-broken': u'機械人：重定向到已刪除或不存在的頁面',
		'redirect-fix-broken-moved': u'機械人：修復損壞的重定向頁到移動目標頁面 %(to)s',
		'redirect-fix-loop': u'機械人：修復重定向迴圈至%(to)s',
		'redirect-remove-loop': u'機械人：重定向目標構成循環',
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	# Author: Justincheng12345
	'zh-hk': {
		'redirect-fix-double': u'機械人修正雙重定向至%(to)s',
		'redirect-remove-broken': u'[[WP:CSD#G15|G15]]：[[Wikipedia:重定向|重定向]]到不存在的頁面',
		'redirect-fix-loop': u'機械人修復重定向迴圈至%(to)s',
		'redirect-remove-loop': u'[[WP:CSD#R5|R5]]：[[Wikipedia:重定向|重定向]]目標構成循環',
		'redirect-broken-redirect-template': u'{{db-r1}}',
	},
	'zh-yue': {
		'redirect-fix-double': u'機械人：拉直連串跳轉 → %(to)s',
		'redirect-remove-broken': u'機械人：跳轉目標唔存在',
	},
};
