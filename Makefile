
install:
	poetry install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl
	
lint:
	poetry run flake8 brain_games/

full-install:
	poetry install
	poetry build
	poetry publish --dry-run
	python3 -m pip install --user dist/*.whl
	python3 -m pip install --force-reinstall --user dist/*.whl
