# Répresentation du plan du métro parisiens avec Neo4j
Création d'un graphe qui permet de représenter les stations, les liaisons par train, les liaisons à pied et les correspondances a partir des données du métro parisien (avant prolongement de la ligne 14).

# Création des noeuds (stations de metros)
```neo4j
LOAD CSV WITH HEADERS FROM 'https://github.com/pauldechorgnat/cool-datasets/raw/master/ratp/stations.csv' AS row
CREATE (:station {nom_clean : row.nom_clean , 
                    nom_gare :row.nom_gare , 
                    latitude: toFloat(row.x), 
                    longitude: toFloat(row.y), 
                    trafic: row.Trafic,
					          ville: row.Ville,
					        ligne: row.ligne
});
```
