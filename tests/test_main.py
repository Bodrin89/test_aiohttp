from src.create_app import create_app


async def test_healthcheck(aiohttp_client):
    """
    Тест проверки состояния сервиса
    """
    client = await aiohttp_client(create_app())
    resp = await client.get('/healthcheck')
    text = await resp.text()
    assert resp.status == 200
    assert text == '{}'


async def test_hash_string_valid(aiohttp_client):
    """
    Тест проверки хэширования строки
    """
    client = await aiohttp_client(create_app())
    resp = await client.post(path='/hash', json={'string': 'Hello, World!'})
    data = await resp.json()
    assert resp.status == 200
    assert 'hash_string' in data
    assert data['hash_string'] == 'dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f'


async def test_hash_string_invalid(aiohttp_client):
    """
    Тест проверки не валидного запроса
    """
    client = await aiohttp_client(create_app())
    resp = await client.post(path='/hash', json={'not_string': 'Hello, World!'})
    data = await resp.json()
    assert resp.status == 400
    assert 'validation_errors' in data
