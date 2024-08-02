first_greeting = [
    'ga',
    'gm',
    'ge',
    'ga om',
    'gm om',
    'ge om',
    'gm {name}',
    'ga {name}',
    'ge {name}',
    'de {callsign}',
    'de {randsign}',
    'gm {callsign} de {randsign}',
    'ga {callsign} de {randsign}',
    'ge {callsign} de {randsign}'
]

second_greeting = [
    'bk r r tu',
    'bk r de {randsign}',
    'bk r de {callsign}',
    'r r r tu',
    'tu',
    'bk tu',
    'bk r r',
    'bk r qsl tu',
    'qsl qsl tu'
]

ending_templates = [
    '{br} e e',
    '{callsign} de {randsign} {br} e s 88 gl e e',
    '{br} e s gl e e',
    '{br} e s gl de {randsign} e e',
    'e e',
    'gl e s {br} de {randsign} e e',
    'gl e s {br} e e',
    'gl {name} {br} de {randsign} e e',
    '{br} {name} de {randsign} e e',
    '{br} {name} e e',
    '{br}'
]

ota_phrases = [
    'Cq cq pota de {randsign}',
    'Cq cq sota de {randsign}',
    'Cq cq pota de {randsign} k',
    'Cq cq sota de {randsign} k',
    '{randsign} {greeting1} ur {sig} {sig} {state} {ota} bk',
    '{callsign} {greeting1} ur {sig} {sig} {state} {ota} bk',
    '{randsign} {greeting1} ur {sig} {sig} {ota} bk',
    '{callsign} {greeting1} ur {sig} {sig} {ota} bk',
    '{greeting2} {sig} {sig} {state} {state} {ota} bk',
    '{greeting2} {sig} {sig} {state} {state} {ota} {ending} bk',
    '{greeting2} {state} {state} {ota} bk',
    '{greeting2} {state} {state} {ota} {ending}',
    '{greeting2} {ending}',
    '{ending}'
]

ragchew_phrases = [
    'cq cq de {randsign} {randsign} k',
    'cq cq de {callsign} {callsign} k',
    '{callsign} de {randsign} ga rst {sig} op {randname} rig 100w ant dipole qth {state} bk',
    '{callsign} de {randsign} gm rst {sig} op {randname} rig 5w ant vert qth {state} bk',
    '{callsign} de {randsign} ge rst {sig} rig yaesu 100w ant efhw qth {state} bk',
    'bk {callsign} de {randsign} thx {randname} qth {state} rst {sig} {ending}',
    '{callsign} de {randsign} qsl thx rig 5w qrp ant efhw {ending}',
    'bk qsl qsl thx {callsign} de {randsign} qth {state}',
    '{callsign} de {randsign} thx fer call name is {randname} bt qth {state} {state} ur {sig} hw copy?',
    '{callsign} de {randsign} thx {randname} for nice report bt rig is 100w ant is dipole wx sunny hw copy?',
    '{callsign} de {randsign} qsl wx is cloudy hw abt you?',
    'bk thx fer call {callsign} name is {randname} qth is {state} ur rst {sig}',
    '{callsign} de {randsign} thx fer qso {ending}',
    'sri {name} no copy no copy qrm qrm {ending}',
    'thx {name} good sig wx is sunny '
    '{ending}'
]

states = [
    'al',
    'ak',
    'az',
    'ar',
    'as',
    'ca',
    'co',
    'ct',
    'de',
    'dc',
    'fl',
    'ga',
    'gu',
    'hi',
    'id',
    'il',
    'in',
    'ia',
    'ks',
    'ky',
    'la',
    'me',
    'md',
    'ma',
    'mi',
    'mn',
    'ms',
    'mo',
    'mt',
    'ne',
    'nv',
    'nh',
    'nj',
    'nm',
    'ny',
    'nc',
    'nd',
    'mp',
    'oh',
    'ok',
    'or',
    'pa',
    'pr',
    'ri',
    'sc',
    'sd',
    'tn',
    'tx',
    'tt',
    'ut',
    'vt',
    'va',
    'vi',
    'wa',
    'wv',
    'wi',
    'wy'
]

callsign_format = [
    'PNS',
    'PPNS',
    'PNSS',
    'PNSSS',
    'PPNSS',
    'PPNSSS',
    'PPNSSSS'
]

parks = [
    'US3791',
    'US4567',
    'US4556',
    'US4581',
    'US4572',
    'US4239',
    'US9935',
    'US1126',
    'US1181',
    'US0063',
    'W6/CT225',
    'W6/CT226',
    'W7I/IC172',
    'W70/CE188',
    'W0C/FR063',
    'W0C/FR194',
    'WOI/IA001',
    'W7M/FS149',
    'W7M/FS089',
    'W0C/PR082'
]

names = [
    'steve',
    'mike',
    'paul',
    'julie',
    'laura',
    'jenny',
    'will',
    'casey',
    'katie',
    'stacey'
]