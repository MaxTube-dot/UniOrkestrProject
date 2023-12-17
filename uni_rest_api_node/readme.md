###UniOrkestrProject
# UniOrkestrProject - проект на базе искусственного интеллекта с элементами кластеризации и высокой масштабируемостью. Проект состоит из трех основных частей:
![train_batch2521](https://github.com/MaxTube-dot/Asserts/blob/master/browser_w0omazXrbT.gif)
Backend - uni_rest_api_node: Зависимая часть бэкэнда, предназначенная для легкой масштабируемости. Она может горизонтально масштабироваться для эффективной обработки увеличенной нагрузки.

##Запуск

-Для запуска блога у вас уже должен быть установлен Python 3.9.0
-Установите зависимости командой pip install -r requirements.txt
-Запустите сервер командой python3 manage.py runserver или python manage.py runserver
-Для корректной работы возможно потребуется изменить политику безопасностии, CORS в файле setting.py 

## Для корректной работы
После того как будет запущен uni_rest_api_node измените в файлах проекта три строчки, указав актуальный url node 
http://localhost:8080 -> your-ulr-node.ru:port
