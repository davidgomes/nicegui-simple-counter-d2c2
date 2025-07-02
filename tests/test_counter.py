import pytest
from nicegui.testing import User
from nicegui import ui
from app.models import Counter


async def test_counter_initial_state(user: User) -> None:
    """Test that counter starts at 0"""
    await user.open('/')
    await user.should_see('Count: 0')


async def test_counter_increment(user: User) -> None:
    """Test increment functionality"""
    await user.open('/')
    
    # Click increment button
    user.find(marker='increment-btn').click()
    await user.should_see('Count: 1')


async def test_counter_decrement(user: User) -> None:
    """Test decrement functionality"""
    await user.open('/')
    
    # Click decrement button
    user.find(marker='decrement-btn').click()
    await user.should_see('Count: -1')


async def test_counter_multiple_operations(user: User) -> None:
    """Test multiple increment and decrement operations"""
    await user.open('/')
    
    # Increment 3 times
    for _ in range(3):
        user.find(marker='increment-btn').click()
    await user.should_see('Count: 3')
    
    # Decrement 2 times
    for _ in range(2):
        user.find(marker='decrement-btn').click()
    await user.should_see('Count: 1')


async def test_counter_reset(user: User) -> None:
    """Test reset functionality"""
    await user.open('/')
    
    # Increment to 5
    for _ in range(5):
        user.find(marker='increment-btn').click()
    await user.should_see('Count: 5')
    
    # Reset
    user.find(marker='reset-btn').click()
    await user.should_see('Count: 0')


async def test_counter_persistence(user: User) -> None:
    """Test that counter value persists in user storage"""
    await user.open('/')
    
    # Increment counter twice
    user.find(marker='increment-btn').click()
    user.find(marker='increment-btn').click()
    
    await user.should_see('Count: 2')
    
    # Simulate page reload by opening again
    await user.open('/')
    await user.should_see('Count: 2')  # Should persist


def test_counter_model():
    """Test Counter model"""
    counter = Counter()
    assert counter.value == 0
    
    counter = Counter(value=10)
    assert counter.value == 10
    
    # Test serialization
    data = counter.model_dump()
    assert data == {'value': 10}
    
    # Test deserialization
    new_counter = Counter(**data)
    assert new_counter.value == 10