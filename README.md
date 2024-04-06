# Configure the project

    python3 -m venv .venv 
    source .venv/bin/activate 
    pip install -r requirements.txt 

# Run benchmarks

    py.test --benchmark-sort=name 

or

    py.test --benchmark-sort=name -m piechart

s. [pytest.ini](./pytest.ini)