# Simulação do Modelo SIR em Grade

Este projeto implementa uma simulação do modelo epidemiológico SIR (Suscetível-Infectado-Recuperado) em uma grade 2D usando Python. A simulação mostra visualmente como uma doença se espalha através de uma população.

## Descrição

O modelo SIR divide a população em três grupos:
- **Suscetível (S)**: Indivíduos que podem ser infectados
- **Infectado (I)**: Indivíduos que têm a doença e podem transmiti-la
- **Recuperado (R)**: Indivíduos que se recuperaram e estão imunes

## Parâmetros da Simulação

- `grid_size`: Tamanho da grade (50x50)
- `tau`: Taxa de infecção (0.3)
- `gamma`: Taxa de recuperação (0.1)
- `steps`: Número de passos da simulação (100)

## Visualização

A simulação usa um mapa de cores 'viridis':
- Azul escuro: Suscetível (0)
- Verde/Amarelo: Infectado (1)
- Amarelo claro: Recuperado (2)

## Requisitos

- Python 3.7+
- NumPy
- Matplotlib

## Instalação

1. Clone este repositório
2. Instale as dependências:

```bash
pip install numpy matplotlib
```

## Uso

```bash
python main.py
```


## Como Funciona

1. A simulação começa com uma grade de 50x50 células, onde a maioria está suscetível (azul)
2. Algumas células são inicialmente infectadas (verde/amarelo)
3. A cada passo:
   - Células suscetíveis podem ser infectadas por vizinhos infectados
   - Células infectadas podem se recuperar
4. A simulação continua por 100 passos, mostrando a evolução da epidemia

## Resultados

A simulação produz uma animação que mostra a propagação da doença ao longo do tempo.

