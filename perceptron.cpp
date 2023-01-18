#include <bits/stdc++.h>
using namespace std;
int x[4] = {1, -1, 1, -1};
int y[4] = {1, 1, -1, -1};
int R1[4] = {1, -1, -1, -1};
int R2[4] = {-1, -1, 1, -1};
int R3[4] = {1, 1, 1, -1};
int R4[4] = {-1, 1, 1, 1};
void solve(int *x, int *y, int *R1, int theta, int alpha, int b, int w1, int w2)
{
    int epoch = 1;
    bool f = false;
    while (!f)
    {
        f = true;
        cout << "epoch " << epoch << endl;
        for (int i = 0; i < 4; i++)
        {
            int yin = b;
            yin += w1 * x[i] + w2 * y[i];
            cout << "Yin for " << i << "th pair " << yin << endl;
            //apply activation function
            int Y = 0;
            if (yin > theta)
                Y = 1;
            else if (yin < theta)
                Y = -1;
            cout << "Y for " << i << "th pair " << Y << endl;
            if (Y != R1[i])
            {
                w1 = w1 + alpha * R1[i] * x[i];
                w2 = w2 + alpha * R1[i] * y[i];
                b += alpha * R1[i];
                f = false;
            }
            cout << "after " << i << "th pair w1 " << w1 << " w2 " << w2 << " b " << b << endl;
        }
        cout << "after " << epoch << "th w1 " << w1 << " w2 " << w2 << " b " << b << endl;
        epoch++;
    }
}
int main()
{
    int b, w1, w2, theta, alpha, option;
    cout << "Choose Option " << endl;
    cout << "1. AND" << endl;
    cout << "2. OR " << endl;
    cout << "3. ANDNOT " << endl;
    cout << "4. NAND" << endl;
    cin >> option;
    cout << "give the value of b,w1,w2,theta,alpha" << endl;
    cin >> b >> w1 >> w2 >> theta >> alpha;
    if (option == 1)
    {
        solve(x, y, R1, theta, alpha, b, w1, w2);
    }
    else if (option == 2)
    {
        solve(x, y, R3, theta, alpha, b, w1, w2);
    }
    else if (option == 3)
    {
        solve(x, y, R2, theta, alpha, b, w1, w2);
    }
    else
    {
        solve(x, y, R4, theta, alpha, b, w1, w2);
    }
}