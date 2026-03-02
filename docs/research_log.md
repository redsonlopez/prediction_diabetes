# Research Log - Diabetes Dataset

## Próximo passos

### Tratamento de outlies
- IQR aplicado, porém os valores detectados como outliers estão dentro de causas possíveis.
- A remoção deles pode diminuir o poder preditivo.


## 28/02/2026 - EDA

### Variável: screen_time_hours_per_day
- Tipo: Contínua
- Teste aplicado: Qui-Quadrado
- p-value: 0.026
- Resultado: Estatisticamente significativa para diabetes

### Observações
- Pode haver relação comportamental indireta (sedentarismo)
- Avaliar associação com BMI

### Próximos passos para screen_time_hours_per_day
- Testar associação com:
    - Teste de Cramér's V (força da associação)
    - Regressão logística univariada
- Verificar multicolinearidade

