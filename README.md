# GEngine
# Sistema de Anti-Cheat e Atualização de Drivers

Este projeto contém um conjunto de scripts Python para gerenciamento de drivers e proteção contra trapaças em jogos. O sistema integra funcionalidades de monitoramento e atualização de drivers, além de um mecanismo de anti-cheat que registra atividades suspeitas.

## Funcionalidades

### Anti-Cheat
- Monitoramento em tempo real de processos suspeitos, incluindo cheats conhecidos e funções críticas do sistema.
- Verificação da integridade do script anti-cheat e geração de logs de atividades.
- Relatórios de trapaças enviados a uma API de segurança.
- Registra atividades em um arquivo `anticheat_logs.txt`.

### Atualização de Drivers
- Verificação e atualização de drivers de dispositivos.
- Exibição de logs de atualizações realizadas em `log.txt`.
- Modo de depuração para funcionalidades avançadas (com senha).
- Suporte para Light e Black Modes.
- Permite exclusão de arquivos de configuração e logs.

## Pré-requisitos

Antes de usar os scripts, você precisa ter o Python instalado em seu sistema. Você pode baixar a versão mais recente do Python [aqui](https://www.python.org/downloads/).

### Dependências

Os scripts utilizam bibliotecas padrão do Python, como `os`, `hashlib`, `psutil`, `requests`, `time`, `ctypes`, `threading` e `subprocess`. Não são necessárias bibliotecas externas.

## Como Usar

1. Clone ou baixe o repositório:
   ```bash
   git clone <https://github.com/BaHost01/GEngine>
   cd <GEngine>
