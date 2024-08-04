from rest_framework import status
from rest_framework.test import APITestCase

from core.models import RaceResultModel


class TestRaceResultView(APITestCase):
    def test_get_all(self):
        '''Test Race Result view get all method'''
        url: str = 'http://localhost:8000/api/race_result/'
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == RaceResultModel.objects.count()

    def test_get_all_filter_by_season(self):
        '''Test Race Result view get all method filter by season'''
        url: str = 'http://localhost:8000/api/race_result/?season=2023'
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == RaceResultModel.objects.filter(season=2023).count()

    def test_get_all_sort_by_id(self):
        '''Test Race Result view get all method sort by id'''
        url: str = 'http://localhost:8000/api/race_result/?ordering=id'
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        for i in range(1, len(response.json())):
            assert response.json()[i].get('id') > response.json()[i - 1].get('id')

    def test_get(self):
        '''Test Driver Standing view get method'''
        race_result = RaceResultModel.objects.order_by('id').first()
        url: str = f'http://localhost:8000/api/race_result/{race_result.id}/'
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.json().get('id') == race_result.id

    def test_create(self):
        '''Test Race Result view post method'''
        url: str = 'http://localhost:8000/api/race_result/'
        data: dict = {
            'grand_prix': 'Test Grand Prix',
            'race_date': '2024-01-01',
            'winner': 'Test Winner',
            'car': 'Test Car',
            'laps': 50,
            'race_time': '1:30:00',
            'season': 2024
        }
        response = self.client.post(url, data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert RaceResultModel.objects.filter(**data).exists()

    def test_update(self):
        '''Test Race Result view put method'''
        race_result = RaceResultModel.objects.order_by('-id').first()
        url: str = f'http://localhost:8000/api/race_result/{race_result.id}/'
        data: dict = {
            'grand_prix': 'Test Grand Prix Updated',
            'race_date': '2024-01-02',
            'winner': 'Test Winner Updated',
            'car': 'Test Car Updated',
            'laps': 60,
            'race_time': '2:30:00',
            'season': 2025
        }
        response = self.client.put(url, data, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert RaceResultModel.objects.filter(**data).exists()

    def test_delete(self):
        '''Test Race Result view delete method'''
        race_result = RaceResultModel.objects.order_by('-id').first()
        url: str = f'http://localhost:8000/api/race_result/{race_result.id}/'
        response = self.client.delete(url, format='json')
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not RaceResultModel.objects.filter(id=race_result.id).exists()
