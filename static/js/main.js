// Funções para gerenciar produtos
async function carregarProdutos() {
    try {
        const response = await fetch('/api/produtos');
        const produtos = await response.json();
        atualizarTabelaProdutos(produtos);
    } catch (erro) {
        console.error('Erro ao carregar produtos:', erro);
    }
}

async function cadastrarProduto(evento) {
    evento.preventDefault();
    const formData = new FormData(evento.target);
    const produto = {
        nome: formData.get('nome'),
        preco: parseFloat(formData.get('preco')),
        quantidade: parseFloat(formData.get('quantidade')),
        unidade: formData.get('unidade')
    };

    try {
        const response = await fetch('/api/produtos', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(produto)
        });
        const resultado = await response.json();
        alert(resultado.mensagem);
        carregarProdutos();
    } catch (erro) {
        console.error('Erro ao cadastrar produto:', erro);
    }
}

// Função para registrar venda
async function registrarVenda(total) {
    try {
        const response = await fetch('/api/vendas/nova', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ total })
        });
        const resultado = await response.json();
        alert(resultado.mensagem);
    } catch (erro) {
        console.error('Erro ao registrar venda:', erro);
    }
} 