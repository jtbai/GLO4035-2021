### Devoir 3: Aggrégateur de nouvelles élastique ###
#
# Les requêtes sont toutes indépendantes :)
#
# Encore une fois, vos réponses doivent s'imprimer sur une seule ligne sous le tag du numéro de question
import elasticsearch

SERVER_HOST = "https://j7Lcqgrunp:yu2BarFJsHD3EPLwQR7m@jdm-4560318065.us-east-1.bonsaisearch.net:443"
es = elasticsearch.Elasticsearch(SERVER_HOST)

#QTEST - Combien de documents sont retournés au maximum par requêtes?
print("#QTEST")
print(es.search(index="jdm", body={})['hits']['total']['value'])

# Q0 - Combien de documents contiennent le mot "corruption" ?
# Réponse: entier
print("#Q0")

# Q1 - Combien de documents ont le mot "corruption" dans leur contenu
# Réponse: entier
print("#Q1")

# Q2 - Combien d'articles ont été écrit par des auteurs ayant le prénom "Jonathan"
# Réponse: entier
print("#Q2")

# Q3 - Combien d'articles mentionnent au moins 2 niveau de gouvernement (municipal, provincial, fédéral) dans leur contenu
# Réponse: entier
print("#Q3")

# Q4 - On désire trouver un document qui a le mot "bière" dans son contenu et de préférence qui ce soit en lien avec l'"Autriche"
# Quel est la valeur du produit entre le nombre total de document trouvés et le score du premier document (total * _score)
print("#Q4")

# Q5- On désire trouver des articles qui parlent d'au moins deux niveau de gouvernement, mais on aimerait accorder 2x plus de poids aux documents qui contiennent le mot corruption.
# Qui est l'auteur du premier document ?
# Hint: Booostez les mots importants!
# Réponse: Chaîne de caractères
print("#Q5")

# Q6 - cherche un document qui avait une phrase très similaire à "Awaye continue comme ça". On se rappelle qu'il y avait au plus 5 mots entre ces mots.
# Quel est le nom de cet article ?
# Réponse: Chaîne de caractère
print("#Q6")


