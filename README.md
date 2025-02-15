# Gerador de Números - Versão Inicial

Este projeto é um programa em Python para geração de números válidos, começando com a funcionalidade de **geração de CPFs**. Ele apresenta uma interface interativa e intuitiva, onde o usuário pode gerar um CPF válido ou sair do programa. Este README descreve as funcionalidades e como utilizar o código.

---

## Funcionalidades

1. **Interface Gráfica Simples**  
   - O programa apresenta um menu inicial, com as opções de gerar um CPF ou sair.
   - Mensagens amigáveis e animações de carregamento para uma experiência mais dinâmica.

2. **Geração de CPFs Válidos**  
   - O CPF é gerado seguindo o cálculo oficial dos dígitos verificadores, garantindo sua validade.
   - O CPF é formatado no padrão `XXX.XXX.XXX-XX`.

3. **Opções Pós-Geração**  
   - Após gerar o CPF, o usuário pode:
     - Gerar um novo CPF.
     - Retornar ao menu inicial.

4. **Tratamento de Erros**  
   - Opções inválidas são identificadas e o programa redireciona o usuário ao menu apropriado.

---

## Estrutura do Código

### 1. Arquivo `interface.py`
Este arquivo gerencia a interface principal do programa. Ele:
- Apresenta o menu inicial com opções de geração de números (atualmente apenas CPF).
- Encaminha o usuário para a funcionalidade escolhida ou encerra o programa.

### 2. Arquivo `gerador_cpf.py`
Este arquivo contém a lógica de geração de CPFs válidos:
- **Passos da geração**:
  1. Geração de 9 números aleatórios.
  2. Cálculo do 10º e 11º dígitos (verificadores) com base nas regras oficiais.
  3. Formatação e exibição do CPF gerado.
- Após gerar o CPF, apresenta opções de gerar outro CPF ou voltar ao menu.

---

## Como Executar

1. Certifique-se de que todos os arquivos necessários estão no mesmo diretório:
   - `interface.py`
   - `gerador_cpf.py`

2. Execute o arquivo `interface.py`:
   ```bash
   python interface.py

