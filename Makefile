TEST_PATH=./tests

requirements:
	pip install -r requirements.txt

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +

build:
	python setup.py sdist bdist_wheel

install: build
	pip uninstall bv -y
	pip install dist/*.whl

clean-build:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info

test:clean-pyc
	python -m pytest --verbose --color=yes $(TEST_PATH)
