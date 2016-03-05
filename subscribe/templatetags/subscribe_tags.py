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
def get_bookshops():
    bookshops = [
        ["Librairie Dewolf A", "50.67434", "5.51338", "Avenue Du Progrès, 3 / 6, 4432 Alleur", "Alleur"],
        ["Riga James Lib", "50.539376", "5.287872", "Rue De La Gare , 6A, 4540 Ampsin (Amay)", "Ampsin (Amay)"],
        ["Magasin Du Monde-Oxfam Anderlecht", "50.835657", "4.305595", "Rue Saint Guidon, 13, 1070 Anderlecht", "Anderlecht"],
        ["Librairie Le Quotidien - Angleur", "50.611121", "5.59968", "Rue De Tilff, 15, 4031 Angleur", "Angleur"],
        ["Lettre Ecarlate", "49.683556", "5.815549", "Rue Du Marché Au Beurre,, 17, 6700 Arlon", "Arlon"],
        ["Magasin Du Monde-Oxfam Arlon Commerce Équitable", "49.68394", "5.812907", "Place Du Marché Aux Légumes,11, 6700 Arlon", "Arlon"],
        ["Librairie Littérath", "50.628981", "3.776741", "Rue Ernest Cambier, 18, 7800 Ath", "Ath"],
        ["Librairie Claire Laval", "50.22493", "5.29695", "Rue Grande , 24, 6900 Aye", "Aye"],
        ["Librairie Du Centre - Aywaille", "50.474687", "5.675311", "Place Joseph Thiry, 29, 4920 Aywaille", "Aywaille"],
        ["Librairie Chez Tante Jack", "50.6285596", "5.9700023", "Route De Dolhain, 16, 4837 Baelen-Sur-Vesdre", "Baelen-Sur-Vesdre"],
        ["Le Libre Air", "50.66866", "5.69992", "Rue De Heuseux, 3, 4671 Barchon", "Barchon"],
        ["Librairie Du Centre -Barvaux", "50.35064", "5.49306", "En Charotte , 3, 6940 Barvaux-Sur-Ourthe", "Barvaux-Sur-Ourthe"],
        ["Librairie Croisy", "50.003326", "5.718727", "Rue Du Sablon, 131, 6600 Bastogne", "Bastogne"],
        ["Librairie Cloquette", "50.478479", "3.831097", "Rue Louis Anciaux, 9, 7331 Baudour", "Baudour"],
        ["Librairie D'En Haut", "50.235648", "4.237498", "Rue D'En Haut, 11, 6500 Beaumont", "Beaumont"],
        ["Librairie Centrale - Beauraing", "50.109161", "4.956887", "Rue De Bouillon , 23, 5570 Beauraing", "Beauraing"],
        ["Librairie De La Gare Beauraing", "50.114455", "4.956279", "Rue De La Gare, 23, 5570 Beauraing", "Beauraing"],
        ["Magasin Du Monde-Oxfam Beauraing", "50.110241", "4.955416", "Rue De Dinant, 2, 5570 Beauraing", "Beauraing"],
        ["Librairie De La Gare - Bertrix", "49.853041", "5.267005", "Rue De La Gare, 170, 6880 Bertrix", "Bertrix"],
        ["Librairie Guisset", "50.623819", "5.652469", "Rue De Jupille, 24, 4610 Beyne-Heusay", "Beyne-Heusay"],
        ["Librairie De Bierges", "50.709305", "4.595763", "Rue Provinciale, 155, 1301 Bierges", "Bierges"],
        ["Librairie De La Reine", "50.411239", "4.16534", "Grand Place,, 9, 7130 Binche", "Binche"],
        ["Magasin Du Monde-Oxfam Boitsfort", "50.79893", "4.41712", "Rue Du Ministre, 18, 1170 Boitsfort", "Boitsfort"],
        ["Librairie Au Passe Temps", "50.683226", "4.389967", "Route Du Lion, 86, 1420 Braine L'Alleud", "Braine L'Alleud"],
        ["Le Baobab", "50.680666", "4.377926", "Rue Des Alliés, 3, 1420 Braine-L'Alleud", "Braine-L'Alleud"],
        ["Librairie Bonaventure", "50.679294", "4.366512", "Chaussée D’Ophain, 14, 1420 Braine-L’Alleud", "Braine-L’Alleud"],
        ["Librairie Glineur", "50.602697", "4.13247", "Rue Neuve, 81, 7090 Braine-Le-Comte", "Braine-Le-Comte"],
        ["Librairie Kikadikoi", "50.606384", "4.137893", "Rue De La Station, 133, 7090 Braine-Le-Comte", "Braine-Le-Comte"],
        ["Magasin Du Monde-Oxfam Braine-le-Comte", "50.61025", "4.136941", "Rue De La Station, 4, 7090 Braine-Le-Comte", "Braine-Le-Comte"],
        ["Librairie Herman", "50.627256", "5.148487", "Rue Du Sacre-Coeur, 2, 4260 Braives", "Braives"],
        ["Librairie Joskin-Meens", "50.641622", "5.592515", "Rue Du Marché, 11, 4020 Bressoux", "Bressoux"],
        ["Alti-Cent Loisir - Boek In Sa", "50.812589", "4.321891", "Pl De L'Altitude Cent, 26, 1190 Bruxelles", "Bruxelles"],
        ["Boom - Le Café Du Commerce Équitable", "50.848051", "4.346416", "Rue Pletinckx, 7, 1000 Bruxelles", "Bruxelles"],
        ["Brüsel - Anspach", "50.849631", "4.351997", "Boulevard Anspach, 100, 1000 Bruxelles", "Bruxelles"],
        ["Coffee & Food - Press World", "50.815526", "4.36677", "Chaussee De Waterloo, 715, 1180 Bruxelles", "Bruxelles"],
        ["Continental Press Club", "50.836272", "4.365632", "Rue De La Paix, 38, 1050 Bruxelles", "Bruxelles"],
        ["Couleurs Du Sud", "50.823572", "4.376693", "Avenue Adolphe Buyl, 80, 1050 Bruxelles", "Bruxelles"],
        ["Eskimmo", "50.851919", "4.39392", "Avenue Léon Mahillon , 97-101, 1030 Bruxelles", "Bruxelles"],
        ["Euro City Press", "50.840674", "4.37331", "Rue Montoyer, 66, 1000 Bruxelles", "Bruxelles"],
        ["Fnac City 2", "50.85071", "4.353733", "Rue Neuve, 1000 Bruxelles", "Bruxelles"],
        ["Heyday", "50.83726", "4.347268", "Rue Des Renards , 8, 1000 Bruxelles", "Bruxelles"],
        ["Jolitab", "50.811434", "4.390369", "Av Guillaume Gilbert, 43, 1050 Bruxelles", "Bruxelles"],
        ["La Detente", "50.830589", "4.392219", "Rue Des Champs, 50, 1040 Bruxelles", "Bruxelles"],
        ["La Feuille De Chou", "50.815987", "4.390191", "Avenue De La Couronne, 467, 1050 Bruxelles", "Bruxelles"],
        ["Le Petit Filigranes", "50.79049", "4.355919", "Parvis St. Pierre, 10, 1180 Bruxelles", "Bruxelles"],
        ["Lestadho Sprl", "50.871445", "4.399754", "Avenue Henri Conscience, 147, 1140 Bruxelles", "Bruxelles"],
        ["Librairie 1992", "50.841815", "4.383456", "Rue Froissart, 143, 1040 Bruxelles", "Bruxelles"],
        ["Librairie Coin Lecture", "50.850308", "4.427823", "Rue G. Et J. Martin, 31, 1200 Bruxelles", "Bruxelles"],
        ["Librairie De Helmet.", "50.872583", "4.389616", "Place De Helmet, 9, 1030 Bruxelles", "Bruxelles"],
        ["Librairie De La Trinite", "50.825277", "4.358783", "Parvis De La Trinite, 7, 1050 Bruxelles", "Bruxelles"],
        ["Librairie Des Archiducs", "50.80859", "4.417811", "Avenue Des Archiducs, 64, 1170 Bruxelles", "Bruxelles"],
        ["Librairie Des Maieurs", "50.83727", "4.431334", "Place Des Maieurs, 2, 1150 Bruxelles", "Bruxelles"],
        ["Librairie Du Domaine", "50.806318", "4.328643", "Rue Gatti De Gamond, 2, 1180 Bruxelles", "Bruxelles"],
        ["Librairie Du Dries - Quenima", "50.803618", "4.399499", "Dries, 77, 1170 Bruxelles", "Bruxelles"],
        ["Librairie Du Millenaire", "50.831769", "4.38584", "Rue Philippe Baucq, 45, 1040 Bruxelles", "Bruxelles"],
        ["Librairie Etienne", "50.897184", "4.359123", "Avenue De Busleyden, 1B, 1020 Bruxelles", "Bruxelles"],
        ["Librairie Filigranes", "50.833574", "4.394348", "Avenue Des Arts, 39, 1040 Bruxelles", "Bruxelles"],
        ["Librairie Klb & Co", "50.851955", "4.387187", "Av De La Brabanconne, 116, 1030 Bruxelles", "Bruxelles"],
        ["Librairie Le Centenaire", "50.885793", "4.341957", "Av Houba De Strooper, 30, 1020 Bruxelles", "Bruxelles"],
        ["Librairie Moliere", "50.815959", "4.339761", "Chaussee D'Alsemberg, 349, 1190 Bruxelles", "Bruxelles"],
        ["Librairie Place Marie José - Quenima", "50.806411", "4.387455", "Place Marie José, 5A, 1050 Bruxelles", "Bruxelles"],
        ["Librairie Saint-Julien", "50.821048", "4.407612", "Chaussee De Wavre, 1285, 1160 Bruxelles", "Bruxelles"],
        ["Librairie Topaze", "50.852753", "4.394623", "Avenue De La Topaze, 65, 1030 Bruxelles", "Bruxelles"],
        ["Librairie Vismet", "50.853189", "4.346632", "Quai Aux Briques, 82, 1000 Bruxelles", "Bruxelles"],
        ["Librairie Wallonie Bruxelles", "50.859251", "4.343197", "À L'Intention De Sylvain Poupier, Service De La Promotion Des Lettres, Ministère De La Communautré Française, Boulevard Léopold 2, 44, 1080 Bruxelles", "Bruxelles"],
        ["Magasin Du Monde-Oxfam Bruxelles-Bourse", "50.846337", "4.347212", "Boulevard Anspach, 137, 1000 Bruxelles", "Bruxelles"],
        ["Maison De La Presse", "50.863874", "4.324634", "Av Berchem-Ste-Agathe, 73, 1081 Bruxelles", "Bruxelles"],
        ["Nos Pilifs", "50.903708", "4.388841", "Trassersweg, 347, 1020 Bruxelles", "Bruxelles"],
        ["Ozfair", "50.83237", "4.343026", "Avenue Jean Volders, 9, 1060 Bruxelles", "Bruxelles"],
        ["Passa Porta", "50.849593", "4.346756", "Rue Antoine Dansaert , 46, 1000 Bruxelles", "Bruxelles"],
        ["Pointculture Bruxelles", "50.8528", "4.365625", "Rue Royale, 145, 1000 Bruxelles", "Bruxelles"],
        ["Press & Cafe - Bruxelles", "50.821537", "4.343051", "Place Albert, 2, 1190 Bruxelles", "Bruxelles"],
        ["Press Center", "50.822844", "4.357945", "Rue Du Page, 61, 1050 Bruxelles", "Bruxelles"],
        ["Press Et Lis", "50.876978", "4.327574", "Rue Henri Werrie, 88, 1090 Bruxelles", "Bruxelles"],
        ["Press Line Sablon", "50.839817", "4.355592", "Rue Des Sablons, 17, 1000 Bruxelles", "Bruxelles"],
        ["Tapage - Telelivre Sprl", "50.833644", "4.402445", "Rue Père De Deken, 83, 1040 Bruxelles", "Bruxelles"],
        ["Théâtre 140", "50.851863", "4.396203", "Avenue Eugène Plasky , 140, 1030 Bruxelles", "Bruxelles"],
        ["Théâtre De Poche", "50.812406", "4.371271", "Chemin Du Gymnase, 1A, 1000 Bruxelles", "Bruxelles"],
        ["Théâtre La Balsamine", "50.851955", "4.389504", "Avenue Félix Marchal , 1, 1030 Bruxelles", "Bruxelles"],
        ["Théatre Le Rideau", "50.852241", "4.384035", "Rue Thomas Vinçotte , 68/4 , 1030 Bruxelles", "Bruxelles"],
        ["Tipi Bookshop", "50.827257", "4.345107", "Rue Hôtel Des Monnaies, 186, 1060 Bruxelles", "Bruxelles"],
        ["Toute La Presse Sprl", "50.839665", "4.398982", "Avenue De Tervueren, 14, 1040 Bruxelles", "Bruxelles"],
        ["Tropismes", "50.848145", "4.354793", "Galerie Des Princes, 11, 1000 Bruxelles", "Bruxelles"],
        ["Tulitu", "50.85181", "4.346493", "Rue De Flandre, 55, 1000 Bruxelles", "Bruxelles"],
        ["Worldwide", "50.850349", "4.367569", "Rue Des Cultes, 28, 1000 Bruxelles", "Bruxelles"],
        ["Librairie De Bosquetville", "50.406879", "4.44842", "Rue De Montigny, 106, 6000 Charleroi", "Charleroi"],
        ["Librairie Du Pont Neuf", "50.408211", "4.447455", "Rue Du Pont Neuf, 68, 6000 Charleroi", "Charleroi"],
        ["Magasin Du Monde-Oxfam Charleroi", "50.407711", "4.4467", "Rue De Montigny, 68, 6000 Charleroi", "Charleroi"],
        ["Molière & Cie", "50.407796", "4.44299", "Boulevard Tirou 68, 68, 6000 Charleroi", "Charleroi"],
        ["Pointculture Charleroi", "50.413248", "4.442676", "Avenue De L’Europe, 1, 6000 Charleroi", "Charleroi"],
        ["Le Passe-Temps - Chatelet", "50.405234", "4.522278", "Rue Neuve, 12, 6200 Chatelet", "Chatelet"],
        ["Librairie Le Kiosque", "50.684439", "4.698792", "Rue Colleau, 8, 1325 Chaumont Gistoux", "Chaumont Gistoux"],
        ["Librairie Vidéo Night", "50.6111024", "5.619261", "Rue De Beaufraipont, 16, 4032 Chenée", "Chenée"],
        ["Librairie Cardon", "50.586236", "3.806593", "Rue Saint Jean, 33, 7950 Chievres", "Chievres"],
        ["Le Papyrus - Chimay", "50.047639", "4.316195", "Rue Des Ormeaux, 25, 6460 Chimay", "Chimay"],
        ["Dlire De Lire", "50.295655", "5.100826", "Rue Du Ctre, 88, 5590 Ciney", "Ciney"],
        ["New Press 2000", "50.294926", "5.10061", "Rue Courtejoie, 10A, 5590 Ciney", "Ciney"],
        ["La Petite Lanterne", "50.46075", "4.380839", "Rue Winston Churchill, 9, 6180 Courcelles", "Courcelles"],
        ["Librairie Le Rond Point", "50.65325", "4.564441", "Avenue Des Metallurgistes, 1, 1490 Court-Saint-Etienne", "Court-Saint-Etienne"],
        ["Quatre-Quarts", "50.620949", "4.559869", "Rue De Werchai (Dans La Gare), , 1490 Court-Saint-Etienne", "Court-Saint-Etienne"],
        ["Librairie Aux Nouvelles", "50.706207", "5.40506", "Grand Route, 63, 4367 Crisnee", "Crisnee"],
        ["Dlivre", "50.257769", "4.914564", "Rue Grande, 67A, 5500 Dinant", "Dinant"],
        ["Biosphere", "50.7046638", "4.6514723", "Boulevard Du Centenaire, 8, 1325 Dion-Valmont", "Dion-Valmont"],
        ["Chez Sarah", "50.610751", "5.850261", "Rue Leopold, 83, 4820 Dison", "Dison"],
        ["Librairie Plaisir De Lire - Embourg", "50.59288", "5.605573", "Rue Pierre Henvard, 6, 4053 Embourg", "Embourg"],
        ["Magasin Du Monde-Oxfam Embourg", "50.59283", "5.605547", "Rue Pierre Henvard, 2, 4053 Embourg", "Embourg"],
        ["Magasin Du Monde-Oxfam Enghien", "50.693656", "4.039492", "Rue D'Hérinnes, 4, 7850 Enghien", "Enghien"],
        ["Librairie Européenne - Etterbeek", "50.84336", "4.396244", "Rue De L'Orme, 1, 1040 Etterbeek", "Etterbeek"],
        ["Magasin Du Monde-Oxfam Etterbeek", "50.830408", "4.390915", "Rue Des Champs, 8, 1040 Etterbeek", "Etterbeek"],
        ["Libr Pap Du Bati", "50.40029", "5.60564", "Place Du Chablis, 17, 4190 Ferrieres", "Ferrieres"],
        ["Librairie Tombal", "50.656545", "5.399806", "Grand'Route , 296 6B, 4347 Fexhe-Le-Haut-Clocher", "Fexhe-Le-Haut-Clocher"],
        ["Librairie De Fléron S.A", "50.614563", "5.682539", "Avenue Des Martyrs, 232, 4620 Fleron", "Fleron"],
        ["Librairie Carine sprl", "50.737229", "3.737648", "Rue René Dubreucq, 1, 7880 Flobecq", "Flobecq"],
        ["Librairie Wéry-Pérani", "49.698017", "5.31024", "Rue Généraux Cuvelier, 4, 6820 Florenville", "Florenville"],
        ["Librairie Du Wiels", "50.82468", "4.326136", "Avenue Van Volxem, 354, 1190 Forest", "Forest"],
        ["Press & Café - Forest", "50.821537", "4.343051", "Place Albert, 2, 1190 Forest", "Forest"],
        ["La Librairie.Be", "50.573652", "4.99807", "Avenue De La Libération, 15, 5380 Forville", "Forville"],
        ["Librairie La Souris", "50.39455", "4.69617", "Vitrival, 6, 5070 Fosses-La-Ville", "Fosses-La-Ville"],
        ["Librairie Du Circuit", "50.446606", "5.962572", "Route Du Circuit, 16, 4970 Francorchamps", "Francorchamps"],
        ["Librairie Rimes Et Bulles", "49.979305", "4.936266", "Rue De Charleville, 12, 5575 Gedinne", "Gedinne"],
        ["Agricovert", "50.572513", "4.691364", "Chaussée De Wavre, 37, 5030 Gembloux", "Gembloux"],
        ["Antigone", "50.560796", "4.691966", "Place De L'Orneau 17/A, , 5030 Gembloux", "Gembloux"],
        ["L'Apostrophe - Gembloux", "50.560401", "4.692851", "Grand'Rue , 5, 5030 Gembloux", "Gembloux"],
        ["Magasin Du Monde-Oxfam Gembloux", "50.560202", "4.692306", "Rue Léopold, 17-19, 5030 Gembloux", "Gembloux"],
        ["Librairie Le Canard - Genappe", "50.610164", "4.450566", "Rue De Charleroi, 18, 1470 Genappe", "Genappe"],
        ["L'Entree Livre", "50.7211", "4.49388", "Place Communale, 53, 1332 Genval", "Genval"],
        ["Librairie Le Paon", "50.7211", "4.49388", "Rue De La Station, 37, 1332 Genval", "Genval"],
        ["Gesves Presse", "50.40659", "5.067857", "Chaussee De Gramptinne, 161, 5340 Gesves", "Gesves"],
        ["Alphapress", "50.475839", "3.901172", "Place De Ghlin , 7, 7011 Ghlin", "Ghlin"],
        ["La Librairie De Gastuche", "50.735129", "4.650504", "Chaussée De Wavre, 404, 1390 Grez-Doiceau", "Grez-Doiceau"],
        ["Le Diffuseur De Presse", "50.6412", "5.5718", "Rue Fraichamps, 129, 4030 Grivegnee", "Grivegnee"],
        ["Librairie De L'Avenue", "50.62894", "5.60144", "Avenue De Peville, 321, 4030 Grivegnée", "Grivegnée"],
        ["Al'Binète Haccourt", "50.734314", "5.670914", "Avenue Reine Elisabeth, 17, 4684 Haccourt", "Haccourt"],
        ["Ready Night", "50.44449", "4.6734915", "5190 Ham Sur Sambre", "Ham Sur Sambre"],
        ["Mordant Librairie", "50.670083", "5.081587", "Rue Albert 1Er , 52, 4280 Hannut", "Hannut"],
        ["Librairie Du Rond Point - Herve", "50.638735", "5.784492", "Rue De La Clef, 74, 4650 Herve", "Herve"],
        ["Magasin Du Monde-Oxfam Herve", "50.639452", "5.792851", "Rue Léopold, 34, 4650 Herve", "Herve"],
        ["Papyland", "50.581779", "5.863964", "Avenue Hanlet,, 41, 4802 Heusy", "Heusy"],
        ["Librairie Le Quotidien - Hognoules", "50.6667", "5.4667", "Rue Des Moulins , 7, 4342 Hognoul", "Hognoul"],
        ["Librairie A L'Écolier", "50.48578", "4.1446", "Rue Liébin, 29, 7110 Houdeng-Aimeries", "Houdeng-Aimeries"],
        ["Librairie Recto-Verso", "50.141901", "5.69122", "Place Roi Albert, 10, 6660 Houffalize", "Houffalize"],
        ["Diachron", "50.518993", "5.240715", "Rue Des Augustins, 4, 4500 Huy", "Huy"],
        ["La Dérive", "50.518019", "5.241256", "Grand Place, 10, 4500 Huy", "Huy"],
        ["Magasin Du Monde-Oxfam Huy", "50.518983", "5.240719", "Rue Des Fouarges, 14, 4500 Huy", "Huy"],
        ["Brüsel Flagey", "50.828498", "4.372682", "Place Eugène Flagey, 29, 1050 Ixelles", "Ixelles"],
        ["Candide", "50.833343", "4.366629", "Place Brugman, 1, 1050 Ixelles", "Ixelles"],
        ["Fnac Toison d’Or", "50.83747", "4.35998", "Avenue De La Toison D'Or, 17A, 1050 Ixelles", "Ixelles"],
        ["L’Air Libre", "50.825601", "4.373831", "Rue Alphonse De Witte, 44, 1050 Ixelles", "Ixelles"],
        ["L’Autre Filigranes", "50.819898", "4.359679", "Avenue Louis Lepoutre, 2, 1050 Ixelles", "Ixelles"],
        ["Librairie Louis D’Or", "50.826066", "4.361142", "Rue Du Bailli, 54, 1050 Ixelles", "Ixelles"],
        ["Magasin Du Monde-Oxfam Ixelles Commerce Équitable", "50.835662", "4.363258", "Chaussée D'Ixelles, 77, 1050 Ixelles", "Ixelles"],
        ["Magasin Du Monde-Oxfam Ixelles Seconde Main", "50.817056", "4.387638", "Avenue Brillat Savarin, 18, 1050 Ixelles", "Ixelles"],
        ["Peinture Fraiche", "50.833343", "4.366629", "Rue De Tabellion, 10, 1050 Ixelles", "Ixelles"],
        ["Ptyx", "50.827871", "4.369362", "Rue Lesbroussart, 39, 1050 Ixelles", "Ixelles"],
        ["Rodriguez Patrick", "50.814159", "4.386325", "Avenue De L'Université, 74, 1050 Ixelles", "Ixelles"],
        ["Théatre Varia", "50.834722", "4.378715", "Rue Du Sceptre, 78, 1050 Ixelles", "Ixelles"],
        ["Press' Gourmande Sprl", "50.520562", "5.911344", "Tiege, 76, 4845 Jalhay", "Jalhay"],
        ["Lib. Au Bia Bouquin", "50.456425", "4.871489", "Avenue Jean Materne, 128, 5100 Jambes", "Jambes"],
        ["Magasin Du Monde-Oxfam Jette", "50.880858", "4.322789", "Rue Léopold 1er, 527, 1090 Jette", "Jette"],
        ["Ver Sprl", "50.880858", "4.322789", "Rue E Desmet, 2 - 4, 1090 Jette", "Jette"],
        ["L'Apostrophe - Jodoigne", "50.725088", "4.876564", "Rue De Piétrain, 36, 1370 Jodoigne", "Jodoigne"],
        ["L'Ivre De Papier Sa", "50.724733", "4.871595", "Rue Saint-Jean, 34, 1370 Jodoigne", "Jodoigne"],
        ["La Librairie De La Bruyère", "50.724671", "4.869681", "Rue Saint Jean, 1, 1370 Jodoigne", "Jodoigne"],
        ["Librairie Du Chateau", "50.724137", "4.868145", "Place De La Victoire, 7, 1370 Jodoigne", "Jodoigne"],
        ["Librairie Du Château - Doublon", "50.724137", "4.868145", "Place De La Victoire , 7, 1370 Jodoigne", "Jodoigne"],
        ["Librairie Chez Arlette", "50.642556", "5.634788", "Rue Jean Hermesse, 48, 4020 Jupille", "Jupille"],
        ["Tibo", "50.647666", "5.632289", "Rue De Visé, 164, 4020 Jupille", "Jupille"],
        ["La librairie - Zorza", "50.641947", "5.641622", "Rue Du Couvent, 30, 4020 Jupille-Sur-Meuse", "Jupille-Sur-Meuse"],
        ["Librairie De Jurbise", "50.509852", "3.926545", "Route D'Ath, 190 A, 7050 Jurbise", "Jurbise"],
        ["Librairie Kain Tombe", "50.626445", "3.38992", "Rue Albert, 21, 7540 Kain", "Kain"],
        ["Astrid Press", "50.848735", "4.466245", "Av.Reine Astrid, 272, 1950 Kraainem", "Kraainem"],
        ["Librairie De L'Eglise", "50.731291", "4.490178", "Rue De L'Eglise, 6, 1310 La Hulpe", "La Hulpe"],
        ["Librairie De La Mazerine", "50.730996", "4.485671", "Square Marie-Pouli, 1A, 1310 La Hulpe", "La Hulpe"],
        ["Librairie Des 3 Colonnes", "50.731845", "4.48085", "Chaussée De Bruxelles 8A, 8A, 1310 La Hulpe", "La Hulpe"],
        ["Librairie Les 2 Freres", "50.731213", "4.488088", "Rue Des Combattants, 62, 1310 La Hulpe", "La Hulpe"],
        ["L’Ecrivain Public", "50.479447", "4.190122", "Rue Louis De Brouckère, 45, 7100 La Louvière", "La Louvière"],
        ["Le Litherer", "50.17999", "5.576262", "Place Du Bronze, 14, 6980 La Roche-En-Ardenne", "La Roche-En-Ardenne"],
        ["Librairie Nicolay", "49.982828", "5.256236", "Rue Du Commerce, 44, 6890 Libin", "Libin"],
        ["Le Temps De Lire", "49.92191", "5.37726", "Rue Du Serpont, 13, 6800 Libramont", "Libramont"],
        ["Barricade / Entre-Temps", "50.646898", "5.573082", "Rue Pierreuse, 21, 4000 Liege", "Liege"],
        ["Librairie De L'Observatoire", "50.619736", "5.564807", "Avenue De L'Observatoire, 351, 4000 Liege", "Liege"],
        ["Librairie Des Vennes", "50.628118", "5.581361", "Rue Des Vennes, 44, 4020 Liege", "Liege"],
        ["Librairie Du Thier", "50.635076", "5.562887", "Rue Walther Dewe, 26, 4000 Liege", "Liege"],
        ["Librairie Espace-Papier", "50.630799", "5.558946", "Rue Des Wallons, 35, 4000 Liege", "Liege"],
        ["Librairie Stéphane Hessel", "50.642689", "5.568026", "Place Xavier Neujean, 22, 4000 Liege", "Liege"],
        ["Cochet", "50.635076", "5.562887", "Place Général Leuman, 14, 4000 Liège", "Liège"],
        ["Espace Ulg Opéra", "50.635076", "5.562887", "Place De La République Française, 35/RDC, 4000 Liège", "Liège"],
        ["Fnac Liège", "50.644157", "5.57239", "Rue Joffre, 3, 4000 Liège", "Liège"],
        ["La Carotte - Liège", "50.643951", "5.586977", "Boulevard De La Constitution, 73, 4020 Liège", "Liège"],
        ["La Diode - Liège", "50.641559", "5.575259", "Place Cockerill, 12, 4000 Liège", "Liège"],
        ["Librairie Varia", "50.646084", "5.576845", "Rue Des Mineurs, 8, 4000 Liège", "Liège"],
        ["Livre Aux Trésors", "50.642758", "5.567842", "Place Xavier-Neujean,, 27A, 4000 Liège", "Liège"],
        ["Magasin Du Monde-Oxfam Liège Centre", "50.641255", "5.571586", "Rue Cathédrale, 114, 4000 Liège", "Liège"],
        ["Pax", "50.641701", "5.575851", "Place Cockerill, 4, 4000 Liège", "Liège"],
        ["Pointculture Liège", "50.6448", "5.571383", "Rue De L’Official, 1 – 5, 4000 Liège", "Liège"],
        ["Wattitude", "50.635076", "5.562887", "Rue Du Souverain, 4, 4000 Liège", "Liège"],
        ["Librairie Robin Des Bois Techpress", "50.676165", "5.546319", "Place Reine Astrid, 3, 4000 Liège Rocourt", "Liège Rocourt"],
        ["Aurore Lierneux", "50.283838", "5.796668", "Rue Chienrue, 23, 4990 Lierneux", "Lierneux"],
        ["L’Yves De Poche", "50.603665", "5.935724", "Rue G. Maisier, 58, 4830 Limbourg", "Limbourg"],
        ["Librairie Dethier", "50.603665", "5.935724", "Avenue David, 37, 4830 Limbourg", "Limbourg"],
        ["Librairie De L'Europe", "50.6805002", "4.5731775", "Avenue Albert Ier, 1, 1342 Limelette", "Limelette"],
        ["Winkelbeek", "50.766026", "4.345609", "Rue De Hollebeek , 163A, 1630 Linkebeek", "Linkebeek"],
        ["Fnac Louvain-La-Neuve", "50.67097", "4.616631", "Place De L'Accueil, 10, 1348 Louvain-La-Neuve", "Louvain-La-Neuve"],
        ["Galerie Livre Et Art", "50.669279", "4.612252", "Grand’Place, 13, 1348 Louvain-La-Neuve", "Louvain-La-Neuve"],
        ["L’Actualité", "50.669124", "4.614552", "Grand Rue, 32, 1348 Louvain-La-Neuve", "Louvain-La-Neuve"],
        ["Libris Agora Louvain-La-Neuve", "50.669193", "4.612409", "Place Agora, 14, 1348 Louvain-La-Neuve", "Louvain-La-Neuve"],
        ["Magasin Du Monde-Oxfam Louvain-la-Neuve", "50.669279", "4.612252", "Grand-Place, 5, 1348 Louvain-La-Neuve", "Louvain-La-Neuve"],
        ["Pointculture Louvain-La-Neuve", "50.668379", "4.618716", "Place Galilée , 9A, 1348 Louvain-La-Neuve", "Louvain-La-Neuve"],
        ["Librairie De Maisières", "50.487547", "3.963258", "Rue Grande , 109, 7020 Maisières", "Maisières"],
        ["Librairie Cunibert", "50.425731", "6.02653", "Chemin-Rue, 49, 4960 Malmedy", "Malmedy"],
        ["Magasin Du Monde-Oxfam Malmédy", "50.4254633", "6.028204", "Chemin Rue, 4, 4960 Malmédy", "Malmédy"],
        ["Librairie Du Bois Planté", "50.377004", "4.428159", "Rue De La Bruyère, 122, 6001 Marcinelle", "Marcinelle"],
        ["Florilège", "50.400144", "4.433045", "Avenue Eugène Mascaux, 450 B8, 6001 Marcinelle (Charleroi)", "Marcinelle (Charleroi)"],
        ["Librairie Zigrand", "49.592182", "5.486091", "Rue De Virton, 29, 6769 Meix-Devant-Virton", "Meix-Devant-Virton"],
        ["Le Point Du Jour", "50.459445", "3.953167", "Grand Rue, 72, 7000 Mons", "Mons"],
        ["Librairie André Leto", "50.453775", "3.953859", "Rue D’Havré, 35, 7000 Mons", "Mons"],
        ["Librairie Scientia", "50.454217", "3.95669", "Passage Du Centre, 9 - 11 - 13, 7000 Mons", "Mons"],
        ["Magasin Du Monde-Oxfam Mons", "50.453913", "3.953077", "Rue D'Havré, 15, 7000 Mons", "Mons"],
        ["Librairie Papeterie Huwart, Scrl Saraco", "50.38897", "4.404937", "Rue Paul Pastur, 22-24, 6032 Mont-Sur-Marchienne", "Mont-Sur-Marchienne"],
        ["Au Bienvenu", "50.653294", "3.559003", "Ch De La Liberation, 34, 7911 Montroeul-Au-Bois", "Montroeul-Au-Bois"],
        ["Librairie Em2N", "50.27498", "4.56593", "Grand Place , 162, 5621 Morialmé", "Morialmé"],
        ["Librairie Le Grand Matin", "50.454975", "4.242622", "Grand-Place, 17, 7140 Morlanwelz", "Morlanwelz"],
        ["Melpomène", "50.743452", "3.222594", "Rue De La Station, 85, 7700 Mouscron", "Mouscron"],
        ["Proxi Store", "50.471976", "4.994584", "Rue JB Wauthier, 4, 5030 Namêche", "Namêche"],
        ["Lib. De La Chance", "50.468231", "4.856487", "Avenue Des Combattants, 10, 5000 Namur", "Namur"],
        ["Librairie De La Monnaie", "50.463248", "4.866641", "Rue De La Monnaie, 13, 5000 Namur", "Namur"],
        ["Libris Agora Namur", "50.464798", "4.865797", "Rue Emile Cuvelier , 53-55, 5000 Namur", "Namur"],
        ["Magasin Du Monde-Oxfam Namur Commerce Équitable", "50.464459", "4.863823", "Rue Haute Marcelle, 11, 5000 Namur", "Namur"],
        ["Papyrus - Namur", "50.463025", "4.86901", "Rue Bas De La Place, 16, 5000 Namur", "Namur"],
        ["Point Virgule Sprl - Namur", "50.464812", "4.860991", "Rue Lelièvre, 1, 5000 Namur", "Namur"],
        ["Pointculture Namur", "50.462392", "4.868905", "Avenue Golenvaux, 14, 5000 Namur", "Namur"],
        ["Oxygene", "49.84343", "5.434228", "Rue Saint-Roch, 26, 6840 Neufchateau", "Neufchateau"],
        ["Bio Fagnes - Neupré", "50.539026", "5.462985", "Tige Manchère, 5, 4121 Neupré", "Neupré"],
        ["Compagnie Des Mots - Mulalu Sprl", "50.59847", "4.328008", "Place Emile De Lalieux , 26, 1400 Nivelles", "Nivelles"],
        ["Librairie Willems", "50.599299", "4.329237", "Rue De Namur, 98, 1400 Nivelles", "Nivelles"],
        ["Magasin Du Monde-Oxfam Nivelles", "50.598103", "4.325427", "Rue De Namur, 17, 1400 Nivelles", "Nivelles"],
        ["Librairie Des Saules", "50.69907", "4.46919", "Rue Des Saules, 18, 1380 Ohain", "Ohain"],
        ["Lemme Feron Sprl", "50.728191", "5.351208", "Grand'Route , 82, 4360 Oreye", "Oreye"],
        ["Icg-Librairie Du Centre", "50.665973", "4.569167", "Boulevard Martin , 16, 1340 Ottignies", "Ottignies"],
        ["Le Petit Bouquineur", "50.669462", "4.573296", "Rue Des Fusillés, 2, 1340 Ottignies", "Ottignies"],
        ["Ps Ottignies Douaire Shop", "50.665106", "4.568145", "Av Du Douaire, 2, 1340 Ottignies", "Ottignies"],
        ["Librairie De Pery", "50.439747", "5.463558", "Rue Sauvenière , 20, 4590 Ouffet", "Ouffet"],
        ["Librairie Du Rond Point - Oupeye", "50.709004", "5.643766", "Rue Vise-Voie, 4, 4680 Oupeye", "Oupeye"],
        ["Librairie Wallonie-Bruxelles", "48.861051", "2.350543", "Rue Quincampoix, 46, 75004 Paris, France", "Paris, France"],
        ["Apostrophe Perwez", "50.631185", "4.795386", "Ch De Wavre 150, , 1360 Perwez", "Perwez"],
        ["Librairie Maquoi", "50.509111", "5.57755", "Rue De L'Ourthe, 16, 4171 Poulseur", "Poulseur"],
        ["Librairie Sapio Ransart", "50.451218", "4.471688", "Rue Masses-Diarbois, 93-9, 6043 Ransart (Charleroi)", "Ransart (Charleroi)"],
        ["Autre Chose - Rixensart", "50.710974", "4.530633", "Avenue Kennedy , 1, Bte 11, 1330 Rixensart", "Rixensart"],
        ["Librairie Le Chat Botte", "50.712203", "4.530381", "Rue Du Monastere, 4, 1330 Rixensart", "Rixensart"],
        ["Magasin Du Monde-Oxfam Rixensart", "50.710974", "4.530633", "Rue A. Collin, 1, 1330 Rixensart", "Rixensart"],
        ["Lib Du Pont De Pierre", "50.162017", "5.220014", "Rue De Behogne, 81, 5580 Rochefort", "Rochefort"],
        ["Librairie Point Barre", "50.1615621", "5.2222715", "Rue De Behogne, 63, 5580 Rochefort", "Rochefort"],
        ["Al'Binète Rocourt", "50.676281", "5.545686", "Chaussée De Tongres, 412, 4000 Rocourt", "Rocourt"],
        ["Parade - Café Litéraire", "50.823847", "4.343298", "Rue De Savoie, 59, 1060 Saint Gilles", "Saint Gilles"],
        ["Aux Portes De L’Info", "50.826813", "4.356861", "Rue Defacqz, 89, 1060 Saint-Gilles", "Saint-Gilles"],
        ["Hors Format", "50.82246", "4.342768", "ChausséE D’Alsemberg, 142, 1060 Saint-Gilles", "Saint-Gilles"],
        ["Joli Mai", "50.825789", "4.344794", "Avenue Paul Dejaer, 29, 1060 Saint-Gilles", "Saint-Gilles"],
        ["Les Yeux Gourmands", "50.831065", "4.344096", "Avenue Jean Volders,, 64A, 1060 Saint-Gilles", "Saint-Gilles"],
        ["Librairie-Presse Volders", "50.831814", "4.343584", "Avenue Jean Volders,, 40, 1060 Saint-Gilles", "Saint-Gilles"],
        ["Magasin Du Monde-Oxfam Saint-Gilles", "50.828064", "4.344159", "Chaussée De Waterloo, 137, 1060 Saint-Gilles", "Saint-Gilles"],
        ["Vidéo Express", "50.8251", "4.348188", "Chaussée De Waterloo, 241, 1060 Saint-Gilles", "Saint-Gilles"],
        ["Librairie Du Centre - Saint-Marc", "50.487775", "4.845986", "Rue Du Centre, 86, 5003 Saint-Marc", "Saint-Marc"],
        ["Cooperative Ardente", "50.640506", "5.530999", "Rue Aux Cailloux, 110, 4420 Saint-Nicolas", "Saint-Nicolas"],
        ["Le Point Press Sprl - Saint Sauveur", "50.7226931", "3.5841589", "Chaussée De Renaix, 67, 7912 Saint-Sauveur", "Saint-Sauveur"],
        ["Au Jour Le Jour Falisolle (Sambreville)", "50.424334", "4.623951", "Rue De Fosses , 23,  Sambreville", "Sambreville"],
        ["Bar Du Gaspi", "50.864506", "4.373429", "Chaussée De Haecht, 309, 1030 Schaerbeek", "Schaerbeek"],
        ["Librairie Du Noyer", "50.847453", "4.392727", "Rue Du Noyer, 238, 1030 Schaerbeek", "Schaerbeek"],
        ["Magasin Du Monde-Oxfam Schaerbeek", "50.867416", "4.377298", "Place D'Helmet, 2, 1030 Schaerbeek", "Schaerbeek"],
        ["Librairie La Placa", "50.598563", "5.52047", "Rue De La Chatqueue, 179, 4100 Seraing", "Seraing"],
        ["Lib Cordovero Veronique", "50.579899", "4.07349", "Rue Chanoine Scarmure, 52, 7060 Soignies", "Soignies"],
        ["Tempresse Sprl Lib Keumiee", "50.52871", "4.5884", "Chaussée De Nivelle , 21, 5140 Sombreffe", "Sombreffe"],
        ["Librairie Somzee  Benedicte Martinesse", "50.29517", "4.48336", "Grand Rue 19 5651 Somzee, , 5651 Somzee", "Somzee, , 5651 Somzee"],
        ["Au Post Scriptum", "50.633709", "5.734016", "Rue Louis Pasteur, 64, 4630 Soumagne", "Soumagne"],
        ["Libr De Soumagne-Bas", "50.612157", "5.746079", "Chaussee De Wegimont, 3, 4630 Soumagne", "Soumagne"],
        ["Librairie Multipresse", "50.490894", "5.863318", "Place Verte, 7, 4900 Spa", "Spa"],
        ["Librairie Pesesse", "50.491186", "5.864606", "Rue Servais, 29, 4900 Spa", "Spa"],
        ["Pages Après Pages", "50.492121", "5.866442", "Rue Docteur Henri Schaltin, 7, 4900 Spa", "Spa"],
        ["Librairie Du Centre - Sprimont", "50.503146", "5.661749", "Rue Du Centre, 35, 4140 Sprimont", "Sprimont"],
        ["Librairie De L’Allée Verte", "50.396697", "5.936292", "Avenue Des Démineurs, 28, 4970 Stavelot", "Stavelot"],
        ["Librairie Atmosphere", "50.43353", "4.60819", "Avenue Du Président Roosevelt, 65, 5060 Tamines", "Tamines"],
        ["La Libre.Et.Rie", "50.092619", "5.503068", "Route De La Barrière, 13, 6970 Tenneville", "Tenneville"],
        ["Bio Fagnes - Theux", "50.507963", "5.826891", "Les Digues, 6, 4910 Theux", "Theux"],
        ["Long Courrier", "50.567667", "5.581643", "Avenue Laboulle, 55, 4130 Tilff", "Tilff"],
        ["Le Comptoir De La Cigogne", "49.652725", "5.77981", "Rue Haute, 30, 6700 Toernich", "Toernich"],
        ["Chantelivre", "50.609351", "3.388805", "Quai Notre-Dame, 10, 7500 Tournai", "Tournai"],
        ["Décallonne", "50.606278", "3.387119", "Grand Place, 18, 7500 Tournai", "Tournai"],
        ["La Procure", "50.606254", "3.384139", "Rue Des Maux, 22, 7500 Tournai", "Tournai"],
        ["Librairie Saint-Jacques", "50.609269", "3.384299", "Rue Saint-Jacques, 4, 7500 Tournai", "Tournai"],
        ["Magasin Du Monde-Oxfam Tournai", "50.607384", "3.388833", "Rue Du Curé Notre-Dame, 9, 7500 Tournai", "Tournai"],
        ["La Rime", "50.372104", "5.870325", "Avenue Joseph Lejeune, 11, 4980 Trois-Ponts", "Trois-Ponts"],
        ["Librairie Du Centre - Tubize", "50.692228", "4.205758", "Plateau De La Gare , 30, 1480 Tubize", "Tubize"],
        ["Edgar And Co", "50.792981", "4.362217", "Chaussée De Saint Job, 713, 1180 Uccle", "Uccle"],
        ["L'Harmonium", "50.814042", "4.355262", "Rue Vanderkindere, 293, 1180 Uccle", "Uccle"],
        ["La Licorne - Vivlia Scrl", "50.801482", "4.336738", "Chaussée D’Alsemberg,, 732, 1180 Uccle", "Uccle"],
        ["Librairie Des 4 Bras", "50.5", "4.8667", "Ruedes Frères Bieva, 3, 5020 Vedrin", "Vedrin"],
        ["Au Fil D’Ariane", "50.591034", "5.865577", "Rue Henri Huard, 5, 4800 Verviers", "Verviers"],
        ["La Traversée", "50.591504", "5.858936", "Rue Xhavée,, 33, 4800 Verviers", "Verviers"],
        ["Les Augustins", "50.591793", "5.855221", "Pont Du Chêne, 1, 4800 Verviers", "Verviers"],
        ["Librairie Boumal", "50.592183", "5.860459", "Place Verte, 42, 4800 Verviers", "Verviers"],
        ["Librairie Milo", "50.586889", "5.860865", "Rue De France , 50, 4800 Verviers", "Verviers"],
        ["Le Rat Des Champs", "50.283792", "5.9149", "Rue De L'Hotel De Ville, 11, 6690 Vielsalm", "Vielsalm"],
        ["La Dédicace", "49.5677263", "5.5329559", "Place Nestor Outer, 11, 6770 Virton", "Virton"],
        ["Magasin Du Monde-Oxfam Visé Commerce Équitable", "50.733915", "5.696298", "Rue Haute, 45, 4600 Visé", "Visé"],
        ["Librairie De L'Avenir", "50.253811", "4.432237", "Rue De La Montagne, 26, 5650 Walcourt", "Walcourt"],
        ["Librairie De La Place", "50.536171", "5.215682", "Chaussée De Wavre, 30, 4520 Wanze", "Wanze"],
        ["Autre Chose - Waremme", "50.694473", "5.271846", "Chaussée Romaine, 186, , 4300 Waremme", "Waremme"],
        ["L'Epi", "50.69757", "5.25553", "Avenue De La Reine Astrid, 40, 4300 Waremme", "Waremme"],
        ["Librairie Warnotte", "50.697864", "5.257777", "Av Edmond Leburton, 14, 4300 Waremme", "Waremme"],
        ["Librairie De La Gare - Waterloo", "50.714551", "4.382863", "Rue Emile Dury, 2, 1410 Waterloo", "Waterloo"],
        ["Librairie Graffiti", "50.719306", "4.397679", "Chaussée De Bruxelles, 129, 1410 Waterloo", "Waterloo"],
        ["Librairie Press O Kay", "50.704494", "4.417094", "Dreve Richelle , 158B, 1410 Waterloo", "Waterloo"],
        ["Magasin Du Monde-Oxfam Waterloo", "50.71818", "4.398071", "Chaussée De Bruxelles, 139/B, 1410 Waterloo", "Waterloo"],
        ["Abao", "50.796538", "4.417923", "Rue Middelbourg, 40, 1170 Watermael-Boitsfort", "Watermael-Boitsfort"],
        ["Cd Wavre", "50.7160578", "4.6056991", "Place Henri Berger, 10, 1300 Wavre", "Wavre"],
        ["Librairie Des Princes", "50.716502", "4.620705", "Chaussee De Louvain, 150, 1300 Wavre", "Wavre"],
        ["Librairie Despontin (My Stock Sprl)", "50.71658", "4.608024", "Rue Du Chemin De Fer, 10, 1300 Wavre", "Wavre"],
        ["Magasin Du Monde-Oxfam Wavre Commerce Équitable", "50.716944", "4.610639", "Place Cardinal Mercier, 9, 1300 Wavre", "Wavre"],
        ["Grignard", "50.660623", "5.971538", "Rue De L'Eglise, 3, 4840 Welkenraedt", "Welkenraedt"],
        ["Franlu Sprl", "50.42529", "4.870967", "Chaussee De Dinant, 874, 5100 Wepion", "Wepion"],
        ["A Livre Ouvert", "50.843906", "4.435846", "Rue Saint Lambert, 116, 1200 Woluwé-Saint-Lambert", "Woluwé-Saint-Lambert"],
        ["Cook & Book Woluwé", "50.847997", "4.437286", "Place Du Temps Libre, 1, 1200 Woluwé-Saint-Lambert", "Woluwé-Saint-Lambert"],
        ["Magasin Du Monde-Oxfam Stockel", "50.8407029", "4.4627462", "Rue De l'Eglise, 91, 1150 Woluwe-Saint-Pierre", "Woluwe-Saint-Pierre"],
    ]
    d = {}
    for bookshop in bookshops:
        try:
            d[bookshop[4]].append(bookshop[0])
        except KeyError:
            d[bookshop[4]] = [bookshop[0]]
    for key in d.keys():
        d[key].sort()
    return sorted(d.items())
