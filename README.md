# Exercícios de Programação Orientada a Objetos - Python

Este repositório contém uma série de exercícios práticos de **Programação Orientada a Objetos (POO)** em Python, desenvolvidos no contexto de uma **Escola de Ensino Superior**.

## Objetivo

Proporcionar aos estudantes uma experiência prática e progressiva dos conceitos fundamentais de POO através de exercícios que simulam situações reais de uma instituição de ensino.

## Conceitos Abordados

### Fundamentos de POO

#### Classes e Objetos
- **Classe**: Um modelo ou template que define a estrutura e comportamento de objetos. É como um "molde" que especifica quais atributos (dados) e métodos (funções) os objetos terão.
- **Objeto**: Uma instância específica de uma classe. É a materialização concreta do modelo definido pela classe.
- **Instanciação**: O processo de criar um objeto a partir de uma classe usando o operador de chamada `()`.

#### Construtores
- **Método `__init__()`**: Método especial chamado automaticamente quando um objeto é criado. Responsável por inicializar os atributos do objeto.
- **Parâmetros do Construtor**: Valores passados durante a criação do objeto para configurar seu estado inicial.
- **Self**: Referência ao próprio objeto, usado para acessar atributos e métodos da instância.

#### Atributos e Métodos
- **Atributos de Instância**: Variáveis que pertencem a cada objeto específico, definidas com `self.atributo`.
- **Atributos de Classe**: Variáveis compartilhadas por todas as instâncias da classe.
- **Métodos de Instância**: Funções que operam sobre dados específicos de cada objeto.
- **Métodos de Classe**: Funções que operam sobre a classe como um todo, marcadas com `@classmethod`.
- **Métodos Estáticos**: Funções relacionadas à classe mas que não acessam dados da instância ou classe, marcadas com `@staticmethod`.

### Encapsulamento

#### Princípio do Encapsulamento
O encapsulamento é um dos pilares fundamentais da POO que consiste em:
- **Ocultar detalhes internos**: Proteger dados e implementação interna da classe
- **Controlar acesso**: Definir como os dados podem ser acessados e modificados
- **Manter integridade**: Garantir que o objeto sempre esteja em um estado válido

#### Níveis de Visibilidade em Python
- **Público**: Atributos e métodos acessíveis de qualquer lugar (`atributo`)
- **Protegido**: Convenção para indicar uso interno, prefixo `_` (`_atributo`)
- **Privado**: Dificultam acesso externo, prefixo `__` (`__atributo`)

#### Properties e Getters/Setters
- **@property**: Decorator que permite acessar métodos como se fossem atributos
- **Getter**: Método para obter o valor de um atributo privado
- **Setter**: Método para definir o valor de um atributo com validação
- **Validação de Dados**: Verificações realizadas antes de alterar o estado do objeto

### Herança

#### Conceitos Fundamentais
- **Classe Base (Pai/Superclasse)**: Classe que define características comuns
- **Classe Derivada (Filha/Subclasse)**: Classe que herda e especializa a classe base
- **Relação "é um"**: A herança representa uma relação hierárquica onde a subclasse "é um" tipo da superclasse

#### Mecanismos de Herança
- **Herança Simples**: Uma classe herda de apenas uma classe pai
- **Herança Múltipla**: Uma classe herda de múltiplas classes pai (suportada em Python)
- **Método super()**: Função que permite chamar métodos da classe pai
- **Sobrescrita de Métodos**: Redefinição de métodos herdados para comportamento específico
- **Extensão de Funcionalidade**: Adicionar novos métodos e atributos às classes filhas

### Polimorfismo

#### Definição e Tipos
- **Polimorfismo**: Capacidade de objetos de diferentes classes responderem à mesma interface de forma específica
- **Polimorfismo de Sobrescrita**: Mesmo método implementado diferentemente em classes relacionadas por herança
- **Polimorfismo de Interface**: Objetos não relacionados que implementam os mesmos métodos

#### Benefícios do Polimorfismo
- **Flexibilidade**: Código que funciona com diferentes tipos de objetos
- **Extensibilidade**: Facilita adição de novos tipos sem modificar código existente
- **Manutenibilidade**: Reduz acoplamento entre componentes do sistema

### Relacionamentos entre Objetos

#### Composição
- **Definição**: Relacionamento "tem um" onde um objeto contém outros objetos como partes integrantes
- **Ciclo de Vida**: Os objetos componentes dependem do objeto principal
- **Exemplo**: Um Carro "tem um" Motor - se o carro é destruído, o motor também é

#### Agregação
- **Definição**: Relacionamento "usa um" onde objetos existem independentemente mas se referenciam
- **Ciclo de Vida**: Os objetos podem existir separadamente
- **Exemplo**: Um Professor "leciona para" Alunos - professor e alunos existem independentemente

#### Relacionamentos N:N (Muitos para Muitos)
- **Definição**: Múltiplos objetos de um tipo se relacionam com múltiplos objetos de outro tipo
- **Implementação**: Geralmente usando listas ou conjuntos para armazenar referências
- **Exemplo**: Alunos podem estar matriculados em várias Disciplinas, e cada Disciplina pode ter vários Alunos

### Recursos Avançados

#### Métodos de Classe (@classmethod)
- **Propósito**: Métodos que operam sobre a classe, não sobre instâncias específicas
- **Primeiro Parâmetro**: `cls` (referência à classe)
- **Uso Comum**: Factory methods (métodos fábrica) para criar objetos de formas específicas
- **Acesso**: Podem ser chamados tanto pela classe quanto por instâncias

#### Métodos Estáticos (@staticmethod)
- **Propósito**: Funções relacionadas à classe mas que não precisam acessar dados da classe ou instância
- **Parâmetros**: Não recebem `self` nem `cls` automaticamente
- **Uso Comum**: Funções utilitárias relacionadas ao domínio da classe
- **Acesso**: Podem ser chamados pela classe ou instâncias, mas funcionam como funções normais

## Lista de Exercícios

| Exercício | Conceito Principal | Descrição | Link |
|-----------|-------------------|-----------|------|
| 01 | **Modelagem Básica** | Criação de classes simples (Aluno, Disciplina) | [Exercício 01](exercicio_01.md) |
| 02 | **Métodos e Comportamento** | Adição de métodos para manipular estado | [Exercício 02](exercicio_02.md) |
| 03 | **Encapsulamento** | Atributos privados e properties | [Exercício 03](exercicio_03.md) |
| 04 | **Herança Simples** | Classes base e derivadas | [Exercício 04](exercicio_04.md) |
| 05 | **Herança com super()** | Uso correto de super() em construtores | [Exercício 05](exercicio_05.md) |
| 06 | **Composição** | Relacionamento "tem um" entre objetos | [Exercício 06](exercicio_06.md) |
| 07 | **Agregação N:N** | Relacionamentos muitos-para-muitos | [Exercício 07](exercicio_07.md) |
| 08 | **Métodos de Classe** | Factory methods com @classmethod | [Exercício 08](exercicio_08.md) |
| 09 | **Polimorfismo** | Diferentes implementações do mesmo método | [Exercício 09](exercicio_09.md) |
| 10 | **Jogo dos 7 Erros** | Identificação e correção de erros comuns | [Exercício 10](exercicio_10.md) |

## Contexto dos Exercícios

Todos os exercícios são baseados em entidades e situações de uma **escola de ensino superior**:

- **Aluno**: Matrícula, notas, disciplinas
- **Professor**: Salário, departamento, disciplinas
- **Funcionário**: Cargo, salário, dados pessoais
- **Disciplina**: Código, carga horária, alunos matriculados
- **Curso**: Disciplinas, carga horária total
- **Departamento**: Professores, área de atuação
- **Secretaria**: Gerenciamento de matrículas

## Como Usar

### Para Estudantes

1. **Fork este repositório**: Clique em "Fork" no GitHub para criar sua cópia
2. **Clone seu fork**: `git clone https://github.com/SEU_USUARIO/EngSoftPraticaPOO.git`
3. **Leia o exercício**: Cada arquivo `.md` contém a descrição detalhada
4. **Implemente sua solução**: Crie o arquivo Python solicitado
5. **Teste localmente**: Execute e verifique se atende aos requisitos
6. **Commit e push**: Envie suas alterações para seu fork
7. **Abra um Pull Request**: Submeta sua solução para correção automática

### Executando Testes Localmente

Antes de submeter sua solução, você pode executar os testes localmente para verificar se sua implementação está correta:

#### Pré-requisitos
```bash
# Instale as dependências
pip install -r requirements.txt
```

#### Executando um teste específico
```bash
# Para testar apenas o exercício 1
python -m pytest tests/test_exercicio01.py -v

# Para testar apenas o exercício 2
python -m pytest tests/test_exercicio02.py -v
```

#### Executando todos os testes
```bash
# Executa todos os testes do projeto
python -m pytest tests/ -v
```

#### Interpretando a saída dos testes
- **PASSED**: Teste passou - sua implementação está correta
- **FAILED**: Teste falhou - verifique a mensagem de erro
- **ERROR**: Erro de importação - verifique o nome do arquivo

#### Exemplo de saída de teste bem-sucedido
```
tests/test_exercicio01.py::test_aluno_creation PASSED
tests/test_exercicio01.py::test_disciplina_creation PASSED
tests/test_exercicio01.py::test_aluno_attributes PASSED
```

#### Exemplo de saída com erro
```
tests/test_exercicio01.py::test_aluno_creation FAILED
E   AttributeError: 'Aluno' object has no attribute 'nome'
```

### Correção Automática

Este repositório possui **correção automática via GitHub Actions**!

- **Ao abrir um Pull Request**, os testes são executados automaticamente
- **Cada exercício é testado** individualmente
- **Resultado aparece como comentário** no seu PR
- **Feedback imediato** sobre acertos e erros

### Nomenclatura dos Arquivos

Para que a correção automática funcione, nomeie seus arquivos corretamente:

- `respExercicio01.py` - Exercício 1
- `respExercicio02.py` - Exercício 2
- `respExercicio03.py` - Exercício 3
- ...
- `Resposta_10.py` - Exercício 10 (Jogo dos 7 Erros)

### Fluxo de Trabalho

```bash
# 1. Fork e clone
git clone https://github.com/SEU_USUARIO/EngSoftPraticaPOO.git
cd EngSoftPraticaPOO

# 2. Crie uma branch para seu exercício
git checkout -b exercicio-01

# 3. Implemente sua solução
# Crie o arquivo respExercicio01.py

# 4. Commit e push
git add respExercicio01.py
git commit -m "Implementa exercício 01 - Modelagem Básica"
git push origin exercicio-01

# 5. Abra um Pull Request no GitHub
# A correção automática será executada!
```

## Estrutura do Repositório

```
EngSoftPraticaPOO/
├── README.md                 # Este arquivo
├── .gitignore               # Arquivos ignorados pelo Git
├── requirements.txt         # Dependências Python
├── .github/
│   └── workflows/
│       └── test-exercises.yml  # GitHub Actions
├── tests/
│   ├── test_exercicio01.py   # Testes do exercício 1
│   ├── test_exercicio02.py   # Testes do exercício 2
│   └── ...                    # Demais testes
├── exercicio_01.md          # Exercício 1: Modelagem Básica
├── exercicio_02.md          # Exercício 2: Métodos
├── exercicio_03.md          # Exercício 3: Encapsulamento
├── exercicio_04.md          # Exercício 4: Herança
├── exercicio_05.md          # Exercício 5: super()
├── exercicio_06.md          # Exercício 6: Composição
├── exercicio_07.md          # Exercício 7: Agregação
├── exercicio_08.md          # Exercício 8: @classmethod
├── exercicio_09.md          # Exercício 9: Polimorfismo
├── exercicio_10.md          # Exercício 10: Jogo dos 7 Erros
└── Arquivos de resposta     # (Incluídos no .gitignore)
```

## Progressão Recomendada

Os exercícios foram organizados em ordem crescente de complexidade:

1. **Básico** (Ex. 1-3): Classes, objetos, encapsulamento
2. **Intermediário** (Ex. 4-6): Herança, composição
3. **Avançado** (Ex. 7-9): Relacionamentos complexos, polimorfismo
4. **Desafio** (Ex. 10): Identificação e correção de erros

## Testes Automáticos

Cada exercício possui testes automatizados que verificam:

- **Existência das classes** solicitadas
- **Implementação dos métodos** obrigatórios
- **Funcionamento correto** dos conceitos de POO
- **Relacionamentos** entre objetos
- **Herança e polimorfismo** adequados
- **Encapsulamento** correto

### Interpretando os Resultados

- **Vermelho (Failed)**: Exercício com erros - verifique os logs
- **Verde (Passed)**: Exercício aprovado - parabéns!
- **Amarelo (Pending)**: Testes em execução - aguarde

## Dicas de Estudo

- **Pratique gradualmente**: Não pule exercícios
- **Entenda antes de implementar**: Leia bem os requisitos
- **Use a correção automática**: Abra PRs para feedback imediato
- **Analise os logs de teste**: Eles mostram exatamente o que está faltando
- **Refatore quando necessário**: Melhore seu código após funcionar
- **Use as convenções Python**: PEP 8 para estilo de código

## Contribuições

Este material foi desenvolvido para fins educacionais. Sugestões de melhorias são bem-vindas!

## Suporte

Para dúvidas sobre os exercícios:

1. **Consulte os logs dos testes** no GitHub Actions
2. **Analise as mensagens de erro** nos Pull Requests
3. **Revise a documentação oficial do Python**
4. **Estude os conceitos teóricos de POO**
5. **Compare com os exemplos** nos arquivos `.md`

### Debugando Problemas Comuns

- **ImportError**: Verifique o nome do arquivo
- **AttributeError**: Classe ou método não implementado
- **AssertionError**: Valor retornado diferente do esperado
- **NameError**: Variável ou classe não definida

---

**Bons estudos!**