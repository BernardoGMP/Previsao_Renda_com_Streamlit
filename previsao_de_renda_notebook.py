import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

#Configurando a página

st.set_page_config(
     page_title="Análise de Renda",
     page_icon="https://cdn-icons-png.flaticon.com/512/272/272369.png",
#     layout="wide",
)

#Importando dados e configurando legenda
renda = pd.read_csv('./input/previsao_de_renda.csv')
datas = ['01-2015','02-2015','03-2015','03-2015','05-2015','06-2015',
         '07-2015','08-2015','09-2015','10-2015','11-2015','12-2015',
         '01-2016','02-2016','03-2016',]
color_mapping = {True: 'green', False: 'red'}
order_legenda = [True, False]

#Título
st.title('Análise Exploratória da Previsão de Renda')

#Primeira Seção
st.header('Gráficos ao longo do tempo')
st.write('Os gráficos abaixo mostram a média de renda por alguns indicadores ao longo do ano.')

#Gráfico 1
fig1, ax1 = plt.subplots()
sns.lineplot(x='data_ref',y='renda', hue='posse_de_imovel', data=renda, 
             ax=ax1, palette=color_mapping, hue_order=order_legenda)
ax1.tick_params(axis='x', rotation=90)
ax1.set_title('Posse de Imóvel X Renda')
ax1.set_xticklabels(datas)
ax1.set_xlabel(' ')
ax1.set_ylabel('Renda')
ax1.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
st.pyplot(fig1)

#Análise 1
st.write('''O grafico acima mostra a média dos valores da renda de quem possui imóvel comparado a quem não 
         possui ao longo do ano. Vemos que neste quesito, não há um padrão claro ao longo do ano. Em alguns 
         meses quem não tem imóvel tem uma renda maior e em outros quem tem imóvel tem uma renda maior.''')

#Gráfico 2
fig2, ax2 = plt.subplots()
sns.lineplot(x='data_ref',y='renda', hue='posse_de_veiculo',
             data=renda, ax=ax2, palette=color_mapping, hue_order=order_legenda)
ax2.tick_params(axis='x', rotation=90)
ax2.set_title('Posse de Veículo X Renda')
ax2.set_xticklabels(datas)
ax2.set_xlabel(' ')
ax2.set_ylabel('Renda')
ax2.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
st.pyplot(fig2)

#Análise 2
st.write('''O grafico acima mostra a média dos valores da renda de quem possui veículo comparado a quem não 
         possui ao longo do ano. Ao contrário do gráfico anterior, há um padrão claro neste. Quem possui
         veículo quase sempre tem uma renda maior.''')

#Gráfico 3
fig3, ax3 = plt.subplots()
sns.lineplot(x='data_ref',y='renda', hue='sexo',
             data=renda, ax=ax3, hue_order=['M','F'])
ax3.tick_params(axis='x', rotation=90)
ax3.set_title('Gênero X Renda')
ax3.set_xticklabels(datas)
ax3.set_xlabel(' ')
ax3.set_ylabel('Renda')
ax3.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
st.pyplot(fig3)

#Análise 3
st.write('''O gráfico acima mostra a dimensão da discrepância entre a renda dos homens (M) e mulheres (F).
         Consistentemente, ao longo de todo o ano, homens recebem mais que o dobro do que as mulheres na
         base apresentada.''')

#Segunda Seção
st.header('Gráficos de barra')
st.write('''Os gráficos abaixo mostram a média de renda por indicador ao longo do ano. Cada barra representa 
         a estimativa central da distribuição dos dados naquele grupo específico. A linha preta no topo de
         cada barra é conhecida como "barra de erro" e representa o intervalo de confiança de 95% para 
         a média da distribuição.''')

#Gráfico 4
fig4, ax4 = plt.subplots()
sns.barplot(x='tipo_renda',y='renda',data=renda, ax=ax4)
ax4.tick_params(axis='x', rotation=60)
ax4.set_title('Tipo de Renda X Renda')
ax4.set_xlabel(' ')
ax4.set_ylabel('Renda')
st.pyplot(fig4)

#Análise 4
st.write('''O gráfico acima mostra que servidores públicos costumam ter as maiores rendas e pensiosistas, 
         as menores. Assalariados e empresários costumam ter a renda próxima um do outro e bolsistas
         possuem a maior variância.''')

#Gráfico 5
fig5, ax5 = plt.subplots()
sns.barplot(x='educacao',y='renda',data=renda, ax=ax5)
ax5.tick_params(axis='x', rotation=60)
ax5.set_title('Educação X Renda')
ax5.set_xlabel(' ')
ax5.set_ylabel('Renda')
st.pyplot(fig5)

#Análise 5
st.write('''O gráfico acima mostra algumas informações curiosas. Quem possui ensino superior completo
         costuma ter salários mais altos (o que é esperado), mas o mesmo não é verdade para quem possui
         pós-graduação (que também possui a maior variância). Outra conclusão curiosa é que quem possui 
         apenas o secundário concluído costuma ter remuneração maior do que quem possui superior incompleto, 
         cuja remuneração é parecida com a de quem tem apenas o primário concluído.''')

#Gráfico 6
fig6, ax6 = plt.subplots()
sns.barplot(x='estado_civil',y='renda',data=renda, ax=ax6)
ax6.tick_params(axis='x', rotation=60)
ax6.set_title('Estado Civil X Renda')
ax6.set_xlabel(' ')
ax6.set_ylabel('Renda')
st.pyplot(fig6)

#Análise 6
st.write('''No gráfico acima podemos observar que viúvos possuem a menor renda enquanto casados a maior.
         Quem possui união estável ganha menos do que quem é casado, solteiro ou separado.''')

#Gráfico 7
fig7, ax7 = plt.subplots()
sns.barplot(x='tipo_residencia',y='renda',data=renda, ax=ax7)
ax7.tick_params(axis='x', rotation=60)
ax7.set_title('Tipo de Residência X Renda')
ax7.set_xlabel(' ')
ax7.set_ylabel('Renda')
st.pyplot(fig7)

#Análise 7
st.write('''No gráfico acima vemos que a maioria das rendas médias é bem próxima entre diferentes tipos
         de residência, porém quem vive em estúdios geralmente possui uma renda mais alta (mas também
         com uma variância maior).''')

