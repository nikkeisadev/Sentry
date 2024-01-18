![image](https://github.com/nikkeisadev/Sentry/assets/137056695/db78c61d-6be6-434d-b573-08bc29c63726)
Sentry is a **school cyber security system** developed in Python.  It's a private project that I have been working on for one year. The goal of Sentry is to provide robust security measures for educational institutions, ensuring the safety of student's computers. 👾

## Features ✨
- Protect the computer from malicious programs in startup folder.
- Prevent wallpaper changes.
- Generate reports on security incidents and vulnerabilities.
- Report to the database.
- Scan files for viruses.
- Block different websites.
- Prevent installed apps from runing for a specified time. (Disable any app which can students help on exams)

## Usage 📖
If the client, and the enviorment is ready, then you just have to start the software. Then you have to register a user from the administrator terminal window, and then login with these credentials.
After that you will face the menu of Sentry where you can select various options, such as blocking websites, blockin apps from running, etc. > To install and setup the enviorment please check above!

# Installation and backend setup for clients. 💻
> If you want to run Sentry, you have to setup the enviorment. First of all you have to get the client, then you have to setup the SQL database localy. (Server and client in MySQL)
## Downloading ✅
Clone sourcecode
1. Clone the repository: `git clone https://github.com/nikkeisadev/Sentry.git`
2. Install the required dependencies: `pip install -r requirements.txt` (You can find the requirements in main)
3. Run the security system by `python sentry_main.py`
Download release 
1. Click to Download the release.
2. Then you just need to unzip the program, you don't need to install any requirements.
## SQL Database 🎛
Open sql folder, and there you will find all the files which needed for the database. (Including already stored informations) 
- Download MySQL
- Install workbench, and server (Try to install with the same version number)
- Creat new test connection and insert host informations from sql_structure.txt.
- Then the server should run, and you have to import the sql files from the folder, and the backend is ready.
  
## Contributing ❗
As this is a private project, there is no possibility for external contributions. However, if you have any suggestions or feedback, feel free to reach out to me.

## Contact 📨
For any inquiries or support, please contact me at [notnikkecrd@gmail.com](mailto:notnikkecrd@gmail.com).

## License 📜
This project is licensed under the [MIT License](LICENSE).
