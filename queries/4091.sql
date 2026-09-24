SELECT
    itens.cod_item AS cod_item,
    estoque.qtde AS quantidade_estoque,
    itens_fornecedor.preco_venda2 AS preco_supermercado,
    itens.descricao AS descricao
FROM
    estoque
JOIN
    itens_fornecedor ON estoque.cod_item = itens_fornecedor.cod_item
                     AND estoque.cod_fornecedor = itens_fornecedor.cod_fornecedor
JOIN
    itens ON itens_fornecedor.cod_item = itens.cod_item
WHERE
    estoque.qtde > 0
    AND itens_fornecedor.tipo_item = 'E'
    AND estoque.cod_empresa = 9
ORDER BY
    itens_fornecedor.cod_item