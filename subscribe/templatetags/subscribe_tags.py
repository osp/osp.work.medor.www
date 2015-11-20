# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import caldav
import datetime
import pytz

from django import template
from django.db.models import Sum
from subscribe.models import Subscription, Cooperation
from django.conf import settings


register = template.Library()


@register.assignment_tag
def get_subscriber_count():
    return Subscription.objects.exclude(status=2).count()


@register.assignment_tag
def get_capital_amount():
    return Cooperation.objects.exclude(status=2).aggregate(total=Sum('share_number'))['total'] * 20


def _get_next_events():

    def sort_key_func(x):
        val = getattr(x.instance.vevent, 'dtstart', None)
        if not val:
            return None
        val = val.value
        if hasattr(val, 'strftime'):
            return val.strftime('%F%H%M%S')
            return val.strftime('%F%H%M%S')

    url = settings.CALDAV_URL
    client = caldav.DAVClient(url)
    principal = client.principal()
    cal = principal.calendar(cal_id=settings.CALDAV_CAL_ID)


    now = datetime.datetime.now()
    now = now.replace(tzinfo=pytz.timezone(settings.TIME_ZONE))

    events = cal.date_search(now)
    events.sort(key=sort_key_func)

    #for event in events:
        #vevent = event.instance.vevent
        #dtstart = vevent.getChildValue('dtstart')
        #summary = vevent.getChildValue('summary')
        #print()
        #print(dtstart)
        #print(summary)

    return [e.instance.vevent for e in events[:4]]


@register.assignment_tag
def get_next_events():
    try:
        events = _get_next_events()
    except:
        events = []

    return events

@register.assignment_tag
def get_libraries():
    libraries = [
        ["Riga James Lib", "5.2896569", "50.5395031", "Rue De La Gare  6A 4540 Ampsin (Amay) Belgique", "Ampsin (Amay)"],
        ["Librairie Du Piétonnier", "5.8154941", "49.6831234", "Grand Rue 58 6700 Arlon Belgique", "Arlon"],
        ["Lettre Ecarlate", "5.815487", "49.6835173", "Rue Du Marché Au Beurre, 17 6700 Arlon Belgique", "Arlon"],
        ["Librairie Claire Laval", "5.2954185", "50.2224537", "Rue Grande  24 6900 Aye Belgique", "Aye"],
        ["Librairie Du Centre", "5.6752984", "50.4744433", "Place Joseph Thiry 29 4920 Aywaille Belgique", "Aywaille"],
        ["Oxfam Magasins du Monde, Aywaille", "5.6759423", "50.4735644", "Rue J. Wilmotte 1 4920  Belgique", "Aywaille"],
        ["Librairie Chez Tante Jack", "5.9698744", "50.6284872", "Route De Dolhain 16 4837 Baelen-Sur-Vesdre Belgique", "Baelen-Sur-Vesdre"],
        ["Le Libre Air", "5.703224", "50.6627797", "Rue De Heuseux 3 4671 Barchon Belgique", "Barchon"],
        ["Librairie Du Tenimont", "5.4958522", "50.350296", "Grand'Rue 2 6940 Barvaux-Sur-Ourthe Belgique", "Barvaux-Sur-Ourthe"],
        ["Librairie Du Centre", "5.4928413", "50.3504878", "En Charotte  3 6940 Barvaux-Sur-Ourthe Belgique", "Barvaux-Sur-Ourthe"],
        ["Librairie Croisy", "5.7174116", "50.0022244", "Rue Du Sablon 131 6600 Bastogne Belgique", "Bastogne"],
        ["Oxfam Magasins du Monde, Bastogne", "5.7065458", "50.0141434", "Rue de la Roche 5 6600 Bastogne Belgique", "Bastogne"],
        ["Librairie Cloquette", "3.8273477", "50.4744354", "Rue Louis Anciaux 9 7331 Baudour Belgique", "Baudour"],
        ["Librairie D'En Haut", "4.2374984", "50.235648", "Rue D'En Haut 11 6500 Beaumont Belgique", "Beaumont"],
        ["Oxfam Magasins du Monde, Thuin", "4.2393379", "50.2371957", "Rue t'Serstevens 50 6530 Beaumont Belgique", "Beaumont"],
        ["Librairie De La Gare", "4.9562792", "50.1144545", "Rue De La Gare 23 5570 Beauraing Belgique", "Beauraing"],
        ["Oxfam Magasins du Monde, Beauraing", "4.9531716", "50.1222387", "Rue de Dinant 9 5570 Beauraing Belgique", "Beauraing"],
        ["Librairie De La Gare", "5.2670049", "49.8530412", "Rue De La Gare 170 6880 Bertrix Belgique", "Bertrix"],
        ["Oxfam Magasins du Monde, Bertrix", "5.254048", "49.8550208", "Rue de la Gare 6 6880 Bertrix Belgique", "Bertrix"],
        ["Librairie Guisset", "5.6526658", "50.6258689", "Rue De Jupille 24 4610 Beyne-Heusay Belgique", "Beyne-Heusay"],
        ["Librairie De Bierges", "4.6000012", "50.7126467", "Rue Provinciale 155 1301 Bierges Belgique", "Bierges"],
        ["Librairie Abcd", "4.1190524", "50.6964108", "Place L. Nuttinck 1A 1430 Bierghes Belgique", "Bierghes"],
        ["Librairie De La Reine", "4.1653396", "50.4112389", "Grand Place, 9 7130 Binche Belgique", "Binche"],
        ["Librairie Au Passe Temps", "4.3934842", "50.6831127", "Route du Lion 84 1420 Braine L'Alleud Belgique", "Braine L'Alleud"],
        ["Le Baobab", "4.3778249", "50.6807653", "Rue Des Alliés 3 1420 Braine-L'Alleud Belgique", "Braine-L'Alleud"],
        ["Oxfam Magasins du Monde, Braine l'alleud", "4.3707556", "50.6828894", "Rue des Trois Apôtres 7 1420 Braine-L'Alleud Belgique", "Braine-L'Alleud"],
        ["Librairie Bonaventure", "4.3675964", "50.6802334", "Chaussée D’Ophain 14 1420 Braine-L’Alleud Belgique", "Braine-L’Alleud"],
        ["Librairie Kikadikoi", "4.1378928", "50.6063841", "Rue De La Station 133 7090 Braine-Le-Comte Belgique", "Braine-Le-Comte"],
        ["Librairie Glineur", "4.1324698", "50.6026972", "Rue Neuve 81 7090 Braine-Le-Comte Belgique", "Braine-Le-Comte"],
        ["Oxfam Magasins du Monde, Braine-le-Comte", "4.1369413", "50.6102498", "Rue de la Station 4 7090 Braine-Le-Comte Belgique", "Braine-Le-Comte"],
        ["Librairie Herman", "5.1475558", "50.6280063", "Rue Du Sacre-Coeur 2 4260 Braives Belgique", "Braives"],
        ["Brüsel", "4.3470678", "50.8458296", "Boulevard Anspach 100 1000 Bruxelles Belgique", "Bruxelles"],
        ["Théâtre De Poche", "4.3712231", "50.8124632", "Chemin Du Gymnase 1A 1000 Bruxelles Belgique", "Bruxelles"],
        ["Tropismes", "4.3545534", "50.8483497", "Galerie Des Princes 11 1000 Bruxelles Belgique", "Bruxelles"],
        ["Librairie Vismet", "4.3466322", "50.8531887", "Quai Aux Briques 82 1000 Bruxelles Belgique", "Bruxelles"],
        ["Tulitu", "4.3465516587", "50.85182565", "Rue De Flandre 55 1000 Bruxelles Belgique", "Bruxelles"],
        ["European Bookshop", "4.3666249", "50.8405817", "Rue Du Luxembourg 8 1000 Bruxelles Belgique", "Bruxelles"],
        ["Livresse", "4.345685", "50.8535516", "Rue Du Marché Aux Porcs 26 1000 Bruxelles Belgique", "Bruxelles"],
        ["Euro City Press", "4.3733104662", "50.84067435", "Rue Montoyer 66 1000 Bruxelles Belgique", "Bruxelles"],
        ["Boom - Le Café Du Commerce Équitable", "4.3464158", "50.8480513", "Rue Pletinckx 7 1000 Bruxelles Belgique", "Bruxelles"],
        ["Passa Porta", "4.3467578", "50.8495887", "Rue Antoine Dansaert  46 1000 Bruxelles Belgique", "Bruxelles"],
        ["FGTB Bruxelles", "4.3521108", "50.8418485", "Rue Haute 42 1000 Bruxelles Belgique", "Bruxelles"],
        ["PointCulture Bruxelles", "4.3650423", "50.8517678", "rue Royale  145 1000 Bruxelles Belgique", "Bruxelles"],
        ["Oxfam Magasins du Monde, ULB", "4.3817397", "50.8132323", "Avenue Paul Héger  22 (BXL) 1000 Bruxelles Belgique", "Bruxelles"],
        ["Librairie Etienne", "4.3591266", "50.8971836", "Avenue De Busleyden 1B 1020 Bruxelles Belgique", "Bruxelles"],
        ["Librairie Klb & Co", "4.387248", "50.851956", "Av De La Brabanconne 116 1030 Bruxelles Belgique", "Bruxelles"],
        ["Librairie Le Printemps", "4.3749600237", "50.86658065", "Chaussee De Haecht 339 1030 Bruxelles Belgique", "Bruxelles"],
        ["Librairie De Helmet.", "4.3896163", "50.8725824", "Place De Helmet 9 1030 Bruxelles Belgique", "Bruxelles"],
        ["Librairie Du Noyer", "4.3898033", "50.8490727", "Rue Du Noyer 238 1030 Schaerbeek Belgique", "Bruxelles"],
        ["Théâtre 140", "4.3960029852", "50.85203935", "Avenue Eugène Plasky  140 1030 Bruxelles Belgique", "Bruxelles"],
        ["Théâtre la Balsamine- ", "4.3914884", "50.8511885", "Avenue Félix Marchal  1 1030 Bruxelles Belgique", "Bruxelles"],
        ["Oxfam Magasins du Monde, Schaerbeek", "4.37966", "50.8625502", "Place d'Helmet 2 1030 Bruxelles Belgique", "Bruxelles"],
        ["Librairie Filigranes", "4.3679982", "50.843535", "Avenue Des Arts 39 1040 Bruxelles Belgique", "Bruxelles"],
        ["Librairie Européenne", "4.3988507", "50.8446322", "Rue De L'Orme 1 1040 Etterbeek Belgique", "Bruxelles"],
        ["Tapage - Telelivre Sprl", "4.4007105", "50.8382683", "Rue Père De Deken 83 1040 Bruxelles Belgique", "Bruxelles"],
        ["Librairie Du Millenaire", "4.3858406", "50.831768", "Rue Philippe Baucq 45 1040 Bruxelles Belgique", "Bruxelles"],
        ["Toute la Presse SPRL", "4.3989922627", "50.8396835", "Avenue de Tervueren 14 1040 Bruxelles Belgique", "Bruxelles"],
        ["Oxfam Magasins du Monde, Etterbeek", "4.3909251909", "50.83039145", "Rue des Champs 8 1040 Bruxelles Belgique", "Bruxelles"],
        ["Jolitab", "4.390376314", "50.81141975", "Av Guillaume Gilbert 43 1050 Bruxelles Belgique", "Bruxelles"],
        ["Librairie De La Trinite", "4.3587448566", "50.8255046", "Parvis De La Trinite 7 1050 Bruxelles Belgique", "Bruxelles"],
        ["Candide", "4.3550817", "50.8177847", "Place Brugman 1 1050 Ixelles Belgique", "Bruxelles"],
        ["Brüsel Flagey", "4.3726825", "50.828497", "Place Eugène Flagey 29 1050 Ixelles Belgique", "Bruxelles"],
        ["Continental Press Club", "4.3656322", "50.8362714", "Rue De La Paix 38 1050 Bruxelles Belgique", "Bruxelles"],
        ["Peinture Fraiche", "4.3585909", "50.8247328", "Rue De Tabellion 10 1050 Ixelles Belgique", "Bruxelles"],
        ["Librairie Louis D’Or", "4.3611502328", "50.8260598", "Rue Du Bailli 54 1050 Ixelles Belgique", "Bruxelles"],
        ["Press Center", "4.3579540852", "50.8228399", "Rue Du Page 61 1050 Bruxelles Belgique", "Bruxelles"],
        ["Théatre Varia", "4.3786134977", "50.83489795", "Rue Du Sceptre 78 1050 Ixelles Belgique", "Bruxelles"],
        ["Ptyx", "4.369364872", "50.8278499", "Rue Lesbroussart 39 1050 Ixelles Belgique", "Bruxelles"],
        ["La Quincaillerie des Temps Présents", "4.3698813096", "50.8334809", "Rue du Viaduc 66 1050 Bruxelles Belgique", "Bruxelles"],
        ["Oxfam Magasins du Monde, Ixelles", "4.3632250345", "50.8356474", "Chaussée d’Ixelles 77 1050  Belgique", "Bruxelles"],
        ["Ozfair", "4.3428988", "50.8323564", "Avenue Jean Volders 9 1060 Bruxelles Belgique", "Bruxelles"],
        ["Les Yeux Gourmands", "4.3440967", "50.8310642", "Avenue Jean Volders, 64a 1060 Saint-Gilles Belgique", "Bruxelles"],
        ["Joli Mai", "4.3448027507", "50.82575975", "Avenue Paul Dejaer 29 1060 Saint-Gilles Belgique", "Bruxelles"],
        ["Hors Format", "4.3427898", "50.8224546", "ChausséE D’Alsemberg 142 1060 Saint-Gilles Belgique", "Bruxelles"],
        ["Tipi Bookshop", "4.3451068", "50.8272572", "Rue Hôtel Des Monnaies 186 1060 Bruxelles Belgique", "Bruxelles"],
        ["Librairie-Presse Volders", "4.343585", "50.8318131", "Avenue Jean Volders 40 1060 Saint-Gilles Belgique", "Bruxelles"],
        ["FGTB - IRB ", "4.338806", "50.8334348", "Rue de Suède 45, 2e étage 1060  BRUSSEL (SINT-GILLIS) Belgique", "Bruxelles"],
        ["Librairie aux portes de l'info", "4.356865764", "50.82680815", "Rue Defacqz 89 1060 Bruxelles Belgique", "Bruxelles"],
        ["Oxfam Magasins du Monde, Saint-Gilles", "4.3441748847", "50.8280659", "Chaussée de Waterloo 137 1060 Bruxelles Belgique", "Bruxelles"],
        ["Oxfam Magasins du Monde, Anderlecht", "4.3055952375", "50.8356322", "Rue Saint-Guidon 13 1070 Bruxelles Belgique", "Bruxelles"],
        ["Maison De La Presse", "4.3134866", "50.8639589", "Av Berchem-Ste-Agathe 73 1081 Bruxelles Belgique", "Bruxelles"],
        ["Press Et Lis", "4.3275823424", "50.87698945", "Rue Henri Werrie 88 1090 Bruxelles Belgique", "Bruxelles"],
        ["Oxfam Magasins du Monde, Jette", "4.3314996", "50.8747739", "Rue Léopold 1er 527 1090 Bruxelles Belgique", "Bruxelles"],
        ["Lestadho Sprl", "4.3997405947", "50.87145445", "Avenue Henri Conscience 147 1140 Bruxelles Belgique", "Bruxelles"],
        ["Librairie Des Maieurs", "4.4316278", "50.8375741", "Place Des Maieurs 2 1150 Bruxelles Belgique", "Bruxelles"],
        ["Oxfam Magasins du Monde, Stockel", "4.4627456", "50.8407034", "Rue de l’Eglise  91 (WSP)  1150 Bruxelles Belgique", "Bruxelles"],
        ["Librairie Saint-Julien", "4.4075899563", "50.82099495", "Chaussee De Wavre 1285 1160 Bruxelles Belgique", "Bruxelles"],
        ["Librairie Des Archiducs", "4.4178113", "50.808589", "Avenue Des Archiducs 64 1170 Bruxelles Belgique", "Bruxelles"],
        ["Abao", "4.4180205524", "50.7965237", "Rue Middelbourg 40 1170 Watermael-Boitsfort Belgique", "Bruxelles"],
        ["Oxfam Magasins du Monde, Boitsfort", "4.4171204", "50.7989295", "Rue du Ministre 18 1170 Watermael-Boitsfort Belgique", "Bruxelles"],
        ["Coffee & Food, Pressworld Sprl", "4.3667703", "50.8155256", "Chaussee De Waterloo 715 1180 Bruxelles Belgique", "Bruxelles"],
        ["Librairie Du Domaine", "4.3284228", "50.8065178", "Rue Gatti De Gamond 2 1180 Bruxelles Belgique", "Bruxelles"],
        ["L'Harmonium", "4.3552702803", "50.8139644", "Rue Vanderkindere 293 1180 Uccle Belgique", "Bruxelles"],
        ["Edgar and co", "4.3622374154", "50.7929626", "Chaussée de Saint Job 713 1180 Uccle Belgique", "Bruxelles"],
        ["Librairie Moliere", "4.3397133031", "50.81597365", "Chaussee D'Alsemberg 349 1190 Bruxelles Belgique", "Bruxelles"],
        ["Press & Cafe", "4.3430509", "50.821537", "Place Albert 2 1190 Bruxelles Belgique", "Bruxelles"],
        ["Alti-Cent Loisirs", "4.3358501", "50.8165588", "Place De L’Altitude Cent 26 1190 Forest Belgique", "Bruxelles"],
        ["Librairie Saint-Henri", "4.409888478", "50.8413139", "Avenue Prekelinden 52 1200 Woluwé-Saint-Lambert Belgique", "Bruxelles"],
        ["Cook & Book Woluwé", "4.4372855", "50.8479965", "Place Du Temps Libre 1 1200 Woluwé-Saint-Lambert Belgique", "Bruxelles"],
        ["Librairie Coin Lecture", "4.4128924", "50.8392749", "Rue G. Et J. Martin 31 1200 Bruxelles Belgique", "Bruxelles"],
        ["A Livre Ouvert", "4.4358456", "50.8439055", "Rue Saint Lambert 116 1200 Woluwé-Saint-Lambert Belgique", "Bruxelles"],
        ["Molière & Cie", "4.4429905", "50.4077955", "Boulevard Tirou 68 6000 Charleroi Belgique", "Charleroi"],
        ["Librairie Du Pont Neuf", "4.4474545", "50.4082108", "Rue Du Pont Neuf 68 6000 Charleroi Belgique", "Charleroi"],
        ["PointCulture Charleroi", "4.4426759", "50.4132475", "Avenue de l'Europe 1 6000 Charleroi Belgique", "Charleroi"],
        ["Oxfam Magasins du Monde, Charleroi", "4.4466997", "50.4077105", "Rue de Montigny 68 6000 Charleroi Belgique", "Charleroi"],
        ["Le Passe-Temps", "4.5222781", "50.4052341", "Rue Neuve 12 6200 Chatelet Belgique", "Chatelet"],
        ["Biosphere", "4.6572118", "50.710076", "Boulevard Du Centenaire 8 1325 Chaumont-Gistoux Belgique", "Chaumont-Gistoux"],
        ["Librairie Cardon", "3.8074726", "50.5867161", "Rue Saint Jean 33 7950 Chievres Belgique", "Chievres"],
        ["Le Papyrus", "4.3158855", "50.0477116", "Rue Des Ormeaux 25 6460 Chimay Belgique", "Chimay"],
        ["New Press 2000", "5.1006098", "50.2949255", "Rue Courtejoie 10a 5590 Ciney Belgique", "Ciney"],
        ["Dlire De Lire", "5.1107952", "50.2682507", "Rue du Ctre 88 5590 Ciney Belgique", "Ciney"],
        ["Oxfam Magasins du Monde, Ciney CE", "5.0938331", "50.2913212", "Rue du Commerce 24 5590 Ciney Belgique", "Ciney"],
        ["La Petite Lanterne", "4.3900047", "50.4625077", "Rue Winston Churchill 9 6180 Courcelles Belgique", "Courcelles"],
        ["Librairie Le Rond Point", "4.5644414", "50.6532496", "Avenue Des Metallurgistes 1 1490 Court-Saint-Etienne Belgique", "Court-Saint-Etienne"],
        ["Quatre-Quarts", "4.5598691", "50.6209493", "Rue De Werchai (Dans La Gare)  1490 Court-Saint-Etienne Belgique", "Court-Saint-Etienne"],
        ["Librairie Aux Nouvelles", "5.4050604", "50.7062073", "Grand Route 63 4367 Crisnee Belgique", "Crisnee"],
        ["D-Livre", "4.9122657", "50.2607696", "Rue Grande 67a 5500 Dinant Belgique", "Dinant"],
        ["Librairie Saint Vincent", "4.9441993199", "50.2644701", "Rue Saint-Jacques  501 5500 Dinant Belgique", "Dinant"],
        ["Chez Sarah", "5.8520685", "50.6099233", "Rue Leopold 83 4820 Dison Belgique", "Dison"],
        ["Librairie Plaisir De Lire", "5.5990114", "50.5940949", "Rue Pierre Henvard 6 4053 Embourg Belgique", "Embourg"],
        ["Oxfam Magasins du Monde, Embourg", "5.5990114", "50.5940949", "Rue Pierre Henvard 2 4053 Embourg Belgique", "Embourg"],
        ["Oxfam Magasins du Monde, Enghien", "4.0394923", "50.6936563", "Rue d’Herinnes 4 7850 Enghien Belgique", "Enghien"],
        ["Libr Pap Du Bati", "5.6065792", "50.4001499", "Place Du Chablis 17 4190 Ferrieres Belgique", "Ferrieres"],
        ["Librairie Tombal", "5.3998056", "50.6565446", "Grand'Route  296 6b 4347 Fexhe-Le-Haut-Clocher Belgique", "Fexhe-Le-Haut-Clocher"],
        ["Librairie Wéry-Pérani", "5.3095144", "49.6979649", "Rue Généraux Cuvelier 4 6820 Florenville Belgique", "Florenville"],
        ["Librairie La Souris", "4.6953773", "50.3959627", "Rue de Vitrival 6 5070 Fosses-La-Ville Belgique", "Fosses-La-Ville"],
        ["Librairie Du Circuit", "5.9532560919", "50.4542572", "Rue De Pommard 213 4970 Francorchamps Belgique", "Francorchamps"],
        ["Librairie Rimes Et Bulles", "4.9369451", "49.9802979", "Rue De Charleville 12 5575 Gedinne Belgique", "Gedinne"],
        ["Agricovert", "4.6913408", "50.5725797", "Chaussée de Wavre 37 5030 Gembloux Belgique", "Gembloux"],
        ["L'Apostrophe", "4.6932439", "50.560486", "Grand'Rue  5 5030 Gembloux Belgique", "Gembloux"],
        ["Antigone", "4.6919493", "50.560116'", "Place De L'Orneau 17/A  5030 Gembloux Belgique", "Gembloux"],
        ["Oxfam Magasins du Monde, Gembloux", "4.6922498", "50.5600903", "Rue Léopold  17-19 5030 Gembloux Belgique", "Gembloux"],
        ["Librairie Le Canard", "4.4505411", "50.6082402", "Rue De Charleroi 18 1470 Genappe Belgique", "Genappe"],
        ["L'Entree Livre", "4.4985918", "50.7166744", "Place Communale 53 1332 Genval Belgique", "Genval"],
        ["Librairie Le Paon", "4.5148667", "50.7250207", "Rue De La Station 37 1332 Genval Belgique", "Genval"],
        ["Gesves Presse", "5.060951", "50.4053199", "Chaussee De Gramptinne 161 5340 Gesves Belgique", "Gesves"],
        ["La Librairie De Gastuche", "4.6827656", "50.7450529", "Chaussée De Wavre 404 1390 Grez-Doiceau Belgique", "Grez-Doiceau"],
        ["Ready Night", "4.6770441", "50.4413712", "Rue Try de bois 21 5190 Ham Sur Sambre Belgique", "Ham Sur Sambre"],
        ["Chapitre 7", "5.0746928", "50.6707284", "Rue Zénobe Gramme  49 4280 Hannut Belgique", "Hannut"],
        ["Mordant Librairie", "5.0856463", "50.6678717", "Rue Albert 1Er  52 4280 Hannut Belgique", "Hannut"],
        ["Librairie Du Rond Point", "5.7844918", "50.638735", "Rue De La Clef 74 4650 Herve Belgique", "Herve"],
        ["Oxfam Magasins du Monde, Herve", "5.7928514", "50.6394521", "Rue Léopold 34 4650  Belgique", "Herve"],
        ["Papyland", "5.863964", "50.5817786", "Avenue Hanlet, 41 4802 Heusy Belgique", "Heusy"],
        ["Librairie A L'Écolier", "4.1476373", "50.4817829", "Rue Liébin 29 7110 Houdeng-Aimeries Belgique", "Houdeng-Aimeries"],
        ["Librairie Recto-Verso", "5.6912202", "50.1419014", "Place Roi Albert 10 6660 Houffalize Belgique", "Houffalize"],
        ["La Dérive", "5.2408903244", "50.51775195", "Grand Place 10 4500 Huy Belgique", "Huy"],
        ["Diachron", "5.2425382", "50.5216085", "Rue Des Augustins 4 4500 Huy Belgique", "Huy"],
        ["Oxfam Magasins du Monde, Huy", "5.2410305", "50.5183748", "Rue des Fouarges 14 4500 Huy Belgique", "Huy"],
        ["Press' Gourmande Sprl", "5.9108551", "50.5206749", "Tiege 76 4845 Jalhay Belgique", "Jalhay"],
        ["Lib. Au Bia Bouquin", "4.8714893", "50.4564247", "Avenue Jean Materne 128 5100 Jambes Belgique", "Jambes"],
        ["Loch Ness", "4.6724255", "50.4754786", "Route D'Eghezee 88 5190 Jemeppe-Sur-Sambre Belgique", "Jemeppe-Sur-Sambre"],
        ["Librairie Du Chateau", "4.8683055", "50.7241196", "Place De La Victoire 7 1370 Jodoigne Belgique", "Jodoigne"],
        ["L'Apostrophe", "4.9462445", "50.7310857", "Rue De Piétrain 36 1370 Jodoigne Belgique", "Jodoigne"],
        ["La Librairie De La Bruyère", "4.8378288", "50.6796184", "Rue Saint Jean 1 1370 Jodoigne Belgique", "Jodoigne"],
        ["L'Ivre De Papier Sa", "4.8709827", "50.724689", "Rue Saint-Jean 34 1370 Jodoigne Belgique", "Jodoigne"],
        ["Tibo", "5.623769", "50.644632", "Rue De Visé 164 4020 Jupille Belgique", "Jupille"],
        ["Librairie Kain Tombe", "3.3899202", "50.6264446", "Rue Albert 21 7540 Kain Belgique", "Kain"],
        ["Astrid Press", "4.4662525", "50.8487348", "Av.Reine Astrid 272 1950 Kraainem Belgique", "Kraainem"],
        ["Librairie Des 3 Colonnes", "4.4758517", "50.7346744", "Chaussée De Bruxelles 8a 1310 La Hulpe Belgique", "La Hulpe"],
        ["Librairie De L'Eglise", "4.4906288", "50.7303484", "Rue De L'Eglise 6 1310 La Hulpe Belgique", "La Hulpe"],
        ["Librairie Les 2 Freres", "4.4898563", "50.7317066", "Rue Des Combattants 62 1310 La Hulpe Belgique", "La Hulpe"],
        ["Librairie De La Mazerine", "4.4856707", "50.7309955", "Square Marie-Pouli 1A 1310 La Hulpe Belgique", "La Hulpe"],
        ["L’Ecrivain Public", "4.1907798", "50.4800117", "Rue Louis De Brouckère 45 7100 La Louvière Belgique", "La Louvière"],
        ["Le Lietherer", "5.5763460337", "50.18025285", "Place Du Bronze 14 6980 La Roche-En-Ardenne Belgique", "La Roche-En-Ardenne"],
        ["Librairie Nicolay", "5.2562012", "49.9815057", "Rue Du Commerce 44 6890 Libin Belgique", "Libin"],
        ["Le Temps De Lire", "5.3580899", "49.928646", "Rue Du Serpont 13 6800 Libramont Belgique", "Libramont"],
        ["Librairie De L'Observatoire", "5.5640644", "50.6238482", "Avenue De L'Observatoire 351 4000 Liege Belgique", "Liege"],
        ["Librairie Cochet", "5.5733104796", "50.6204139", "Pl Du General Leman 14 4000 Liege Belgique", "Liege"],
        ["Librairie Stéphane Hessel", "5.5680981536", "50.64296235", "Place Xavier Neujean 22 4000 Liege Belgique", "Liege"],
        ["Librairie Espace-Papier", "5.5603695", "50.6319985", "Rue Des Wallons 35 4000 Liege Belgique", "Liege"],
        ["Librairie Du Thier", "5.5950698", "50.6629754", "Rue Walther Dewe 26 4000 Liege Belgique", "Liege"],
        ["Librairie Des Vennes", "5.5812109075", "50.62789735", "Rue Des Vennes 44 4020 Liege Belgique", "Liege"],
        ["Centre Poly-Culturel Résistances", "5.584908", "50.6500593", "En Jonrelle 13 4000 Liège Belgique", "Liège"],
        ["Cochet", "5.5735367", "50.620498", "Place Général Leuman 14 4000 Liège Belgique", "Liège"],
        ["Librairie Robin Des Bois", "5.5461386", "50.6762016", "Place Reine Astrid 3 4000 Liège Belgique", "Liège"],
        ["Livre Aux Trésors", "5.5680981536", "50.64296235", "Place Xavier-Neujean, 27A 4000 Liège Belgique", "Liège"],
        ["Varia", "5.5768192097", "50.64609115", "Rue Des Mineurs 8 4000 Liège Belgique", "Liège"],
        ["Wattitude", "5.5750747", "50.643816", "Rue Du Souverain 4 4000 Liège Belgique", "Liège"],
        ["PointCulture Liège", "5.5628874", "50.6350757", "rue de l'Official  1à5 4000 Liège Belgique", "Liège"],
        ["Oxfam Magasins du Monde, Liège Centre", "5.5717067542", "50.6413594", "Rue de la Cathédrale 114 4000 Liège Belgique", "Liège"],
        ["La Carotte", "5.5885333613", "50.6443152", "Boulevard De La Constitution 73 4020 Liège Belgique", "Liège"],
        ["Aurore Lierneux", "5.7944310988", "50.285678", "Rue Chienrue 23 4990 Lierneux Belgique", "Lierneux"],
        ["L’Yves De Poche", "5.9389364", "50.6183102", "Rue G. Maisier 58 4830 Limbourg Belgique", "Limbourg"],
        ["Librairie De L'Europe", "4.5736665", "50.6934914", "Avenue Albert Ier 1 1342 Limelette Belgique", "Limelette"],
        ["Once Upon A Time", "4.3359177", "50.7727383", "Place Communale 21 1630 Linkebeek Belgique", "Linkebeek"],
        ["L’Actualité", "4.6145516", "50.6691244", "Grand Rue 32 1348 Louvain-La-Neuve Belgique", "Louvain-La-Neuve"],
        ["Galerie Livre Et Art", "4.6115387949", "50.66934475", "Grand’Place 13 1348 Louvain-La-Neuve Belgique", "Louvain-La-Neuve"],
        ["Libris Agora Louvain-La-Neuve", "4.6124085", "50.6691933", "Place Agora 14 1348 Louvain-La-Neuve Belgique", "Louvain-La-Neuve"],
        ["Pointculture Louvain-La-Neuve", "4.6187161", "50.6683794", "Place Galilée  9a 1348 Louvain-La-Neuve Belgique", "Louvain-La-Neuve"],
        ["Oxfam Magasins du Monde, Louvain-la-Neuve", "4.6115387949", "50.66934475", "Grand Place 5 1348 Louvain-La-Neuve Belgique", "Louvain-La-Neuve"],
        ["Librairie Cunibert", "6.0264487165", "50.4256205", "Chemin-Rue 49 4960 Malmedy Belgique", "Malmedy"],
        ["Oxfam Magasins du Monde, Malmédy", "6.028204", "50.4254633", "Chemin Rue 4 4960  Belgique", "Malmedy"],
        ["Scs Chanpat", "4.5397698", "50.5483126", "Rue De Priesmont 90 1495 Marbais Belgique", "Marbais"],
        ["Oxfam Magasins du Monde, Marche", "5.223424", "50.1583984", "Place Roi Albert 1er 16 6900  Belgique", "Marche-en-Famenne"],
        ["Librairie Du Bois Planté", "4.4281595", "50.377004", "Rue De La Bruyère 122 6001 Marcinelle Belgique", "Marcinelle"],
        ["Florilège", "4.4339798", "50.388535", "Avenue Eugène Mascaux  450 b8 6001  Marcinelle (Charleroi) Belgique", "Marcinelle (Charleroi)"],
        ["FNAC ", "4.4448867", "51.0530073", "Zandvoorstraat, 3 3 2800 Mechelen Belgique", "Mechelen"],
        ["Librairie Zigrand", "5.4860908", "49.592182", "Rue De Virton 29 6769 Meix-Devant-Virton Belgique", "Meix-Devant-Virton"],
        ["Librairie André Leto", "3.9538229", "50.4538285", "Rue D’Havré 35 7000 Mons Belgique", "Mons"],
        ["Librairie Scientia", "3.9491068", "50.4514199", "Passage du Centre 9 7000 Mons Belgique", "Mons"],
        ["Oxfam Magasins du Monde, Mons CE", "3.9531995", "50.4538974", "Rue d'Havre 15  7000 Mons Belgique", "Mons"],
        ["Librairie Papeterie Huwart, Scrl Saraco", "4.4049374", "50.3889702", "Rue Paul Pastur 22-24 6032 Mont-Sur-Marchienne Belgique", "Mont-Sur-Marchienne"],
        ["Au Bienvenu", "3.5590033", "50.6532938", "Ch De La Liberation 34 7911 Montroeul-Au-Bois Belgique", "Montroeul-Au-Bois"],
        ["Librairie Le Grand Matin, Lecture Loisirs", "4.2426672", "50.4549169", "Grand-Place 17 7140 Morlanwelz Belgique", "Morlanwelz"],
        ["Melpomène", "3.2203546", "50.743572", "Rue De La Station 85 7700 Mouscron Belgique", "Mouscron"],
        ["Lib. De La Chance", "4.8571755", "50.4679616", "Avenue Des Combattants 10 5000 Namur Belgique", "Namur"],
        ["Papyrus", "4.8690755", "50.4630248", "Rue Bas De La Place 16 5000 Namur Belgique", "Namur"],
        ["Librairie De La Monnaie", "4.8665875", "50.4631891", "Rue De La Monnaie 13 5000 Namur Belgique", "Namur"],
        ["Libris Agora Namur", "4.8657689", "50.4648087", "Rue Emile Cuvelier  53-55 5000 Namur Belgique", "Namur"],
        ["Point Virgule", "4.8611744", "50.4659373", "Rue Lelièvre 1 5000 Namur Belgique", "Namur"],
        ["PointCulture Namur", "4.8691377", "50.4625297", "Avenue Golenvaux 5 5000 Namur Belgique", "Namur"],
        ["Oxfam Magasins du Monde, Namur CE", "4.8644172", "50.4645039", "Rue Haute Marcelle 11 5000 Namur Belgique", "Namur"],
        ["Oxygene", "5.4342279", "49.8434301", "Rue Saint-Roch 26 6840 Neufchateau Belgique", "Neufchateau"],
        ["Bio Fagnes", "5.4638852", "50.5381378", "Tige Manchère 5 4121 Neupré  Belgique", "Neupré "],
        ["Librairie Les 4 Canons", "4.32653", "50.5989183", "Rue De Namur 179 1400 Nivelles Belgique", "Nivelles"],
        ["Librairie Willems", "4.32653", "50.5989183", "Rue De Namur 98 1400 Nivelles Belgique", "Nivelles"],
        ["Oxfam Magasins du Monde, Nivelles", "4.32653", "50.5989183", "Rue de Namur 17  1400  Belgique", "Nivelles"],
        ["Librairie Des Saules", "4.4362041", "50.7064678", "Rue Des Saules 18 1380 Ohain Belgique", "Ohain"],
        ["Librairie Winden Sprl", "5.33923", "50.5447278", "Grand-Route  30 4540 Ombret-Rawsa Belgique", "Ombret-Rawsa"],
        ["Lemme Feron Sprl", "5.3445189", "50.7308322", "Grand'Route  82 4360 Oreye Belgique", "Oreye"],
        ["Ps Ottignies Douaire Shop", "4.5669187", "50.6615653", "Av Du Douaire 2 1340 Ottignies Belgique", "Ottignies"],
        ["Icg-Librairie Du Centre", "4.5690877", "50.6660087", "Boulevard Martin  16 1340 Ottignies Belgique", "Ottignies"],
        ["Le Petit Bouquineur", "4.5745461", "50.6709249", "Rue Des Fusillés 2 1340 Ottignies Belgique", "Ottignies"],
        ["Librairie De Pery", "5.4643983", "50.4382941", "Rue Sauvenière  20 4590 Ouffet Belgique", "Ouffet"],
        ["Librairie Du Rond Point", "5.6399957", "50.707192", "Rue Vise-Voie 4 4680 Oupeye Belgique", "Oupeye"],
        ["Librairie Maquoi", "5.5786029", "50.5097799", "Rue De L'Ourthe 16 4171 Poulseur Belgique", "Poulseur"],
        ["Librairie Masses Diarbois", "4.4716878", "50.4512181", "Rue Masses-Diarbois  93-9 6043 Ransart (Charleroi) Belgique", "Ransart (Charleroi)"],
        ["Le Chat Botté", "4.5303937", "50.7121647", "Rue Du Monastère 4 1330 Rixensart Belgique", "Rixensart"],
        ["Oxfam Magasins du Monde, Rixensart", "4.5305369", "50.7124894", "Rue A.Collin 1 1330 Rixensart Belgique", "Rixensart"],
        ["Librairie Point Barre", "5.2211139", "50.1619125", "Rue De Behogne 63 5580 Rochefor Belgique", "Rochefor"],
        ["Lib Du Pont De Pierre", "5.2222715", "50.1615621", "Rue De Behogne 81 5580 Rochefort Belgique", "Rochefort"],
        ["Cooperative Ardente", "5.5309653", "50.6404853", "Rue Aux Cailloux 110 4420 Saint-Nicolas Belgique", "Saint-Nicolas"],
        ["Au Jour Le Jour Falisolle ", "4.6413234", "50.422963", "Rue De Fosses  23 5060 Sambreville Belgique", "Sambreville"],
        ["Librairie La Placa", "5.52047", "50.5985625", "Rue De La Chatqueue 179 4100 Seraing Belgique", "Seraing"],
        ["Librairie Chevrotine", "4.177978", "50.1663456", "Rue Godart 46 6470 Sivry Belgique", "Sivry"],
        ["Lib Cordovero Veronique", "4.0734904", "50.5798989", "Rue Chanoine Scarmure 52 7060 Soignies Belgique", "Soignies"],
        ["Oxfam Magasins du Monde, Soignies CE ", "4.0711921", "50.578464", "Rue de Mons 36 7060 Soignies Belgique", "Soignies"],
        ["Tempresse Sprl Lib Keumiee", "4.6105616", "50.5251313", "Chaussée De Nivelle  21 5140 Sombreffe Belgique", "Sombreffe"],
        ["Libr De Soumagne-Bas", "5.7257517", "50.6061205", "Chaussee De Wegimont 3 4630 Soumagne Belgique", "Soumagne"],
        ["Au Post Scriptum", "5.7332151", "50.63481", "Rue Louis Pasteur 64 4630 Soumagne Belgique", "Soumagne"],
        ["Librairie Multipresse", "5.8631855", "50.4902018", "Place Verte 7 4900 Spa Belgique", "Spa"],
        ["Pages Après Pages", "5.8666322", "50.4914591", "Rue Docteur Henri Schaltin 7 4900 Spa Belgique", "Spa"],
        ["Librairie Pesesse", "5.8663521", "50.4913238", "Rue Servais 29 4900 Spa Belgique", "Spa"],
        ["Librairie Du Centre", "5.6629452", "50.5051593", "Rue Du Centre 35 4140 Sprimont Belgique", "Sprimont"],
        ["Lib. Recto-Verso", "4.7027614", "50.4798866", "Rue Haute 24 5190 Spy Belgique", "Spy"],
        ["Librairie De L’Allée Verte", "5.9342804", "50.3960377", "Avenue Des Démineurs 28 4970 Stavelot Belgique", "Stavelot"],
        ["Librairie Atmosphere", "4.6086474", "50.4332499", "Rue De La Passerelle 2 5060 Tamines Belgique", "Tamines"],
        ["Bio Fagnes", "5.8300062", "50.4987499", "Les Digues 6 4910 Theux Belgique", "Theux"],
        ["Long Courrier", "5.5836281", "50.5688719", "Avenue Laboulle 55 4130 Tilff Belgique", "Tilff"],
        ["Le Comptoir De La Cigogne", "5.7798095", "49.6527252", "Rue Haute 30 6700 Toernich Belgique", "Toernich"],
        ["Oxfam Magasins du Monde, Arlon CE", "5.8129068", "49.6839404", "Place du Marché aux Légumes 11 6700 Toernich Belgique", "Toernich"],
        ["Oxfam Magasins du Monde, Virton", "5.5318057", "49.5684756", "Rue de la Roche 3 6760 Toernich Belgique", "Toernich"],
        ["Décallonne", "3.3870362721", "50.60614695", "Grand Place 18 7500 Tournai Belgique", "Tournai"],
        ["Chantelivre", "3.3899489", "50.6088389", "Quai Notre-Dame 10 7500 Tournai Belgique", "Tournai"],
        ["La Procure  ", "3.3860733", "50.6061793", "Rue Des Maux 22 7500 Tournai Belgique", "Tournai"],
        ["Oxfam Magasins du Monde, Tournai", "3.3888326", "50.6073839", "Rue du Curé Notre Dame 9 7500 Tournai Belgique", "Tournai"],
        ["La Rime", "5.8697476784", "50.37199265", "Avenue Joseph Lejeune 11 4980 Trois-Ponts Belgique", "Trois-Ponts"],
        ["Librairie Du Centre", "4.2057584", "50.6922282", "Plateau De La Gare   30 1480 Tubize Belgique", "Tubize"],
        ["Librairie Boumal", "5.8611386", "50.592586", "Place Verte 42 4800 Verviers Belgique", "Verviers"],
        ["Les Augustins", "5.8552568", "50.5922065", "Pont Du Chêne 1 4800 Verviers Belgique", "Verviers"],
        ["Au Fil D’Ariane", "5.8655774", "50.5910337", "Rue Henri Huard 5 4800 Verviers Belgique", "Verviers"],
        ["La Traversée", "5.8588464", "50.5914499", "Rue Xhavée, 33 4800 Verviers Belgique", "Verviers"],
        ["Oxfam Magasins du Monde, Verviers CE ", "5.8561605", "50.5918899", "Rue de l'Harmonie 6 4800 Verviers Belgique", "Verviers"],
        ["La Dédicace", "5.5325386", "49.5675369", "Place Nestor Outer 11 6770 Virton Belgique", "Virton"],
        ["Librairie Des Remparts", "5.6950798", "50.7356995", "Rue Des Remparts 4 4600 Vise Belgique", "Vise"],
        ["Oxfam Magasins du Monde, Visé CE ", "5.69612", "50.7340807", "Rue Haute 45 4600 Vise Belgique", "Vise"],
        ["Librairie Warnotte", "5.2708847", "50.6994643", "Av Edmond Leburton 14 4300 Waremme Belgique", "Waremme"],
        ["L'Epi", "5.2507079", "50.6952084", "Avenue De La Reine Astrid 40 4300 Waremme Belgique", "Waremme"],
        ["Oxfam Magasins du Monde, Waremme", "5.25622", "50.6978508", "Rue Joseph Wouters 6 4300  Belgique", "Waremme"],
        ["Librairie Ste.Anne", "4.3254275", "50.5981029", "Chaussee De Bruxelles 473Abis 1410 Watreloo Belgique", "Waterloo"],
        ["Librairie Graffiti", "4.397967", "50.7186867", "Chaussée De Bruxelles 129 1410 Waterloo Belgique", "Waterloo"],
        ["Librairie Press O Kay", "4.4228855", "50.7013876", "Dreve Richelle  158B 1410 Waterloo Belgique", "Waterloo"],
        ["Librairie De La Gare", "4.3791756", "50.707315", "Rue Emile Dury 2 1410 Waterloo Belgique", "Waterloo"],
        ["Oxfam Magasins du Monde, Waterloo", "4.4008699", "50.7114481", "Chaussée de Bruxelles  139/B 1410 Waterloo Belgique", "Waterloo"],
        ["Cd Wavre", "4.6060405", "50.7157437", "Place Henri Berger 10 1300 Wavre Belgique", "Wavre"],
        ["Librairie Despontin (My Stock Sprl)", "4.6080238", "50.7165804", "Rue Du Chemin De Fer 10 1300 Wavre Belgique", "Wavre"],
        ["Librairie Des Princes", "4.6194018148", "50.71641325", "Chaussee De Louvain 150 1300 Wavre Belgique", "Wavre"],
        ["Oxfam Magasins du Monde, Wavre CE", "4.6105101", "50.7170789", "Place Cardinal Mercier 9 1300  Belgique", "Wavre"],
        ["Grignard", "5.9682365", "50.6597517", "Rue De L'Eglise 3 4840 Welkenraedt Belgique", "Welkenraedt"],
        ["Franlu Sprl", "4.8792483", "50.3979623", "Chaussee De Dinant 874 5100 Wepion Belgique", "Wepion"],
    ]
    cities_with_libraries = {}
    for library in libraries:
        try:
            cities_with_libraries[library[4]].append(library[0])
        except KeyError:
            cities_with_libraries[library[4]] = [library[0]]
    return sorted(cities_with_libraries.items())

