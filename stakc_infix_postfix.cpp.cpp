#include <iostream>
#include <sstream>
#define N 20

using namespace std;

class Stacks
{   
    public: 
    int top=-1;
    char s[N];

    public:
        void push(char data)
        {
        if(isFull())
        {
            cout << "Stack is full\n";
            return;
        }
        else
        {
            top=top+1;
            s[top]=data;
            return;
        }
        }

        char pop()
        {   
            if(isEmpty())
            {
                cout << "Stack is empty\n";
                return ' ';
            }
            else
            {
                char value=s[top];
                s[top]=s[top+1];
                
                return value;
            }
        }

        int isFull()
        {
            if(top==N-1)
                return 1;
            else
                return 0;
        }

        int isEmpty()
        {
            if(top==-1)
                return 1;
            else
                return 0;
        }

        char peek()
        { 
            if(isEmpty() != 1)
                return s[top];
            else
                return 'Z';
        }


        void display()
        {   
            cout <<"your stack\n";
            for(int i=0; i<top;i++)
                cout<< s[i]<<"\n";
        }
};



int tv(string x, char m)  ///to check if the closing braket is present.
{
    for(int i=0; i<x.length(); i++)
    {
        if(x[i]==m)
            return 0;
    }
    return 1;
}

int brack(string x)
{
    Stacks S;

    for(int i=0; i<x.length(); i++)   //this is to make sure every braket thats been opened has been closed.
    {   
        cout<<x[i]<<endl;

        if (x[i] == '[')
        {    int k= tv(x, ']');
            if(k==1)  ///the braket wasnt closed
                return 3;

            S.push(3);
        }
        
        if (x[i] == '{')
        {    int k= tv(x,'}');
            if(k==1)
                return 2;
            S.push(2);
        }

        if (x[i] == '(')
        {   
            cout<<x[i];
            int k= tv(x,')'); 
            cout<<k;
            if (k==1)
                return 1;
            S.push(1);
        }

    }
   
    for(int i=0; i<=x.length(); i++)
    {   
        if (x[i] == ')')
        {
            int k = S.pop();
            if (k-1 != 0)
                return 1;
        }

        else if (x[i] == '}')
        {
            int k=S.pop();
            if (k-2 != 0)
                return 2;
        }

        else if (x[i] == ']')
        {
            int k=S.pop();
            if (k-3 != 0)
                return 3;
        }
        else
            return 0;
    }
}


int main()
{
    string a;
    cout<< "enter expression: ";
    cin >> a;

    cout<<a<<endl;
    int check=brack(a);
    cout<<check;

    if (check!=0)
    {
        cout << "incorrect bracket placement\n";
        return 0;
    }

/*
    string k=postfix(a);
    cout <<"post fix: "<<k <<'\n';

    int x=eval(k);
    cout<<"result: "<<x<<"\n";
    return 0;*/
}
