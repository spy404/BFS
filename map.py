import utils


cities = {
    'Araak': {
        'x': 4970,
        'y': 3408,
        'neighbors': {
            'Qom': 131,
            'Khorramabad': 205,
            'Malayer': 106,
        },
    },
    'Ardabil': {
        'x': 4829,
        'y': 3824,
        'neighbors': {
            'Tabriz': 215,
            'Rasht': 254,
            'Parsabad': 203,
            'Mianeh': 154,
        },
    },
    'Urmia': {
        'x': 4507,
        'y': 3755,
        'neighbors': {
            'Tabriz': 146,
            'Mahabad': 130,
        },
    },
    'Isfahan': {
        'x': 5167,
        'y': 3267,
        'neighbors': {
            'Yazd': 311,
            'Shahrekord': 104,
            'Kashan': 207,
            'Eghlid': 256,
            'Yasuj': 330,
        },
    },
    'Ahvaz': {
        'x': 4871,
        'y': 3134,
        'neighbors': {
            'Dezful': 148,
            'Abadan': 124,
        },
    },
    'Bojnurd': {
        'x': 5732,
        'y': 3747,
        'neighbors': {
            'Mashhad': 258,
            'Gorgan': 305,
            'Sabzevar': 178,
        },
    },
    'Bandar-Abbas': {
        'x': 5630,
        'y': 2719,
        'neighbors': {
            'Chabahar': 663,
            'Sirjan': 311,
            'Jahrom': 419,
            'Jiroft': 295,
        },
    },
    'Tabriz': {
        'x': 4630,
        'y': 3807,
        'neighbors': {
            'Ardabil': 215,
            'Urmia': 146,
            'Parsabad': 329,
            'Mahabad': 217,
            'Mianeh': 160,
        },
    },
    'Tehran': {
        'x': 5138,
        'y': 3570,
        'neighbors': {
            'Qazvin': 150,
            'Qom': 145,
            'Hamedan': 317,
            'Amol': 180,
            'Sari': 248,
            'Saveh': 141,
            'Semnan': 222,
        },
    },
    'Khorramabad': {
        'x': 4835,
        'y': 3348,
        'neighbors': {
            'Araak': 205,
            'Kermanshah': 188,
            'Malayer': 165,
            'Ilam': 252,
            'Dezful': 188,
        },
    },
    'Rasht': {
        'x': 4959,
        'y': 3728,
        'neighbors': {
            'Ardabil': 254,
            'Qazvin': 175,
        },
    },
    'Zahedan': {
        'x': 6085,
        'y': 2950,
        'neighbors': {
            'Bam': 321,
            'Zabol': 211,
            'Birjand': 451,
        },
    },
    'Sanandaj': {
        'x': 4699,
        'y': 3531,
        'neighbors': {
            'Kermanshah': 134,
            'Hamedan': 176,
        },
    },
    'Shiraz': {
        'x': 5253,
        'y': 2959,
        'neighbors': {
            'Eghlid': 206,
            'Yasuj': 175,
            'Kazeroon': 133,
            'Sirjan': 386,
            'Jahrom': 188,
        },
    },
    'Qazvin': {
        'x': 5000,
        'y': 3627,
        'neighbors': {
            'Tehran': 150,
            'Rasht': 175,
            'Hamedan': 239,
            'Saveh': 157,
            'Zanjan': 181,
        },
    },
    'Zanjan': {
        'x': 4849,
        'y': 3664,
        'neighbors': {
            'Mianeh': 136,
            'Qazvin': 181,
        },
    },
    'Qom': {
        'x': 5087,
        'y': 3464,
        'neighbors': {
            'Araak': 131,
            'Tehran': 145,
            'Saveh': 79,
            'Kashan': 108,
        },
    },
    'Kerman': {
        'x': 5707,
        'y': 3028,
        'neighbors': {
            'Bam': 192,
            'Sirjan': 183,
            'Rafsanjan': 115,
            'Yazd': 361
        },
    },
    'Kermanshah': {
        'x': 4707,
        'y': 3432,
        'neighbors': {
            'Khorramabad': 188,
            'Sanandaj': 134,
            'Hamedan': 188,
            'Ilam': 168,
        },
    },
    'Gorgan': {
        'x': 5443,
        'y': 3684,
        'neighbors': {
            'Bojnurd': 305,
            'Shahrud': 205,
            'Sari': 142,
        },
    },
    'Mashhad': {
        'x': 5954,
        'y': 3632,
        'neighbors': {
            'Bojnurd': 258,
            'Torbat_heydariyeh': 155,
            'Neyshabur': 138,
        },
    },
    'Torbat_heydariyeh': {
        'x': 5921,
        'y': 3526,
        'neighbors': {
            'Birjand': 372,
            'Neyshabur': 171,
            'Mashhad': 155,
        },
    },
    'Hamedan': {
        'x': 4851,
        'y': 3479,
        'neighbors': {
            'Tehran': 317,
            'Sanandaj': 176,
            'Qazvin': 239,
            'Kermanshah': 188,
            'Saveh': 198,
            'Malayer': 86,
        },
    },
    'Yazd': {
        'x': 5435,
        'y': 3188,
        'neighbors': {
            'Isfahan': 311,
            'Kerman': 361,
            'Eghlid': 219,
            'Rafsanjan': 248,
        },
    },
    'Parsabad': {
        'x': 4791,
        'y': 3964,
        'neighbors': {
            'Ardabil': 203,
            'Tabriz': 329,
        },
    },
    'Shahrekord': {
        'x': 5085,
        'y': 3232,
        'neighbors': {
            'Isfahan': 104,
        },
    },
    'Mahabad': {
        'x': 4570,
        'y': 3675,
        'neighbors': {
            'Urmia': 130,
            'Tabriz': 217,
        },
    },
    'Mianeh': {
        'x': 4768,
        'y': 3741,
        'neighbors': {
            'Tabriz': 160,
            'Ardabil': 154,
            'Zanjan': 136
        },
    },
    'Amol': {
        'x': 5234,
        'y': 3644,
        'neighbors': {
            'Sari': 75,
            'Tehran': 180,
        },
    },
    'Sari': {
        'x': 5305,
        'y': 3656,
        'neighbors': {
            'Amol': 75,
            'Gorgan': 142,
            'Tehran': 248,
        },
    },
    'Saveh': {
        'x': 5037,
        'y': 3500,
        'neighbors': {
            'Tehran': 141,
            'Qom': 79,
            'Hamedan': 198,
            'Qazvin': 157,
        },
    },
    'Malayer': {
        'x': 4881,
        'y': 3427,
        'neighbors': {
            'Hamedan': 86,
            'Araak': 106,
            'Khorramabad': 165,
        },
    },
    'Ilam': {
        'x': 4642,
        'y': 3362,
        'neighbors': {
            'Kermanshah': 168,
            'Khorramabad': 252,
        },
    },
    'Dezful': {
        'x': 4842,
        'y': 3237,
        'neighbors': {
            'Ahvaz': 148,
            'Khorramabad': 188,
        },
    },
    'Abadan': {
        'x': 4828,
        'y': 3035,
        'neighbors': {
            'Ahvaz': 124,
        },
    },
    'Kashan': {
        'x': 5143,
        'y': 3397,
        'neighbors': {
            'Isfahan': 207,
            'Qom': 108,
        },
    },
    'Eghlid': {
        'x': 5269,
        'y': 3088,
        'neighbors': {
            'Yasuj': 160,
            'Shiraz': 206,
            'Yazd': 219,
            'Isfahan': 256,
        },
    },
    'Yasuj': {
        'x': 5158,
        'y': 3063,
        'neighbors': {
            'Eghlid': 160,
            'Shiraz': 175,
            'Isfahan': 330,
        },
    },
    'Kazeroon': {
        'x': 5165,
        'y': 2959,
        'neighbors': {
            'Shiraz': 133,
            'Bushehr': 195,
        },
    },
    'Bushehr': {
        'x': 5085,
        'y': 2892,
        'neighbors': {
            'Kazeroon': 195,
        },
    },
    'Sirjan': {
        'x': 5566,
        'y': 2941,
        'neighbors': {
            'Kerman': 183,
            'Rafsanjan': 173,
            'Bandar-Abbas': 311,
            'Shiraz': 386,
        },
    },
    'Rafsanjan': {
        'x': 5600,
        'y': 3037,
        'neighbors': {
            'Sirjan': 173,
            'Kerman': 115,
            'Yazd': 248,
        },
    },
    'Jahrom': {
        'x': 5355,
        'y': 2847,
        'neighbors': {
            'Shiraz': 188,
            'Bandar-Abbas': 419,
        },
    },
    'Jiroft': {
        'x': 5772,
        'y': 2864,
        'neighbors': {
            'Bam': 116,
            'Bandar-Abbas': 295,
        },
    },
    'Bam': {
        'x': 5835,
        'y': 2909,
        'neighbors': {
            'Iranshahr': 355,
            'Jiroft': 116,
            'Zahedan': 321,
            'Kerman': 192,
        },
    },
    'Iranshahr': {
        'x': 6069,
        'y': 2720,
        'neighbors': {
            'Bam': 355,
            'Chabahar': 331,
        },
    },
    'Chabahar': {
        'x': 6065,
        'y': 2527,
        'neighbors': {
            'Iranshahr': 331,
            'Bandar-Abbas': 663,
        },
    },
    'Zabol': {
        'x': 6148,
        'y': 3102,
        'neighbors': {
            'Zahedan': 211,
        },
    },
    'Birjand': {
        'x': 5921,
        'y': 3285,
        'neighbors': {
            'Zahedan': 451,
            'Torbat_heydariyeh': 372,
        },
    },
    'Neyshabur': {
        'x': 5879,
        'y': 3618,
        'neighbors': {
            'Torbat_heydariyeh': 171,
            'Mashhad': 138,
            'Sabzevar': 116,
        },
    },
    'Sabzevar': {
        'x': 5768,
        'y': 3618,
        'neighbors': {
            'Neyshabur': 116,
            'Bojnurd': 178,
            'Shahrud': 280,
        },
    },
    'Shahrud': {
        'x': 5496,
        'y': 3641,
        'neighbors': {
            'Sabzevar': 280,
            'Semnan': 181,
            'Gorgan': 205,
        },
    },
    'Semnan': {
        'x': 5338,
        'y': 3557,
        'neighbors': {
            'Shahrud': 181,
            'Tehran': 222,
        },
    },
}


for key, val in cities.items():
    val['pygame_x'] = val['x'] * 100 // 220 - 1980
    val['pygame_y'] = utils.SCREEN_HEIGH - (val['y'] * 100 // 230 - 1050)
