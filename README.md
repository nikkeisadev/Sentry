![image](https://github.com/nikkeisadev/Sentry/assets/137056695/db78c61d-6be6-434d-b573-08bc29c63726)
Sentry is a **school cyber security system** developed in Python.  It's a private project that I have been working on for one year. The goal of Sentry is to provide robust security measures for educational institutions, ensuring the safety of student's computers. 👾

> This project is licensed under the [Creative Commons Zero CC0 ](LICENSE).

📌 YouTube demo video: 
https://www.youtube.com/watch?v=pboiQy_5B8g

## Features ✨
- Protect the computer from malicious programs in startup folder.
- Prevent wallpaper changes.
- Generate reports on security incidents and vulnerabilities.
- Report to the database.
- Block different websites.
- Prevent installed apps from runing for a specified time. (Disable any application while, for example, exams.)

## Usage 📖
### Always run the program from VS Code terminal, and open the `/source` directory, otherwise the software will break. 📘
If the client, and the enviorment is ready, then you just have to start the software. Then you have to register a user from the administrator terminal window, and then login with these credentials.

### Backend management 🎛
Start `terminal.py`, and login with the root password of the database, which should be *neumannverseny*, or the one what you selected while installing it. (MySQL)

| Action           | Description                               |
|------------------|-------------------------------------------|
| User Register    | Register a new user in the system          |
| User Delete      | Remove an existing user from the system    |
| Get Activity     | Retrieve activity from the database        |
| Get Requests     | Retrieve requests from clients             |


## Installation 👾
Run `setup.py` from main, which will download all the requirements for Sentry with pip, and also gonna download the official MySQL installer for the backend.

### MySQL backend 🌐
1. When you start installing Sentry's requirements with `setup.py`, the mysql installer should start.
2. Click on Custom, we need only the graphical interface and the server.
3. In the installer, select MySQL Workbench from Applications, and MySQL server.
4. After installation the setup of the backend's open port, and root password will start.
5. Make the open port `8080`, and the password `neumannverseny`.
  IF THE PASSWORD IS SOMETHING ELSE, THEN CHANGE THE PASSWORD IN `sql/key/sql.key` TOO!
7. Initalize Workbench, and create a new connection. You can name it as you want, I recommend SENTRY-Neumannverseny or something like that.
8. The IP, is `127.0.0.0`, so `localhost`, and the port should be `8080` again.
9. Then click on test connection, and write the root password, which was `neumannverseny`.
10. Check the backend if it's running.
11. If the backend can't run, please try again installing it, or restart the computer.

Import the exported backend tables, which will be in the sql folder (in main).
- The exported database will already contain demo informations for testing.

### Client initialization 💻
BEFORE RUNNING THE CLIENT, PLEASE INSTALL THE BACKEND FIRST!
1. To start the client open the files in Visual Studio code.
2. Run `main.py` with the play button.
3. You will see the debug status in the terminal, and it should start booting up.
4. Login with your login credentials, but first register a new user from the terminal.

## Contributing ❗
As this is a private project, there is no possibility for external contributions. However, if you have any suggestions or feedback, feel free to reach out to me.

## Contact 📨
For any inquiries or support, please contact me at [notnikkecrd@gmail.com](mailto:notnikkecrd@gmail.com).
Discord: notnikkecrd, contact me anytime! 😇

## License 📜
This project is licensed under the [Creative Commons Zero CC0 ](LICENSE).
