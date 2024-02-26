from unittest.mock import Mock
from bonzer_implementace import Observer, Kontejner, Notifikator, Karta

def test_bonzeru() -> None:
    mock_kontejner = Mock()
    mock_notifikator = Mock()
    o = Observer(mock_kontejner, mock_notifikator)
    mock_kontejner.ctecka.return_value = Karta(5, "Linda Stastna", 1238568356, "linda@stastna.arcig.cz")
    o.vstup(5)

    mock_notifikator.zprava.assert_called_with("linda@stastna.arcig.cz", "Žák Linda Stastna právě dorazil do školy.") 