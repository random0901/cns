#include<iostream>
using namespace std;
int main()
{
    int len,i,n,key,cc,cp;
    char ch;
    string str;
    cout<<"1 for encryption or 2 for decryption\n";
    cin>>n;
    cout<<"enter the msg:\n";
    getline(cin,str);
    getline(cin,str);
    len=str.length();
    cout<<"key\n";
    cin>>key;
    for(i=0;i<len;i++)
    {
        if((int)str[i]!=32)
        {
            cc=toupper(str[i])-65;
            if(n==1)
                cp=(cc+key)%26;
            else if(n==2)
                cp=(cc-key)%26;
            ch=cp+65;
            cout<<ch;
        }
    }
    return 0;
}