import requests
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import CreateUserSerializer

CLIENT_ID = "FFkBdq6jhLkR8E9fZ2yXT1TWqchqfs0KHvA4QpmZ"
CLIENT_SECRET = "jVUu2AllmRbYdvSGbPCDKzwfVWzViEUpwcilEuy0eI3wteFM2ol8XLwNA3CQb9E0wW9S1aJ14TKeS5X3xaezRnaIazkOD13gZT0iaBdu9ZBWQ5NRLzNMmHp5fpqN6nr7"
HOST = 'https://students-monitor.herokuapp.com/api/v0/auth/'


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    '''
    Registers user to the server. Input should be in the format:
    {"username": "username", "password": "1234abcd", "email": "email@mail.com", "first_name": "Oleg", "last_name": "Olegov"}
    '''
    # Put the data from the request into the serializer 
    serializer = CreateUserSerializer(data=request.data)
    if serializer.is_valid():
        # If it is valid, save the data (creates a user).
        serializer.save()
        # Then we get a token for the created user.
        # This could be done differentley 
        r = requests.post(HOST + 'o/token/',
                          data={
                              'grant_type': 'password',
                              'username': request.data.get('username', None),
                              'password': request.data.get('password', None),
                              'client_id': CLIENT_ID,
                              'client_secret': CLIENT_SECRET,
                          },
                          )
        return Response(r.json())
    return Response(serializer.errors, status=400)


@api_view(['POST'])
@permission_classes([AllowAny])
def token(request):
    '''
    Gets tokens with username and password. Input should be in the format:
    {"username": "username", "password": "1234abcd"}
    '''
    r = requests.post(
        HOST + 'o/token/',
        data={
            'grant_type': 'password',
            'username': request.data.get('username', None),
            'password': request.data.get('password', None),
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    return Response(r.json())


@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token(request):
    '''
    Registers user to the server. Input should be in the format:
    {"refresh_token": "<token>"}
    '''
    r = requests.post(
        HOST + 'o/token/',
        data={
            'grant_type': 'refresh_token',
            'refresh_token': request.data.get('refresh_token', None),
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    return Response(r.json())


@api_view(['POST'])
@permission_classes([AllowAny])
def revoke_token(request):
    '''
    Method to revoke tokens.
    {"token": "<token>"}
    '''
    r = requests.post(
        HOST + 'o/revoke_token/',
        data={
            'token': request.data.get('token', None),
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    # If it goes well return sucess message (would be empty otherwise) 
    if r.status_code == requests.codes.ok:
        return Response({'message': 'token revoked'}, r.status_code)
    # Return the error if it goes badly
    return Response(r.json(), r.status_code)
