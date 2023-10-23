# Объекты

Вот практичкески все объекты, которые я создал:

![allobjects_list](screenshots/allobjects.png)

# Политика паролей

Поскольку максимальный срок жизни пароля 45 дней (по условиям задачи), и при этом пользователь не должен менять пароль, то я установил минимальный срок жизни пароля 45 дней, а максимальный 46. Это значит, что до прошествия 45 дней пользователь не сможет менять пароль, а на следующий день он станет недействительным.

![password-setup](screenshots/password-setup.png)

Так же я поставил запрет на смену пароля "пользователем" вручную.

![first_user](screenshots/first_user.png)

![second_user](screenshots/second_user.png)

# Пользователь

Картинка рабочего стола, а так же результат вывода команды gpresult /r.

![user-wallpaper-screenshot](screenshots/user-wallpaper.png)

![user-gpresult-output](screenshots/user-gpresult.png)

А так же запрет на редактирование реестра windows.

![regedit-denied-message](screenshots/regedit-denied.png)

# Оператор

Картинка рабочего стола, а так же результат вывода команды gpresult /r.

![operator-wallpaper-screenshot](screenshots/operator-wallpaper.png)

![operator-gpresult-output](screenshots/operator-gpresult.png)

А так же запуск powershell при входе в учётную запись оператора.

![operator-powershell-running](screenshots/operator-powershell.png)

# KDC Armoring

KDC активирован успешно.

![kdc-activated-policy](screenshots/kdc-activated.png)

А так же значение TheMachineAccountQuota поставлено на "5".

![machine-account-quota-changed](screenshots/machine-account-quota.png)
