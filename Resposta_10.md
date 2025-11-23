# Relatório Detalhado dos 7 Erros - Exercício 10

## Resumo
Este relatório descreve os **7 erros** encontrados no exercício 10, suas soluções e os conceitos de Programação Orientada a Objetos (POO) violados em cada caso.

---

## Erro 1: Nome da classe em minúsculas

### Descrição do Problema
```python
class pessoa:  # ❌ Erro 1 - nome em minúsculas
```
A classe foi nomeada como `pessoa` em vez de `Pessoa`. Em Python, a convenção **PascalCase** (primeira letra maiúscula) é usada para nomes de classes, enquanto `snake_case` é usado para variáveis e funções.

### Solução
```python
class Pessoa:  # ✅ Correto - PascalCase
```

### Conceito POO Violado
- **Convenção de Nomenclatura**: violação do **PEP 8** (guia de estilo Python)
- **Legibilidade**: torna o código menos legível e profissional

---

## Erro 2: Atributo `nome` não é atribuído com `self`

### Descrição do Problema
```python
def __init__(self, nome, idade):
    nome = nome  # ❌ Erro 2 - apenas atribui à variável local, não ao objeto
    self.idade = idade
```
A linha `nome = nome` apenas atribui o parâmetro local `nome` a si mesmo, não cria um atributo de instância. O atributo `self.nome` nunca é criado, portanto, `self.nome` não existirá no objeto.

### Solução
```python
def __init__(self, nome, idade):
    self.nome = nome  # ✅ Correto - atribui ao atributo de instância
    self.idade = idade
```

### Conceito POO Violado
- **Encapsulamento**: o atributo não é adequadamente encapsulado na instância
- **Inicialização de Objeto**: o construtor não inicializa corretamente o estado do objeto

---

## Erro 3: Inicialização inadequada de atributo privado

### Descrição do Problema
```python
def __init__(self, nome, idade):
    nome = nome
    self.idade = idade
    self.__cpf = None  # ❌ Erro 3 - inicializa com None sem parâmetro
```
O atributo `__cpf` (privado) é inicializado com `None`, mas não há parâmetro no construtor para receber o CPF. Quando o objeto é criado, o CPF será sempre `None`, violando a integridade dos dados.

### Solução
```python
def __init__(self, nome, idade, cpf):
    self.nome = nome
    self.idade = idade
    self.__cpf = cpf  # ✅ Correto - recebe como parâmetro e atribui
```

### Conceito POO Violado
- **Encapsulamento**: atributo privado não está sendo inicializado corretamente
- **Completude de Estado**: o objeto não contém todos os dados necessários para representar uma pessoa
- **Contrato de Interface**: o construtor não oferece forma de definir o CPF

---

## Erro 4: Método `apresentar()` sem parâmetro `self`

### Descrição do Problema
```python
def apresentar():  # ❌ Erro 4 - falta o parâmetro self
    return f"Olá, sou {self.nome}"
```
O método não inclui o parâmetro `self`, que é obrigatório em métodos de instância. Isso causará um **NameError** porque `self` não está definido, e ao chamar `pessoa.apresentar()`, Python não terá como passar a instância como argumento implícito.

### Solução
```python
def apresentar(self):  # ✅ Correto - inclui o parâmetro self
    return f"Olá, sou {self.nome}"
```

### Conceito POO Violado
- **Métodos de Instância**: violação da sintaxe obrigatória de métodos em Python
- **Acesso a Atributos**: sem `self`, não há acesso ao estado do objeto

---

## Erro 5: Classe filha não usa `super().__init__()`

### Descrição do Problema
```python
class Estudante(pessoa):
    def __init__(self, nome, idade, curso):
        self.nome = nome  # ❌ Erro 5 - duplicação de código, não usa super()
        self.idade = idade
        self.curso = curso
        self.notas = []
```
A classe `Estudante` herda de `pessoa`, mas seu construtor não chama `super().__init__()`. Isso resulta em:
1. **Duplicação de código** (repetindo `self.nome` e `self.idade`)
2. **Falta de inicialização** de atributos privados da classe pai (como `__cpf`)
3. **Violação do princípio DRY** (Don't Repeat Yourself)

### Solução
```python
class Estudante(Pessoa):
    def __init__(self, nome, idade, cpf, curso):
        super().__init__(nome, idade, cpf)  # ✅ Inicializa a classe pai
        self.curso = curso
        self.notas = []
```

### Conceito POO Violado
- **Herança**: não reutiliza o construtor da classe pai
- **Responsabilidade Única**: a classe filha assume responsabilidade de inicializar atributos da classe pai
- **DRY (Don't Repeat Yourself)**: código duplicado viola o princípio de não repetição

---

## Erro 6: Divisão por zero em `calcular_media()`

### Descrição do Problema
```python
def calcular_media(self):
    return sum(self.notas) / len(self.notas)  # ❌ Erro 6 - sem verificação de lista vazia
```
Se a lista `self.notas` estiver vazia (nenhuma nota adicionada), ocorrerá **ZeroDivisionError**. Não há tratamento para esse caso extremo, tornando o método frágil.

### Solução
```python
def calcular_media(self):
    if len(self.notas) == 0:
        return 0  # ou lançar uma exceção informativa
    return sum(self.notas) / len(self.notas)  # ✅ Protegido
```

### Conceito POO Violado
- **Robustez**: o método não trata casos extremos (edge cases)
- **Encapsulamento**: não valida o estado interno antes de operar
- **Defesa Defensiva**: falta proteção contra estados inválidos

---

## Erro 7: Chamada de método em objeto com estado incompleto

### Descrição do Problema
```python
estudante = Estudante("João", 20, "Engenharia")
professor = Professor("Dr. Silva", 45, "Computação", 8000)

print(estudante.apresentar())  # ❌ Erro 7a - Estudante não sobrescreve apresentar()
print(professor.apresentar())
print(f"Média do estudante: {estudante.calcular_media()}")  # ❌ Erro 7b - lista vazia, ZeroDivisionError
```

**Dois sub-problemas:**

### 7a) `Estudante` não sobrescreve `apresentar()`
- A classe `Estudante` herda `apresentar()` de `pessoa`, mas o método tenta acessar `self.nome`
- Como `self.nome` não foi inicializado (Erro 2), será um **AttributeError**: `'pessoa' object has no attribute 'name'`

### 7b) Média calculada de lista vazia
- Nenhuma nota foi adicionada a `estudante.notas` antes de chamar `calcular_media()`
- Chamar `calcular_media()` com lista vazia gera **ZeroDivisionError** (Erro 6)

### Solução
```python
estudante = Estudante("João", 20, "123.456.789-00", "Engenharia")
professor = Professor("Dr. Silva", 45, "987.654.321-00", "Computação", 8000)

# Adicionar notas antes de calcular
estudante.adicionar_nota(8.5)
estudante.adicionar_nota(9.0)

print(estudante.apresentar())
print(professor.apresentar())
print(f"Média do estudante: {estudante.calcular_media()}")  # ✅ Agora funciona
```

### Conceito POO Violado
- **Polimorfismo**: `Estudante` não oferece sua própria implementação de `apresentar()` customizada
- **Estado do Objeto**: o objeto é criado em estado incompleto/inválido
- **Lógica de Negócio**: tentativa de calcular algo com dados incompletos (lista vazia)
- **Contrato de Dados**: instâncias não respeitam os parâmetros obrigatórios

---

## Resumo Comparativo

| Erro | Tipo | Severidade | Causa Raiz | Conceito POO |
|------|------|-----------|-----------|------------|
| 1 | Convenção | Baixa | Nome em minúsculas | PEP 8 / Legibilidade |
| 2 | Inicialização | **Alta** | Falta `self.` | Encapsulamento |
| 3 | Inicialização | Média | Parâmetro faltando | Encapsulamento |
| 4 | Sintaxe | **Alta** | Falta `self` em método | Métodos de Instância |
| 5 | Herança | **Alta** | Não usa `super()` | Herança/DRY |
| 6 | Lógica | Média | Sem validação | Robustez |
| 7 | Integração | **Alta** | Consequência de 2,3,5,6 | Polimorfismo/Estado |

---

## Checklist de Correção

✅ **Erro 1** - Renomear `pessoa` → `Pessoa`  
✅ **Erro 2** - Mudar `nome = nome` → `self.nome = nome`  
✅ **Erro 3** - Adicionar `cpf` como parâmetro e `self.__cpf = cpf`  
✅ **Erro 4** - Adicionar `self` como parâmetro: `def apresentar(self):`  
✅ **Erro 5** - Usar `super().__init__()` em `Estudante`  
✅ **Erro 6** - Validar se lista não está vazia  
✅ **Erro 7** - Adicionar notas e CPF nas instâncias de teste  

---

## Conceitos POO Aplicados na Solução

1. **Herança**: Uso correto de `super().__init__()` para inicializar a classe pai
2. **Encapsulamento**: Proteção contra estados inválidos (lista vazia) e uso correto de atributos privados (`__cpf`)
3. **Polimorfismo**: Sobrescrita correta do método `apresentar()` em subclasses
4. **Responsabilidade Única**: Cada classe é responsável apenas por seus atributos específicos
5. **Contrato de Interface**: Respeito ao contrato definido pela classe pai
6. **DRY (Don't Repeat Yourself)**: Reutilização de código através de herança

---

## Conclusão

Todas as correções aplicadas garantem que o código:
- ✅ Respeita os princípios fundamentais de POO
- ✅ É robusto e trata casos extremos adequadamente
- ✅ Mantém a integridade e completude de dados
- ✅ Segue as convenções e boas práticas de Python (PEP 8)
- ✅ Implementa corretamente herança e reutilização de código

O código corrigido está pronto para ser usado, mantido e estendido com segurança.
