#include <bits/stdc++.h>
using namespace std;
int n, m;
double mat[100][100];
double w[100];
double b, theta, alpha;
int detect;
void solve()
{
    int epoch = 0;
    bool f = false;
    while (!f)
    {
        cout << "Epoch " << epoch << endl;
        f = true;
        for (int i = 0; i < m; i++)
        {
            double yin = b;
            for (int j = 0; j < n; j++)
            {
                yin += w[j] * mat[i][j];
            }
            cout << "yin for " << i << "th " << yin << endl;
            int Y = 0;
            if (yin > theta)
                Y = 1;
            else if (yin < theta)
                Y = -1;
            cout << "Y " << Y << endl;
            if (i == detect)
            {
                if (Y != 1)
                {
                    b = b + alpha;
                    for (int k = 0; k < n; k++)
                    {
                        w[k] = w[k] + alpha * mat[i][k];
                    }
                    f = false;
                }
            }
            else if (Y != -1)
            {
                b = b + alpha * (-1);
                for (int k = 0; k < n; k++)
                {
                    w[k] = w[k] + alpha * mat[i][k] * (-1);
                }
                f = false;
            }
            cout << "After update weigth is " << endl;
            for (int i = 0; i < n; i++)
                cout << w[i] << " ";
            cout << endl;
        }
        epoch++;
    }
}
int main()
{
    cout << "Enter the sieze of parameters " << endl;
    cin >> n;
    cout << "Enter the number of colors " << endl;
    cin >> m;
    cout << "Enter the matrix of n*m " << endl;
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> mat[i][j];
        }
    }

    cout << "Enter the weights " << endl;
    for (int i = 0; i < n; i++)
        cin >> w[i];
    cout << "b theta alpha " << endl;

    cin >> b >> theta >> alpha;
    cout << "enter the ith pair you want to detect " << endl;
    cin >> detect;
    solve();
}