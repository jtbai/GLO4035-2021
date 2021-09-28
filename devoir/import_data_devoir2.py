# Lorsque vous démarrez le conteneur pour la première fois,
# Assurez vous de changer le mot de passe par défaut et de mettre le mot de passe suivant
# supersecret

from py2neo import Graph, Node, Relationship

url = "bolt://localhost:7687"
user = "neo4j"
password = "supersecret"

graph = Graph(url, auth=(user, password), secure=False)

transaction = graph.begin()

quebec = Node("Ville", fondation=1608, population=531900, altitude=98, langues="français", nom="Québec")
levis = Node("Ville", fondation=1681, population=145000, altitude=62, langues="français", nom="Lévis")
pierre_laporte = Relationship(quebec, "route", levis, nom="Pont Pierre-Laporte", distance=1000)
transaction.create(quebec)
transaction.create(levis)
transaction.create(pierre_laporte)

stoneham = Node("Ville", fondation=1805, population=1900, altitude=198, langues="français", nom="Stoneham")

transaction.create(quebec)
transaction.create(Relationship(quebec, "route", stoneham, nom="La 73", distance=24000))

trois_rivieve = Node("Ville", nom="Trois-Rivières", fondation=1634, population=134410, altitude=61, langues="français")
la_40_qc_tr = Relationship(quebec, "route", trois_rivieve, nom="La 40", distance=128000)
transaction.create(trois_rivieve)
transaction.create(la_40_qc_tr)

shawinigan = Node("Ville", nom="Shawinigan", fondation=1901, population=50060, altitude=123, langues="français")
la_55_tr_shawi = Relationship(trois_rivieve, "route", shawinigan, nom="La 55", distance=42600)
transaction.create(shawinigan)
transaction.create(la_55_tr_shawi)

montreal = Node("Ville", nom="Montréal", fondation=1642, population=1705000, altitude=6, langues="anglais")
la_40_tr_mtl = Relationship(trois_rivieve, "route", montreal, nom="La 40", distance=141600)
transaction.create(montreal)
transaction.create(la_40_tr_mtl)

st_jerome = Node("Ville", nom="Saint-Jérôme", fondation=1642, population=68456, altitude=6, langues="français")
la_15_mtl_stje = Relationship(montreal, "route", st_jerome, nom="La 15", distance=58500)
transaction.create(st_jerome)
transaction.create(la_15_mtl_stje)

rigaud = Node("Ville", nom="Rigaud", fondation=1732, population=7566, altitude=221, langues="français")
la_40_mtl_rigaud = Relationship(montreal, "route", rigaud, nom="La 40", distance=67600)
transaction.create(rigaud)
transaction.create(la_40_mtl_rigaud)

drummunville = Node("Ville", nom="Drummondville", fondation=1815, population=77235, altitude=111, langues="français")
la_20_drummon_levis = Relationship(levis, "route", drummunville, nom="La 20", distance=143400)
la_20_drummon_mtl = Relationship(drummunville, "route", montreal, nom="La 20", distance=107600)
transaction.create(drummunville)
transaction.create(la_20_drummon_levis)
transaction.create(la_20_drummon_mtl)

matane = Node("Ville", nom="Matane", fondation=1891, population=14462, altitude=15, langues="français")
transaction.create(matane)
perce = Node("Ville", nom="Percé", fondation=1800, population=3312, altitude=5, langues="français")
transaction.create(perce)
val_espoir = Node("Ville", nom="Val D'Espoir", fondation=1800, population=400, altitude=98, langues="français")
transaction.create(val_espoir)

la_20_levis_matane = Relationship(levis, "route", matane, nom="La 20", distance=309700)
la_132_matane_perce = Relationship(matane, "route", perce, nom="La 132", distance=346500)
la_132_perce_valdespoir = Relationship(perce, "route", val_espoir, nom="La 132", distance=21400)

transaction.create(la_20_levis_matane )
transaction.create(la_132_matane_perce)
transaction.create(la_132_perce_valdespoir)

trou_du_diable = Node("Microbrasserie", nom="Le trou du diable")
corsaire = Node("Microbrasserie", nom="Le corsaire")
dieu_du_ciel = Node("Microbrasserie", nom="Dieu du ciel")
auval = Node("Microbrasserie", nom="Auval")
castor = Node("Microbrasserie", nom="Le castor")
bockale = Node("Microbrasserie", nom="Bockale")
souche = Node("Microbrasserie", nom="La souche")
forge_du_malt = Node("Microbrasserie", nom="Les Forges du malt")
la_fabrique = Node("Microbrasserie", nom="La fabrique")
pit_caribou = Node("Microbrasserie", nom="Pit Caribou")
noctem = Node("Microbrasserie", nom="Le Noctem")

transaction.create(trou_du_diable)
transaction.create(Relationship(trou_du_diable, "est_à", shawinigan))

transaction.create(noctem)
tdd_shawi = Relationship(noctem, "est_à", quebec)

transaction.create(tdd_shawi)
transaction.create(corsaire)

transaction.create(Relationship(corsaire, "est_à", levis))
transaction.create(dieu_du_ciel)
transaction.create(Relationship(dieu_du_ciel, "est_à", st_jerome))
transaction.create(auval)
transaction.create(Relationship(auval, "est_à", val_espoir))
transaction.create(castor)
transaction.create(Relationship(castor, "est_à", rigaud))
transaction.create(bockale)
transaction.create(Relationship(bockale, "est_à", drummunville))
transaction.create(souche)
transaction.create(Relationship(souche, "est_à", quebec))
transaction.create(forge_du_malt)
transaction.create(Relationship(forge_du_malt, "est_à", trois_rivieve))
transaction.create(la_fabrique)
transaction.create(Relationship(la_fabrique, "est_à", matane))
transaction.create(pit_caribou)
transaction.create(Relationship(pit_caribou, "est_à", perce))

india_pale_ale = Node("Type_Bière", nom="India Pale Ale")
rousse = Node("Type_Bière", nom="Rousse")
stout = Node("Type_Bière", nom="Stout")
saison = Node("Type_Bière", nom="Saison")

transaction.create(india_pale_ale)
transaction.create(rousse)
transaction.create(stout)
transaction.create(saison)

nordet = Node("Bière", nom="Nordet", cote=5)
transaction.create(nordet)
transaction.create(Relationship(nordet, "est_une", india_pale_ale))
transaction.create(Relationship(auval, "fait_la", nordet))

moralite = Node("Bière", nom="Moralité", cote=4.5)
transaction.create(moralite)
transaction.create(Relationship(moralite, "est_une", india_pale_ale))
transaction.create(Relationship(dieu_du_ciel, "fait_la", moralite))

gros_char = Node("Bière", nom="Les gros chars", cote=3.5)
transaction.create(gros_char)
transaction.create(Relationship(gros_char, "est_une", india_pale_ale))
transaction.create(Relationship(la_fabrique, "fait_la", gros_char))

surfeur = Node("Bière", nom="Les surfeurs de l'apocalypso", cote=4)
transaction.create(surfeur)
transaction.create(Relationship(surfeur, "est_une", india_pale_ale))
transaction.create(Relationship(trou_du_diable, "fait_la", surfeur))

uss_vermont = Node("Bière", nom="USS Vermont", cote=4)
transaction.create(Relationship(uss_vermont, "est_une", india_pale_ale))
transaction.create(Relationship(corsaire, "fait_la", uss_vermont))

peche_mortel = Node("Bière", nom="Peché mortel", cote=5)
transaction.create(peche_mortel)
transaction.create(Relationship(peche_mortel, "est_une", stout))
transaction.create(Relationship(dieu_du_ciel, "fait_la", peche_mortel))

sang_encre = Node("Bière", nom="Sang d'encre", cote=3.5)
transaction.create(peche_mortel)
transaction.create(Relationship(sang_encre, "est_une", stout))
transaction.create(Relationship(trou_du_diable, "fait_la", sang_encre))

saison_rayee = Node("Bière", nom="La saison rayée", cote=5)
transaction.create(saison_rayee)
transaction.create(Relationship(saison_rayee, "est_une", saison))
transaction.create(Relationship(castor, "fait_la", saison_rayee))

barouette = Node("Bière", nom="La barouette", cote=3)
transaction.create(barouette)
transaction.create(Relationship(barouette, "est_une", saison))
transaction.create(Relationship(souche, "fait_la", barouette))

gros_pins = Node("Bière", nom="Gros Pins", cote=4)
transaction.create(gros_pins)
transaction.create(Relationship(gros_pins, "est_une", rousse))
transaction.create(Relationship(souche, "fait_la", gros_pins))

cat_nip = Node("Bière", nom="La Catnip", cote=4.5)
transaction.create(cat_nip)
transaction.create(Relationship(cat_nip, "est_une", india_pale_ale))
transaction.create(Relationship(noctem, "fait_la", cat_nip))


saison_c = Node("Bière", nom="La saison C", cote=4.5)
transaction.create(saison_c)
transaction.create(Relationship(saison_c, "est_une", saison))
transaction.create(Relationship(pit_caribou, "fait_la", saison_c))

tignasse = Node("Bière", nom="Tignasse", cote=4)
transaction.create(tignasse)
transaction.create(Relationship(forge_du_malt, "fait_la", tignasse))
transaction.create(Relationship(tignasse, "est_une",rousse))

euphorique = Node("Bière",nom="Euphorique", cote=4.5)
transaction.create(euphorique)
transaction.create(Relationship(euphorique, "est_une",rousse))
transaction.create(Relationship(bockale, "fait_la", euphorique))

graph.commit(transaction)