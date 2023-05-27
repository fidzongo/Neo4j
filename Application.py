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
