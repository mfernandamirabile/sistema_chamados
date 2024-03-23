# Sistema de Gerenciamento de Chamados para o Governo do Maranhão

Este é um sistema de gerenciamento de chamados no formato de app desktop desenvolvido para facilitar o processo de monitoramento e acompanhamento de solicitações feitas ao Governo do Maranhão. O sistema permite o registro, organização e acompanhamento eficiente de chamados relacionados a diferentes áreas de atuação governamental.

O sistema foi criado como uma demonstração fictícia e não está associado ao Governo do Maranhão ou a qualquer outra entidade oficial.

## Funcionalidades Principais

- Registro e visualização de chamados pendentes.
- Atribuição de prioridades e status aos chamados.
- Acompanhamento do progresso e status de cada chamado.
- Comunicação entre os agentes responsáveis pelos chamados e os solicitantes.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para o desenvolvimento do sistema.
- **Tkinter**: Biblioteca gráfica utilizada para a criação da interface de usuário.
- **PIL (Python Imaging Library)**: Biblioteca utilizada para manipulação de imagens.
- **ttkbootstrap**: Biblioteca utilizada para estilização dos elementos da interface.
- **Random**: Módulo utilizado para geração de números aleatórios.

## Estrutura do Código Fonte

O código fonte do sistema está organizado em:

1. **app.py**: Contém a implementação da interface gráfica e a lógica principal do sistema, incluindo a definição das classes e métodos responsáveis por gerenciar as diferentes funcionalidades do sistema.
2. **chamados.py**: Contém a implementação das funcionalidades relacionadas aos chamados, incluindo as trocas de mensagem, responsável e detalhes do chamado. Esse módulo ainda não está completo e contém somente uma demonstração de como seria essa funcionalidade.
3. **dashboards.py**: Contém o módulo ainda não inciado de análise dos chamados.
4. **imgens.py**: Contém o carregamento das imagens utilizadas no app.

## Como Executar o Sistema

Para executar o sistema, é necessário ter o Python instalado em seu ambiente. Em seguida, basta executar o arquivo `app.py` utilizando o interpretador Python. O sistema abrirá uma interface gráfica onde você poderá interagir com as diferentes funcionalidades disponíveis.

```
python app.py
```

## Contribuições

Contribuições são bem-vindas! Se você deseja contribuir para o desenvolvimento deste projeto, sinta-se à vontade para enviar pull requests com melhorias, correções de bugs ou novas funcionalidades. Certifique-se de seguir as diretrizes de contribuição e código do projeto.

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE).

## Nomenclatura Visual:

- `frame`: Termina com FR.
- `label`: Termina com LB.
- `imagens`: Termina com IM.
- `botão`: Termina com BT.
- `separador`: Termina com ST.
- `treeview`: Termina com TW.

## Requisitos:

- Python 3.11
- Bibliotecas: `tkinter`, `PIL`, `ttkbootstrap`, `random`