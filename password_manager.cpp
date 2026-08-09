#include <iostream>
#include <conio.h>
#include <fstream>
#include <vector>

using namespace std;

struct user
{
    string userName;
    string password;
    string accountName;
};

class passmanager
{
private:
    string LoginUserName;
    string Loginpassword;
    vector<user> listofusers;

public:
    void xor_Encrypt_Decrypt(string &data, const char &key);
    void savetoFile();
    void loadFromFile();
    void mainMenu();
    void addUser();
    void deleteUser();
    void updateUser();
    void displayUser();
    void searchUser();
    void login_main_menu();
    void regiUser();
    void login();
    void logout();
};

void passmanager::savetoFile()
{
    ofstream file(LoginUserName + ".txt");
    if (file.is_open())
    {
        file << LoginUserName << "\n";
        file << Loginpassword << "\n";
        for (const auto &user : listofusers)
        {
            file << user.userName << "\n";
            file << user.password << "\n";
            file << user.accountName << "\n";
        }
        file.close();
    }
    else
    {
        cout << "Unable to open file for writing." << endl;
    }
}

void passmanager::loadFromFile()
{
    ifstream file(LoginUserName + ".txt");
    if (file.is_open())
    {
        getline(file, LoginUserName);
        getline(file, Loginpassword);
        user user;
        while (getline(file, user.userName) && getline(file, user.password) && getline(file, user.accountName))
        {
            listofusers.push_back(user);
        }
        file.close();
    }
    else
    {
        cout << "Unable to open file for reading." << endl;
    }
}

void passmanager ::login_main_menu()
{
    int choice;
    do
    {
        cout << "Welcome to the Password Manager !" << endl;
        cout << "1. Resister" << endl;
        cout << "2. login" << endl;
        cout << "3. Exit" << endl;
        cout << "Plese select an option : " << endl;
        cin >> choice;
        cin.ignore();
        system("clear");
        switch (choice)
        {
        case 1:
            regiUser();
            break;
        case 2:
            login();
            break;
        case 3:
            cout << "Exiting the program." << endl;
            break;
        default:
            cout << "Invalid choice. plese try again." << endl;
        }
    } while (choice != 3);
}

void passmanager ::regiUser()
{
    string inUsername, inpass;
    cout << "Registering the new user ..." << endl;
    cout << "Enter Username : ";
    getline(cin, inUsername);
    cout << "Enter password : ";
    getline(cin, inpass);

    ifstream file(LoginUserName + ".txt");
    if (file.is_open())
    {
        cout << "Username already exists. Please choose a different username ." << endl;
        file.close();
    }else{
        LoginUserName = inUsername ;
        Loginpassword = inpass ;

        savetoFile();
        cout << "user registered successfully !" <<endl;
        file.close();
    }
}

int main()
{
    cout << "hello world";
    return 0;
}
