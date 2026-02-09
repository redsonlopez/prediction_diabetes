# Prediction Diabetes

Projeto de Machine Learning para previsão de diabetes, com pipeline estruturado, treinamento de modelo e disponibilização via API.
<blockquote>
Esse projeto tem como objetivo desenvolver um modelo de classificação para prever a ocorrência de diabetes a partir de dados clínicos, aplicando boas práticas de organização de código e conceitos de MLOps.
</blockquote>

Link para acesso a API:
https://prediction-diabetes-wc45.onrender.com/docs

### Executar localmente

```bash
poetry install
poetry run uvicorn prediction_diabetes.api.main:app --reload

## Tecnologias Utilizadas

- Python
- pandas
- scikit-learn
- FastAPI
- Poetry

## Status do Projeto

Em desenvolvimento.

Próximos passos planejados:
- Containerização com Docker
- CI/CD com GitHub Actions
- Versionamento de modelos
- Monitoramento e validação de dados

