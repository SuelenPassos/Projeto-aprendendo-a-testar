Funcionalidade: Projeto aprendendo a testar

EU COMO detentor de conhecimentos de automação de testes.
DESEJO acesso a uma página para a automação de testes.
PARA QUE seja possível demonstrar e aprimorar meus conhecimentos com automação de testes.

Contexto: Logar na pagina aprendendo a testar

Cenário 1: Verificar a obrigatoriedade do campo usuario
    Dado que o usuario esteja na pagina aprendendo a testar
    Quando o usuario clicar no botão enviar
    E não tiver preenchido nenhum campo 
    Então a mensagem Preencha este campo para o campo usuario é exibida
    E o sistema não permite que os dados sejam enviados

Cenário 2: Verificar a obrigatoriedade do campo senha
    Dado que o usuário esteja na pagina aprendendo a testar
    Quando o usuario clicar no botão enviar
    E tiver preenchido o campo usuario  
    Então a mensagem Preencha este campo para o campo senha é exibida
    E o sistema não permite que os dados sejam enviados

Cenário 3: Verificar a obrigatoriedade do campo nome
    Dado que o usuário esteja na pagina aprendendo a testar
    Quando o usuario clicar no botão enviar
    E tiver preenchido o campo usuario  
    E tiver preenchido o campo senha  
    Então a mensagem Existem campos em branco é exibida
    E o sistema não permite que os dados sejam enviados

Cenário 4: Verificar inclusão dos dados na tabela usuarios
    Dado que o usuário esteja na pagina aprendendo a testar
    Quando o usuario clicar no botão enviar
    E tiver preenchido o campo usuario  
    E tiver preenchido o campo senha
    E tiver preenchido o campo nome  
    Então a os dados incluidos são inceridos na tabela de usuários
    E um ID é gerado aleatoriamente
    E a opção apagar é exibida na coluna ações

Cenário 5: Verificar ordenação da tabela usuarios
    Dado que o usuário tenha incluido corretamente mais de um registro
    Quando os registros forem incluidos na tabela
    Então a os registros serão exibidos em ordem alfabetica pelo campo nome

Cenário 6: Verificar exclusão de um registro
    Dado que o usuário tenha incluido corretamente mais de um registro
    Quando o usuário clicar em apagar
    E atualizar a pagina
    Então o registro é removido da tabela de usuario

Cenário 7: Verificar atualização de dados
    Dado que o usuário tenha sido incluido corretamente na tabela de usuarios
    Quando o usuario clicar no botão enviar
    E tiver preenchido o campo usuario com um valor existente na tabela de usuarios 
    E tiver preenchido o campo senha
    E tiver preenchido o campo nome 
    Então o sistema irá alterar os campos senha e nome na tabela de usuarios

Cenário 8: Verificar atualização da pagina
    Dado que o usuário tenha incluido corretamente mais de um registro
    Quando o usuário clicar no botão clique aqui
    Então o sistema deve atualizar a página
    E nenhum item é alterado










