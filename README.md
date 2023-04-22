## Telas de login

## Projeto

💻Este é um projeto de duas telas criadas em PySimpleGUI. O objetivo do projeto é fornecer uma interface gráfica simples para cadastro e login de usuários. Para que o programa pudesse ser criado, os seguintes requisitos foram necessários:💻

- PySimpleGUI instalado e importado
- GIMP para renderizar o tamanho das imagens
- Google como fonte para buscar artes

## Dificuldades

Uma das dificuldades encontradas foi renderizar cada imagem mais de uma vez para que ficasse no lugar correto. Também foi um desafio organizar a imagem ao lado das interações e corrigir todos os erros possíveis na tela de cadastro para remover possíveis erros que possam ocorrer.

Um dos desafios mais difíceis que tive que enfrentar foi encontrar uma maneira de fazer o programa ler um arquivo TXT e verificar se um determinado nome de usuário e senha estavam corretos. Para resolver esse problema, criei a função "achando_conta(usuario, senha)" que faz a leitura dos dados do arquivo e verifica se os dados do usuário e senha correspondem a algum registro no arquivo.

🔍 Para fazer isso, precisei de muita ajuda e muita reflexão, pois inicialmente não estava conseguindo fazer sozinho. Mas, com perseverança e ajuda, consegui entender a lógica e a implementação dessa função.

📂 Para ler o arquivo TXT, usei o comando "open("contas.txt", "r")". O "r" indica que o arquivo será aberto em modo leitura. Em seguida, percorri cada linha do arquivo com um laço "for" e separei os dados em uma lista usando o método "strip().split(',')".

👀 Para verificar se os dados correspondiam a uma conta registrada, usei um laço "for" para percorrer a lista e verifiquei se o nome de usuário e a senha correspondiam aos valores na lista usando a estrutura de decisão "if". Se os dados correspondessem a uma conta registrada, a função retornaria "True", caso contrário, retornaria "False".

    def achando_conta(usuario, senha):
        with open("contas.txt", "r") as arquivo:
            for c in arquivo:
                dados = c.strip().split(',')
                if dados[0] == usuario and dados[1] == senha:
                    return True
            return False 

## Curiosidades

Os registros são salvos em um arquivo de bloco de notas usando o comando "with open" dentro das funções. Embora essa não seja a maneira mais correta de salvar os dados, foi uma solução simples e prática para guardar as contas (nome e senha) e permitir que o programa as busque posteriormente.📝📝

As imagens usadas no projeto foram um astronauta e um arquivo com o símbolo do Python. As cores do projeto foram baseadas nessas imagens e foram usadas imagens nos botões para tornar a interface mais atraente.

O GIMP foi usado várias vezes para corrigir o tamanho das imagens, que eram 4 no total, 2 na tela de cadastro e 3 na tela de login, com o botão "enter" sendo usado em ambas as partes.

## Futuro

No futuro, pode haver uma atualização no projeto ou talvez seja alterado para uma tela de login de um jogo produzido pelo desenvolvedor (eu). 👀

## Como executar

Para rodar o projeto, basta ter todos os arquivos e as imagens dentro da mesma pasta, assim, na hora de executar, o programa rodará sem nenhum problema, se não rodar, algo está faltando.
Lembre-se, Não altere o nome das imagens, se você alterar, precisará alterar no programa também.
recomendo que deixe do jeito que está e pode testar e usar para suas ideias.
Todas as imagens ja estão renderizadas no tamanho ideal, precisa delas para rodar tudo direitinho.🚀🚀

## 🔗 Links 

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jos%C3%A9-davi-779356240) 🌐

[![instagram](https://img.shields.io/badge/instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/davi_dg_21?igshid=ZDdkNTZiNTM=) 📷

[![github](https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/J-Davi2) 💻

📧 E-mail: j.davi2077t@gmail.com
