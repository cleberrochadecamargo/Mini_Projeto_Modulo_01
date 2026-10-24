import modulo_vendas as mv
    # import modulo_vendas as mv = importa o módulo e cria o apelido mv.

if __name__ == "__main__":
    # 1. Gera o arquivo CSV com os dados de venda.
    mv.gerar_dataset_sintetico()
    # if __name__ == "__main__" = Verifica se o arquivo main.py está
    # sendo executado diretamente.
    # mv.gerar_dataset_sintetico() = chama a função que gera o CSV.

    # 2. Inspeciona os dados originais.
    mv.inspecionar_dados()
    # Chamada a função de inspeção na geração do arquivo.

    # 3. Limpa os dados e guarda os registros válidos.
    registros_limpos = mv.limpar_dados()
    # Recebe a lista de vendas válidas.

    # 4. Calcula a receita total e a faixa de preço de cada venda.
    registros_analisados = mv.calcular_metricas(registros_limpos)
    # Recebe essa mesma lista com os novos campos receita_total e faixa_preco.

    # 5. Calcula as receitas por categoria, por região e o total geral.
    receita_categoria, receita_regiao, receita_geral = (
        mv.resumir_vendas(registros_analisados)
    )

    # 6. Classifica os clientes conforme o gasto acumulado.
    segmentos = mv.segmentar_clientes(registros_analisados)
    # A variável segmentos guardará o resultado da classificação.

    # 7. Exporta o resumo das receitas para CSV.
    mv.exportar_metricas_csv(
        receita_categoria,
        receita_regiao,
        receita_geral
    )

    # 8. Exibe um exemplo para conferir os cálculos.
    print("\nExemplos de vendas analisadas")
    print(registros_analisados[0])
    # registros_analisados[0] = mostra o primeiro registro, para verificarmos
    # se os cálculos foram adicionados corretamente.

    # 9. Exporta as estatísticas e os segmentos para JSON.
    mv.exportar_estatisticas_json(
    receita_categoria,
    receita_regiao,
    receita_geral,
    segmentos
)