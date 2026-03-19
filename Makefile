.PHONY: help install lock data train evaluate pipeline serve test lint format clean

PYTHON=poetry run python
APP_MODULE=prediction_diabetes.api.main:app

help:
	@echo "Comandos disponíveis:"
	@echo " make install    -> Instala dependências"
	@echo " make data       -> Gera dataset"
	@echo " make train      -> Treina modelo"
	@echo " make evaluate   -> Avalia modelo"
	@echo " make pipeline   -> Executa pipeline completo"
	@echo " make serve      -> Sobe API"
	@echo " make test       -> Executa testes"
	@echo " make lint       -> Verifica código"
	@echo " make format     -> Formata código"
	@echo " make clean      -> Limpa artefatos"

install:
	poetry install

lock:
	poetry lock

data:
	$(PYTHON) src/prediction_diabetes/data/make_dataset.py

train:
	$(PYTHON) src/prediction_diabetes/models/train.py

evaluate:
	$(PYTHON) src/prediction_diabetes/models/evaluate.py

pipeline: data train evaluate

serve:
	poetry run uvicorn $(APP_MODULE) --reload

test:
	poetry run pytest

lint:
	poetry run ruff check .

format:
	poetry run ruff format .

clean:
	rm -rf data/processed/*
	rm -rf models/*
	rm -rf __pycache__
	rm -rf .pytest_cache

