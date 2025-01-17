clean:
	rm build -R; rm dist -R

build:
	python3 setup.py sdist bdist_wheel

upload:
	python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/* --verbose

release:
	make clean; make build; make upload

install:
	python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps zyplots