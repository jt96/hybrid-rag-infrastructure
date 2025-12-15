import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import pytest # noqa: E402
from state_manager import StateManager, compute_file_hash # noqa: E402

@pytest.fixture
def temp_state_file(tmp_path):
    """
    Returns a path to a temporary JSON file.
    Pytest ensures this path is unique per test function.
    """
    file_path = tmp_path / "test_state.json"
    return str(file_path)

@pytest.fixture
def manager(temp_state_file):
    """Initializes a StateManager instance pointing to the temporary file."""
    return StateManager(state_file=temp_state_file)

def test_initialization_is_empty(manager):
    """Verifies that a new StateManager starts with an empty state."""
    assert manager.state == {}
    
def test_compute_hash(manager, tmp_path):
    """Verifies SHA-256 hashing logic against a known input."""
    # Create a dummy file with known content
    dummy_file = tmp_path / "dummy.txt"
    dummy_file.write_text("Hello World", encoding="utf-8")
    
    # Pre-calculated SHA-256 for "Hello World"
    expected_hash = "a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e"
    
    computed_hash = compute_file_hash(str(dummy_file))
    
    assert computed_hash == expected_hash
    
def test_persistence(manager, temp_state_file):
    """
    Verifies that state is correctly saved to disk and can be reloaded 
    by a new StateManager instance.
    """
    fake_path = "C:/fake/file.pdf"
    fake_hash = "12345fakehash"
    
    # Adding a processed file should update memory and write to disk
    manager.add_processed(fake_hash, fake_path)
    
    # Initialize a new manager using the same file to simulate a restart
    new_manager = StateManager(state_file=temp_state_file)
    
    assert fake_hash in new_manager.state
    assert new_manager.state[fake_hash] == fake_path