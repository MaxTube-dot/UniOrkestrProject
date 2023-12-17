UniOrkestrProject
UniOrkestrProject - проект на базе искусственного интеллекта с элементами кластеризации и высокой масштабируемостью. Проект состоит из трех основных частей:

Frontend (Angular) - Frontend: Пользовательский интерфейс, разработанный с использованием фреймворка Angular, обеспечивает плавный и интерактивный опыт для пользователей.

Backend - uni_rest_api_master: Основное приложение, отвечающее за взаимодействие с другими компонентами. Оно является центральным хабом для обработки данных и коммуникации.

Backend - uni_rest_api_node: Зависимая часть бэкэнда, предназначенная для легкой масштабируемости. Она может горизонтально масштабироваться для эффективной обработки увеличенной нагрузки.

Структура проекта
Структура проекта организована следующим образом:

Frontend: Содержит код фронтенда, разработанный с использованием фреймворка Angular.
uni_rest_api_master: Основное бэкэнд-приложение.
uni_rest_api_node: Масштабируемая часть бэкэнда.
main_parse_data.py: Скрипт для предварительной обработки набора данных перед обучением.
train.py: Скрипт для обучения модели машинного обучения.
Начало работы
Чтобы начать работу с UniOrkestrProject, выполните следующие шаги:

Настройте фронтенд Angular, перейдя в каталог Angular и выполните необходимые команды для установки зависимостей и запуска сервера разработки. Инструкий по запуску находится отдельно в папке приложения.

Настройте и запустите бэкэнд-приложение uni_rest_api_master, чтобы обрабатывать основные взаимодействия и коммуникацию.Инструкий по запуску находится отдельно в папке приложения.

Настройте и разверните несколько экземпляров зависимой части бэкэнда uni_rest_api_node, чтобы достичь масштабируемости и обработки увеличенной нагрузки.Инструкий по запуску находится отдельно в папке приложения.

Скрипт main_parse_data.py для предварительной обработки набора данных перед обучением модели машинного обучения.

Скрипт train.py для обучения модели с использованием предварительно обработанного набора данных.
