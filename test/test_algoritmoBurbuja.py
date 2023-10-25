from src.algoritmoBurnuja import algoritmoBurbuja

def test_algoritmoBurbuja():
    
    assert algoritmoBurbuja([45, 6, 46 ,56, 5, 87, 8, 51]) == [5, 6, 8, 45, 46, 51, 56, 87]