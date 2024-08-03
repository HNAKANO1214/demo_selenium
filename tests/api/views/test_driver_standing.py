from rest_framework import status
from rest_framework.test import APITestCase

from core.models import DriverStandingModel


class TestDriverStanding(APITestCase):
    def test_get_all(self):
        '''Test Driver Standing view get all method'''
        url: str = 'http://localhost:8000/api/driver_standing/'
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == DriverStandingModel.objects.count()

    def test_get_all_filter_by_season(self):
        '''Test Driver Standing view get all method filter by season'''
        url: str = 'http://localhost:8000/api/driver_standing/?season=2023'
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == DriverStandingModel.objects.filter(season=2023).count()

    def test_get_all_sort_by_id(self):
        '''Test Driver Standing view get all method sort by id'''
        url: str = 'http://localhost:8000/api/driver_standing/?ordering=id'
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        for i in range(1, len(response.json())):
            assert response.json()[i].get('id') > response.json()[i - 1].get('id')

    def test_get(self):
        '''Test Driver Standing view get method'''
        driver_standing = DriverStandingModel.objects.order_by('id').first()
        url: str = f'http://localhost:8000/api/driver_standing/{driver_standing.id}/'
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.json().get('id') == driver_standing.id

    def test_create(self):
        '''Test Driver Standing view post method'''
        url: str = 'http://localhost:8000/api/driver_standing/'
        data: dict = {
            'driver': 'Test Driver',
            'position': 1,
            'nationality': 'Test National',
            'team': 'Test Team',
            'points': 100,
            'season': 2024
        }
        response = self.client.post(url, data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert DriverStandingModel.objects.filter(**data).exists()

    def test_update(self):
        '''Test Driver Standing view put method'''
        driver_standing = DriverStandingModel.objects.order_by('-id').first()
        url: str = f'http://localhost:8000/api/driver_standing/{driver_standing.id}/'
        data: dict = {
            'driver': 'Test Driver Updated',
            'position': 2,
            'nationality': 'Test National Updated',
            'team': 'Test Team Updated',
            'points': 200,
            'season': 2025
        }
        response = self.client.put(url, data, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert DriverStandingModel.objects.filter(**data).exists()

    def test_delete(self):
        '''Test Driver Standing view delete method'''
        driver_standing = DriverStandingModel.objects.order_by('-id').first()
        url: str = f'http://localhost:8000/api/driver_standing/{driver_standing.id}/'
        response = self.client.delete(url, format='json')
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not DriverStandingModel.objects.filter(id=driver_standing.id).exists()
