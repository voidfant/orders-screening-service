Пытаюсь закинуть на гит папку с фронтом, столкнулся с некоторыми проблемами..

Последовательность действий такая: 

  1) venv тож закинул на гит, вместе со всеми .env, пускай так делать и не очень хорошо
  2) из корня запускаем "pip install -r requirements.txt"
  3) далее перейдем в папку с реактом - "cd frontend"
  4) "npm install axios"
  5) "npm install tailwindcss"
  6) из зависимостей вроде все, если вдруг будет ругаться на отсутствие чего-либо, доустановите пж..
  7) перейдем обратно в корень - "cd .."
  8) в папках dataMonitoring, telegramBot и backend в файлах .env меняем переменную DEV_USER на имя вашего пользователя в PostgreSQL
  9) а вот теперь уже вроде можно переходить к запуску проекта
  10) откроем 4 окна terminal.app (MacOS) или cmd.exe/powershell.exe (Windows) и в каждом окне переходим в корневую папку проекта
  11) в первом окне для начала инициализируем базу данных командой "npm run init-database"
  12) теперь, когда все таблицы в нашей БД созданы, можно запустить мониторинг данных командой "npm run service"
  13) к сервису можно дальше прикрутить бота, выкидывающий оповещения раз в день о просроченных позициях - "npm run bot"
  14) далее запускаем бэкенд нашего проекта командой "npm run backend", работать он будет на "http://localhost:5000"
  15) ну и напоследок, можно и реакт включить, как только у меня получится его закоммитить - "npm run frontend", работает на "http://localhost:3000"
  16) а чтоб получать уведомления от бота, предлагаю что-нибудь ему написать: https://t.me/unwind_digital_bot
  
P.S.: Не успел доделать полностью фронт, скажу честно. Вывел график, с таблицей возникли проблемы, при том пока не вполне понимаю, с чем связана проблема отображения: с парсингом JSON или с тем, что я как-то неправильно data.map() использую. Если дадите доп время до понедельника, скажем, то постараюсь и там доделат, и в докер все завернуть.
