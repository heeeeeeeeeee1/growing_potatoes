
# PJT 04

### 오늘 pjt 를 통해 배운 내용

* 가상환경을 설정하여 프로젝트를 진행하는 방법을 배울 수 있었다.

* 장고에서 프로젝트를 생성하고, 앱을 생성하여 메인 페이지, create 페이지 등을 만들 수 있었다.

* Bootstrap을 이용하는 방법에 대해 학습할 수 있었다.


## A. settings.py — templates 베이스 설정하기

* 주요 요구 사항 : 베이스 템플릿을 세팅에 미리 선언해놓기

* 결과 : 해당하는 위치에 적절한 명령어를 입력하여 선언할 수 있었다.
  
  * 기억해볼 부분
  
    ```
    TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]
    ```
  
    * 핵심 내용
    - 구체적인 명령어에 대한 이해가 필요할 것 같다. 
    * 생각해본 다른 활용 법
  * 트러블 슈팅한 부분
    * 트러블 현상 및 에러 정보
      위치는 찾아내었는데 어떤 명령어를 작성해야하는지 알 수 없었다.
    * 원인 및 해결 방법
      ```
      'DIRS': [
            BASE_DIR / 'templates',
        ],
      ```
## B. urls.py — detail 페이지 연결하기

* 주요 요구 사항 : 메인 화면에서 DETAIL 버튼을 클릭하면 detail.html을 호출할 수 있게 연결하기

* 결과 : pk 값을 받아 주소에 올리고, 그걸 디테일 함수에서 인자로 받아갈 수 있게 url 경로를 수정해줌
  
  * 기억해볼 부분
  
    ```
    from django.urls import path
    from . import views

    app_name = 'movies'
    urlpatterns = [
        path('', views.index, name='index'),
        path('create/', views.create, name='create'),
        path('<int:pk>/', views.detail, name='detail'),
    ]
    ```
    ```
    {% extends "base.html" %}
    {% block content %}
        <h1 class='p-3'>메인 페이지</h1>
        {% for movie in movies %}
            {% comment %} <p>{{ movie.title }}</p>
            <p>{{ movie.content }}</p> {% endcomment %}
            {% comment %} <img src="" alt=""> {% endcomment %}
        <div class="row row-cols-1 row-cols-md-3 g-4">
            <div class="p-3">
            <div class="card">
                <div class="card-header">
                <h3> {{ movie.title }} </h3>
                </div>
                <div class="card-body">
                    <p class="card-text">{{ movie.content }}</p>
                    <a href="{% url "movies:detail" movie.pk %}" class="btn btn-primary">Detail</a>
                </div>
            </div>
            </div>
        </div>

        {% endfor %}
    {% endblock content %}
    ```
  
    * 핵심 내용
      - url에서 path를 <int:pk>로 설정해주기
    * 생각해본 다른 활용 법
  * 트러블 슈팅한 부분
    * 트러블 현상 및 에러 정보
      pk인자 값을 찾을 수 없다는 에러 발생
    * 원인 및 해결 방법
      ```
      path('<int:pk>/', views.detail, name='detail'),
      ```
      - pk값을 경로 요청시부터 받아, 그것을 detail view에서 받아 올 수 있게 해야하는데 이 과정을 인지하지 못하고 진행했음.

-----


# 오늘 후기

* 오랜만에 bootstrap을 다시 이용해보아서 잊은 부분들도 많고, 반가웠던 부분도 많았다.
* 처음부터 끝까지 장고를 이용하여 작업을 해보니, 내가 부족한 부분이 어디인지를 인지할 수 있었다.
* 이론 공부를 조금 더 꼼꼼히 진행하고, 내용을 이해할 수 있게 해야겠다.



### 참고 사이트

* [bootstrap 공식 사이트](https://getbootstrap.com/)
