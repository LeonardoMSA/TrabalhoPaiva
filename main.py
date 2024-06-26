def main():
    # Checa componentes essenciais para o funcionamento do código em geral
    import install as ins
    ins.CheckEssentials.installLibs()
    ins.CheckEssentials.checkAPIJsonWin()

    import kaggle_link as kag
    import db as dbPost
    # Baixar o dataset e obter o nome
    dataset_name, columns, file_name = kag.kaggle.downloadDataset()

    dataset_name = "paivaDB"

    # Criar o banco de dados com o nome do dataset e inserir os dados
    dbPost.postDatabase.createDatabase(dataset_name)
    dbPost.postDatabase.insertData(dataset_name, columns, file_name)
    dbPost.postDatabase.createDimensionTables(dataset_name)  # Cria as tabelas de dimensão
    dbPost.postDatabase.insertDataIntoDimensions(dataset_name, file_name)
    # dbPost.postDatabase.createFactTables(dataset_name)
    # dbPost.postDatabase.populateFactTables(dataset_name)
    # dbPost.postDatabase.insertHostPerformanceFacts(dataset_name)
    # dbPost.postDatabase.insertFinancePerformanceFacts(dataset_name)




if __name__ == "__main__":
    main()
