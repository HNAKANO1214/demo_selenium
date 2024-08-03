from rest_framework import status
from rest_framework.test import APITestCase

from core.models import ConstructorStandingModel


class TestConstructorStandingView(APITestCase):
    def test_get_all(self):
        '''Test Constructor Standing view get all method'''
        url: str = 'http://localhost:8000/api/constructor_standing/'
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == ConstructorStandingModel.objects.count()

    def test_get_all_filter_by_season(self):
        '''Test Constructor Standing view get  all method filter by season'''
        url: str = 'http://localhost:8000/api/constructor_standing/?season=2023'
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == ConstructorStandingModel.objects.filter(season=2023).count()

    def test_get_all_sort_by_id(self):
        '''Test Constructor Standing view get all method sort by id'''
        url: str = 'http://localhost:8000/api/constructor_standing/?ordering=id'
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        for i in range(1, len(response.json())):
            assert response.json()[i].get('id') > response.json()[i - 1].get('id')

    def test_get(self):
        '''Test Constructor Standing view get method'''
        constructor_standing = ConstructorStandingModel.objects.order_by('id').first()  # id=1
        url: str = f'http://localhost:8000/api/constructor_standing/{constructor_standing.id}/'
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.json().get('id') == constructor_standing.id

    def test_create(self):
        '''Test Constructor Standing view post method'''
        url: str = 'http://localhost:8000/api/constructor_standing/'
        data: dict = {
            'constructor': 'Test Constructor',
            'position': 1,
            'points': 100,
            'season': 2024
        }
        response = self.client.post(url, data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert ConstructorStandingModel.objects.filter(**data).exists()

    def test_update(self):
        '''Test Constructor Standing view put method'''
        constructor_standing = ConstructorStandingModel.objects.order_by('-id').first()
        url: str = f'http://localhost:8000/api/constructor_standing/{constructor_standing.id}/'
        data: dict = {
            'constructor': 'Test Constructor Updated',
            'position': 2,
            'points': 200,
            'season': 2024
        }
        response = self.client.put(url, data, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert ConstructorStandingModel.objects.filter(**data).exists()

    def test_delete(self):
        '''Test Constructor Standing view delete method'''
        constructor_standing = ConstructorStandingModel.objects.order_by('-id').first()
        url: str = f'http://localhost:8000/api/constructor_standing/{constructor_standing.id}/'
        response = self.client.delete(url, format='json')
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not ConstructorStandingModel.objects.filter(id=constructor_standing.id).exists()
