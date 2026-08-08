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
        void savetoFile();
        void loadFromFile();
        void mainMenu();
        void adduser();
        void deleteuser();
        void updateuser();
        void displayuser();
        void searchuser();
        void xor_Encrypt_Decrypt(string &data ,const string &key);
        void login_main_menu();
        void regiuser();
        void login();
        void logout();
    

};


int main(){
    cout<<"hello world";
    return 0;
}
