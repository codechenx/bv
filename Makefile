TEST_PATH=./tests

requirements:
	pip install -r requirements.txt

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +

clean-build:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info

test:clean-pyc
	python -m pytest --verbose --color=yes $(TEST_PATH)
