from collections import Counter
import math
import random
import random
import string

def generate_random_key():
    alphabet = list(string.ascii_lowercase)
    shuffled_alphabet = random.sample(alphabet, len(alphabet))
    random_key = {original: shuffled for original, shuffled in zip(alphabet, shuffled_alphabet)}
    return random_key

def load_word_list(file_path):
    with open(file_path, 'r') as f:
        return {line.strip() for line in f if len(line.strip()) >= 4}

def english_detect_numVar(message, crib, spaces,total_iterations):
    english_percentage_dict = {
        "th": 2.9, "he": 2.48, "in": 1.87, "er": 1.73, "an": 1.65,
        "re": 1.38, "es": 1.35, "st": 1.19, "on": 1.17, "nd": 1.14,
        "en": 1.13, "at": 1.08, "nt": 1.08, "ed": 1.04, "ea": 1.01,
        "to": 1.0, "or": 0.96, "ti": 0.96, "ha": 0.94, "ar": 0.89,
        "ng": 0.89, "is": 0.89, "it": 0.88, "te": 0.88, "ou": 0.85,
        "et": 0.84, "of": 0.82, "al": 0.82, "as": 0.8, "le": 0.74,
        "se": 0.73, "hi": 0.72, "sa": 0.68, "ra": 0.64, "ro": 0.64,
        "ne": 0.64, "ve": 0.63, "me": 0.62, "ri": 0.62, "so": 0.6,
        "de": 0.59, "ll": 0.58, "ta": 0.58, "li": 0.57, "si": 0.57,
        "el": 0.55, "ec": 0.52, "co": 0.52, "no": 0.52, "ot": 0.51,
        "ma": 0.5, "di": 0.5, "ic": 0.49, "la": 0.49, "ho": 0.49,
        "om": 0.48, "tt": 0.48, "na": 0.48, "sh": 0.47, "ch": 0.46,
        "be": 0.46, "ss": 0.46, "rt": 0.46, "ee": 0.45, "em": 0.45,
        "ns": 0.44, "rs": 0.44, "ce": 0.43, "ur": 0.42, "ei": 0.41,
        "ca": 0.41, "io": 0.41, "ac": 0.4, "ts": 0.4, "da": 0.39,
        "lo": 0.39, "us": 0.39, "wa": 0.38, "ni": 0.38, "dt": 0.38,
        "pe": 0.38, "fo": 0.38, "ew": 0.37, "ut": 0.37, "wi": 0.36,
        "il": 0.36, "eo": 0.36, "ly": 0.36, "wh": 0.36, "ad": 0.35,
        "un": 0.34, "ow": 0.34, "tr": 0.34, "nc": 0.33, "ft": 0.33,
        "do": 0.32, "ge": 0.32, "ep": 0.32, "mo": 0.32, "we": 0.31
    }  
    message = message.lower()
    letter_freq_dict={}
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        letter_freq_dict[letter]=0
    for i in alphabet:
        for letter in message:
            if letter==i:
                letter_freq_dict[i]+=1
    message_freq = sorted(letter_freq_dict.items(), key=lambda item: item[1], reverse=True)
    freq_dict = Counter(message[i-1:i+1] for i in range(1, len(message)))
    total_bigrams = sum(freq_dict.values())
    percentage_dict = {bigram: (count / total_bigrams * 100) for bigram, count in freq_dict.items()}
    precision = 0
    for bigram, target_percentage in english_percentage_dict.items():
        if bigram in percentage_dict:
            if target_percentage - 2 <= percentage_dict[bigram] <= target_percentage + 2:
                precision += 5
    #precision += sum(crib.count(message) * 200 for _ in crib)
    word_list_file = "Oxford 3000 Word List No Spaces.txt" if spaces == "f" else "Oxford 3000 Word List.txt"
    word_set = load_word_list(word_list_file)
    n = 4  # Length of n-grams to check
    ngrams = [message[i:i+n] for i in range(len(message) - n + 1)]
    for ngram in ngrams:
        if ngram in word_set:
            precision += 2
    for word in word_set:
        if word in message:
            precision += 3
    message_freq = sorted(letter_freq_dict.items(), key=lambda item: item[1], reverse=True)
    if message_freq[0]!="e":
        precision+=15 #math.floor(15 * (1+(total_iterations/100)))
    common="aeiotn"
    for i in common:
        if i in message_freq[1:12]:
            precision += 10
    if "z" in message_freq[-1:-9]:
        precision+=30
    vowels = "aeiou"
    vowel_count = sum(letter_freq_dict[v] for v in vowels)
    consonant_count = len(message) - vowel_count
    vowel_consonant_ratio = vowel_count / (consonant_count + 1)  # Avoid division by zero
    if 0.35 <= vowel_consonant_ratio <= 0.6:
        precision += 20
    corpus_freq = list("etaoinshrdlcumwfgypbvkjxqz")
    for i in range(len(message_freq)):
        if message_freq[i]==corpus_freq[i]:
            precision+=3

    english_transition_matrix = {
        'a': {'d': 0.05072366082917683, 's': 0.10396696037941641, 'n': 0.20853686932437898, 'l': 0.0857731099645829, 'i': 0.04054706552776382, 'y': 0.026370421206142233, 'v': 0.022125271143028712, 'r': 0.1026507677790169, 'm': 0.030985673844042206, 't': 0.14704837069081728, 'k': 0.011299158077917622, 'b': 0.022970869741050746, 'c': 0.04599811272196963, 'f': 0.013693795267098862, 'g': 0.021090944741969878, 'w': 0.013478106349342517, 'p': 0.025456194316106816, 'o': 0.001833355800928933, 'j': 0.0011985440998051446, 'h': 0.004137305604235346, 'u': 0.010835917106827289, 'q': 0.0004730450128065295, 'z': 0.001311290579541416, 'x': 0.001389722913270996, 'a': 0.0034951408718244094, 'e': 0.002610326106937585},
        'd': {'v': 0.007081246521981079, 'a': 0.09273789649415692, 'o': 0.0745501762196253, 'h': 0.04529308106102764, 'e': 0.1434752365052866, 'p': 0.02077072899276572, 'l': 0.02182804674457429, 't': 0.11311445000927471, 'm': 0.02166110183639399, 'r': 0.03829066963457615, 'f': 0.02390558337970692, 'j': 0.003682062697087739, 'u': 0.025621406047115564, 'i': 0.12499072528287887, 'n': 0.027202745316267853, 'y': 0.014347987386384715, 'q': 0.001145427564459284, 's': 0.06384715266184382, 'd': 0.024615099239473196, 'g': 0.012966054535336672, 'b': 0.04303932480059358, 'c': 0.01847523650528659, 'w': 0.03425153032832499, 'k': 0.0028937117417918755, 'z': 0.00018085698386199222, 'x': 3.246150992394732e-05},
        'v': {'e': 0.5943421454767727, 'i': 0.1771088019559902, 'a': 0.09176344743276284, 'o': 0.06238539119804401, 'y': 0.005367512224938875, 'u': 0.0018910452322738387, 'r': 0.0041450183374083125, 't': 0.005291106356968215, 's': 0.015873319070904647, 'p': 0.0017000305623471883, 'x': 3.820293398533007e-05, 'j': 0.00019101466992665038, 'c': 0.0017764364303178484, 'd': 0.0017382334963325183, 'n': 0.011384474327628362, 'm': 0.0008977689486552567, 'v': 0.00017191320293398534, 'g': 0.0012224938875305623, 'l': 0.005558526894865526, 'w': 0.008500152811735941, 'h': 0.004698960880195599, 'z': 1.9101466992665037e-05, 'b': 0.0017955378973105135, 'f': 0.0014708129584352079, 'q': 5.730440097799511e-05, 'k': 0.0006112469437652812},
        'e': {'n': 0.0968934806179895, 'i': 0.030452822982214415, 'm': 0.037018448460629134, 'r': 0.14658232363167473, 's': 0.1080187435981206, 'w': 0.03122459963099922, 'l': 0.04123875676093705, 'a': 0.07832033623578172, 'y': 0.013457953955394782, 'e': 0.03328582724513615, 'c': 0.04512920551196885, 'd': 0.09958601837428169, 'o': 0.02948376191400609, 'x': 0.011395148065902467, 'f': 0.02663970972359664, 'p': 0.02832215125244041, 'b': 0.016103143451025325, 't': 0.05882390077067186, 'v': 0.019548518551837663, 'h': 0.020047253564140322, 'u': 0.006945989839063262, 'k': 0.0030239755809237014, 'j': 0.0015088312397510744, 'q': 0.0027146336112676235, 'g': 0.013770452475761636, 'z': 0.00046401295448411704},
        'n': {'t': 0.15661585919562818, 'd': 0.17696776169732914, 'b': 0.009544359178008669, 'i': 0.05416240861567487, 'h': 0.016228934506883813, 'y': 0.012198130162180918, 'a': 0.06663160833701536, 'o': 0.07796231590988563, 'e': 0.08662840971621728, 's': 0.0595133217134849, 'c': 0.05320011168065837, 'g': 0.12099189773087672, 'w': 0.015510600175110936, 'l': 0.013331200919467944, 'k': 0.007955891561333554, 'n': 0.012290293812295173, 'f': 0.01646747571894424, 'm': 0.009522673613275903, 'u': 0.009834403606309414, 'p': 0.007890834867135255, 'v': 0.0058794987381712025, 'q': 0.0013526371002062839, 'r': 0.005920159172045139, 'x': 0.0005719567698267052, 'j': 0.0026754565489050144, 'z': 0.00015179895312936252},
        't': {'u': 0.023115752450634505, 'o': 0.11440202346964252, 'h': 0.34059423137463496, 'i': 0.11310370281917954, 'e': 0.09879395130212008, 'w': 0.02270541364973567, 't': 0.05357201011734821, 'a': 0.06484221496108294, 'p': 0.006539367557181472, 'r': 0.03535861222983315, 'f': 0.008002692169910659, 's': 0.03746458385349385, 'b': 0.00968964057360588, 'l': 0.016283285749953864, 'y': 0.017505617733583733, 'k': 0.00147418013656249, 'm': 0.009889382212138647, 'c': 0.009774313659505639, 'g': 0.003219748368957544, 'n': 0.005091240677818908, 'd': 0.006046526775149535, 'z': 0.0003690878103322876, 'v': 0.001150685526330073, 'j': 0.0006513314299981546, 'q': 0.00033869234359904036, 'x': 2.1711047666605153e-05},
        'u': {'r': 0.14951869344197283, 'n': 0.12432490896636263, 'l': 0.10533222771027868, 't': 0.143562750117172, 'c': 0.04111475646248693, 's': 0.14296427155063635, 'b': 0.024847676388938963, 'p': 0.045917006165050296, 'm': 0.035641922341998054, 'e': 0.037761834372859356, 'f': 0.007412481522875582, 'g': 0.04192955258319213, 'd': 0.01979305620651116, 'i': 0.025352417348667843, 'h': 0.00408119118866496, 'k': 0.00404513826297004, 'w': 0.004593142733532826, 'a': 0.030169088221509176, 'u': 0.00043263510833904174, 'v': 0.0012257994736272848, 'y': 0.0010815877708476042, 'q': 9.373760680679237e-05, 'o': 0.002992392832678372, 'j': 0.00013700111764069654, 'z': 0.00508346252298374, 'x': 0.0005912679813966903},
        'r': {'e': 0.24271910548086867, 'l': 0.013986556359875904, 'd': 0.028551577042399173, 'u': 0.01986168562564633, 'a': 0.09891739917269907, 'n': 0.023180584281282317, 's': 0.06695966907962772, 'i': 0.1045275336091003, 't': 0.06950943640124095, 'r': 0.030261116856256463, 'f': 0.013220656670113753, 'v': 0.008990434332988625, 'h': 0.015528050672182006, 'p': 0.011672699069286453, 'o': 0.11046406411582213, 'w': 0.013582600827300931, 'b': 0.010341261633919338, 'y': 0.039581178903826265, 'm': 0.030581049638055843, 'c': 0.021047699069286455, 'g': 0.015631463288521198, 'k': 0.008486297828335057, 'q': 0.0003974922440537746, 'j': 0.0007885211995863495, 'x': 0.0008790072388831437, 'z': 0.0003328593588417787},
        'i': {'a': 0.02739377491306929, 'n': 0.26913091176703935, 't': 0.12406127144541627, 's': 0.13110601032498817, 'h': 0.003247419436913337, 'm': 0.04268974969974365, 'o': 0.0700616380454201, 'p': 0.007753316498915247, 'r': 0.03358220184339614, 'c': 0.06349293200664258, 'b': 0.009504241890342826, 'l': 0.0464788616796299, 'v': 0.02206165993198749, 'g': 0.025467756982498955, 'f': 0.020789503202278393, 'e': 0.04231767805406529, 'k': 0.006027013495804618, 'w': 0.002962894060806356, 'd': 0.04144495117927561, 'z': 0.0040161851165870085, 'x': 0.0020682806186238275, 'u': 0.0016880015101731502, 'y': 6.839552310263979e-05, 'i': 0.002106582111561306, 'j': 7.933880679906216e-05, 'q': 0.0003994298549194164},
        's': {'c': 0.03072098440953348, 'h': 0.07109491667164447, 's': 0.08372259721641478, 'a': 0.09852458037154292, 't': 0.163843259064572, 'e': 0.12132190430679171, 'n': 0.012791947912311093, 'i': 0.09113254883220835, 'o': 0.09096828146466758, 'p': 0.03284750014933397, 'f': 0.018816080281942538, 'm': 0.023863568484558867, 'b': 0.016886685383190967, 'u': 0.04177169822591243, 'g': 0.005803118093303865, 'w': 0.03170957529418792, 'l': 0.017188340003584015, 'd': 0.011200047786870558, 'r': 0.009608147661430023, 'y': 0.007601099098022818, 'v': 0.0033630010154709995, 'q': 0.0019622483722597215, 'j': 0.0014425661549489278, 'k': 0.011624156263066723, 'z': 6.869362642613942e-05, 'x': 0.00012245385580311808},
        'c': {'a': 0.12648104061001278, 'k': 0.03520684539212642, 'l': 0.038491529517303245, 'u': 0.04025118172721941, 'o': 0.20322947934996377, 'i': 0.05503226029051513, 'e': 0.1761653383017631, 't': 0.09297174205568781, 'h': 0.14852154711382534, 'r': 0.03468240002760239, 'c': 0.02325501155849981, 'y': 0.009785046406514163, 'q': 0.0017113480316047337, 's': 0.005161646482420729, 'm': 0.0008142704343925749, 'f': 0.0012214056515888624, 'w': 0.0011938032639823345, 'b': 0.0010281889383431666, 'd': 0.0016630438532933098, 'n': 0.0005727495428354553, 'p': 0.0014146223648345581, 'g': 0.0005313459614256633, 'v': 0.00028982506986854363, 'j': 0.00011731014732774385, 'z': 0.00020011731014732775, 'x': 6.900596901631991e-06},
        'l': {'i': 0.12149335052143394, 'o': 0.09456812379460891, 'm': 0.011899066907702921, 'w': 0.01188899575500914, 'd': 0.06114196800394789, 'e': 0.16926586332438678, 't': 0.04068242130653064, 'l': 0.1286589756630595, 'a': 0.11776198844838787, 'y': 0.09738301097252086, 'f': 0.021310559100041794, 's': 0.03047027247503613, 'h': 0.007165625141625585, 'r': 0.008001530815209455, 'u': 0.02288165892027172, 'p': 0.010262504594963416, 'k': 0.007664147199967772, 'c': 0.011108481421241068, 'v': 0.0075181154859079394, 'g': 0.004431307185263889, 'q': 0.0004229884131388258, 'b': 0.008459768262776515, 'n': 0.0046327302391395205, 'j': 0.0007553364520336175, 'z': 0.00016113844310050506, 'x': 1.0071152693781566e-05},
        'b': {'o': 0.11760442025219509, 'h': 0.0006291200525178479, 'u': 0.11832927596487869, 'l': 0.1180967750759047, 'a': 0.07944692141469953, 's': 0.023154353237232965, 'e': 0.3100741267540141, 't': 0.010189009546212971, 'i': 0.036830876118055744, 'y': 0.09443639049208129, 'r': 0.06612598812877814, 'b': 0.006318553570940124, 'v': 0.0017779479745069614, 'f': 0.00032823654913974673, 'j': 0.006605760551437402, 'm': 0.0027079515304029105, 'd': 0.002106184523646708, 'c': 0.0026395689159987965, 'n': 0.0011351513991082907, 'w': 0.0008889739872534807, 'g': 0.00015044175168905057, 'p': 0.0003966191635438606, 'k': 1.367652288082278e-05, 'q': 1.367652288082278e-05},
        'o': {'h': 0.012970289349158327, 's': 0.04299640576112533, 'c': 0.018516794662943138, 'l': 0.042758513691722906, 'm': 0.0645282238254079, 'n': 0.1715175962557857, 't': 0.0662529413285755, 'f': 0.11625940578698317, 'v': 0.029255552969772194, 'r': 0.11756005481860729, 'b': 0.013234039252191451, 'u': 0.10986993509683758, 'k': 0.012895301631629302, 'a': 0.015620717296304916, 'w': 0.04818348718744343, 'i': 0.015641403563209474, 'd': 0.02129651177824322, 'o': 0.03353761021901585, 'p': 0.023861608874408503, 'y': 0.006081762469940268, 'g': 0.007878881907273809, 'e': 0.006017117885863522, 'q': 0.0002689214697592636, 'j': 0.00130840638171334, 'z': 0.0004447547384480128, 'x': 0.001243761797636594},
        'h': {'e': 0.48080284859861305, 'o': 0.08219931364795095, 'a': 0.16624519265039833, 'i': 0.14222626535551475, 'm': 0.005529512798666671, 't': 0.04110644566719054, 'r': 0.012399822132307765, 'p': 0.003414788137175366, 'h': 0.009650340630208316, 'b': 0.003160206516610602, 'y': 0.007932763296798042, 'u': 0.010468396237623091, 'w': 0.006446006632699821, 's': 0.00845210980275016, 'l': 0.0029599356417663214, 'c': 0.004426325776219361, 'n': 0.0028547085719328857, 'f': 0.0030142463874868043, 'v': 0.0007705337049093519, 'd': 0.0028173699342500533, 'g': 0.0020468362293407016, 'q': 0.0001561433939463885, 'j': 0.0002885258366400657, 'k': 0.0005974182029253126, 'z': 3.054979446777166e-05, 'x': 3.394421607530185e-06},
        'm': {'i': 0.0973432518597237, 'e': 0.25406384067383003, 'a': 0.19650490022434763, 'h': 0.011217381036722164, 'm': 0.029834297634510173, 'o': 0.1187940331404731, 's': 0.03754083520289684, 'p': 0.07073641122525288, 'y': 0.03351832172235998, 'w': 0.012122643366001495, 'b': 0.03136930767111426, 't': 0.03735978273704097, 'u': 0.032424135080883223, 'c': 0.005313496280552604, 'f': 0.006376195536663124, 'r': 0.0066280946195930255, 'n': 0.00670681308300862, 'l': 0.004463336875664187, 'g': 0.002023064509780769, 'd': 0.0031802259219900026, 'v': 0.0011571614122092336, 'j': 0.0004250797024442083, 'k': 0.0006612350926909907, 'x': 7.871846341559413e-06, 'q': 0.00019679615853898533, 'z': 3.148738536623765e-05},
        'k': {'h': 0.04639882858973186, 'i': 0.18486318294133797, 'e': 0.29581159818187364, 's': 0.06217015954363808, 't': 0.039077514413837285, 'b': 0.010402367224916872, 'n': 0.09743448949086361, 'u': 0.027698971965467802, 'a': 0.0677221561270248, 'w': 0.02016411945944297, 'o': 0.0528354839693725, 'l': 0.023946798450321834, 'm': 0.00826698392361429, 'p': 0.008236478447881395, 'd': 0.004880876117263048, 'v': 0.0015252737866447027, 'r': 0.00857203868094323, 'c': 0.00857203868094323, 'f': 0.0112870260211708, 'g': 0.0034776242335499224, 'y': 0.014093529788597053, 'j': 0.0008541533205210335, 'k': 0.0010981971263841859, 'q': 0.0005490985631920929, 'z': 6.101095146578811e-05},
        'w': {'a': 0.21408165694560172, 'o': 0.08668610879657183, 'h': 0.2059278657302702, 'e': 0.1521743443240884, 'i': 0.17943300400745943, 'n': 0.04255445780264254, 's': 0.02216997976431377, 'l': 0.0066956314724437565, 'r': 0.012438995357695512, 'p': 0.003075030750307503, 'y': 0.005049002102924255, 'd': 0.00887791135975876, 't': 0.021406181803753522, 'c': 0.005326746815855255, 'w': 0.011278419235805262, 'm': 0.005128357735190255, 'q': 0.00036701979923025034, 'f': 0.005108518827123755, 'j': 0.000962187041225251, 'b': 0.005257310637622505, 'u': 0.0018350989961512518, 'v': 0.0007737174145935007, 'k': 0.0012200928460897513, 'z': 6.943617823275007e-05, 'g': 0.002083085346982502, 'x': 1.983890806650002e-05},
        'y': {'s': 0.09065481520789802, 'o': 0.15278653002111595, 'e': 0.06650967905984323, 'w': 0.04854454799730246, 'b': 0.044100250959061615, 'a': 0.11504317159187645, 'i': 0.06461919449880048, 'm': 0.03312217394669054, 'f': 0.03201662741976496, 't': 0.11114059235182913, 'p': 0.03285684278022841, 'h': 0.0369141985340453, 'l': 0.024001415099554464, 'd': 0.03158546427426398, 'c': 0.03510110222988735, 'j': 0.0026090898035443823, 'r': 0.023846638585784882, 'g': 0.013653499607530983, 'u': 0.008026267785479753, 'y': 0.006235282411860303, 'n': 0.016428421390114203, 'k': 0.003957856566393597, 'v': 0.0040684112190861555, 'q': 0.0014261550197340056, 'z': 0.00039799674969321085, 'x': 0.0003537748886161874},
        'p': {'s': 0.023987945349554524, 'r': 0.16786505263796608, 'a': 0.12791885359465227, 'e': 0.17682513677780812, 'l': 0.09274597251296987, 'o': 0.12549174276670408, 'p': 0.06223516681330461, 'i': 0.07450218945622604, 't': 0.048774814679975326, 'u': 0.04130133592225155, 'h': 0.029448944712437933, 'f': 0.00356987550944045, 'w': 0.004469929108137901, 'c': 0.0031552440763326357, 'b': 0.002952984840670287, 'm': 0.0031956959234651053, 'y': 0.007342010254543248, 'k': 0.00044497031845716655, 'g': 0.0007180202866013369, 'd': 0.0009607313693961551, 'j': 0.00036406662419222717, 'n': 0.0013349109553714997, 'v': 0.00021237219744546585, 'x': 2.0225923566234842e-05, 'q': 0.00016180738852987874},
        'f': {'h': 0.024842767295597486, 'e': 0.09096325719960278, 'o': 0.15508937437934459, 'i': 0.1009682224428997, 'a': 0.1007282356835485, 't': 0.1755627275736511, 'r': 0.10033101621979477, 'd': 0.007629923866269447, 'm': 0.01353856338960609, 'f': 0.06155246607083747, 's': 0.022500827540549488, 'c': 0.016492883151274413, 'u': 0.0320506454816286, 'p': 0.013066865276398543, 'l': 0.03117345249917246, 'v': 0.0030370738166170144, 'y': 0.006661701423369745, 'n': 0.007588546838795101, 'w': 0.013720622310493214, 'b': 0.011494538232373386, 'g': 0.006744455478318438, 'k': 0.0014812975835815955, 'q': 0.000264812975835816, 'j': 0.0023584905660377358, 'x': 5.792783846408474e-05, 'z': 9.930486593843098e-05},
        'x': {'i': 0.133034074678637, 'c': 0.13456437461742501, 't': 0.16853703325851868, 'a': 0.11660885533564579, 'p': 0.23015711079371556, 'f': 0.004386859824525607, 'd': 0.003774739849010406, 'e': 0.08651295653948174, 'w': 0.007549479698020812, 'n': 0.0020403999183840034, 'o': 0.022648439094062438, 'u': 0.01265047949398082, 'l': 0.002550499897980004, 's': 0.0071413997143440116, 'k': 0.000612119975515201, 'h': 0.01754743929810243, 'v': 0.013364619465415221, 'r': 0.011120179555192818, 'b': 0.002448479902060804, 'q': 0.0007141399714344012, 'y': 0.0065292797388288104, 'x': 0.010508059579677617, 'm': 0.003774739849010406, 'g': 0.0007141399714344012, 'j': 0.0005100999795960009},
        'g': {'a': 0.11600755628503298, 'm': 0.012975751757455637, 'i': 0.08110619057941841, 's': 0.03736851341447049, 't': 0.08873473516872607, 'f': 0.016939704561642562, 'h': 0.13233821601478224, 'r': 0.08466755442693011, 'e': 0.1429810163822737, 'y': 0.005058168942842691, 'o': 0.08775406976144023, 'u': 0.03697624725155616, 'n': 0.029419962218574836, 'c': 0.0113653959307547, 'l': 0.04083697211813405, 'g': 0.013708670114479782, 'w': 0.01962363093947746, 'b': 0.015504836228876983, 'd': 0.009207932034725879, 'p': 0.012449289275649561, 'j': 0.0014038999514828694, 'v': 0.0019510080208107522, 'k': 0.0007948551195895657, 'q': 0.0006503360069369175, 'z': 0.00015484190641355176, 'x': 2.06455875218069e-05},
        'j': {'u': 0.3454658578317001, 'o': 0.28884741017265514, 'a': 0.09877119303157567, 'e': 0.2507388396329134, 's': 0.0010888163011354799, 'f': 0.001244361487011977, 'b': 0.0015554518587649713, 'r': 0.0009332711152589828, 'w': 0.0020220874163944624, 'k': 0.0006221807435059885, 't': 0.0015554518587649713, 'c': 0.0010888163011354799, 'q': 0.00031109037175299425, 'i': 0.002644268159900451, 'g': 0.0006221807435059885, 'p': 0.0004666355576294914, 'm': 0.0004666355576294914, 'h': 0.0007777259293824856, 'l': 0.00031109037175299425, 'd': 0.00031109037175299425, 'n': 0.00015554518587649713},
        'q': {'u': 0.9980306345733042, 't': 0.0002188183807439825, 'o': 0.0002188183807439825, 'a': 0.0006564551422319475, 'r': 0.000437636761487965, 'p': 0.0002188183807439825, 's': 0.0002188183807439825},
        'z': {'e': 0.42028985507246375, 'h': 0.043741765480895915, 'a': 0.09196310935441371, 'i': 0.10223978919631094, 'w': 0.007641633728590251, 'z': 0.021870882740447958, 'l': 0.020289855072463767, 'y': 0.008432147562582345, 't': 0.005270092226613966, 'f': 0.001844532279314888, 's': 0.002635046113306983, 'u': 0.04453227931488801, 'o': 0.1876152832674572, 'g': 0.0005270092226613965, 'r': 0.0013175230566534915, 'c': 0.0015810276679841897, 'p': 0.0015810276679841897, 'n': 0.006060606060606061, 'b': 0.002108036890645586, 'v': 0.0013175230566534915, 'm': 0.017391304347826087, 'd': 0.008432147562582345, 'k': 0.001054018445322793, 'q': 0.00026350461133069827},

   }
    def markov_probability(message, transition_matrix):
        message = message.lower()
        probability = 0
        for i in range(1, len(message)):
            prev_char = message[i - 1]
            curr_char = message[i]
            if prev_char in transition_matrix and curr_char in transition_matrix[prev_char]:
                probability += transition_matrix[prev_char][curr_char]
        return probability
    precision+= math.floor(markov_probability(message, english_transition_matrix))
    return precision

def sub_decrypt(message, key):
    chars = "abcdefghijklmnopqrstuvwxyz"
    message = message.upper()
    translation_table = str.maketrans(''.join(chars.upper()), ''.join(key))
    return message.translate(translation_table)

def substitution(ciphertext, brute_precision, crib, spaces):
    if brute_precision==0:
        brute_precision=9999999
    letter_freq_dict={}
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        letter_freq_dict[letter]=0
    for i in alphabet:
        for letter in ciphertext:
            if letter==i:
                letter_freq_dict[i]+=1
    corpus_freq = list("etaoinshrdlcumwfgypbvkjxqz")
    message_freq = sorted(letter_freq_dict.items(), key=lambda item: item[1], reverse=True)
    best_key_dict = {message_freq[i][0]: corpus_freq[i] for i in range(len(corpus_freq))}
    best_key = "".join(best_key_dict.get(char, char) for char in "abcdefghijklmnopqrstuvwxyz")
    solved = False
    crib_list = crib.split(",")
    chars = "abcdefghijklmnopqrstuvwxyz"
    total_iterations=0
    best_score = 0
    iterations=0
    while not solved:
        ranA, ranB = random.sample(range(len(chars)), 2)
        new_key = list(best_key)
        new_key[ranA], new_key[ranB] = new_key[ranB], new_key[ranA]
        plaintext = sub_decrypt(ciphertext, new_key)
        current_score = english_detect_numVar(plaintext, crib_list, spaces,total_iterations)
        print(f"Current Key: {''.join(new_key)}")
        #print(f"Plaintext: {plaintext}")
        print(f"Current Score: {current_score}, Best Score: {best_score}")
        if current_score > best_score:
            best_score = current_score
            best_key = new_key
            iterations=0
        if best_score >= brute_precision:
            solved = True
            return sub_decrypt(ciphertext,best_key)
        if iterations >1000 and best_score > 800:
            solved = True
            return sub_decrypt(ciphertext,best_key)
                
        if iterations > 1000 and best_score <800:
            shuffle=list(generate_random_key())
            new_key=shuffle
            best_key=shuffle
            best_score=0
            iterations=0
            total_iterations=0
        iterations+=1
        total_iterations+=1
        print(iterations)
    return None

def generate_shuffled_key(table):
    
    flat_table = [cell for row in table for cell in row]
    random.shuffle(flat_table)
    rows, cols = len(table), len(table[0])
    shuffled_table = [flat_table[i * cols:(i + 1) * cols] for i in range(rows)]
    
    return shuffled_table

def caesar_shift(message,brute_precision):
    from cipher import english_detect
    letters_caesar='abcdefghijklmnopqrstuvwxyz'
    output_brute=""
    for i in range(26):
        output_caesar=''
        for letter in message:
            if letter not in letters_caesar:
                output_caesar += letter
            else:
                index=(letters_caesar.find(letter))
                shifted_index= (index + i) % len(letters_caesar)
                output_caesar += letters_caesar[shifted_index]
        if english_detect(output_caesar,brute_precision):
            output_brute += f"{i + 1}: {output_caesar}\n"
    return output_brute

def english_detect(message,precision_percentage):
    english_percentage_dict = {
        "th": 2.9, "he": 2.48, "in": 1.87, "er": 1.73, "an": 1.65,
        "re": 1.38, "es": 1.35, "st": 1.19, "on": 1.17, "nd": 1.14,
        "en": 1.13, "at": 1.08, "nt": 1.08, "ed": 1.04, "ea": 1.01,
        "to": 1.0, "or": 0.96, "ti": 0.96, "ha": 0.94, "ar": 0.89,
        "ng": 0.89, "is": 0.89, "it": 0.88, "te": 0.88, "ou": 0.85,
        "et": 0.84, "of": 0.82, "al": 0.82, "as": 0.8, "le": 0.74,
        "se": 0.73, "hi": 0.72, "sa": 0.68, "ra": 0.64, "ro": 0.64,
        "ne": 0.64, "ve": 0.63, "me": 0.62, "ri": 0.62, "so": 0.6,
        "de": 0.59, "ll": 0.58, "ta": 0.58, "li": 0.57, "si": 0.57,
        "el": 0.55, "ec": 0.52, "co": 0.52, "no": 0.52, "ot": 0.51,
        "ma": 0.5, "di": 0.5, "ic": 0.49, "la": 0.49, "ho": 0.49,
        "om": 0.48, "tt": 0.48, "na": 0.48, "sh": 0.47, "ch": 0.46,
        "be": 0.46, "ss": 0.46, "rt": 0.46, "ee": 0.45, "em": 0.45,
        "ns": 0.44, "rs": 0.44, "ce": 0.43, "ur": 0.42, "ei": 0.41,
        "ca": 0.41, "io": 0.41, "ac": 0.4, "ts": 0.4, "da": 0.39,
        "lo": 0.39, "us": 0.39, "wa": 0.38, "ni": 0.38, "dt": 0.38,
        "pe": 0.38, "fo": 0.38, "ew": 0.37, "ut": 0.37, "wi": 0.36,
        "il": 0.36, "eo": 0.36, "ly": 0.36, "wh": 0.36, "ad": 0.35,
        "un": 0.34, "ow": 0.34, "tr": 0.34, "nc": 0.33, "ft": 0.33,
        "do": 0.32, "ge": 0.32, "ep": 0.32, "mo": 0.32, "we": 0.31
    }
    freq_dict = {}
    message=message.lower()
    for i in range(1, len(message)):
        bigram = message[i-1:i+1]
        if bigram in freq_dict:
            freq_dict[bigram] += 1
        else:
            freq_dict[bigram] = 1
    total_bigrams=0
    for i in freq_dict:
        total_bigrams+=freq_dict.get(i)
    percentage_dict={}
    for i in freq_dict:
        percentage_dict[i]=(freq_dict.get(i)/total_bigrams*100)
    precision=0
    for i in english_percentage_dict:
        if percentage_dict.get(i) is not None and (english_percentage_dict.get(i)-0.5) <= percentage_dict.get(i,0) <= (english_percentage_dict.get(i)+0.5):
            precision += 1
        else:
            pass
    if precision >= precision_percentage:
        return True
    else:
        return False
    
def columnar_transposition():
    pass

def space_remover(text):
    output=""
    for i in range(len(text)):
        if text[i]!=" ":
            output+=text[i]
    return output
    
def text_reverser(text):
    output=""
    for i in range(len(text)):
            output+=text[-i-1]
    return output

def vigenere():
    pass

def morse(ciphertext):
    morslet=""
    word=""
    curval=""
    plaintext=""
    alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"]
    morse_code= [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..",".----","..---","...--","....-",".....","-....","--...","---..","----.","-----"]
    for i in range(0,len(ciphertext)):
        curval=ciphertext[i]
        if curval==" ":
            for i in range(0,len(morse_code)):
                if morslet==morse_code[i]:
                    letter=alphabet[i]
            morslet=""
            word+=letter
            letter=""
        elif curval=="/":
            plaintext+=word
            plaintext+=" "
            word=""
        elif curval!=" "or"/":
            morslet+=curval
    return plaintext

def find_repeats(sequence, min_length=3):
    """Finds repeated substrings in the sequence that may indicate the key length."""
    repeats = {}
    for length in range(min_length, len(sequence) // 2):
        seen_substrings = {}
        for i in range(len(sequence) - length):
            substring = sequence[i:i+length]
            if substring in seen_substrings:
                if substring not in repeats:
                    repeats[substring] = []
                repeats[substring].append(i - seen_substrings[substring])
            seen_substrings[substring] = i
    return repeats

def kasiski_analysis(ciphertext, max_key_length=20):
    """Applies the Kasiski examination to guess the key length."""
    repeats = find_repeats(ciphertext)
    spacings = []
    for positions in repeats.values():
        spacings.extend(positions)
    
    if not spacings:
        return 1  # fallback if no patterns are found
    
    key_length_guesses = gcd(spacings)
    if key_length_guesses < 1 or key_length_guesses > max_key_length:
        return min(max_key_length, len(ciphertext))  # limit max key length
    return key_length_guesses

def gcd(numbers):
    """Calculates the greatest common divisor for a list of numbers."""
    from math import gcd
    from functools import reduce
    return reduce(gcd, numbers)

def frequency_score(text):
    """Calculates a score based on the frequency of common English letters."""
    english_freq = {
        'E': 12.7, 'T': 9.1, 'A': 8.2, 'O': 7.5, 'I': 7.0,
        'N': 6.7, 'S': 6.3, 'H': 6.1, 'R': 6.0, 'D': 4.3,
        'L': 4.0, 'C': 2.8, 'U': 2.8, 'M': 2.4, 'W': 2.4,
        'F': 2.2, 'G': 2.0, 'Y': 2.0, 'P': 1.9, 'B': 1.5,
        'V': 1.0, 'K': 0.8, 'X': 0.2, 'J': 0.2, 'Q': 0.1, 'Z': 0.1
    }
    score = sum(english_freq.get(letter, 0) for letter in text.upper())
    return score

def decrypt_caesar(text, shift):
    """Decrypts a text using Caesar shift."""
    decrypted_text = []
    for char in text:
        if char in string.ascii_uppercase:
            decrypted_text.append(chr((ord(char) - shift - 65) % 26 + 65))
        else:
            decrypted_text.append(char)
    return ''.join(decrypted_text)

def decrypt_with_key(ciphertext, key):
    """Decrypts the ciphertext using the provided Vigenère key."""
    decrypted_text = []
    key_repeats = (len(ciphertext) // len(key)) + 1
    full_key = (key * key_repeats)[:len(ciphertext)]
    
    for c, k in zip(ciphertext, full_key):
        if c in string.ascii_uppercase:
            shift = ord(k) - 65
            decrypted_text.append(chr((ord(c) - shift - 65) % 26 + 65))
        else:
            decrypted_text.append(c)
    return ''.join(decrypted_text)

def vigenere_crack(ciphertext, max_key_length=20):
    """Attempts to decrypt Vigenère cipher by trying different key lengths and analyzing letter frequencies."""
    ciphertext = ''.join(filter(str.isalpha, ciphertext)).upper()
    best_decrypted_text = ""
    best_score = -float('inf')
    probable_key = ""

    for key_length in range(1, max_key_length + 1):
        current_key = ''
        for i in range(key_length):
            segment = ciphertext[i::key_length]
            max_score = -float('inf')
            best_shift = 0

            for shift in range(26):
                decrypted_segment = decrypt_caesar(segment, shift)
                score = frequency_score(decrypted_segment)

                if score > max_score:
                    max_score = score
                    best_shift = shift

            current_key += chr(best_shift + 65)
        
        decrypted_text = decrypt_with_key(ciphertext, current_key)
        total_score = frequency_score(decrypted_text)

        if total_score > best_score:
            best_score = total_score
            best_decrypted_text = decrypted_text
            probable_key = current_key

    return best_decrypted_text, probable_key

def spaces_n_chars(ciphertext,nchars,split_char):
    j=0
    eightbit=""
    plaintext=""
    for i in ciphertext:
        if j == nchars:
            plaintext+=eightbit
            plaintext+=split_char
            eightbit=""
            j=0
        j=j+1
        eightbit=eightbit+i
    return (plaintext+eightbit)

def coord_pair(strA,strB):
    if len(strA)==len(strB):
        output=''
        for i in range(0,len(strA)):
            output+=strA[i]
            output+=strB[i]
        return (output)
    else:
        print("String lengths are different")


def letter_to_number(letter):
    """Convert a letter to its corresponding position (a=1, ..., z=26)."""
    return ord(letter) - ord('a') + 1

def number_to_letter(number):
    """Convert a number back to a letter (1=a, ..., 26=z)."""
    return chr((number - 1) % 26 + ord('a'))

def clean_text(text):
    chars="abcdefghijklmnopqrstuvwxyz"
    text = ""
    print("Enter your lines of text (type BREAK on an empty line to finish):")
    while True:
        line = input()
        if line == "BREAK":
            break
        text += line
    text=text.lower()
    text2=""
    for i in range(0,len(text)):
        if text[i] in chars:
            text2+=text[i]
        else:
            pass
    return text2
