# Отчёт о шифровке и расшифровке gpg файла

## Подготовка

С начала создаётся ключ отправителя.

![sender_key_gen](screenshots/sender/gpg_key_gen.png)

Затем получателя.

![recipient_key_gen](screenshots/recipient/gpg_key_gen.png)

Демонстрация публичного ключа.

![recipient_key_showcase](screenshots/recipient/gpg_key_showcase.png)

Публичный ключ получателя отправляется отправителю для дальнейшего шифрования.

![recipient_key_transfer](screenshots/recipient/gpg_export_file.png)

## Шифровка и расшифровка файла

Отправитель шифрует файл, используя публичный ключ получателя.

![sender_file_encryption](screenshots/sender/gpg_encryption.png)

После получения файла, получатель расшифровывает его.

![recipient_file_decryption](screenshots/recipient/gpg_decryption.png)