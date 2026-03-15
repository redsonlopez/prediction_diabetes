# Architecture Decision Record

### Versão do Python
- Pyenv

### Versionameto de dependências
- Poetry

### Registro dos Modelos
- Pickle (ou MLFlow)

### Make file
python src/prediction_diabetes/data/make_dataset.py
python src/prediction_diabetes/models/train.py
poetry run uvicorn prediction_diabetes.api.main:app --reload

### Teste automatizado do modelo
- Pytest

### Data Drift
- Evidently

### API
- Fast API

### Conteinerização
- Docker

### CI/CD
- Github Actions

### Instancia do Modelo
- Render (ou Azure)

### Teste de carga
- Locust

