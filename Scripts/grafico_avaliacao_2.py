import matplotlib.pyplot as plt
import numpy as np

# Dados de avaliação - Segunda tabela
criterios = ['Fluência', 'Adequação/Fidelidade', 'Clareza', 'Consistência', 'Estilo/Registro', 'Formatação']
avaliador_1 = [3, 3, 3, 2, 4, 5]
avaliador_2 = [4, 3, 3, 3, 4, 4]
avaliador_3 = [4, 5, 4, 5, 4, 4]
avaliador_4 = [5, 5, 4, 4, 3, 4]

# Configurações do gráfico
x = np.arange(len(criterios))
width = 0.2

# Criar figura e eixos
fig, ax = plt.subplots(figsize=(12, 8))

# Criar as barras
bars1 = ax.bar(x - 1.5*width, avaliador_1, width, label='Avaliador 1', color='#1f77b4')
bars2 = ax.bar(x - 0.5*width, avaliador_2, width, label='Avaliador 2', color='#ff7f0e')
bars3 = ax.bar(x + 0.5*width, avaliador_3, width, label='Avaliador 3', color='#2ca02c')
bars4 = ax.bar(x + 1.5*width, avaliador_4, width, label='Avaliador 4', color='#d62728')

# Personalizar o gráfico
ax.set_xlabel('Critérios de Avaliação', fontsize=12)
ax.set_ylabel('Pontuação', fontsize=12)
ax.set_title('Avaliação por Critérios e Avaliadores - Segunda Avaliação', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(criterios, rotation=45, ha='right')
ax.legend()
ax.grid(True, axis='y', alpha=0.3)
ax.set_ylim(0, 6)

# Adicionar valores nas barras
def add_value_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.05,
                f'{height}', ha='center', va='bottom', fontsize=9)

add_value_labels(bars1)
add_value_labels(bars2)
add_value_labels(bars3)
add_value_labels(bars4)

# Ajustar layout
plt.tight_layout()

# Salvar o gráfico
plt.savefig('grafico_avaliacao_2.png', dpi=300, bbox_inches='tight')
print("Gráfico salvo como 'grafico_avaliacao_2.png'")

# Mostrar o gráfico
plt.show() 