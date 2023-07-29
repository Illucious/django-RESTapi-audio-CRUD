# Django RESTapi Audio CRUD

A simple REST API service for CRUD operations on audio elements in a video editing platform. It is built using DjangoRestFramework

---

## Prerequisites

- Python ≥3.8
- pip(prefer latest)

---

## Setup

1. First clone the repository using the following command

```bash
git clone https://github.com/Illucious/django-RESTapi-audio-CRUD.git
```

2. Install all the required libraries

```bash
pip install -r requirements.txt
```

3. Run the server on local machine using 

```bash
python manage.py runserver
```

---

## Endpoints

- `/api/video-element/` - GET, POST video elements
- `/api/video-element-audio-elements/<video_element_id>/` - GET, DELETE an audio element using video ID
- `/api/"audio-element/` - POST audio elements
- `/api/audio-element/<id>/`- GET, PUT, DELETE
- Parameters
    - `video_element_id` - ID of the project
    - `id` - ID of the audio-element
