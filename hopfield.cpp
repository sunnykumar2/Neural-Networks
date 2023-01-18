#include <bits/stdc++.h>
using namespace std;
int n;
int a[100], b[100], c[100];
int weight[101][101];
void mistaken()
{

    cout << "MISTAKEN " << endl;
    int p = 0;

    for (int i = 0; i < n; i++)
    {
        cout << i + 1 << "th element " << endl;
        int yin = b[i];
        for (int j = 0; j < n; j++)
        {
            yin = yin + weight[p][j] * c[j];
        }
        p++;
        cout << "yin" << i + 1 << " " << yin << endl;
        int Y = -1;
        if (yin > 0)
            Y = 1;
        if (c[i] != Y)
        {
            cout << "updated " << endl;
            if (c[i] == 1)
                c[i] = -1;
            else
                c[i] = 1;
        }

        cout << "after activation function " << Y << endl;
        for (int i = 0; i < n; i++)
            cout << c[i] << " ";
        cout << endl;
    }
}
void missing()
{
    int p = 0;
    cout << "MISSING " << endl;
    for (int i = 0; i < n; i++)
    {
        cout << i + 1 << "th element " << endl;
        int yin = b[i];
        for (int j = 0; j < n; j++)
        {
            yin = yin + weight[p][j] * b[j];
        }
        p++;
        cout << "yin" << i + 1 << " " << yin << endl;
        int Y = -1;
        if (yin > 0)
            Y = 1;
        if (b[i] != Y)
        {
            cout << "Updated " << endl;
            b[i] = Y;
        }

        cout << "after activation function " << Y << endl;
        for (int i = 0; i < n; i++)
            cout << b[i] << " ";
        cout << endl;
    }
}
void matrixmultiplication()
{
    cout << "weight matrix:  " << endl;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (i != j)
                weight[i][j] = a[i] * a[j];
            else
                weight[i][j] = 0;
            cout << weight[i][j] << " ";
        }
        cout << endl;
    }
}
int main()
{

    cin >> n;
    cout << "input vector " << endl;
    for (int i = 0; i < n; i++)
        cin >> a[i];
    cout << "missing vector " << endl;
    for (int i = 0; i < n; i++)
        cin >> b[i];
    cout << "mistaken vector " << endl;
    for (int i = 0; i < n; i++)
        cin >> c[i];
    matrixmultiplication();
    missing();
    mistaken();
}