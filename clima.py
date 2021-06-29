from pomegranate import *

# Probabilidade do estado inicial
start = DiscreteDistribution({
    "sun": 0.7,
    "rain": 0.3
})

# Modelo de transição
transitions = ConditionalProbabilityTable([
    ["sun", "sun", 0.9],
    ["sun", "rain", 0.1],
    ["rain", "sun", 0.6],
    ["rain", "rain", 0.4]
], [start])

# Cadeia de Markov
model = MarkovChain([start, transitions])

# 100 amostras
print(model.sample(100))