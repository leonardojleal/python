def jogar_quiz():
    perguntas = [
        {
            "pergunta": "\033[34mQual é a capital do Brasil?\033[m",
            "opcoes": ["Rio de Janeiro", "Brasília", "São Paulo", "Belo Horizonte"],
            "resposta": 1
        },
        {
            "pergunta": "\033[34mQuem escreveu 'Dom Quixote'?\033[m",
            "opcoes": ["Miguel de Cervantes", "William Shakespeare", "Friedrich Nietzsche", "Charles Dickens"],
            "resposta": 0
        },
        {
            "pergunta": "\033[34mQuem pintou a 'Mona Lisa'?\033[m",
            "opcoes": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"],
            "resposta": 2
        },

        {
            "pergunta": "\033[34mEm que ano Ayrton Senna se consagrou campeão mundial da Fórmula 1 pela primeira vez ?\033[m",
            "opcoes": ['1993', '1998', '1834', '1999', '1988'],
            "resposta": 4

        },

        {
            "pergunta": "\033[34mNormalmente, quantos litros de sangue uma pessoa tem? Em média, quantos são retirados numa doação de sangue?\033[m",
            "opcoes": ['Tem entre 2 a 4 litros. São retirados 450 mililitros', 'Tem entre 4 a 6 litros. São retirados 450 mililitros', 'Tem 10 litros. São retirados 2 litros', 'Tem 7 litros. São retirados 1,5 litros', 'Tem 0,5 litros. São retirados 0,5 litros'],
            "resposta": 1
        },

        {
            "pergunta": "\033[34mDe quem é a famosa frase 'Penso, logo existo'?\033[m",
            "opcoes": ['Platão', 'Galileu Galilei', 'Descartes', 'Sócrates', 'Francis Bacon'],
            "resposta": 2
        },

        {
            "pergunta": "\033[34mDe onde é a invenção do chuveiro elétrico?\033[m",
            "opcoes": ['França', 'Inglaterra', 'Brasil', 'Austrália', 'Itália'],
            "resposta": 2
        },

        {
            "pergunta": '\033[34mQuais o menor e o maior país do mundo?\033[m',
            "opcoes": ['Vaticano e Rússia', 'Nauru e China', 'Mônaco e Canadá', 'Malta e Estados Unidos', 'São Marino e Índia'],
            "resposta": 0
        },

        {
            "pergunta": '\033[34mQual o nome do presidente do Brasil que ficou conhecido como Jango?\033[m',
            "opcoes": ['Jânio Quadros', 'Jacinto Anjos', 'Getúlio Vargas', 'João Figueiredo', 'João Goulart'],
            "resposta": 4
        },

        {
            "pergunta": '\033[34mQual o grupo em que todas as palavras foram escritas corretamente?\033[m',
            "opcoes": ['Asterístico, beneficiente, meteorologia, entertido', 'Asterisco, beneficente, meteorologia, entretido', 'Asterisco, beneficente, metereologia, entretido', 'Asterístico, beneficiente, metereologia, entretido', 'Asterisco, beneficiente, metereologia, entretido'],
            "resposta": 1
        },

        {
            "pergunta": '\033[34mQual o livro mais vendido no mundo a seguir à Bíblia?\033[m',
            "opcoes": ['O Senhor dos Anéis', 'Dom Quixote', 'O Pequeno Príncipe', 'Ela, a Feiticeira', 'Um Conto de Duas Cidades'],
            "resposta": 1
        },

        {
            "pergunta": '\033[34mQuantas casas decimais tem o número pi?\033[m',
            "opcoes": ['Duas', 'Centenas', 'Infinitas', 'Vinte', 'Milhares'],
            "resposta":     2
        },

        {
            "pergunta": '\033[34mAtualmente, quantos elementos químicos a tabela periódica possui?\033[m',
            "opcoes":['113', '109', '108', '118', '92'],
            "resposta": 3
        },

        {
            "pergunta": '\033[34mQuais os países que têm a maior e a menor expectativa de vida do mundo?\033[m',
            "opcoes": ['Japão e Serra Leoa', 'Austrália e Afeganistão', 'Itália e Chade', 'Brasil e Congo', 'Estados Unidos e Angola'],
            "resposta": 0
        },

        {
            "pergunta": '\033[34mQual o número mínimo de jogadores em cada time numa partida de futebol?\033[m',
            "opcoes": ['8', '10', '9', '5', '7'],
            "resposta": 4
        },

        {
            "pergunta": '\033[34mEm que ordem surgiram os modelos atômicos?\033[m',
            "opcoes": ['Thomson, Dalton, Rutherford, Rutherford-Bohr', ' Rutherford-Bohr, Rutherford, Thomson, Dalton', 'Dalton, Rutherford-Bohr, Thomson, Rutherford', 'Dalton, Thomson, Rutherford-Bohr, Rutherford', 'Dalton, Thomson, Rutherford, Rutherford-Bohr'],
            "resposta": 4
        },

        {
            "pergunta": '\033[34mQual das alternativas abaixo apenas contêm classes de palavras?\033[m',
            "opcoes": ['Vogais, semivogais e consoantes', 'Artigo, verbo transitivo e verbo intransitivo', 'Fonologia, Morfologia e Sintaxe', 'Hiatos, ditongos e tritongos', 'Substantivo, verbo e preposição'],
            "resposta": 4
        },


        {
            "pergunta": '\033[34mQual a velocidade da luz?\033[m',
            "opcoes": ['300 000 000 metros por segundo (m/s)', '150 000 000 metros por segundo (m/s)', '199 792 458 metros por segundo (m/s)', '299 792 458 metros por segundo (m/s)', '30 000 000 metros por segundo (m/s)'],
            "resposta": 3
        },

        {
            "pergunta": '\033[34mQuais os planetas do sistema solar?\033[m',
            "opcoes": ['Terra, Vênus, Saturno, Urano, Júpiter, Marte, Netuno, Mercúrio', 'Júpiter, Marte, Mercúrio, Netuno, Plutão, Saturno, Terra, Urano, Vênus', 'Vênus, Saturno, Urano, Júpiter, Marte, Netuno, Mercúrio', 'Júpiter, Marte, Mercúrio, Netuno, Plutão, Saturno, Sol, Terra, Urano, Vênus', 'Terra, Vênus, Saturno, Júpiter, Marte, Netuno, Mercúrio'],
            "resposta": 0
        },

        {
            "pergunta": '\033[34mQuem foi o primeiro homem a pisar na Lua? Em que ano aconteceu?\033[m',
            "opcoes": ['Yuri Gagarin, em 1961', 'Buzz Aldrin, em 1969', 'Charles Conrad, em 1969', 'Charles Duke, em 1971', 'Neil Armstrong, em 1969.'],
            "resposta": 3
        },

        {
            "pergunta": '\033[34mQual o nome do cientista que descobriu o processo de pasteurização e a vacina contra a raiva?\033[m',
            "opcoes": ['Marie Curie', 'Blaise Pascal', 'Louis Pasteur', 'Antoine Lavoisier', 'Charles Darwin'],
            "resposta": 2
        },

        {
            "pergunta": '\033[34mAs pessoas de qual tipo sanguíneo são consideradas doadores universais?\033[m',
            "opcoes": ['Tipo A', 'Tipo B', 'Tipo O', 'Tipo AB', 'Tipo ABO'],
            "resposta": 2
        },


        {
            "pergunta": '\033[34mComo se chamam os vasos que transportam sangue do coração para a periferia do corpo?\033[m',
            "opcoes": ['Veias', 'Átrios', 'Ventrículos', 'Artérias', 'Aurículos'],
            "resposta": 3
        },

        {
            "pergunta": '\033[34mEm que século o continente europeu foi devastado pela peste bubônica?\033[m',
            "opcoes": ['No século X', 'No século XI', 'No século XII', 'No século XIII', 'No século XIV'],
            "resposta": 4
        }
    ]

    pontuacao = 0

    print("Bem-vindo ao jogo de quiz!")
    print("Responda às perguntas e veja sua pontuação no final.\n") 

    for idx, pergunta in enumerate(perguntas, 1):
        print(f"Pergunta {idx}: {pergunta['pergunta']}")
        for i, opcao in enumerate(pergunta['opcoes']):
            print(f"{i + 1}. {opcao}")
        
        resposta = int(input("Escolha a opção correta (1, 2, 3, 4 ou 5): ")) - 1
       
        if resposta == pergunta['resposta']:
            print("Resposta correta!\n")
            pontuacao += 1
        else:
            print("Resposta incorreta.\n")

    print(f"Fim do quiz! Sua pontuação final é: {pontuacao}/{len(perguntas)}")

jogar_quiz()