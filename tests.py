from main import request_artist_info, request_song_url


# artist info test
def test_request_artist_info():
    response = request_artist_info('ariana grande', 2)
    assert response.status_code == 200


# song url test
def test_request_song_url():
    url = request_song_url('ariana grande', 1)
    assert url == ['https://genius.com/Ariana-grande-thank-u-next-lyrics']


if __name__ == '__main__':
    test_request_artist_info()
    test_request_song_url()
