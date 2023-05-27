# Répresentation du plan du métro parisien avec Neo4j
- Création d'un graphe qui permet de représenter les stations, les liaisons par train, les liaisons à pied et les correspondances a partir des données du métro parisien (avant prolongement de la ligne 14).
- Analyse statistiques a partir du graphe crée (calcul de distance, de temps...)
- Mise en place d'une recherche d'intinéraire en fonction de coordonnées géographiques

![Alt text]([relative%20path/to/img.jpg?raw=true "Title"](https://www.bouygues-construction.com/sites/default/files/ligne_14_paris_01_1_13.jpg))

# 1 - Création du plan

## Création des noeuds (stations de metros)
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

## Création des liaisons entre stations
```neo4j
LOAD CSV WITH HEADERS FROM 'https://github.com/pauldechorgnat/cool-datasets/raw/master/ratp/liaisons.csv' AS row
MATCH (s1:station {ligne: "1"}) WHERE s1.nom_clean = row.start AND s1.ligne = row.ligne
MATCH (s2:station {ligne: "1"}) WHERE s2.nom_clean = row.stop AND s2.ligne = row.ligne AND s2.nom_clean <> s1.nom_clean
MERGE (s1)-[:M1 {name: row.ligne}]->(s2);

LOAD CSV WITH HEADERS FROM 'https://github.com/pauldechorgnat/cool-datasets/raw/master/ratp/liaisons.csv' AS row
MATCH (s1:station {ligne: "2"}) WHERE s1.nom_clean = row.start AND s1.ligne = row.ligne
MATCH (s2:station {ligne: "2"}) WHERE s2.nom_clean = row.stop AND s2.ligne = row.ligne AND s2.nom_clean <> s1.nom_clean
MERGE (s1)-[:M2 {name: row.ligne}]->(s2);

LOAD CSV WITH HEADERS FROM 'https://github.com/pauldechorgnat/cool-datasets/raw/master/ratp/liaisons.csv' AS row
MATCH (s1:station {ligne: "3"}) WHERE s1.nom_clean = row.start AND s1.ligne = row.ligne
MATCH (s2:station {ligne: "3"}) WHERE s2.nom_clean = row.stop AND s2.ligne = row.ligne AND s2.nom_clean <> s1.nom_clean
MERGE (s1)-[:M3 {name: row.ligne}]->(s2);

LOAD CSV WITH HEADERS FROM 'https://github.com/pauldechorgnat/cool-datasets/raw/master/ratp/liaisons.csv' AS row
MATCH (s1:station {ligne: "4"}) WHERE s1.nom_clean = row.start AND s1.ligne = row.ligne
MATCH (s2:station {ligne: "4"}) WHERE s2.nom_clean = row.stop AND s2.ligne = row.ligne AND s2.nom_clean <> s1.nom_clean
MERGE (s1)-[:M4 {name: row.ligne}]->(s2);

LOAD CSV WITH HEADERS FROM 'https://github.com/pauldechorgnat/cool-datasets/raw/master/ratp/liaisons.csv' AS row
MATCH (s1:station {ligne: "5"}) WHERE s1.nom_clean = row.start AND s1.ligne = row.ligne
MATCH (s2:station {ligne: "5"}) WHERE s2.nom_clean = row.stop AND s2.ligne = row.ligne AND s2.nom_clean <> s1.nom_clean
MERGE (s1)-[:M5 {name: row.ligne}]->(s2);

LOAD CSV WITH HEADERS FROM 'https://github.com/pauldechorgnat/cool-datasets/raw/master/ratp/liaisons.csv' AS row
MATCH (s1:station {ligne: "6"}) WHERE s1.nom_clean = row.start AND s1.ligne = row.ligne
MATCH (s2:station {ligne: "6"}) WHERE s2.nom_clean = row.stop AND s2.ligne = row.ligne AND s2.nom_clean <> s1.nom_clean
MERGE (s1)-[:M6 {name: row.ligne}]->(s2);

LOAD CSV WITH HEADERS FROM 'https://github.com/pauldechorgnat/cool-datasets/raw/master/ratp/liaisons.csv' AS row
MATCH (s1:station {ligne: "7"}) WHERE s1.nom_clean = row.start AND s1.ligne = row.ligne
MATCH (s2:station {ligne: "7"}) WHERE s2.nom_clean = row.stop AND s2.ligne = row.ligne AND s2.nom_clean <> s1.nom_clean
MERGE (s1)-[:M7 {name: row.ligne}]->(s2);

LOAD CSV WITH HEADERS FROM 'https://github.com/pauldechorgnat/cool-datasets/raw/master/ratp/liaisons.csv' AS row
MATCH (s1:station {ligne: "8"}) WHERE s1.nom_clean = row.start AND s1.ligne = row.ligne
MATCH (s2:station {ligne: "8"}) WHERE s2.nom_clean = row.stop AND s2.ligne = row.ligne AND s2.nom_clean <> s1.nom_clean
MERGE (s1)-[:M8 {name: row.ligne}]->(s2);

LOAD CSV WITH HEADERS FROM 'https://github.com/pauldechorgnat/cool-datasets/raw/master/ratp/liaisons.csv' AS row
MATCH (s1:station {ligne: "9"}) WHERE s1.nom_clean = row.start AND s1.ligne = row.ligne
MATCH (s2:station {ligne: "9"}) WHERE s2.nom_clean = row.stop AND s2.ligne = row.ligne AND s2.nom_clean <> s1.nom_clean
MERGE (s1)-[:M9 {name: row.ligne}]->(s2);

LOAD CSV WITH HEADERS FROM 'https://github.com/pauldechorgnat/cool-datasets/raw/master/ratp/liaisons.csv' AS row
MATCH (s1:station {ligne: "10"}) WHERE s1.nom_clean = row.start AND s1.ligne = row.ligne
MATCH (s2:station {ligne: "10"}) WHERE s2.nom_clean = row.stop AND s2.ligne = row.ligne AND s2.nom_clean <> s1.nom_clean
MERGE (s1)-[:M10 {name: row.ligne}]->(s2);

LOAD CSV WITH HEADERS FROM 'https://github.com/pauldechorgnat/cool-datasets/raw/master/ratp/liaisons.csv' AS row
MATCH (s1:station {ligne: "11"}) WHERE s1.nom_clean = row.start AND s1.ligne = row.ligne
MATCH (s2:station {ligne: "11"}) WHERE s2.nom_clean = row.stop AND s2.ligne = row.ligne AND s2.nom_clean <> s1.nom_clean
MERGE (s1)-[:M11 {name: row.ligne}]->(s2);

LOAD CSV WITH HEADERS FROM 'https://github.com/pauldechorgnat/cool-datasets/raw/master/ratp/liaisons.csv' AS row
MATCH (s1:station {ligne: "12"}) WHERE s1.nom_clean = row.start AND s1.ligne = row.ligne
MATCH (s2:station {ligne: "12"}) WHERE s2.nom_clean = row.stop AND s2.ligne = row.ligne AND s2.nom_clean <> s1.nom_clean
MERGE (s1)-[:M12 {name: row.ligne}]->(s2);

LOAD CSV WITH HEADERS FROM 'https://github.com/pauldechorgnat/cool-datasets/raw/master/ratp/liaisons.csv' AS row
MATCH (s1:station {ligne: "13"}) WHERE s1.nom_clean = row.start AND s1.ligne = row.ligne
MATCH (s2:station {ligne: "13"}) WHERE s2.nom_clean = row.stop AND s2.ligne = row.ligne AND s2.nom_clean <> s1.nom_clean
MERGE (s1)-[:M13 {name: row.ligne}]->(s2);

LOAD CSV WITH HEADERS FROM 'https://github.com/pauldechorgnat/cool-datasets/raw/master/ratp/liaisons.csv' AS row
MATCH (s1:station {ligne: "14"}) WHERE s1.nom_clean = row.start AND s1.ligne = row.ligne
MATCH (s2:station {ligne: "14"}) WHERE s2.nom_clean = row.stop AND s2.ligne = row.ligne AND s2.nom_clean <> s1.nom_clean
MERGE (s1)-[:M14 {name: row.ligne}]->(s2);

LOAD CSV WITH HEADERS FROM 'https://github.com/pauldechorgnat/cool-datasets/raw/master/ratp/liaisons.csv' AS row
MATCH (s1:station {ligne: "3bis"}) WHERE s1.nom_clean = row.start AND s1.ligne = row.ligne
MATCH (s2:station {ligne: "3bis"}) WHERE s2.nom_clean = row.stop AND s2.ligne = row.ligne AND s2.nom_clean <> s1.nom_clean
MERGE (s1)-[:M3bis {name: row.ligne}]->(s2);

LOAD CSV WITH HEADERS FROM 'https://github.com/pauldechorgnat/cool-datasets/raw/master/ratp/liaisons.csv' AS row
MATCH (s1:station {ligne: "7bis"}) WHERE s1.nom_clean = row.start AND s1.ligne = row.ligne
MATCH (s2:station {ligne: "7bis"}) WHERE s2.nom_clean = row.stop AND s2.ligne = row.ligne AND s2.nom_clean <> s1.nom_clean
MERGE (s1)-[:M7bis {name: row.ligne}]->(s2);
```

## Création des relations entre station de nom identiques
```neo4j
MATCH (s1:station)
WITH s1.nom_clean as nom1, COUNT(s1) as count1
WHERE count1>1
MATCH (s2:station) WHERE s2.nom_clean = nom1
MATCH (s3:station) WHERE s3.nom_clean = s2.nom_clean AND s2.ligne <> s3.ligne
MERGE (s2)-[:M]->(s3)
MERGE (s2)<-[:M]-(s3);
```

## Création des relations ou les correspondances est possibles à pied (moins d'1km):
```neo4j
MATCH (s1)-[*1]->(s2)
WITH s1, s2, SQRT((s2.latitude - s1.latitude)*(s2.latitude - s1.latitude) + (s2.longitude - s1.longitude)*(s2.longitude - s1.longitude))/1000 AS distance
WHERE distance <= 1
MERGE (s1)-[:ALLER_A_PIED {distance: distance}]->(s2)
MERGE (s1)<-[:ALLER_A_PIED {distance: distance}]-(s2);
```

# 2 - Analyse statistique

## Le nombre de correspondances par station
```neo4j
MATCH (s1)-[:M]->(s2) 
MATCH (s1)<-[:M]-(s2) 
RETURN s1.nom_clean AS station, count(*) AS nombre ORDER BY station;
```

## Le nombre de stations à moins de deux kilomètres de la station LA DEFENSE
```neo4j
MATCH (s1 {nom_clean: "LADEFENSE"})
MATCH (s2) WHERE s2.nom_clean <> s1.nom_clean
AND SQRT((s2.latitude - s1.latitude)*(s2.latitude - s1.latitude) + (s2.longitude - s1.longitude)*(s2.longitude - s1.longitude))/1000 <= 2
RETURN count(*);
```

## Le temps qu'il faut pour aller en metro de LA DEFENSE à CHATEAU DE VINCENNES
```neo4j
//# temps_en_metro exprimé en minutes
MATCH (s1 {nom_clean: "LADEFENSE"})
MATCH (s2 {nom_clean: "CHATEAUDEVINCENNES"})
RETURN ((SQRT((s2.latitude - s1.latitude)*(s2.latitude - s1.latitude) + (s2.longitude - s1.longitude)*(s2.longitude - s1.longitude))/1000)/40)*60 AS temps_en_metro;
```

## Le temps qu'il faut pour aller à pied de LA DEFENSE à CHATEAU DE VINCENNES
```neo4j
//# temp_a_pied exprimé en heure
MATCH (s1 {nom_clean: "LADEFENSE"})
MATCH (s2 {nom_clean: "CHATEAUDEVINCENNES"})
RETURN ((SQRT((s2.latitude - s1.latitude)*(s2.latitude - s1.latitude) + (s2.longitude - s1.longitude)*(s2.longitude - s1.longitude))/1000)/4) AS temp_a_pied;
```

## Le nombre de stations se trouvant dans un rayon de 10 stations par train autour de SAINT LAZARE
```neo4j
MATCH (s1 {nom_clean: "STLAZARE"})-[*10]-> (s2) WHERE s2.nom_clean <> s1.nom_clean
RETURN DISTINCT s2;
```

## Le nombre de stations se trouvant dans un rayon de 20 minutes par train autour de SAINT LAZARE
```neo4j
MATCH (s1 {nom_clean: "STLAZARE"})-[:M3|M12|M13|M14]->( s2)
WHERE ((SQRT((s2.latitude - s1.latitude)*(s2.latitude - s1.latitude) + (s2.longitude - s1.longitude)*(s2.longitude - s1.longitude))/1000)/40)*60 <= 20
RETURN COUNT(s2);
```

# 3 - Recherche d'un intinéraire
```neo4j
#! /usr/bin/python

# Import de la librairie GraphDatabase
from neo4j import GraphDatabase

# Creation d'un connecteur à la base neo4j
driver = GraphDatabase.driver('bolt://0.0.0.0:7687', auth=('neo4j', 'neo4j'))

def get_cordonnes(x1, y1, x2, y2):

    print("===>Recherche de l'itineraire:","(",x1,y1,")","(",x2,y2,")")

    # Creation de la requete
    query = '''
    MATCH (start: station {latitude: $x1, longitude: $y1})
    MATCH (end:station {latitude: $x2, longitude: $y2})
    CALL gds.alpha.shortestPath.stream({
          nodeQuery: 'MATCH (n) RETURN id(n) as id',
            relationshipQuery: 'MATCH (n1)-[r:M1|M2|M3|M4|M5|M6|M7|M8|M9|M10|M11|M12|M13|M14|M3bis|M7bis]-(n2) RETURN id(r) as id, id(n1) as source, id(n2) as target',
              startNode: start,
                endNode: end
                })
    YIELD nodeId
    RETURN gds.util.asNode(nodeId)
    '''

    with driver.session() as session:
        result = session.run(query, x1=x1, y1=y1, x2=x2, y2=y2).data()
        print(result)


# Appel de la fonction
# Vous pouvez changer les valeurs x1, y1, x2 et y2 pour d'autres recherches
get_cordonnes(x1=653520.3175,y1=6867583.1321,x2=646627.8252,y2=6858472.7468)
```
