TEST_PATH=./tests

requirements:
	pip install -r requirements.txt
	
build:
	python setup.py sdist bdist_wheel

install: uninstall clean-build build
	pip install dist/*.whl

uninstall:
	pip uninstall bv -y

clean-build:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info

test:
	python -m pytest --verbose --color=yes $(TEST_PATH)
