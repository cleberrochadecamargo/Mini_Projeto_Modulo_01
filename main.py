import modulo_vendas as mv

if __name__ == "__main__":
    mv.gerar_dataset_sintetico()

    # import modulo_vendas as mv = importa o módulo e cria o apelido mv.
    # if __name__ == "__main__" = Verifica se o arquivo main.py está
    # sendo executado diretamente.
    # mv.gerar_dataset_sintetico() = chama a função que gera o CSV.

    mv.inspecionar_dados()
    # chamada a função de inspeção na geração do arquivo.

    registros_limpos = mv.limpar_dados()
    # recebe a lista de vendas válidas.

    registros_analisados = mv.calcular_metricas(registros_limpos)
    # recebe essa mesma lista com os novos campos receita_total e faixa_preco.

    receita_categoria, receita_regiao, receita_geral = (
        mv.resumir_vendas(registros_analisados)
    )

    segmentos = mv.segmentar_clientes(registros_analisados)

    mv.exportar_metricas_csv(
        receita_categoria,
        receita_regiao,
        receita_geral
    )

    print("\nExemplos de vendas analisadas")
    print(registros_analisados[0])
    # registros_analisados[0] = mostra o primeiro registro, para verificarmos
    # se os cálculos foram adicionados corretamente.

    segmentos = mv.segmentar_clientes(registros_analisados)
    # A variável segmentos guardará o resultado da classificação.


