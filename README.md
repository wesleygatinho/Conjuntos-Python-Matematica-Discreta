# Programa de Operações com Conjuntos

## Autores

**ANA PATRICIA GARROS VIEGAS**  
Matrícula: 2022003512
E-mail: garros.ana@discente.ufma.br  

---

**WESLEY DOS SANTOS GATINHO**  
Matrícula: 20250071367
E-mail: santosgatinhowesley@gmail.com  

---
## 1. Descrição do Problema e Objetivo


Este programa foi desenvolvido com o objetivo de aplicar, na prática, os conceitos de **Teoria dos Conjuntos** estudados em sala de aula.

O sistema permite que o usuário insira um conjunto numérico (A) respeitando regras definidas, enquanto um segundo conjunto (B) é gerado automaticamente. A partir desses dois conjuntos, o programa realiza e exibe diversas operações clássicas da teoria dos conjuntos.

O objetivo principal é:

- Trabalhar operações como união, interseção e diferença.
- Validar entradas conforme regras matemáticas.
- Demonstrar a aplicação computacional dos conceitos de conjuntos.
- Desenvolver boas práticas de programação em Python.

---

## 2. Como Executar o Código

Para executar o programa, é necessário possuir o Python instalado no computador, sendo recomendada a versão 3.8 ou superior. O desenvolvimento do sistema foi realizado utilizando apenas bibliotecas padrão da própria linguagem, não sendo necessário instalar dependências externas adicionais.

Para verificar se o Python está instalado e qual versão está disponível, o usuário deve abrir o terminal (em sistemas Linux ou Mac) ou o Prompt de Comando / PowerShell (em sistemas Windows) e digitar o comando de verificação de versão do Python. Caso a versão exibida seja igual ou superior à recomendada, o programa poderá ser executado normalmente. Se o Python não estiver instalado ou estiver em versão inferior, será necessário realizar a instalação ou atualização por meio do site oficial da linguagem.

Após garantir que o ambiente está configurado corretamente, o próximo passo consiste em salvar o arquivo do programa em uma pasta do computador. Em seguida, deve-se abrir o terminal ou prompt de comando dentro dessa mesma pasta onde o arquivo foi armazenado.

Com o diretório correto aberto, basta executar o comando de execução do Python seguido do nome do arquivo do programa. Após esse procedimento, o sistema será iniciado automaticamente, solicitando ao usuário a inserção dos elementos do conjunto A e conduzindo o fluxo normal de funcionamento até a exibição do relatório final das operações realizadas.


## 3. Funcionamento do Programa

O fluxo de execução ocorre da seguinte forma:

1. O usuário insere os elementos do conjunto A.

2. O programa valida:

   - Intervalo permitido (1 a 20).
   - Quantidade de valores digitados (4 a 8).
   - Remoção de duplicatas.

3. O conjunto B é gerado automaticamente.

4. As operações de conjuntos são calculadas.

5. Um relatório completo é exibido.

6. Ao final, o usuário pode escolher executar novamente ou encerrar.

---

## 4. Principais Funções do Programa

### `universo()`

Retorna o conjunto universo contendo números de 1 a 20.

---

### `tokenizar_entrada(entrada)`

Separa a entrada do usuário em tokens, aceitando espaços e vírgulas como separadores.

---

### `parse_conjunto_numeros(tokens)`

Converte os tokens em números inteiros válidos e identifica possíveis entradas inválidas.

---

### `ler_conjunto_usuario(nome)`

Responsável por toda a interação com o usuário:

- Solicita os dados.
- Valida quantidade de valores.
- Remove duplicatas.
- Garante que os elementos pertencem ao universo.

---

### `gerar_conjunto_aleatorio()`

Cria automaticamente o conjunto B com 4 a 8 elementos aleatórios do universo.

---

### `relatorio_operacoes(A, B)`

Calcula e exibe todas as operações de conjuntos:

- União  
- Interseção  
- Diferença  
- Diferença Simétrica  
- Complemento  
- Cardinalidade  

---

### `menu_repeticao()`

Permite ao usuário escolher entre executar novamente ou encerrar o programa.

---

### `main()`

Controla o fluxo principal de execução através de um loop.

---

## 5. Organização do Código

O código foi estruturado de forma modular, separando responsabilidades em funções específicas:

- Entrada e validação de dados  
- Processamento matemático  
- Formatação de saída  
- Controle de execução  

Essa divisão evita repetição de código e facilita manutenção e leitura.

---

## 6. Relação com a Teoria dos Conjuntos

O programa aplica diretamente os conceitos estudados em sala:

### União (A ∪ B)

Reúne todos os elementos de A e B sem repetição.

---

### Interseção (A ∩ B)

Mostra apenas os elementos comuns entre os conjuntos.

---

### Diferença (A − B e B − A)

Exibe elementos exclusivos de cada conjunto.

---

### Diferença Simétrica (A Δ B)

Elementos que pertencem a apenas um dos conjuntos.

---

### Complemento

Elementos do universo que não pertencem ao conjunto analisado.

---

### Cardinalidade

Quantidade de elementos de cada conjunto e de cada operação realizada.

---

## 7. Considerações Finais

Este projeto demonstra como conceitos matemáticos abstratos podem ser implementados computacionalmente.

Além da aplicação da teoria dos conjuntos, o programa também reforça:

- Validação de entrada de dados  
- Estruturação de código  
- Uso de funções  
- Interação com o usuário via terminal  
