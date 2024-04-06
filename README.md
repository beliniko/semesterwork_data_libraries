# Configure the project

    python3 -m venv .venv 
    source .venv/bin/activate 
    pip install -r requirements.txt 

# Run benchmarks

    py.test --benchmark-sort=name

or

    py.test --benchmark-sort=name -m piechart

or

    py.test --benchmark-sort=name --benchmark-histogram=result-hist --benchmark-save-data --benchmark-warmup=on --benchmark-warmup-iterations=2

s. [pytest.ini](./pytest.ini)