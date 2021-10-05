from algoliasearch.search_client import SearchClient

client = SearchClient.create('APP_ID', 'API_KEY')
index = client.init_index('test_index')


index.partial_update_objects([
    {
        '_tags': {
            '_operation': 'AddUnique',
            'value': 'public'
        },
        'objectID': '0'
    },
    {
        'lastmodified': {
            '_operation': 'IncrementSet',
            'value': 1593431913
        },
        'objectID': '0'
    }
])
