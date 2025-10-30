import pandas as pd
import streamlit as st
import altair as alt
import numpy as np

def load_data():
    df= pd.read_csv('Aircrashes.xlsx')
   # replacing special characters in country/region column
    df["Country/Region"] = (df["Country/Region"].str.rstrip().str.replace(r'[^A-Za-z0-9_]', '', regex=True)
)
    df["Country/Region"]=df['Country/Region'].fillna("Unspecified")
    df["Operator"]=df["Operator"].fillna("Unspecified")

    df["Country/Region"]=df["Country/Region"].replace(r'^\s*$',np.nan,regex=True)

    # Dictionary of corrections
    country_corrections = {
        'Alaksa':'Alaska','Alakska':'Alaska','Belgian':'Belgium','BrazilAmazonaves':'Brazil','British':'United kingdom','Cameroons':'Cameroon',
        'AKAlaska':'Alaska','Airzona	':'Arizona','China?':'China', 'Airzona':'Arizona','Democratic':'Democratic Republic of Congo',
        'Equatorial':'Equatorial Guinea','French':'France', 'Hong':'Hong Kong', 'IndiatPawan':'India', 'near':'California',
        'New':'New York','North':'North Korea', 'Northern':'Northern Ireland', 'NorwaytCHC':'Norway', 'ON':'Ontario Canada',
        'Papua':'Papua New Guinea', 'Puerto':'Puerto Rico', 'Saudi':'Saudi Arabia','SK':'South Korea', 'South-West':'South Africa',
        'Sri':'Sri Lanka','Tennesee':'Tennessee', 'USSRAeroflot':'Russia', '100':'Unknown', 'BC':'British Columbia Canada',
        'Bias':'China','BraziltLoide':'Brazil','miles':'Miles','SpainrntrnMoron':'Spain','United':'UAE','Airlines':'Unknown','Coloado':'Colorado',
        'D.C.Capital':'Washington DC','Florida?':'Florida','off':'Angola','The':'Netherlands','Argentinade':'Argentina','Calilfornia?':'California',
        'D.C.Air':'Florida','El':'El Salvador','IndonesiarntrnSarmi':'Indonesia','NSW':'Australia','UARMisrair':'EgyptAir (UAR era)','Minnesota46826/109':'Minnesota',
        'Qld':'Australia','U.S.':'United States','325':'Unspecified','110':'Unspecified','116':'Unspecified','18':'Unspecified','570':'Unspecified',
        'Germany?':'Germany','AzerbaijanrntrnBakou':'Azerbaijan','USSRBalkan':'Balkan Bulgarian Airlines (USSR era)','BrazilrnFlorianopolis':'Brazil','ChiletAerolineas':'Chile',
        'Honduras?':'Honduras','US':'United States','Afghanstan':'Afghanistan','USSRMilitary':'USSR Military Aviation','800':'Unknown',
        'TajikistantMilitary':'Tajikistan','USSRAerflot':'Russia','DjiboutirntDjibouti':'Dijibouti','France?':'France',
        'UAEGulf':'UAE','Virginia.American':'Virginia America','FL':'Florida','Italyde':'Italy','Picrdie':'Picardie','10':'Unspecified','Unknown':'Unspecified',
    }

    df["Country/Region"] = df["Country/Region"].replace(country_corrections)

    manufacturer_corrections = {
        "Doublas": "Douglas","MD Douglas": "McDonnell Douglas","Mc Donnell Douglas": "McDonnell Douglas","De Havilland": "de Havilland","de Havilland  Canada": "De Havilland Canada",
        "Hadley Page 137Jetstream I": "Handley Page Jetstream","Lisnov": "Lisunov","C": "Cessna","Fokke": "Focke-Wulf",
        "B17G Flying": "Boeing B-17G Flying Fortress","Lockheed 14 Super": "Lockheed 14 Super Electra","Lockheed 188C": "Lockheed L-188C Electra",
        "Aerospatiale Caravelle": "Aérospatiale Caravelle","OFM": "OFM Aircraft","??": "Unknown","Swallow?": "Swallow",
        "Embraer 110EJ Band./Embraer 110P": "Embraer 110 Bandeirante","Embraer 110P1": "Embraer 110 Bandeirante","Pilatus Britten Norman": "Pilatus Britten-Norman",
        "NAMC": "Nihon Aircraft Manufacturing Corporation", "Britten Norman": "Britten-Norman", "Lockheed Super": "Lockheed Super Constellation",
        "Lockheed 14": "Lockheed Model 14","Lockheed 18": "Lockheed Model 18 Lodestar", "Lockheed Hudson": "Lockheed Hudson",
        "Vickers 610 Viking": "Vickers Viking 610","Vickers Viking 1B & Soviet": "Vickers Viking 1B","Vickers Valetta": "Vickers Valetta",
        "Vickers Viscount": "Vickers Viscount","Vickers Wellington": "Vickers Wellington","Vickers Vanguard": "Vickers Vanguard",
        "Avro 685 York": "Avro 685 York","Avro Shackleton": "Avro Shackleton","Handley Page": "Handley Page","Hawker Siddeley HS": "Hawker Siddeley",
        "Hawker Siddeley Trident": "Hawker Siddeley Trident","British Aerospace BAe": "British Aerospace","Cams": "CAMS","Hadley Page": "Handley Page",
        "Messerschmidt": "Messerschmitt","Pilgrim": "Fairchild Pilgrim","Aerocomp Comp Air": "Aerocomp Comp Air","Eurocopter EC225LP Super Puma M2+": "Eurocopter EC225LP Super Puma",
        "Bell 212FAC": "Bell 212","Bell 205": "Bell 205","Bell": "Bell","Stearman": "Stearman Aircraft","Stinson Model": "Stinson",
        "Farman": "Farman Aviation Works","Swallow\r\nSwallow?": "Swallow","Sikorsky S43 (flying": "Sikorsky S43 (flying)","Unknown /": "Unknown",
        "Short Sandringham (flying": "Short Sandringham (flying)","Avro 691 Lancastrian (flying": "Avro 691 Lancastrian (flying)",
        "Short Sandringham 5 (flying": "Short Sandringham 5 (flying)","Latécoère 23 (flying": "Latécoère 23 (flying)","Latécoère 300 (float": "Latécoère 300 (float)",
        "Latecoere 301 (flying": "Latecoere 301 (flying)","Helicopter?": "Helicopter","Short Sandringham 2 (flying": "Short Sandringham 2 (flying)","CMASA Wal (flying": "CMASA Wal (flying)",
        "Fairchild packet (C119 flying": "Fairchild C-119 Flying Boxcar","Domier Delphin III (flying": "Dornier Delphin III (flying)","Airship?": "Airship",
        "Latecoere 631 (sea": "Latecoere 631 (sea)","Aeromarine Model 85 (flying": "Aeromarine Model 85 (flying)","Vickers Viscount 745D /": "Vickers Viscount 745D",
        "Stinson?": "Stinson","?42": "Unknown","?VP": "Unknown","Short Calcutta (flying": "Short Calcutta (flying)","Rutan Long EZ (experimental": "Rutan Long EZ (experimental)",
        "Hawker Siddeley Trident 2E /": "Hawker Siddeley Trident 2E","Antonov": "Antonov","Anotonov": "Antonov","Tupelov": "Tupolev",
        "Topolev": "Tupolev","Ilyshin": "Ilyushin","Illuyshin": "Ilyushin","Convair": "Convair","North American": "North American Aviation","Northrop": "Northrop Corporation",
        "Rockwell": "Rockwell International","Beech": "Beechcraft","Grumman": "Grumman","Gulfstream": "Gulfstream Aerospace","Piper": "Piper Aircraft",
        "Cessna?": "Cessna","Douglas Aircraft": "Douglas","McDonnell-Douglas": "McDonnell Douglas","Bombardier": "Bombardier Aerospace","Canadair": "Canadair",
        "Aérospatiale": "Aérospatiale","Aerospatiale": "Aérospatiale","ATR": "ATR","Embraer": "Embraer","Embraer 120": "Embraer EMB 120 Brasilia",
        "Yak": "Yakovlev","Yakovlev": "Yakovlev","Beriev": "Beriev","Let": "LET Aircraft Industries","Fokker": "Fokker",
        "Sukhoi": "Sukhoi","Dassault": "Dassault Aviation"
    }

    df["Aircraft Manufacturer"] = df["Aircraft Manufacturer"].replace(manufacturer_corrections)

    df["Aircraft Manufacturer"]=df["Aircraft Manufacturer"].replace("?"," ")

        # Dictionary of corrections for Aircraft
    aircraft_corrections = {
            "Douglas DC 4?": "Douglas DC-4","Doublas Dc 3?": "Douglas DC-3","Antonov AN 26?": "Antonov An-26","Antonov AN 32?": "Antonov An-32",
        "Mi  8 helicopter?": "Mil Mi-8","Mi  8?": "Mil Mi-8","Mil Mi 8?": "Mil Mi-8","Curtiss seaplane?": "Curtiss Seaplane",
        "Zeppelin L 59 (airship)?": "Zeppelin LZ 59","Curtiss C 46 Commando?": "Curtiss C-46 Commando","??": "Unknown","?VH  TAT": "Unknown",
        "\"Swallow\nSwallow?\"": "Swallow","Zeppelin L 70 (airship)?": "Zeppelin L 70 (airship)","UH  60 Blackhawk helilcopter?": "UH-60 Black Hawk helicopter",
        "Caproni Ca.48?": "Caproni Ca.48","Unknown / Unknown?": "Unknown","Antonov AN 22?": "Antonov AN 22","Siebel Si 204?": "Siebel Si 204",
        "Zeppelin L 23 (airship)?": "Zeppelin L 23 (airship)","Lockheed 18 56 Lodestar?": "Lockheed 18-56 Lodestar","Consolidated B 24?": "Consolidated B-24",
        "Mc Donnell Dougals DC 9?": "McDonnell Douglas DC-9","Fokker Universal F 14?": "Fokker Universal F-14","Douglas C47?": "Douglas C-47",
        "Dirigible Roma (airship)?": "Dirigible Roma (Airship)","Mil Mi 17?": "Mil Mi-17","Helicopter?": "Helicopter (Unspecified)",
        "Douglas DC 3?": "Douglas DC-3","Curtiss C 46?": "Curtiss C-46","Lisunov Li 2?": "Lisunov Li-2","Black Hawk helicopter?": "Sikorsky UH-60 Black Hawk",
        "Mil Mi 8 (helicopter)?": "Mil Mi-8 Helicopter","Mil Mi 8 / Mil Mi": "Mil Mi-8","Douglas C 47?": "Douglas C-47",
        "Fairchild packet (C119 flying boxcar)?": "Fairchild C-119 Flying Boxcar","Farman F 40?": "Farman F.40","Tupolev ANT 9?": "Tupolev ANT-9",
        "Mi  17?": "Mil Mi-17","Boeing RC 135E?": "Boeing RC-135E","Douglas DC 5?": "Douglas DC-5","PBY Catalina?": "Consolidated PBY Catalina",
        "KJ  2000?": "KJ-2000","FD Type Dirigible?": "Dirigible (Type FD)","Pitcairn PA 6 Mailwing?": "Pitcairn PA-6 Mailwing",
        "LVG C VI?": "LVG C.VI","Sukhoi Su 2742": "Sukhoi Su-27 (42)","Loening C W Air Yaht?": "Loening CW Air Yacht","?NC21V": "NC21V",
        "Mil Mi 8T (helicopter)?": "Mil Mi-8T helicopter","Douglas DC 3 (C": "Douglas DC-3", "Douglas DC C": "Douglas DC-3",
        "Five Grumman TBM Avengers?": "Grumman TBM Avenger (5 units)","Antonov AN 12?": "Antonov An-12","Fairchild Pilgrim 100A?": "Fairchild Pilgrim 100A",
        "KB  50?": "Boeing KB-50","Boeing Vertol CH 47 (helicopter)?": "Boeing Vertol CH-47 Chinook","Boeing Vertol CH 47 (helilcopter)?": "Boeing Vertol CH-47 Chinook",
        "Fairchild C 123?": "Fairchild C-123 Provider","Fairchild?": "Fairchild (unspecified model)","Twin Apache?": "Curtiss-Wright XP-60 'Twin Apache'",
        "Ilyushin II 14?": "Ilyushin Il-14","Lockheed 18 08 Lodestar	N410M": "Lockheed 18-08 Lodestar N410M","Lockheed 049 ConsellationNC86505": "Lockheed 049 Constellation NC86505",
        "MI 172 V5 helicopter?": "Mil Mi-172 (helicopter)","Zeppelin L 43 (airship)?": "Zeppelin LZ-43 (airship)","L  Hudson?": "Lockheed Hudson",
        "Fairchild C 199G?": "Fairchild C-119G","Pitcairns PA 6?": "Pitcairn PA-6","Aeromarine Model 85 (flying boat)?": "Aeromarine Model 85 (flying boat)",
        "McDonnel F 4E Phantom II?": "McDonnell F-4E Phantom II","Sepecat Jaguar A?": "SEPECAT Jaguar A","Junkers JU 86?": "Junkers Ju-86",
        "?139": "Unknown","Airship?": "Airship","C  46?": "Curtiss C-46","H  21B?": "Piasecki H-21B","MiG  23?": "Mikoyan-Gurevich MiG-23",
        "MiG  15 UTI?": "Mikoyan-Gurevich MiG-15 UTI","Douglas C 54 Skymaster?": "Douglas C-54 Skymaster","Douglas C 54?": "Douglas C-54","Stinson?": "Stinson",
        "Zeppelin L 22 (airship)?": "Zeppelin L-22 (airship)","Super Zeppelin (airship)?": "Zeppelin (Super airship)","Zeppelin L 34 (airship)?": "Zeppelin L-34 (airship)","Ilyushin IL 18?": "Ilyushin Il-18",
        "Kalinin K 7?": "Kalinin K-7","Boeing Vertol CH47A (helicopter)?": "Boeing Vertol CH-47A (helicopter)","?42  52196": "Douglas C-42 52196",
        "Budd RB 1 Conestoga?": "Budd RB-1 Conestoga","Li  2 / Li": "Lisunov Li-2","Lockheed Hudson?": "Lockheed Hudson",
        "Tempest?": "Hawker Tempest","Ford Tri motor 5?": "Ford Trimotor 5","Douglas A 3D Skywarrior?": "Douglas A-3D Skywarrior",
        "De Havilland DH 4?": "de Havilland DH-4","Zeppelin L 31 (airship)?": "Zeppelin L-31 (Airship)"
    }


    df["Aircraft"] = df["Aircraft"].replace(aircraft_corrections)

        # Dictionary of corrections for Location
    location_corrections = {
        "Shanghi China": "Shanghai China","Ningpo Bay China": "Ningbo Bay China","Near Shensi China?": "Near Shaanxi China","Pao Ting Fou China?": "Baoding (Pao Ting Fu) China",
        "Baranquilla Colombia": "Barranquilla Colombia","Rio de Janerio Brazil": "Rio de Janeiro Brazil","Near Belem Brazil\tLoide": "Near Belem Brazil (Loide)","Manaus Brazil\tAmazonaves": "Manaus Brazil (Amazonaves)","Coen Australila": "Coen Australia",
        "Sorta Norway\tCHC": "Sortland Norway (CHC)","Russian Mission Alaksa": "Russian Mission Alaska","Tamanraset Algeria": "Tamanrasset Algeria","Near Konigs Wusterausen East": "Near Königs Wusterhausen East Germany","Sagone India": "Sangone India",
        "Jirkouk Iraq": "Kirkuk Iraq","Near Alma-Ata Kazakastan": "Near Alma-Ata Kazakhstan","Chrisinau Moldova": "Chisinau Moldova","Ixtaccihuati Mexico": "Iztaccihuatl Mexico",
        "Cerro Lilio Mexico": "Cerro del Lilio Mexico","Benito Bolivia": "Beníto Bolivia","Colorado Bolivia": "Colorada Bolivia","Kupe Mountains Cameroons": "Kupe Mountains Cameroon",
        "Massamba Democratic": "Massamba Congo (Democratic Republic)","Mugogo Democratic": "Mugogo Congo (Democratic Republic)","Bukavu Democratic": "Bukavu Congo (Democratic Republic)",
        "Kongolo Democratic": "Kongolo Congo (Democratic Republic)","Nganga Lingolo Congo": "Nganga Lingolo Congo (DRC)","Bundeena Australia": "Bundeena New South Wales Australia",
        "Chilang Point Bias": "Chilang Point Bissau Guinea-Bissau","Hangow China": "Hangzhou China","Fort Hertz China": "Fort Hertz (Putao) Myanmar","Wangmoon China": "Wangmo China",
        "Sakiya Saugye Japan": "Sakiyama Sogyo Japan","Montnago Italy": "Montagnano Italy","Off Stromboli Italy": "Near Stromboli Italy","Near Ardinello di Amaseno Italy": "Near Ardielle di Amaseno Italy",
        "Kabassaak Turkey": "Kabasakal Turkey","Zaporozhye Ukraine": "Zaporizhzhia Ukraine","Belgrad Yugoslavia": "Belgrade Yugoslavia","?Deutsche Lufthansa": "Deutsche Lufthansa",
        "Belgrade Yugosalvia": "Belgrade Yugoslavia","Green Grove Florida?": "Green Grove Florida","Nnear Albuquerque New": "Near Albuquerque New Mexico","Wroctaw Poland": "Wroclaw Poland","Nnear Yuzhno-Sakhalinsk Russia": "Near Yuzhno-Sakhalinsk Russia",
        "Near Havlien Pakistan": "Near Havellian Pakistan","Preswick Scotland": "Prestwick Scotland","Gazni Afghanistan": "Ghazni Afghanistan",
        "Kranoyarsk Russia": "Krasnoyarsk Russia","Fond-du-Lac Saskatchewan": "Fond du Lac Saskatchewan","Catherham Surrey": "Caterham Surrey","Nurnberg Germany": "Nürnberg Germany",
        "Eubeoa Greece": "Euboea Greece","Hati": "Haiti","Mendotta Minnisota": "Mendota Minnesota","Wisconson": "Wisconsin",
        "Off Venice California?": "Off Venice California","Guaderrama Spain": "Guadarrama Spain","UARMisrair": "UAR Misrair","Horwich Lancs": "Horwich Lancashire",
        "Caravelas Bay Brazil": "Caravelas Brazil","Lapadrera Colombia": "La Pedrera Colombia","Gibraltar?": "Gibraltar","Nnear Kuybyshev Russia": "Near Kuybyshev Russia","Near Syktyvar Russia": "Near Syktyvkar Russia","Khartoom Sudan": "Khartoum Sudan",
        "Near Rijeka Yugoslavia": "Near Rijeka Yugoslavia",'"Bakou Azerbaijan\n\t\nBakou"': "Baku Azerbaijan","San Diego CADuncan": "San Diego CA","Near Wawona Cailifornia": "Near Wawona California",
        "Nacias Nguema Equatorial": "Nacias Nguema Equatorial Guinea","Off Rasal United": "Off Rasal United Kingdom","Torysa Czechoslovakia": "Torysa Czechoslovakia","Burbank Calilfornia": "Burbank California","San Barbra Honduras?": "San Barbara Honduras",
        "Boston Massachutes": "Boston Massachusetts","Near Cuidad de Valles Mexic": "Near Ciudad de Valles Mexico","Zamboanga Philipines": "Zamboanga Philippines","Near Amiens Picrdie": "Near Amiens Picardie","Dearborn Minnesota": "Dearborn Michigan",
        "Near Walsenberg Colorado": "Near Walsenburg Colorado","Off Mar del Plata Aregntina": "Off Mar del Plata Argentina","Guatamala City  Guatemala": "Guatemala City Guatemala","San Salvador El": "San Salvador El Salvador",
        "La Poyatta Colombia": "La Hoyada Colombia","Stephenville Newfoundlandu.s.": "Stephenville Newfoundland U.S.","Near Jalalogori West": "Near Jalalogori West","Near Sarowbi Afghanistan": "Near Sarobi Afghanistan","Near Bagram Afghanstan": "Near Bagram Afghanistan",
        "Luassingua Angola": "Luassingua Angola","Techachapi Mountains California": "Tehachapi Mountains California","Off Cape Mendocino CAMilitary": "Off Cape Mendocino CA Military","Landsdowne House Canada": "Lansdowne House Canada",
        "Ste. Therese de Blainville Canada": "Sainte-Thérèse-de-Blainville Canada","Near Petrich bulgaria": "Near Petrich Bulgaria","Novia Scotia Canada": "Nova Scotia Canada","Between Shanghi and Canton China": "Between Shanghai and Canton China","Near Kindu Congo": "Near Kindu DR Congo",
        "Near Bugulumisa Congo": "Near Bugulma Congo","Near Hasna Egypt": "Near Aswan Egypt","Near Point Alert Ellesmere": "Near Alert Ellesmere","Near Trevelez Granada": "Near Trevélez Granada","Near Chiringa India": "Near Cherringa India",
        "Chiraz Iran": "Shiraz Iran","Venice Italyde": "Venice Italy","Abidjan Ivory": "Abidjan Ivory Coast","Barskoon Kirghizia": "Barskoon Kyrgyzstan",
        "Almelund Minnisota": "Almelund Minnesota","La Rache Morocco": "Larache Morocco","Near Lonkin Myanmar": "Near Lonkin Burma (Myanmar)","Over the Carribean SeaLACSA": "Over the Caribbean Sea LACSA",
        "Juvisy-sur-Orge France?": "Juvisy-sur-Orge France","Isiro Democtratic": "Isiro Democratic Republic of Congo","Near Nador Morroco": "Near Nador Morocco","Centeral Afghanistan": "Central Afghanistan",
        "Kharkov. Ukraine Russia": "Kharkov Ukraine","Georgian SSR USSRAerflot": "Georgian SSR USSR Aeroflot",
        "Gulf of Sivash USSRAeroflot": "Gulf of Sivash USSR Aeroflot","Off St. Petersburg USSRAeroflot": "Off St. Petersburg USSR Aeroflot",
        "Petropavlosk USSRAeroflot": "Petropavlovsk USSR Aeroflot","Near Leningrad USSRAeroflot": "Near Leningrad USSR Aeroflot","Near Khabarovsk USSRAeroflot": "Near Khabarovsk USSR Aeroflot",
    }


    df["Location"] = df["Location"].replace(location_corrections)

        # Dictionary of corrections for Operators
    operator_corrections = {
        "Airways??": "Airways","N/A":"Unknown","GuineaTrans New?": "Guinea Trans New","Nevada      Vegas Las of SW miles United Air Lines /": "Nevada Las Vegas - United Air Lines",
        "Airlines Australia GuineaTrans New": "Airlines Australia - Guinea Trans New","(UK) Airlines International SwitzerlandInvicta": "(UK) Airlines International - Switzerland Invicta","Alaska Air Fuel": "Alaska Air (Fuel Service)","USSRAeroflot": "USSR Aeroflot",
        "Airlines Airlines/Alliance Indian": "Airlines Alliance Indian","Force Air OceanIndian": "Force Air Ocean Indian","England Walcot Air Line": "England Walcott Air Line","Airways) Nigeria by (chartered ArabiaNationair": "Airways Nigeria (chartered by Arabia Nationair)",
        "Amercia Air": "America Air","Foundation Reasearch Purdue - GuineaPrivate": "Foundation Research Purdue - Guinea Private","Airlines Duch Royal KLM": "Airlines Dutch Royal KLM","Force Air US - Militiary": "Force Air US - Military","GuineaAeroflot": "Guinea Aeroflot",
        "Inc. Flight InaguaAgape": "Inc. Flight Inagua Agape","KarkinitskyAeroflot of": "Karkinitsky Aeroflot","Italila Eurojet": "Italia Eurojet","Ivorie CoastAir": "Ivory Coast Air","Airlilnes LeoneParamount": "Airlines Leone Paramount",
        "Aviaition Ababeel": "Aviation Ababeel","Airlines Dutch Royal NetherlandsKLM": "Airlines Dutch Royal Netherlands KLM","UzbekistanAeroflot": "Uzbekistan Aeroflot","Aéreo Taxi AéreoBahia Taxi AéreoBahia Taxi Bahia": "Aéreo Taxi Bahia","Airways Overseas KongPacific": "Airways Overseas Hong Kong Pacific",
        "Service Mail Aerial JerseyUS": "Service Mail Aerial Jersey US","Airways National Zealand ZealandNew": "Airways National New Zealand","Canada Miami Aviaition/Air Manila": "Canada Miami Aviation / Air Manila","Airways) Orient (Filipinas Fairways": "Airways Orient (Filipinas Fairways)","Romane) Aeriene (Transporturile Tarom": "Romane Aeriene (Transporturile Tarom)","Airlines ArabiaVnukovo": "Airlines Arabia Vnukovo",
        "LeoneHelicsa": "Leone Helicsa","Azur VietnamAigle": "Azur Vietnam Aigle","Vietnam) (South Vietnam VietnamAir": "South Vietnam Airlines","Force Air Lankan Sri - LankaMilitary": "Force Air Sri Lankan - Military","Force Air Royal - LankaMilitary": "Force Air Royal Sri Lanka - Military","Airways EmiratesSterling Arab": "Airways Emirates Sterling Arab",
        "KingdomLoganair": "Kingdom Loganair","Singapore Airllines": "Singapore Airlines","Airways Guiena": "Airways Guinea","Lines Air ElalatPhilippine of island Philippine the": "Lines Air El Alat Philippine of the Philippine Island","Air Bay GuineaMilne New": "Air Bay Guinea Milne New","Forces Air Army U.S. - GuineaMilitary": "Forces Air Army U.S. - Guinea Military",
        "Helicopter York  YorkNew": "Helicopter York New York","Reederei Zeppelin JerseyDeutsche": "Reederei Zeppelin Jersey Deutsche","Airlines Cargo JerseyRegina": "Airlines Cargo Jersey Regina","Airways W JerseyFlying": "Airways W Jersey Flying","Private / Airways YorkGreylock": "Private / Airways York Greylock","Force Air U.S. - MexicoMilitary": "Force Air U.S. - Mexico Military",
        "Airlines Ukranian-Mediterranean": "Airlines Ukrainian-Mediterranean","France Indian National Airlines": "Indian Airlines (France Mislabel)","Air Western and Continental Trans": "Air Western & Continental Transport","California          Angeles Continental Airlines": "California Los Angeles Continental Airlines","Airlines VirginiaCapital": "Virginia Capital Airlines","New York          York American Airlines": "New York American Airlines",
        "Airlines YorkMohawk": "Mohawk Airlines New York","New York          York USAir": "New York USAir","Airlines Western JerseyColonial": "Colonial Airlines Western Jersey","Airlines JerseyCentral": "Central Jersey Airlines","Airlines YorkContinental": "Continental Airlines New York","African RepublicUnion Aeromaritime": "African Republic Union Aeromaritime Transport",
        "Aviati Mustang": "Mustang Aviation","Force Air Argentine - RicaMilitary": "Argentine Air Force / Costa Rica Military (Mislabel)","India          Bengal British Overseas Airways": "British Overseas Airways Bengal India","England Bristop Aeroplane Company": "England Bristol Aeroplane Company","USSRAeroflot / Soviet Air Force": "USSR Aeroflot / Soviet Air Force",
        "Aviation Cap Wehite": "Cap White Aviation","Indiaèkoda (India) Ltd": "Indaèkoda (India) Ltd.","Air Paukn": "Air Paukn (Possible Misspelling)","York?": "York Airways (Unclear Entry)",
        "Nordchurchaid": "Nord Church Aid","Charter - Aerocontroctors": "Aerocontractors Charter","Flamence RicoAir": "Flamenco Air Puerto Rico","Russian - /Military Aeroflot": "Aeroflot (Russian Military)","Brazil          Paulo Total  Air Lines": "Total Air Lines São Paulo Brazil","service guard border Kazakhstan - KazakistanMilitary": "Kazakhstan Border Guard Service - Military",
        "Airways HampshireNortheast": "Northeast Airlines (New Hampshire)","Airways JerseySaturn": "Saturn Airways (NJ)","CarolinaStratofreight": "Stratofreight (North Carolina)","Indonesia          Sulawesi Eastindo": "Eastindo Aviation (Sulawesi, Indonesia)","Flyveselksap Wideroe's": "Flyveselskap Widerøe",
        "Canada          Scotia MK Airlines": "Scotia MK Airlines Canada","Aviation Costal": "Coastal Aviation","Unied Kingdom Air Union": "United Kingdom Air Union","Connection) (American Airlines Corporate": "American Airlines Corporate Connection","Air Divi AntillesDivi": "Divi Divi Air (Netherlands Antilles)","Airlines Dutch Royal IndiesKLM": "KLM Royal Dutch Airlines (Netherlands Indies)",
        "Corp. Aviation Paramount - Taxi JerseyAir": "Paramount Aviation Corp. - Air Taxi (NJ)","Airways York YorkNew": "New York Airways","Zealand New Freight ZealandAir": "New Zealand Air Freight","Service Flying YorkChamberlin": "Chamberlin Flying Service (NY)",
        "WNBC - YorkPrivate": "WNBC Private Flight (NY)","Airlines HampshireNortheast": "Northeast Airlines (New Hampshire)"
    }


    df["Operator"] = df["Operator"].replace(operator_corrections)

        # In some cases, fatalities were greater than the number aboard.
    # Such rows were removed.
    df = df[df["Fatalities (air)"] <= df["Aboard"]]

        # reset index
    df = df.reset_index(drop=True)

    return df

try:
    df = load_data()

    st.title("Aircraft Crashes App")

    # filters
    # filters = {
    #     'Quarter': df['Quarter'].unique(),
    #     'Country/Region': df['Country/Region'].unique(),
    #     'Month': df['Month'].unique(),
    #     'Location': df["Location"].unique(),
    #     }
    

    filters = {
    "Location": df["Location"].value_counts().head(5).index.tolist(),
    "Country/Region": df["Country/Region"].value_counts().head(5).index.tolist(),
    "Aircraft Manufacturer": df["Aircraft Manufacturer"].value_counts().head(5).index.tolist(),
    "Aircraft": df["Aircraft"].value_counts().head(5).index.tolist(),
    "Operator": df["Operator"].value_counts().head(5).index.tolist(),
}

    # store user selection
    selected_filters = {}

    #generate multi-select widgets dynamically
    for key, options in filters.items():
        selected_filters[key] = st.sidebar.multiselect(key,options)

    # take copy of the data
    filtered_df = df.copy()

    # apply filter for selection to the data
    for key, selected_values in selected_filters.items():
        if selected_values:
            filtered_df = filtered_df[filtered_df[key].isin(selected_values)]

    #display the data
    # st.dataframe(filtered_df)

    #     most_used_aircraft = df['Aircraft'].mode()[0] 
    #     total_fatalities = filtered_df['Fatalities (air)'].sum()
    #     avg_no_of_fatalities = filtered_df['Fatalities (air)'].mean()
    #     #perct_sales = f'{(total_revenue / df['money'].sum()) * 100:,.2f}%'

    # with st.container():
    #     st.subheader("Quick Overview")
    #     st.metric('Total fatalities:', f'{total_fatalities:,}')
    #     st.metric('Most Used Aircraft:', most_used_aircraft)
        #     st.metric('Average number of Fatalities:', f'{avg_no_of_fatalities:,.2f}')

    # CALCULATIONS / METRICS
    # year_highest_accidents = df['Year'].value_counts().idxmax()         # 1. Year with highest accidents
    # total_fatalities_aboard = df['Fatalities (air)'].sum()              # 2. Total fatalities aboard
    # total_fatalities_ground = df['Ground'].sum()                        # 3. Total fatalities on ground
    # top_country = df['Country/Region'].value_counts().idxmax()          # 4. Country/Region with most crashes
    # top_location = df['Location'].value_counts().idxmax()               # 5. Location with most crashes
    # top_manufacturer = df['Aircraft Manufacturer'].value_counts().idxmax()  # 6. Manufacturer with most crashes

    # with st.container():
    #     st.subheader("Quick Overview")

    #     st.metric("Year with Highest Accidents:", year_highest_accidents)
    #     st.metric("Country/Region with Most Crashes:", top_country)

    #     st.metric("Total Fatalities (Aboard):", f"{total_fatalities_aboard:,}")
    #     st.metric("Total Fatalities (Ground):", f"{total_fatalities_ground:,}")

    #     st.metric("Top Aircraft Manufacturer:", top_manufacturer)
    #     st.metric("Location with Most Crashes:", top_location)


    # st.markdown("### 📊 Exploratory Data Analysis")

    # # Top Country by Fatalities
    # fatalities_by_country = (
    #     df.groupby("Country/Region")["Fatalities (air)"]
    #     .sum()
    #     .nlargest(1)
    #     .reset_index()
    # )
    # most_affected_country = fatalities_by_country.iloc[0]["Country/Region"]
    # total_country_fatalities = int(fatalities_by_country.iloc[0]["Fatalities (air)"])

    # # Month with Highest Fatalities
    # fatalities_by_month = df.groupby("Month")["Fatalities (air)"].sum().reset_index()
    # highest_month = fatalities_by_month.loc[
    #     fatalities_by_month["Fatalities (air)"].idxmax(), "Month"
    # ]
    # month_fatalities = int(fatalities_by_month["Fatalities (air)"].max())

    # # Deadliest Year
    # fatalities_by_year = (
    #     df.groupby("Year")["Aboard"]
    #     .sum()
    #     .reset_index()
    #     .sort_values(by="Aboard", ascending=False)
    # )
    # deadliest_year = int(fatalities_by_year.iloc[0]["Year"])
    # aboard_fatalities = int(fatalities_by_year.iloc[0]["Aboard"])

    # # EDA metrics in a new horizontal row
    # with st.container():

    #         st.metric("🌍 Country with Most Fatalities", most_affected_country, f"{total_country_fatalities:,}")

    #         st.metric("📅 Month with Highest Fatalities", highest_month, f"{month_fatalities:,}")

    #         st.metric("📆 Deadliest Year", deadliest_year, f"{aboard_fatalities:,}")


    left_col, right_col = st.columns(2)

    # -------------------------
    # ⚡ QUICK OVERVIEW SECTION (LEFT)
    # -------------------------
    with left_col:
        st.markdown("### Quick Overview")

        most_used_aircraft = df['Aircraft'].mode()[0] 
        total_fatalities = filtered_df['Fatalities (air)'].sum()
        avg_no_of_fatalities = filtered_df['Fatalities (air)'].mean()
        fatal_accidents = df[df["Fatalities (air)"] > 0].shape[0]
        # total_fatalities = df["Fatalities (air)"].sum()
        # most_used_aircraft = df["Aircraft Manufacturer"].mode()[0]
        # avg_no_of_fatalities = df["Fatalities (air)"].mean()
        # fatal_accidents = df[df["Fatalities (air)"] > 0].shape[0]



        st.metric("Total Fatalities", f"{total_fatalities:,}")
        st.metric("Most Used Aircraft", most_used_aircraft)
        st.metric("Avg. Number of Fatalities", f"{avg_no_of_fatalities:,.2f}")
        st.metric("Accidents with Fatalities", f"{fatal_accidents:,}")



    # EDA SUMMARY SECTION (RIGHT)
    with right_col:
        st.markdown("### Exploratory Data Analysis")

        # Total Crashes
        total_crashes = df.shape[0]

        # Country with Most Crashes
        top_country = df["Country/Region"].value_counts().idxmax()
        total_crashes_country = df["Country/Region"].value_counts().max()

        # Year with Most Crashes
        highest_crash_year = df["Year"].value_counts().idxmax()
        total_crash_in_year = df["Year"].value_counts().max()

        # Average Survivors per Crash
        if "Aboard" in df.columns and "Fatalities (air)" in df.columns:
            df["Survivors"] = df["Aboard"] - df["Fatalities (air)"]
            avg_survivors = df["Survivors"].mean()
        else:
            avg_survivors = 0

        # Display metrics
        st.metric("Total Number of Crashes", f"{total_crashes:,}")
        st.metric("Country with Most Crashes", top_country, f"{total_crashes_country:,}")
        st.metric("Year with Most Crashes", highest_crash_year, f"{total_crash_in_year:,}")
        st.metric("Avg. Survivors per Crash", f"{avg_survivors:,.1f}")




        # RESEARCH QUESTIONS SECTION
    st.markdown("## Research Questions")

    st.markdown("### Top 10 Countries by Fatalities (Air)")

    # Group and prepare data
    fatalities_by_country = (
        df.groupby('Country/Region')['Fatalities (air)']
        .sum()
        .nlargest(10)
        .sort_values(ascending=False)
    )

    # --- Table first ---
    table_data = fatalities_by_country.reset_index()
    table_data.columns = ['Country/Region', 'Fatalities (Air)']
    st.dataframe(table_data)

    # --- Chart second ---
    import altair as alt
    chart_1 = alt.Chart(table_data).mark_bar().encode(
            x=alt.X('Country/Region:N'),
            y=alt.Y('Fatalities (Air):Q'),
            color=alt.Color('Fatalities (Air):Q', legend=None)
            
        ).properties(height = 300)

        # display the chart
    st.altair_chart(chart_1, use_container_width=True)
   # No 2
    st.markdown("### Aircraft Types with Highest Fatalities")

    fatalities_by_aircraft = (
        df.groupby('Aircraft')['Fatalities (air)']
        .sum()
        .nlargest(5)
        .reset_index()
        .sort_values('Fatalities (air)', ascending=False)
    )

    chart = (
        alt.Chart(fatalities_by_aircraft)
        .mark_bar()
        .encode(
            x=alt.X('Aircraft:N', sort='-y'),
            y=alt.Y('Fatalities (air):Q'),  
            color=alt.Color('Fatalities (air):Q', legend=None),
            tooltip=['Aircraft', 'Fatalities (air)']
        )
        .properties(height=350)
    )

    st.altair_chart(chart, use_container_width=True)

    st.markdown("### Top 3 Aircraft Operators by Fatalities")
    # Group and get top 3 operators
    Top3_ops = (
        df.groupby('Operator')['Fatalities (air)']
        .sum()
        .nlargest(3)
        .sort_values(ascending=True)
        .reset_index()
    )

    # Display as a table (optional)
    st.dataframe(Top3_ops)

    # Create Altair horizontal bar chart
    chart_ops = (
        alt.Chart(Top3_ops)
        .mark_bar(color='orange')
        .encode(
            x=alt.X('Fatalities (air):Q', title='Total Fatalities'),
            y=alt.Y('Operator:N', sort='x', title='Operator'),
            tooltip=['Operator', 'Fatalities (air)']
        )
        .properties(
            title='Top 3 Aircraft Operators by Fatalities',
            height=300,
            width='container'
        )
    )

    # Display chart 
    st.altair_chart(chart_ops, use_container_width=True)
    st.markdown("### Top 5 Locations by Fatalities")

    # --- Group and get top 5 locations by fatalities ---
    fatalities_by_location = (
        df.groupby('Location')['Fatalities (air)']
        .sum()
        .nlargest(5)
        .sort_values(ascending=False)
        .reset_index()
    )


    # --- Create the Altair bar chart ---
    chart_location = (
        alt.Chart(fatalities_by_location)
        .mark_bar(color='green')
        .encode(
            x=alt.X('Location:N', 
                    sort='-y', 
                    title='Location',
                    axis=alt.Axis(labelAngle=10)),  # equivalent to plt.xticks(rotation=10)
            y=alt.Y('Fatalities (air):Q', title='Total Fatalities'),
            tooltip=['Location', 'Fatalities (air)']
        )
        .properties(
            title='Fatalities per Location',
            height=300,
            width='container'
        )
    )
    st.altair_chart(chart_location, use_container_width=True)

    # No 5
    st.markdown("### Trend of Air Crashes per Year")
        # --- Group by year and count crashes ---
    crashes_per_year = df.groupby('Year').size().reset_index(name='Number of Crashes')

    # --- Create the Altair line chart ---
    chart_trend = (
        alt.Chart(crashes_per_year)
        .mark_line(point=alt.OverlayMarkDef(color='green', size=50))
        .encode(
            x=alt.X('Year:O', title='Year'),  # O = ordinal (for consistent spacing)
            y=alt.Y('Number of Crashes:Q', title='Number of Crashes'),
            tooltip=['Year', 'Number of Crashes']
        )
        .properties(
            title='Trend of Air Crashes per Year',
            height=400,
            width='container'
        )
        .configure_axis(grid=True, gridOpacity=0.3)
    )

    # --- Display chart in Streamlit ---
    st.altair_chart(chart_trend, use_container_width=True)
    # No 6
    st.markdown("### Air Crashes with More Than 300 Fatalities")
    # --- Filter crashes with more than 300 fatalities ---
    big_crashes = df[df['Fatalities (air)'] > 300]

    # --- Create the Altair horizontal bar chart ---
    chart_big_crashes = (
        alt.Chart(big_crashes)
        .mark_bar(color='purple')
        .encode(
            x=alt.X('Fatalities (air):Q', title='Fatalities'),
            y=alt.Y('Operator:N', sort='x', title='Operator'),
            tooltip=['Operator', 'Fatalities (air)', 'Location', 'Year']
        )
        .properties(
            height=400,
            width='container'
        )
    )

    # --- Display chart in Streamlit ---
    st.altair_chart(chart_big_crashes, use_container_width=True)

# No 7
    st.markdown("### Air Crashes by Month")
        # --- Ensure month is categorical and ordered ---
    df['Month'] = pd.Categorical(df['Month'], ordered=True)

    # --- Count crashes per month ---
    crashes_by_month = (
        df['Month']
        .value_counts()
        .rename_axis('Month')
        .reset_index(name='Number of Crashes')
        .sort_values('Month')  # keeps chronological order
    )

    # --- Create Altair bar chart ---
    chart_month = (
        alt.Chart(crashes_by_month)
        .mark_bar(color='teal', opacity=0.8)
        .encode(
            x=alt.X('Month:N', sort=None, title='Month', axis=alt.Axis(labelAngle=0)),
            y=alt.Y('Number of Crashes:Q', title='Number of Crashes'),
            tooltip=['Month', 'Number of Crashes']
        )
        .properties(
            height=400,
            width='container'
        )
    )

    # --- Display in Streamlit ---
    st.altair_chart(chart_month, use_container_width=True)

     # No 8
    st.markdown("### Average Number Aboard by Aircraft Type")
    # --- Group by aircraft and calculate average number aboard ---
    avg_aboard = (
        df.groupby('Aircraft')['Aboard']
        .mean()
        .head(10)
        .reset_index()
    )

    # --- Create Altair bar chart ---
    chart_avg_aboard = (
        alt.Chart(avg_aboard)
        .mark_bar(color='steelblue', stroke='black', strokeWidth=0.5)
        .encode(
            x=alt.X('Aircraft:N', 
                    sort='-y', 
                    title='Aircraft Type'),
            y=alt.Y('Aboard:Q', title='Average Number Aboard'),
            tooltip=['Aircraft', 'Aboard']
        )
        .properties(
            height=400,
            width='container'
        )
    )

    # --- Display in Streamlit ---
    st.altair_chart(chart_avg_aboard, use_container_width=True)

    # No 9
    st.markdown("### What is the trend of average people aboard over the years?")
    # --- Group by year and calculate average aboard ---
    avg_aboard_trend = (
        df.groupby('Year')['Aboard']
        .mean()
        .reset_index(name='Average Number Aboard')
    )

    # --- Create Altair line chart ---
    chart_avg_aboard_trend = (
        alt.Chart(avg_aboard_trend)
        .mark_line(color='teal', point=alt.OverlayMarkDef(color='teal', size=50))
        .encode(
            x=alt.X('Year:O', title='Year'),
            y=alt.Y('Average Number Aboard:Q', title='Average Number Aboard'),
            tooltip=['Year', 'Average Number Aboard']
        )
        .properties(
            height=400,
            width='container'
        )
        .configure_axis(grid=True, gridOpacity=0.3)
    )

    # --- Display chart in Streamlit ---
    st.altair_chart(chart_avg_aboard_trend, use_container_width=True)

    # No 10

    st.markdown("###  Which quarter of the year records the highest fatalities?")
        # --- Group by quarter and sum fatalities ---
    fatalities_by_quarter = (
        df.groupby('Quarter')['Fatalities (air)']
        .sum()
        .reset_index(name='Total Fatalities')
        .sort_values('Total Fatalities', ascending=False)
    )

    # --- Create Altair bar chart ---
    chart_fatalities_by_quarter = (
        alt.Chart(fatalities_by_quarter)
        .mark_bar(color='skyblue')
        .encode(
            x=alt.X('Quarter:N', title='Quarter'),
            y=alt.Y('Total Fatalities:Q', title='Total Fatalities'),
            tooltip=['Quarter', 'Total Fatalities']
        )
        .properties(
            title='Total Fatalities by Quarter of the Year',
            height=400,
            width='container'
        )
    )

    # --- Display in Streamlit ---
    st.altair_chart(chart_fatalities_by_quarter, use_container_width=True)

except Exception as e:
    st.error("Error: check error details")

    with st.expander("Error Details"):
        st.code(str(e))

         # st.code(traceback.format_exc())
