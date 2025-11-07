from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass

    #caso 1: nessun epoca specifica
    def get_artefatti(self):
        print("artefatto_DAO.get_artefatti(): Executing read from database using SQL query")
        listaArtefatti = []
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            print("Connection failed")
            return None
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT *
                       FROM artefatto"""
            cursor.execute(query)
            for row in cursor:
                artefatto = Artefatto(row["id"], row["nome"], row["tipologia"], row["epoca"], row["id_museo"])
                listaArtefatti.append(artefatto)
            cursor.close()
            cnx.close()
            return listaArtefatti

    def get_epoca(self):
        print("artefatto_DAO.get_epoca(): Executing read from database using SQL query")
        listaEpoche =[]
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            print("Connection failed")
            return None
        else:
            cursor = cnx.cursor()
            query = """SELECT distinct(epoca)
                        FROM artefatto"""
            cursor.execute(query)
            for row in cursor:
                epoca = row[0]
                listaEpoche.append(epoca)
            return listaEpoche

    @staticmethod
    def get_artefattiX_Museo(museo, epoca):
        print("artefatto_DAO.get_artefattiX_Museo(): Executing read from database using SQL query")
        listaArtefatti = []
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            print("Connection failed")
            return None
        else:
            if museo == 'Nessun filtro':
                museo = None
            if epoca == 'Nessun filtro':
                epoca = None
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT a.id, a.nome, a.tipologia, a.epoca, a.id_museo
                       FROM artefatto a, museo m
                       WHERE a.id_museo = m.id and m.nome = COALESCE(%s, m.nome)
                       and a.epoca = COALESCE(%s, a.epoca)"""
            cursor.execute(query, (museo, epoca,))
            for row in cursor:
                artefatto = Artefatto(row["id"], row["nome"], row["tipologia"], row["epoca"], row["id_museo"])
                listaArtefatti.append(artefatto)
            cursor.close()
            cnx.close()
            return listaArtefatti
    # TODO