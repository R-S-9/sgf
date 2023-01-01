# SGF - API
Все POST url для тестирования.
http://127.0.0.1:8000/api/v1/reviews/ POST
{
    "review": "Комментарий",
    "rating": 5,
    "user": 13,
    "training_course_id": 2
}
http://127.0.0.1:8000/api/v1/teachers/ POST
{
    "gender": "F",
    "birth_date": "2022-12-10",
    "first_name": "test1",
    "last_name": "test1",
    "middle_name": "test1",
    "about_me": "test1",
    "rank": "Тренер",
    "user": 13
}
http://127.0.0.1:8000/api/v1/course_program/ POST
{
    "chapter": "Глава 1",
    "chapter_number": 1,
    "training_course_program": 3
}
http://127.0.0.1:8000/api/v1/course_composition/ POST
{
    "quantity": 5,
    "content_type": "Видео",
    "training_course_compositions": 3
}
