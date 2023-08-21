# SSH

Для начала я убрал аутентификацию по паролю (и теперь без ключей сервер не выдаёт доступ вообще).
![access_denied](screenshots/connection_declined.png)

Далее обменялся ключами между машинами.
![keys](screenshots/key_exchange.png)

Собственно, теперь всё работает.
![connection_established](screenshots/connection_established.png)

# Пользователь

С фантазией у меня не очень, по сему я создал нового пользователя newuser с одноимённой домашней директорией, а так же внёс его в группу sudo. Ну и разумеется требуемые команды от его имени можно запускать без пароля (как видите на втором скришноте, все команды, требуемые в задаче он запускает без запроса пароля, а на команду echo 'hello world' требует пароль).
![newuser_created](screenshots/newuser_created.png)
![without password](screenshots/commands_without_password_added.png)

Есть один замечтаельный pam модуль, который по умолчанию имеет ограничение на пароль не меньше 8 символов, по этому установить это ограничение вообще не составило труда.
![limit](screenshots/password_limit_installed.png)

# ОС Linux

В качестве антивируса я выбрал сканер clamav. Установил, обновил базы данных и включил сервис.
![clamav](screenshots/clamav_installed_and_configured.png)

Создал скрипт daily_antivirus.sh (хоть он и был уже на уроках, решил написать заново дабы освежить память) и занёс его в crontab.
![daily_script](screenshots/daily_antivirus_script_created.png)

Так же я настроил firewall (я выбрал iptables в качестве файервола). Команды date и ping нужны для демонстрации того, что не было жульничества (что одна команда была сделана позже другой, а так же что некоторые из них выполнялись приблизительно в одно время, команда ping нужна что бы показать наличие соеденинения с интернетом).
![firewall](screenshots/firewall_configured.png)