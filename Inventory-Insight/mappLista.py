mapp_konfiguration = {
    'ahlsell': {'filtyp': 'csv', 'kolumner': ['"PARTNO"', '"QTYAVAIL"'], 'has_header': True},
    'aida': {'filtyp': 'csv', 'kolumner': ['"Itemid"', '"Available stock"'], 'has_header': True},
    'Also': {'filtyp': 'txt', 'kolumner': ['ProductID', 'AvailableQuantity'], 'has_header': True, 'delimiter': '\t'},
    #'aps': {'filtyp': 'csv', 'kolumner': None, 'has_header': False},  # Uppdatera senare
    'asko': {'filtyp': 'csv', 'kolumner': ['"Artikelnummer"', '"Disponible"'], 'has_header': True},
    #'bastad-gruppen': {'filtyp': 'txt', 'kolumner': ['ProductID', 'AvailableQuantity'], 'has_header': False},  # X pga oklart kolumnamn   ###Hoppar över###
    'bauscher': {'filtyp': 'csv', 'kolumner': ['"A"', '"H"'], 'has_header': True},
    'bergqvist': {'filtyp': 'csv', 'kolumner': ['"Leverantörs Artikelnummer"', '"Lagersaldo"'], 'has_header': True},  # Uppdatera senare
    'blaklader': {'filtyp': 'csv', 'kolumner': ['partNo', 'dispStockValue'], 'has_header': True},
    'blocho': {'filtyp': 'csv', 'kolumner': ['"Artikel"', '"Antal i lager"'], 'has_header': True},
    'bntscandinavia': {'filtyp': 'csv', 'kolumner': ['"ARTIKELNUMMER"', '"LAGERSALDO"'], 'has_header': True},
    'brabantia': {'filtyp': 'csv', 'kolumner': ['"Leverantörs artikelnummer"', '"Lagersaldo"'], 'has_header': True},
    'briscapo': {'filtyp': 'csv', 'kolumner': ['"Artikelnummer"', '"Disponibelt"'], 'has_header': True},
    #'cenor': {'filtyp': 'csv', 'kolumner': ['"Leverantörs artikelnummer"', '"Lagersaldo"'], 'has_header': True}, # Hoppar över
    'craft': {'filtyp': 'csv', 'kolumner': ['"Item"', '"Quantity"'], 'has_header': True},
    'dahlander': {'filtyp': 'csv', 'kolumner': ['"Nummer"', '"Lager"'], 'has_header': True},
    #'davma': {'aktiv': False, 'filtyp': None, 'kolumner': None, 'has_header': None}, # Tom Map
    'Despec': {'filtyp': 'txt', 'kolumner': ['itemId', 'StockActual'], 'has_header': True},
    'durable': {'filtyp': 'csv', 'kolumner': ['Leverantörs artikelnummer', 'Lagersaldo'], 'has_header': True, 'delimiter': '~'},
    #'dzwellnes': {'filtyp': 'csv', 'kolumner': ['Article number', 'Quantity'], 'has_header': True},  # Oklart, Får Fel Kolumn
    'ekofekt': {'filtyp': 'csv', 'kolumner': ['Artnr', 'I Lager'], 'has_header': True},  
    'elstar': {'filtyp': 'csv', 'kolumner': ['"Leverantörs artikelnummer"', '"Lagersaldo"'], 'has_header': True},
    # 'emerio': {'filtyp': 'csv', 'kolumner': ['Supplier_Item_No', 'Stock_Situation'], 'has_header': True}, oklartt
    'ernstalexis': {'filtyp': 'csv', 'kolumner': ['"Artikelkod"', '"Saldo"'], 'has_header': True},
    'espressogear': {'filtyp': 'csv', 'kolumner': ['"ArticleNumber"', '"Stock"'], 'has_header': True}, 
    'etab': {'filtyp': 'csv', 'kolumner': ['"ArticleNumber"', '"Stock"'], 'has_header': True},
    #'excel': {'filtyp': 'csv', 'kolumner': None, 'has_header': True},  # Tom Map
    #'foh': {'filtyp': 'csv', 'kolumner': ['"ABR005CLT23"', '"766"'], 'has_header': True},  # Exempelvärden, verifiera, kolumnerna behöver fixas
    'fristads': {'filtyp': 'csv', 'kolumner': ['"Artnr"', '"Antal"'], 'has_header': True},
    'fritzmagnustrading': {'filtyp': 'csv', 'kolumner': ['"Article number"', '"Quantity"'], 'has_header': True}, 
    'gpbmnordic': {'filtyp': 'csv', 'kolumner': ['"Lev. Artikelnummer"', '"Lagersaldo"'], 'has_header': True},   
    #'greenman': {'filtyp': 'txt', 'kolumner': None, 'has_header': True},  # Specialhantering behövs
    'guneng': {'filtyp': 'csv', 'kolumner': ['"Item ID"', '"Lagersaldo"'], 'has_header': True},
    'habo': {'filtyp': 'csv', 'kolumner': ['"Artikel"', '"Disp.kvant"'], 'has_header': True},
    #'hallins': {'filtyp': 'csv', 'kolumner': None, 'has_header': True},  # Tom Map
    #'hartmann': {'filtyp': 'csv', 'kolumner': None, 'has_header': True},  # Tom Map
    'haxan': {'filtyp': 'csv', 'kolumner': ['"Article number"', '"Quantity"'], 'has_header': True},
    'headwear': {'filtyp': 'csv', 'kolumner': ['"Leverantörs artikelnummer"', '"Lagersaldo"'], 'has_header': True},
    'hecbekgroup': {'filtyp': 'csv', 'kolumner':['"Artikel nr"', '"Lagersaldo"'], 'has_header': True},  
    'hedlundgruppen': {'filtyp': 'csv', 'kolumner': ['"Leverantörs artikelnummer"', '"Lagersaldo"'], 'has_header': True},
    'hejco': {'filtyp': 'csv', 'kolumner': ['"ArticleNumber"', '"Stock"'], 'has_header': True},
    'hippie': {'filtyp': 'csv', 'kolumner':['"ArticleNumber"', '"Stock"'], 'has_header': True}, 
    'hisab': {'filtyp': 'csv', 'kolumner': ['"Leverantörs artikelnummer"', '"Lagersaldo"'], 'has_header': True},
    'hultafors': {'filtyp': 'csv', 'kolumner': ['"ItemNumber"', '"StockStatus"'], 'has_header': True},
    'id': {'filtyp': 'csv', 'kolumner': ['"VARENR"', '"DISPONIBEL"'], 'has_header': True},
    #'Intrum': {'filtyp': 'csv', 'kolumner': None, 'has_header': True},  # Tom map, hoppa över
    #'isolda': {'filtyp': 'csv', 'kolumner': None, 'has_header': True},  # Tom Map
    'jobman-workwear': {'filtyp': 'csv', 'kolumner': ['"Item"', '"Quantity"'], 'has_header': True},
    'kentaur': {'filtyp': 'csv', 'kolumner': ['"KENTAURARTICLE"', '"QUANTITYONSTOCK"'], 'has_header': True},
    #'kofax': {'filtyp': 'csv', 'kolumner': None, 'has_header': True},  # Tom Map
    'kongamek': {'filtyp': 'csv', 'kolumner': ['"Artikelnummer"', '"Saldo"'], 'has_header': True},
    'konstsmide': {'filtyp': 'csv', 'kolumner': ['"ITEMNO"', '"ATP1"'], 'has_header': True},
    'lidenweighing': {'filtyp': 'csv', 'kolumner': ['"LevArtNr"', '"Antal lager"'], 'has_header': True}, 
    #'lindenbaum': {'filtyp': 'csv', 'kolumner': ['"Header1"', '"Header3"'], 'has_header': True},  # Hoppar Över
    #'markslojd': {'filtyp': 'csv', 'kolumner': None, 'has_header': True},  # Tom Mapp
    #'matting': {'filtyp': 'csv', 'kolumner': ['"ItemNo"', '"Stock"'], 'has_header': True}, # Hoppar över
    #'merx': {'filtyp': 'xml', 'kolumner': None, 'has_header': True},  # Specialhantering behövs
    #'NewItem': {'filtyp': 'csv', 'kolumner': None, 'has_header': True},  # Tom Map
    #'norbag': {'filtyp': 'csv', 'kolumner': None, 'has_header': True},  # Tom Map / Specialhantering behövs
    'nordexia': {'filtyp': 'csv', 'kolumner': ['"Product number"', '"Lagerstatus"'], 'has_header': True},
    'onemed': {'filtyp': 'csv', 'kolumner': ['"Leverantörs artikelnummer"', '"Lagersaldo"'], 'has_header': True}, 
    'ordernordic': {'filtyp': 'txt', 'kolumner': None, 'has_header': True},  # Specialhantering behövs
    'patina': {'filtyp': 'csv', 'kolumner': ['"Artikelnummer"', '"Lagersaldo"'], 'has_header': True},
    'portwest': {'filtyp': 'csv', 'kolumner': ['"Item"', '"SoH"'], 'has_header': True},
    #'proheq': {'filtyp': 'csv', 'kolumner': ['01.0101.6060', '0'], 'has_header': True},  # Specialhantering behövs
    'rainwear': {'filtyp': 'csv', 'kolumner': ['"Item No."', '"Quantity"'], 'has_header': True},
    'realisera': {'filtyp': 'csv', 'kolumner': ['"Article number"', '"Stock"'], 'has_header': True},
    'redlunds': {'filtyp': 'csv', 'kolumner': ['"Artnr"', '"Disponibelt"'], 'has_header': True},
    'saponi': {'filtyp': 'csv', 'kolumner': ['"Kunds artikelnummer"', '"Totalt saldo"'], 'has_header': True},  
    'schönwald': {'filtyp': 'csv', 'kolumner': ['"A"', '"H"'], 'has_header': True},
    'seab': {'filtyp': 'csv', 'kolumner': ['"ProductId"', '"InStock"'], 'has_header': True},
    'securit': {'filtyp': 'csv', 'kolumner': ['"Artikelcode"', '"Beschikb."'], 'has_header': True},
    'segers': {'filtyp': 'csv', 'kolumner': ['"Product ID_SKU"', '"Available_Now"'], 'has_header': True},
    'severin': {'filtyp': 'csv', 'kolumner': ['"LeverantorsArtikelnummer"', '"Lagersaldo"'], 'has_header': True},
    #'skotbordspecialisten': {'filtyp': 'csv', 'kolumner': None, 'has_header': True},  # Tom Map
    #'soft touch':  {'aktiv': False, 'filtyp': None, 'kolumner': None, 'has_header': None}, # Tom Map
    #'soft_touch': {'filtyp': 'csv', 'kolumner': ['S-991-10', '144'], 'has_header': True},  # Specialhantering behövs
    #'star_trading': {'filtyp': 'xml'}, # Tom Map
    'sundqvist': {'filtyp': 'csv', 'kolumner': ['"ArticleNumber"', '"Stock"'], 'has_header': True},
    #'test':  {'aktiv': False, 'filtyp': None, 'kolumner': None, 'has_header': None}, # Tom Map
    #'testbolag':  {'aktiv': False, 'filtyp': None, 'kolumner': None, 'has_header': None}, # Tom Map
    #'texet': {'filtyp': 'csv', 'kolumner': ['"Item"', '"Quantity"'], 'has_header': True}, # Tom Map
    'texstar': {'filtyp': 'csv', 'kolumner': ['"ItemId"', '"Quantity"'], 'has_header': True}, 
    'trendmark': {'filtyp': 'csv', 'kolumner': ['"EAN-kod"', '"Saldo"'], 'has_header': True},
    'tura-scandinavia': {'filtyp': 'csv', 'kolumner': ['"Leverantörs artikelnummer"', '"Lagersaldo"'], 'has_header': True},
    'venture': {'filtyp': 'csv', 'kolumner': ['"ItemNum"', '"Qty"'], 'has_header': True},
    'vikingsun': {'filtyp': 'csv', 'kolumner': ['"Artikelnummer"', '"Disponibelt lagersaldo (RitoTrans)"'], 'has_header': True},
    'vikur': {'filtyp': 'csv', 'kolumner': ['"Leverantörs artikelnummer"', '"Lagersaldo"'], 'has_header': True},
    'vulcan': {'filtyp': 'csv', 'kolumner': ['"Artikelkod"', '"Tillgängligt idag"'], 'has_header': True},
    'wearatwork': {'filtyp': 'csv', 'kolumner': ['"ItemId"', '"Quantity"'], 'has_header': True},
    'wegter': {'filtyp': 'csv', 'kolumner': ['"Suppliers article number"', '"Stock"'], 'has_header': True},
    'zwiesel': {'filtyp': 'csv', 'kolumner': ['"Material"', '"Total selected Batches"'], 'has_header': None},
    }
    
