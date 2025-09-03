# Como criar uma nova place pelo mobile
**⚠ Aviso!** Infelizmente, através desse metodo não é possível criar um novo jogo. É possível somente adicionar uma place vazia ao seu jogo já existente.
✅ Entretanto, você pode transformar sua place principal em um hub de jogos, onde você teleporta o jogador para as outras places com a interface.

# Tutorial
O Roblox possui uma API chamada Open Cloud que permite que o usuário interaja com algumas funções do Studio através de requisições. Nós vamos usá-la para criar a nova place.

## 1. Chave 🔑
Crie a chave

1. Vá para a página do criador, na página de criar chaves API (https://create.roblox.com/dashboard/credentials)
2. Clique em "Criar chave API"
3. <sub>Obrigatório</sub> Adicione um nome a sua chave
4. <sub>Opcional</sub> Adicione uma descrição a sua chave
5. Nas permissões de acesso, pesquise "universe" e selecione a opção "universe-places"
6. Clique em "Salvar e gerar chave"
7. Clique em "Copiar a chave para área de transferência"
8. <sub>Opcional</sub> ⚠ Anote a chave em algum lugar, você precisará dela

## 2. Cookie 🍪
É necessário usar seu cookie de segurança para utilizar a API. O cookie é importante, mas você não vai compartilhar ele, você vai usar ele na API oficial do Roblox. O script que você vai usar está aqui (você pode lê-lo) e não disponibilizei nenhum executável para não ter risco de compilar um código diferente.

1. Baixe o Firefox pela Play Store (https://play.google.com/store/apps/details?id=org.mozilla.firefox&hl=pt_BR)
2. Após as configurações iniciais, clique nos três pontos no canto da tela
3. Clique em "Extensões"
4. Desça a lista até o final
5. Clique em "Encontrar mais extensões"
6. Clique em "Pesquisar extensões" no topo da tela
7. Digite "Cookie"
8. Clique em "Cookie-Editor"
9. Clique em "Adicionar ao Firefox"
10. Clique em "Adicionar"
11. Clique em "Ok"
12. Vá para o site do Roblox (https://www.roblox.com)
13. Clique em "Continuar no navegador"
14. Faça login e entre na sua conta
15. Clique nos três pontos no canto da tela
16. Clique em "Extensões"
17. Selecione o "Cookie-Editor"
18. Expanda ".ROBLOSECURITY"
19. Copie o cookie
20. <sub>Opcional</sub> ⚠ Anote o cookie em algum lugar, você precisará dele

## 3. API 🤝
1. Abra a página do criador novamente (https://create.roblox.com/)
2. Abra o jogo no qual você quer adicionar a place
3. No URL https://create.roblox.com/dashboard/creations/experiences/ID_DO_UNIVERSO/overview copie o id do universo
4. <sub>Opcional</sub> ⚠ Anote o id do universo em algum lugar, você precisará dele
5. Faça download do arquivo criar_place.py
6. Abra o arquivo no seu editor de texto preferido
7. Na linha "universe_id = 0", substitua o 0 pelo id do universo
8. Na linha "cookie = """, coloque o seu cookie .ROBLOSECURITY entre as aspas
9. Na linha "api_key = """, coloque a sua chave API entre as aspas
10. Salve as alterações
11. Use sua IDE Python de preferência para executar o código, mas aqui vou ensinar com o Termux
12. Instale o Termux (https://play.google.com/store/apps/details?id=com.termux&hl=pt_BR)
13. Abra o Termux
14. Digite "pkg install python" para instalar o Python
15. Digite "python (caminho para o arquivo criar_place.py modificado)"

# Finalização
Se tudo tiver dado certo, uma nova place chamada "(SEU NOME USUÁRIO)'s Place: (ID da Place)" deve ser criada nas places do seu jogo
