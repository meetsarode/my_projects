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

class passmanager{
    private:
        string LoginUserName;
        string Loginpassword;
        vector<user> listofusers;

    public:
         void xor_Encrypt_Decrypt(string &data ,const char &key);
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

void passmanager::savetoFile(){
    ofstream file(LoginUserName + ".txt");
    if (file.is_open())
    {
        file<<LoginUserName<<"\n";
        file<<Loginpassword<<"\n";
        for (const auto& user :listofusers)
        {
            file << user.userName <<"\n";
            file << user.password <<"\n";
            file << user.accountName <<"\n";
        }
        file.close();
    }else
    {
        cout<< "Unable to open file for writing."<<endl;
    }

}

void passmanager::loadFromFile(){
    ifstream file(LoginUserName + ".txt");
    if (file.is_open()){
        getline(file,LoginUserName);
        getline(file,Loginpassword);
        user user;
        while (getline(file ,user.userName) && getline(file, user.password) && getline(file,user.accountName))
        {
            listofusers.push_back(user);
        }
        file.close();
    }else{
        cout << "Unable to open file for reading." <<endl;
    }
}

int main(){
    cout<<"hello world";
    return 0;
}
