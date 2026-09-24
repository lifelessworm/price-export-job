WITH C_VENDAS AS
 (SELECT estoque.COD_EMPRESA,
         itens.cod_item AS cod_item,
         estoque.qtde AS quantidade_estoque,
         itens_fornecedor.preco_venda2 AS preco_supermercado,
         itens.descricao AS descricao,
         ic.promocao_especifica,
         ic.custo_contabil,
         itens_fornecedor.preco_venda2 *
         (1 - (ic.promocao_especifica / 100)) preco_promocional

    FROM estoque
    JOIN itens_fornecedor
      ON estoque.cod_item = itens_fornecedor.cod_item
     AND estoque.cod_fornecedor = itens_fornecedor.cod_fornecedor
    JOIN itens
      ON itens_fornecedor.cod_item = itens.cod_item
    JOIN ITENS_CUSTOS IC
      ON IC.COD_ITEM = ESTOQUE.COD_ITEM
     AND IC.COD_EMPRESA = ESTOQUE.COD_EMPRESA
     AND IC.COD_FORNECEDOR = ESTOQUE.COD_FORNECEDOR

   WHERE estoque.qtde > 0
     AND itens_fornecedor.tipo_item = 'E'
     AND estoque.cod_empresa IN (2, 9)
     and ic.promocao_especifica > 0
     and ic.promocao_especifica is not null
     AND NVL(itens_fornecedor.Promocao, 'N') = 'S'

   ORDER BY itens_fornecedor.cod_item)

SELECT COD_ITEM, QUANTIDADE_ESTOQUE, preco_promocional, descricao
  FROM C_VENDAS
 ORDER BY COD_EMPRESA